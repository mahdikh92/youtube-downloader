from setuptools import setup

setup(
	name = 'yget',
	version = '0.2',
	description = 'An easy youtube video downloader written in python',
	author = 'nanoman',
	url = '',
	license = 'MIT',
	packages = ['yget',],
	scripts = ['yget.py',],
	entry_points = {'console_scripts':['yget=yget:main',],},
)
