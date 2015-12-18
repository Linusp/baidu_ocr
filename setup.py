# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

VERSION='20151218'

setup(
    name='baiduocr',
    version=VERSION,
    url='https://github.com/Linusp/baidu_ocr',
    author='Linusp',
    author_email='linusp1024@gmail.com',
    description='An OCR client use Baidu API',
    packages=find_packages(),
    scripts=['bin/bocr'],
    install_requires=['requests'],
    include_package_data=True,
    zip_safe=False,
)
