# Package Installer for Python (PIP)

Package is a collection of modules / subpackages. The folder should contain **__init__.py** file. This file can be empty. 

## PIP
- It is used to install, update, upgrade and uninstall python modules which are not present inbuilt in python.
- PIP comes default when you install core-python.
- PIP can be used in command line tools and in the terminals.


### Check the version of PIP:

```
pip --version
```

### Install Python Packges using PIP

```
pip install <package-name>
```

### Uninstall Python Package

```
pip uninstall <package-name>
```

### Install a particular version of python package

```
pip install <package-name>==version_number
```

## Display the information about a python package.

```
pip show <package-name>
```

## Display all the python packages installed on my system

```
pip list
```

### Need to run install/uninstall multiple modules / packages
```
pip install -r <textfileName>.txt
pip uninstall -r <textfileName>.txt
```