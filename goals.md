# pyTenable v2

## Goals

* Drop Python 2.x support.  This should allow for the use of some of the more
  modern functions of Python
* Improved typing support.  Python 3.6+ has dramatically improved typing support
  which should eliminate a lot of the need for the check function.
* Switch to RESTfly for base connection logic.  As RESTfly has been developed
  alongside pyTenable as a more generic solution to the same problem that
  pyTenable has solved, there have been a number of improvements made in how
  RESTfly accomplishes the same tasks.  We should take advantage of this and
  let this library handle the lower connection logic instead of trying to
  handle everything ourselves.
* Improve test suite.  While not something thats specific to the codebase
  itself, we should leverage more modern approaches to testing the library to
  reduce the amount of sprawl that we have with the current test suite.