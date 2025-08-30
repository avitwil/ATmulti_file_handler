"""
File Handling Abstraction Package
=================================

This package provides a unified abstraction layer for working with multiple
file formats. It exposes the main File classes and a factory function
for easy instantiation.

Available Classes
-----------------
- File
- TxtFile
- JsonFile
- CsvFile
- DillFile
- XmlFile
- YamlFile
- ByteFile
- VarDBFile

Factory Function
----------------
- file(name, path=None, *, scope=None, data=None)

Example Usage
-------------
from file_module import file, TxtFile, JsonFile

f = file("example.txt")
f.write("Hello World")
print(f.read())
"""

from .core import (
    File,
    TxtFile,
    JsonFile,
    CsvFile,
    DillFile,
    XmlFile,
    YamlFile,
    ByteFile,
    VarDBFile,
    file
)

__all__ = [
    "File",
    "TxtFile",
    "JsonFile",
    "CsvFile",
    "DillFile",
    "XmlFile",
    "YamlFile",
    "ByteFile",
    "VarDBFile",
    "file"
]