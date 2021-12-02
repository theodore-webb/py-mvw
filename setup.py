from setuptools import setup


setup(
    name="mvw",
    version='0.0.1',
    description='Utility functions used across workstreams.',
    url='https://github.com/theodore-webb/py-mvw',
    author='TW Webb',
    packages=['mvw'],
    entry_points = {
        'console_scripts': ['mvw-cmd=mvw.__init__:init'],
    }
)
