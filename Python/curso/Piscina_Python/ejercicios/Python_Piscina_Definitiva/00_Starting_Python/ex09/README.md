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

Create a file named test_script.py and copy the following code:

from ft_package import count_in_list
print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0

Finally, to test if the package and its function count_in_list work correctly, run the test_script.py script:

*python3 test_script.py*

You should see the following output:

2 0

"""

