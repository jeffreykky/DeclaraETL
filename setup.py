from setuptools import setup, find_packages

print(find_packages())
setup(
    name="declara_etl",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A brief description of my Python project",
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=[
        'pyyaml',
        'pyspark'
    ],
)