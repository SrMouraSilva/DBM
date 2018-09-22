# Copyright 2018 SrMouraSilva
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from os import path
from setuptools import setup


def readme():
    here = path.abspath(path.dirname(__file__))

    with open(path.join(here, 'README.md'), encoding='UTF-8') as f:
        return f.read()

setup(
    name='DBM',
    version='0.2.0',

    description='Deep Boltzmann Machine',
    long_description=readme(),

    url='https://github.com/SrMouraSilva/DBM/',

    author='Paulo Mateus Moura da Silva (SrMouraSilva), Amauri Holanda de Souza Júnior (amauriholanda)',
    author_email='mateus.moura@ppgcc.ifce.edu.br, <insert e-mail here>',
    maintainer='Paulo Mateus Moura da Silva (SrMouraSilva)',
    maintainer_email='mateus.moura@ppgcc.ifce.edu.br',

    license="Apache Software License v2",

    packages=[
        'dbm'
    ],

    install_requires=[
        'numpy',
        #'pytorch'
    ],

    test_suite='test',
    tests_require=['pytest', 'pytest-cov'],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='dbm rbm boltzmann machine',

    platforms='Linux',
)

