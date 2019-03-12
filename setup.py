import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dropSeqPipe",
    version="0.4",
    author="Roelli Patrick",
    author_email="patrick.roelli@gmail.com",
    description="A python wrapper to run and install dropSeqPipe as a python package",
    url="https://github.com/Hoohm/dropSeqPipe",
    packages=setuptools.find_packages(),
    entry_points={
          'console_scripts': [
              'dropSeqPipe = scripts.__main__:main'
          ]
      },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[
          'snakemake>=5.1.2'
      ],
      python_requires='>=3.6'
)
