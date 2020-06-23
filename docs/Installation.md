## Installation

There are a number of ways you could install this utility.

### Python

If you are familiar with the installation of python packages in a virtual environment then you can install with:

```
pip install imagetitle
```

This will give you a command line application that you can use at the terminal.

#### Pipx

Another approach is to use a utility called [Pipx](https://pypi.org/project/pipx/) to install the application.

```console
pipx install imagetitle
or
pipx install git+https://github.com/rnwolf/overlay_image_title/
```

### Docker

The utility is also packaged up in a Docker [image](https://hub.docker.com/r/rnwolf/overlayimagetitle).

If you have docker installed then you can pull down the application and python all in one image.

```
docker pull rnwolf/overlayimagetitle
```

To show application help
```docker run -t -i --rm -v ${PWD}:/app overlayimagetitle:latest```

Show version
```docker run -t -i --rm -v ${PWD}:/app overlayimagetitle:latest --version```

Given a file called input.png in current working dir then with this produce output.png in
```docker run -t -i --rm -v ${PWD}:/app overlayimagetitle:latest -i /app/input.png -f /fnt/Ubuntu-C.ttf```

Open a bash shell inside of the docker container
```docker run -t -i --rm --entrypoint /bin/bash -v ${PWD}:/app overlayimagetitle:latest```

### Setup alias for Docker Image

When using docker to run command setup a command alias for imagetitle
In your powershell profile add the following

```
function imagetitle {
  docker run -it --rm v ${pwd}:/app overlayimagetitle:latest $args
 }
 ```

Or if you use bash terminal then update .bashrc profilr by adding:

```alias imagetitle='docker run -it --rm -v \`pwd\`:/app overlayimagetitle:latest'```
