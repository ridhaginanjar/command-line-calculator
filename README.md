# Calculator Command-line-based Project

## Overview
Create a Python package for a command-line calculator that supports basic arithmetic operations 
like addition, subtraction, multiplication, division, and more advanced operations like power, square root, etc. 
The project will follow best practices in packaging, virtual environments, and testing to ensure code quality and 
maintainability.

## Objective
1. Packaging the Code with Python Style
2. Implementing Virtual Environment
3. Implementing Functions and Module in Python
4. Implementing Uni Testing with Pytest

## Structure of Folder
````
my_calculator/
├── src/
│   ├── calculator/           # The main calculator package
│   │   ├── __init__.py       # Marks this directory as a Python package
│   │   ├── arithmetic.py     # Module for basic arithmetic operations (e.g., add, subtract)
│   │   └── advanced.py       # Module for advanced operations (e.g., trigonometry, exponentiation)
├── tests/                    # Directory for your test files
│   ├── test_arithmetic.py    # Unit tests for arithmetic.py
│   └── test_advanced.py      # Unit tests for advanced.py
├── setup.py                  # Script for installing the package, dependencies, and entry points
└── requirements.txt          # List of dependencies for the project
