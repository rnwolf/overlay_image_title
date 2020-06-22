FROM python:3.8-slim AS base

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1


FROM base AS python-deps

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.0.9

# Install pipenv and compilation dependencies
RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y --no-install-recommends gcc bash git && \
    rm -rf /var/lib/apt/lists/*

# Install a font, "Ubuntu Condensed" from https://design.ubuntu.com/font/
COPY Ubuntu-C.ttf /fnt/Ubuntu-C.ttf

RUN python -m venv /opt/venv
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install "poetry==$POETRY_VERSION"
COPY pyproject.toml poetry.lock ./
# Install the dependencies (No dev packages)
RUN poetry export -f requirements.txt | pip install -r /dev/stdin

# Don't install development deps and main application
#RUN poetry install -n --no-root --no-dev #&& \
#RUN poetry build -f wheel -n
#&& \
#RUN pip install --no-deps dist/*.whl
#&& \
#rm -rf dist *.egg-info
# Install python dependencies in /.venv based on previously created virtualenv
# pip freeze > installed-packages.txt
# python .\list-key-dev-packages.py
# pip-compile dev-dependencies.in --output-file dev-dependencies.txt
#COPY dev-dependencies.txt .
#RUN pip install --no-cache-dir -r dev-dependencies.txt


FROM base AS runtime

# Create and switch to a new user
# add non-priviledged user
RUN useradd --uid 1000 --create-home appuser
WORKDIR /home/appuser
USER appuser

COPY --from=python-deps /opt/venv /home/.venv
# Make sure we use the virtual env
#ENV PATH="/opt/venv/bin:$PATH"
ENV PATH="/home/appuser/.venv/bin:$PATH"
RUN chown appuser.appuser -R .

COPY pyproject.toml poetry.lock ./
COPY ./src ./src
COPY README.md README.md
RUN poetry build -f wheel -n && pip install --no-deps dist/*.whl && rm -rf dist *.egg-info

# Make sure we use the local virtual env
#ENV PATH="/home/appuser/.local/bin:$PATH"



# Install application into container
#COPY . .
#COPY pyproject.toml poetry.lock ./
# Make sure files are owned by user
#RUN chown appuser.appuser -R .

# Install the app
#RUN poetry install --no-dev
# Run the executable
ENTRYPOINT ["python", "-m", "imagetitle"]
CMD ["--help"]
