import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="doberman",
    version="0.0.3",
    author="Bernardi Riccardo",
    author_email="riccardo.bernardi@rocketmail.com",
    description="A watchdog that when launched synchronise the remote directory with the content of the local one",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/riccardobernardi/doberman",
    packages=setuptools.find_packages()+['doberman'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['bcrypt==3.2.0', 'cffi==1.14.2', 'cryptography==3.0', 'paramiko==2.7.1', 'pathtools==0.1.2', 'pycparser==2.20', 'PyNaCl==1.4.0', 'pysftp==0.2.9', 'six==1.15.0', 'watchdog==0.10.3', '']
,
)