# Overlay Image Title

 Overlay image, top, bottom, left or right, with a title.

--------------

For more info visit https://github.com/rnwolf/overlay_image_title/.

## Usage

```console
$ imagetitle [OPTIONS]
```

**Options**:

* `-i, --input PATH`: Image file name.  [default: input.png]
* `-o, --output PATH`: Output file name.  [default: output.png]
* `-p, --position [bottom|top|left|right]`: Where to position the tile.  [default: bottom]
* `-t, --title TEXT`: Text for title.
* `-f, --font TEXT`: Font name or path.
* `-r, --fraction FLOAT RANGE`: What fraction, 0 to 1, of the image edge should be covered by the title?  [default: 0.75]
* `--version`
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.


## Project layout

```
C:\Users\workspace\overlay_image_title
├── changes
|  ├── bugfix
|  ├── doc
|  ├── feature
|  ├── misc
|  └── removal
├── conftest.py
├── dev-dependencies.in
├── dev-dependencies.txt
├── dist
|  ├── imagetitle-0.0.0-py3-none-any.whl
|  └── imagetitle-0.0.0.tar.gz
├── Dockerfile
├── docs
|  ├── changelog.md
|  ├── development.md
|  ├── help.md
|  ├── index.md
|  └── Installation.md
├── imagetitle.egg-info
|  ├── dependency_links.txt
|  ├── entry_points.txt
|  ├── PKG-INFO
|  ├── requires.txt
|  ├── SOURCES.txt
|  └── top_level.txt
├── input copy.png
├── input.png
├── installed-packages.txt
├── list-key-dev-packages.py
├── make-linux-release.sh
├── mkdocs.yml
├── mypy.ini
├── out.png
├── output.jpg
├── poetry.lock
├── public
|  ├── 404.html
|  ├── changelog
|  |  └── index.html
|  ├── css
|  |  ├── base.css
|  |  ├── bootstrap.min.css
|  |  └── font-awesome.min.css
|  ├── development
|  |  └── index.html
|  ├── fonts
|  |  ├── fontawesome-webfont.eot
|  |  ├── fontawesome-webfont.svg
|  |  ├── fontawesome-webfont.ttf
|  |  ├── fontawesome-webfont.woff
|  |  ├── fontawesome-webfont.woff2
|  |  ├── glyphicons-halflings-regular.eot
|  |  ├── glyphicons-halflings-regular.svg
|  |  ├── glyphicons-halflings-regular.ttf
|  |  ├── glyphicons-halflings-regular.woff
|  |  └── glyphicons-halflings-regular.woff2
|  ├── help
|  |  └── index.html
|  ├── img
|  |  ├── favicon.ico
|  |  └── grid.png
|  ├── index.html
|  ├── Installation
|  |  └── index.html
|  ├── js
|  |  ├── base.js
|  |  ├── bootstrap.min.js
|  |  └── jquery-1.10.2.min.js
|  ├── search
|  |  ├── lunr.js
|  |  ├── main.js
|  |  ├── search_index.json
|  |  └── worker.js
|  ├── sitemap.xml
|  └── sitemap.xml.gz
├── pyproject.toml
├── pytest.ini
├── readme-sample-output.png
├── README.md
├── src
|  ├── imagetitle
|  |  ├── imagetitle.py
|  |  ├── __init__.py
|  |  ├── __main__.py
|  |  └── __pycache__
|  └── imagetitle.egg-info
|     ├── dependency_links.txt
|     ├── entry_points.txt
|     ├── PKG-INFO
|     ├── requires.txt
|     ├── SOURCES.txt
|     └── top_level.txt
├── tests
|  ├── baseline_images
|  |  ├── test_app_position_bottom_Windows.png
|  |  ├── test_app_position_left_Windows.png
|  |  ├── test_app_position_right_Windows.png
|  |  └── test_app_position_top_Windows.png
|  ├── input.png
|  ├── test_icon_image.ico
|  ├── test_imagetitle.py
|  ├── __init__.py
|  └── __pycache__
├── Ubuntu-C.ttf
├── vale
|  └── styles
|     ├── demo
|     ├── Google
|     ├── Joblint
|     ├── plugins
|     ├── proselint
|     ├── Spelling
|     ├── vale
|     └── write-good
└── __pycache__
```
