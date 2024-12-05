# Markdown

This file is written in **Markdown**.

## Package Description

    Package Name: ft_package
    Version: 0.0.1
    Main Function: count_in_list


Function count_in_list

The function count_in_list takes two arguments:

    lst: A list of elements (it can be a list of strings, numbers, etc.).
    item: The element you want to count in the list.


La función devuelve un entero que indica cuántas veces aparece el item en la lista lst.

## Steps to Functioning

**Step 1: Make sure you have all the necessary files**

Before starting, ensure that the essential files for your package are in the correct structure. The key files you need to have are:

    setup.py: Defines the package metadata.
    LICENSE: License file.
    README.md or README.txt: Package information file.
    pyproject.toml: Contains the configuration for building the package.
    ft_package/: Package folder containing at least two files:
        __init__.py: File that makes the directory a Python package.
        count.py: File that contains the count_in_list function.

**Step 2: Verify the directory structure**

Make sure your directory structure looks similar to the following:

ex09/
├── LICENSE
├── README.md
├── setup.py
├── pyproject.toml
└── ft_package
    ├── __init__.py
    └── count.py

The rest of the necessary directories and files will be generated automatically.

**Step 3: Build the package**

To build the package in .whl and .tar.gz format, run the following command from the root directory of your project, where setup.py is located:

*python3 setup.py sdist bdist_wheel*

This will generate the files in the dist/ directory:t/:

    ft_package-0.0.1-py3-none-any.whl
    ft_package-0.0.1.tar.gz

**Step 4: Install the package Option 1: Install the .whl file**

Option 1: Install the .whl file

If you want to install the package using the generated .whl file, run the following command:

*pip install ./dist/ft_package-0.0.1-py3-none-any.whl*

Option 2: Install the .tar.gz file

If you prefer to use the source .tar.gz file, you can install the package with this command:

*pip install ./dist/ft_package-0.0.1.tar.gz*

**Step 5: Verify the installation**

After installing the package, you can verify if it was installed correctly by running:

*pip list*

A long list of the packages you have installed appears. 

You should see ft_package in the list of installed packages.

You can also get more detailed information about the package with:

*pip show -v ft_package*

ft-package detail comes out:

Name: ft-package
Version: 0.0.1
Summary: A sample test package
Home-page: UNKNOWN
Author: eagle
Author-email: eagle@42.fr
License: MIT
Location: /home/jurrutia/.local/lib/python3.10/site-packages
Requires: 
Required-by: 
Metadata-Version: 2.1
Installer: pip
Classifiers:
  Programming Language :: Python :: 3
  License :: OSI Approved :: MIT License
  Operating System :: OS Independent
Entry-points:


**Step 6: Run the test script**

Finally, to test if the package and its function count_in_list work correctly, run the test_script.py script:

*python3 test_script.py*

You should see the following output:

2 0

"""

## archivo pyproyect.toml
[build-system]: This section defines the build system that will be used to package your project.

[requires]: This line specifies the dependencies needed to build the package. In this case:

    setuptools>=42: Indicates that you need at least version 42 of 
    setuptools. setuptools is a library that facilitates the creation 
    of Python packages. This minimum version ensures that you have 
    access to the features and improvements introduced in 
    later versions.

    wheel: This is another library that allows creating Python packages
    in "wheel" format, which is a binary distribution format. The 
    .whl files are easier and faster to install than source distribution 
    files, as they do not require compiling the 
    code.


[build-backend] Here you specify which backend will be used for the building of the package. In your case, setuptools.build_meta is a backend that allows setuptools to handle the building of the package according to the metadata you have provided. It is a commonly used option, as setuptools is one of the most popular tools for creating packages in Python.


## dist file

[Wheels]: Files with the .whl extension that are the most commonly used binary distribution format in Python. These files are easy and quick to install, as they contain the precompiled code and the necessary information to make the installation straightforward. For example, in your ls output, we have ft_package-0.0.1-py3-none-any.whl.

[TAR.GZ Files]: Files with the .tar.gz extension are source distributions. They contain the source code of the package and generally need to be compiled or installed from scratch when used. In this case, we have ft_package-0.0.1.tar.gz.

What they are for:

The files in the dist directory are used to distribute your package. When someone wants to install your package, they usually do so from a file in this directory.

## ./ft_package.egg-info directory

The ./ft_package.egg-info directory is created automatically by setuptools when you build your package. This directory contains metadata about your package and is part of the Python packaging system. Here’s a brief description of the files you mentioned:

    dependency_links.txt: This file may list links to dependencies that are not available in the Python Package Index (PyPI). While its usage is rare today, some older configurations may still require it.

    PKG-INFO: Contains important metadata about your package, such as its name, version, author, author's email address, description, and license. Essential for installation and distribution.

    SOURCES.txt: Lists all the source files included in the package. It helps installers know which files need to be installed.

    top_level.txt: Enumerates the top-level modules of the package, including the package name and any submodules considered top-level modules.

These files are automatically generated by setuptools and provide useful information for managing dependencies and facilitating the installation of your package.


## ./build directory

the  is also created automatically by setuptools when you build your package. This directory is used during the building process to hold temporary files and the built distribution files. Here’s a brief overview of what you see in the ./build directory:

    bdist.linux-x86_64: This subdirectory is created to hold the built distribution for the specific platform (in this case, Linux x86_64). It will typically contain the binary distribution files that are ready to be installed.

    lib: This subdirectory contains the package library files, including your package's source code. The ft_package directory within lib holds the actual package files, such as __init__.py and count.py, which you defined in your package.