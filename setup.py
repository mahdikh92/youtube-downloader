from setuptools import setup

setup(
	name = 'yget',
	version = '0.1',
	description = 'An easy youtube video downloader written in python',
	author = 'nanoman',
	url = '',
	license = 'MIT',
	packages = ['yget'],
	scripts = ['main.py'],
	entry_points = {'console_scripts':['yget=main:main',],},
)
