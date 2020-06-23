FROM python:3.8-slim

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_NO_INTERACTION=1

RUN apt-get update && apt-get install -y --no-install-recommends build-essential gcc bash && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /usr/app
WORKDIR /usr/app
#ENV PYTHONPATH=${PYTHONPATH}:${PWD}

ENV POETRY_VERSION=1.0.9
RUN pip3 install --upgrade pip
RUN pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock ./
# As we are already in an isolated environment we do not need to create another
RUN poetry config virtualenvs.create false
# Install the package dependencies (No dev packages)
RUN poetry export -f requirements.txt | pip install -r /dev/stdin

# Build and Install the app
COPY ./src ./src
COPY README.md README.md
RUN poetry build -f wheel -n && pip install --no-deps dist/*.whl && rm -rf dist *.egg-info

# Install a font, "Ubuntu Condensed" from https://design.ubuntu.com/font/
COPY Ubuntu-C.ttf /fnt/Ubuntu-C.ttf

# Create app directory and change PWD for interfacing to outside world
RUN mkdir /app
WORKDIR /app

# Run the executable
ENTRYPOINT ["python", "-m", "imagetitle"]
# The help argument will be overridden with any commandline arguments.
CMD ["--help"]

#Examples for Windows Powershell
# Show help
# docker run -t -i --rm -v ${PWD}:/app overlayimagetitle:latest
# Show version
# docker run -t -i --rm -v ${PWD}:/app overlayimagetitle:latest --version

# Given a file called input.png in current working dir then with this produce output.png in
# docker run -t -i --rm -v ${PWD}:/app overlayimagetitle:latest -i /app/input.png -f /fnt/Ubuntu-C.ttf

# Open a bash shell inside of the docker container
# docker run -t -i --rm --entrypoint /bin/bash -v ${PWD}:/app overlayimagetitle:latest

# When using docker to run command setup a command alias for imagetitle
# In your powershell profile add the following
# function imagetitle {
#  docker run -it --rm v ${pwd}:/app overlayimagetitle:latest $args
# }

# In your bash profile  .bashrc add
# alias imagetitle='docker run -it --rm -v \`pwd\`:/app overlayimagetitle:latest'
#
