import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="routine_de",
    version="0.0.1",
    url='https://github.com/pathirippilly/PyProjects/tree/common',
    author="Akhil Pathirippilly mana",
    author_email="akhilpathirippilly@gmail.com",
    description="Package with utilities for routine DE activities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    py_modules=["custom_exceptions", ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Data Engineering :: Build Tools',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=['requests==2.26.0',
                      'beautifulsoup4==4.10.0',
                      'lxml==4.7.1',
                      'pytz~=2021.3',
                      'PyYAML==6.0',
                      'coloredlogs~=15.0.1',
                      'lazy~=1.4'],
    data_files=[('.', ['../requirements.txt'])]
    # dependency_links=['http://github.com/<username>/<reponame>/tarball/master#egg=<packagename>_<version#>'] # --> dependency links apart from PyPI
)
