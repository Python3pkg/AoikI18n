import os
from setuptools import find_packages
from setuptools import setup

setup(
    name='AoikI18n',

    version='0.1.0',

    description="""A simple I18n solution featuring fallback locale, YAML locale file, synonym locale file, and flexible locale file path.""",
    
    long_description="""`Documentation on Github 
<https://github.com/AoiKuiyuyou/AoikI18n>`_""",

    url='https://github.com/AoiKuiyuyou/AoikI18n',

    author='Aoi.Kuiyuyou',
    
    author_email='aoi.kuiyuyou@google.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='i18n locale fallback yaml synonym flexible file path',

    install_requires=[
        'pyyaml',
    ],
      
    package_dir={'':'src'},
    
    packages=find_packages('src'),
)
