import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pktktime", # Replace with your own username
    version="1.0.0",
    author="Eshan Ramesh",
    author_email="esrh@netc.eu",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    entry_points={'console_scripts':['pktktime=pktktime.pechatimer:main']},
    python_requires='>=3.6',
)
