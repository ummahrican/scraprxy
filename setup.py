from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "scraprxy for proxy rotating"
LONG_DESCRIPTION = "scrape proxies from more than 5 different sources and check which ones are still alive"

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="scraprxy",
    version=VERSION,
    author="Ahmed Mustafa",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'
    keywords=["python", "proxy", "scraper", "rotate proxies"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
