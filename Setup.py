import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

    name="<deepl-py>",

    version="0.0.1",

    author="<affederaffe>",

    description="<A deepl translator integration made with selenium>",

    long_description=long_description,

    long_description_content_type="text/markdown",

    url="<https://github.com/affederaffe/deepl-py>",

    packages=setuptools.find_packages(),

    classifiers=[

        "Programming Language :: Python :: 3",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",

    ],

    python_requires='>=3.6',

)
