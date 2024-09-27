from setuptools import setup, find_packages

setup(
    name="GZSper",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "scanpy",
        "matplotlib",
        "seaborn",
        "pandas",
        "numpy",
        "scipy",
    ],
    author="Benjamin-JHou",
    author_email="zjy888zjy888@gmail.com",
    description="A tool for integrating GWAS Z-scores with single-cell RNA-seq analysis",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Benjamin-JHou/GZSper",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
