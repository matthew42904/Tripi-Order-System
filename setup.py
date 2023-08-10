from distutils.core import setup
import py2exe
import shutil

setup(console=["Main.py"])
shutil.copy('blank.png', './dist')