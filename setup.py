import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='sftplib',
    version='0.0.1',
    author='AP Consulting S.r.l.',
    author_email='areasviluppo@apconsulting.net',
    description=(
        'A **very** simple SFTP and FTP client library'
    ),
    license='MIT',
    url='https://github.com/apconsulting/sftplib',
    packages=['sftplib'],
    long_description=read('README.md'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_reqs=[
        'paramiko==2.7.1'
    ]
)
