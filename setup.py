from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in abakada/__init__.py
from abakada import __version__ as version

setup(
	name="abakada",
	version=version,
	description="Abakada",
	author="Kerwin",
	author_email="kerwin.manisan@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
