from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(

    name='deepl-py',

    version='0.0.1',

    description='A deepl translator integration made with selenium',

    long_description=long_description,

    url='https://github.com/affederaffe/deepl-py',

    author='affederaffe',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],

    keywords='deepl, translator, development',

    py_modules=["deepl.py"],

    python_requires='>=3.5, <4',

    project_urls={
        'Bug Reports': 'https://github.com/affederaffe/deepl-py/issues',
        'Source': 'https://github.com/affederaffe/deepl-py',
    },
)
