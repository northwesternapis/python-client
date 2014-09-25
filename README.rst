nuapiclient
===========

A simple Python wrapper for the `Northwestern Course Data API <http://developer.asg.northwestern.edu>`__

Version
-------

0.0.1

Requirements
------------

-  `Python <http://www.python.org/>`__
-  `An API key <http://developer.asg.northwestern.edu/docs/#getting-started>`__

Installation
------------

Automatic installation using `pip <http://pypi.python.org/pypi>`__:

::

    pip install nuapiclient

Usage
-----

.. code:: python

    import json
    from nuapiclient import NorthwesternAPIClient
    client = NorthwesternAPIClient('Your API key goes here')

    courses = client.courses(term=4530, subject='PHIL')
    print json.dumps(courses[0], indent=4)

Examples
--------

Examples can be found in the /examples folder. Put your API key in /examples/settings.py to try them out. They include:

-  Basic use of several endpoints [basic.py]

Changelog
---------

0.0.1

-  Initial version

Credits
-------

Written by Sheng Wu <shengwu34@gmail.com>

Support
-------

-  Northwestern Course Data API <asg-technology@u.northwestern.edu>
-  Sheng Wu <shengwu34@gmail.com>

References
--------------------------

`Northwestern Course Data API <http://developer.asg.northwestern.edu/docs/>`__

License
-------

(The MIT License)

Copyright (c) 2014 Sheng Wu <shengwu34@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
