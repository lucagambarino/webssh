import codecs
from setuptools import setup
from webssh._version import __version__ as version


with codecs.open('README.rst', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='webssh',
    version=version,
    description='Web based ssh client',
    long_description=long_description,
    author='Shengdun Hua',
    author_email='webmaster0115@gmail.com',
    url='https://github.com/huashengdun/webssh',
    packages=['webssh'],
    entry_points='''
    [console_scripts]
    wssh = webssh.main:main
    ''',
    license='MIT',
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.12',
	'Programming Language :: Python :: 3.13',
    ],
    install_requires=[
        'tornado>=6.5.2',
        'paramiko>=4.0.0',
    ],
)
