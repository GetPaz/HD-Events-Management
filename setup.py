from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in hd_event_management/__init__.py
from hd_event_management import __version__ as version

setup(
	name="hd_event_management",
	version=version,
	description="HD Event Management",
	author="Pazcare",
	author_email="admin@pazcare.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
