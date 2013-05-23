try:
	from setuptools.core import setup
except ImportError:
	from distutils.core import setup

setup(
	name='cliui',
	version='0.0.1',
	author='Feng Zhou',
	packages=['cliui'],
	url='https://github.com/zweifisch/cliui',
	description='utils for command line user iteraction',
	author_email='zf.pascal@gmail.com'
)
