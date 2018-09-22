DBM
===

Deep Boltzmann Machine :cite:`pmlr-v5-salakhutdinov09a`

|Build Status| |codecov|

Development
-----------

Create a venv

::

   python3.6 -m venv venv

Install requirements

::

   # Install before PyTorch from https://pytorch.org/ 
   python setup.py develop
   make install

Execute the tests

::

   make test

See the docs

::

   make docs-see

.. |Build Status| image:: https://travis-ci.org/SrMouraSilva/DBM.svg?branch=master
   :target: https://travis-ci.org/SrMouraSilva/DBM
.. |codecov| image:: https://codecov.io/gh/SrMouraSilva/DBM/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/SrMouraSilva/DBM