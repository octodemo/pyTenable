pyTenable
=========
Release v\ |release|.

.. image:: https://travis-ci.org/tenable/pyTenable.svg?branch=master
    :target: https://travis-ci.org/tenable/pyTenable
.. image:: https://img.shields.io/pypi/v/pytenable.svg
    :target: https://pypi.org/project/pyTenable/
.. image:: https://img.shields.io/pypi/pyversions/pyTenable.svg
    :target: https://pypi.org/project/pyTenable/
.. image:: https://img.shields.io/pypi/dm/pyTenable.svg
    :target: https://github.com/tenable/pytenable
.. image:: https://img.shields.io/github/license/tenable/pyTenable.svg
    :target: https://github.com/tenable/pytenable

Introduction
------------

pyTenable is an interface library into the Tenable suite of products.  The aim
is to make interfacing into these products simple without the need for
unnecessary boilerplate code.

.. warning::

    This branch of pyTenable is a complete rewrite and is under active
    development.  It is not considered stable by any stretch.

Why do a ground-up rewrite?
---------------------------

The pyTenable codebase and test suite had grown to a point where it was starting
to get problematic to continue working on.  Further a lot had been learned while
working on the library in terms of what assumptions were good ones, which were
bad ones, and what could be done to improve maintainability if reworked.  When
the v2 rewrite was started, we had some basic design principals that we decided
should be considered core tenants to code against:

* **Switch to RESTfly for base connection logic.**
    As RESTfly has been developed alongside pyTenable as a more generic solution
    to the same problem that pyTenable has solved, there have been a number of
    improvements made in how RESTfly accomplishes the same tasks.  We should
    take advantage of this and let this library handle the lower connection
    logic instead of trying to handle everything ourselves.
* **Improved test suite.**
    While not something thats specific to the codebase itself, we should
    leverage more modern approaches to testing the library to reduce the amount
    of sprawl that we have with the current test suite.
* **Improve the input validation.**
    Input validation & transformation was an incredible chore in the v1 code,
    to the point where it actually created issues and slowed down adoption of
    new endpoints.  We need a simple, efficient way to validate inputs.  Further
    input validation should be able to be tested independently of the actual
    API requests.
* **Conform to DRY when possible**
    The v1 codebase only adhered to DRY (Don't Repeat Yourself) in a few
    circumstances.  The reasoning was to contain all of the code needed for a
    given method within that method.  While an admirable goal, it lead to a lot
    of code duplication.  We should try to reduce the amount of code that we
    have to test, validate, and maintain overal.  Yes this will make the code
    "more complex", however in many ways it'll make the code cleaner and more
    readable.



.. toctree::
    :hidden:
    :glob:

    quickstart/index
    api/index