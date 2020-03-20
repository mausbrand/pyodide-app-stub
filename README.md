# pyodide-app-stub

This is a basic stub for creating a new Python-based webapp using [Pyodide](https://github.com/iodide-project/pyodide) and the [`viur-html5` library](https://github.com/viur-framework/viur-html5).

## Setup

Clone the repository including its submodule (html5) into a directory of your choice. After that, once execute `./get-pyodide.py` to automatically download and install Pyodide from the official release tarball.

## Usage

To immediatelly test your app, run `./test-server.py` and open [http://localhost:8080](http://localhost:8080).

When Python modules are added, run `./gen-files-json.py` to build the Python files mapping that is used by the app boostrapper.

In case you want to add additional modules, you have to hack the file `app.js`.

## Files

The repository contains these files.

- `app.html` contains the basic HTML structure into which the app is rendered
- `app.js` contains the app bootstrapper which downloads and installs Python files for the Pyodide environment from Python source files.
- `app.py` contains a demo app code.
- `files.json` is generated by `gen-files-json.py`.
- `gen-files-json.py` is a tool that generates `files.json` and omits tooling scripts.
- `get-pyodide.py` downloads and installs pyodide into the `./pyodide` folder
- `html5` is the [`viur-html5` library](https://github.com/viur-framework/viur-html5) as a submodule. It is also added to `files.json` and required to implement Python webapps nicely.
- `__init__.py` is the general app entry point.
- `test-server.py` is an `http.server`-based simple web-server

All files can be modified to fit the needs and purposes of your app!
