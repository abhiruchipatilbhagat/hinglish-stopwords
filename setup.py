# setup.py
from setuptools import setup, find_packages

setup(
    name='hinglish_stopwords',
    version='0.1.0',
    description='A simple library to filter hinglish stopwords from text.',
    author='abhiruchipatilbhagat',
    author_email='abhipatilngp@gmail.com',
    packages=find_packages(),
    install_requires=[],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
