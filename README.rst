corndog
=======

corndog is a command-line script designed to make it easier to inspect and work with Redis.

This is not a Redis command library. It is not a wrapper around Redis. It's goal is to allow you
to write functions that encapsulate various Redis commands and/or format its output to make it easier
to fiddle with your Redis database while debugging or building new code.

Installation
------------
Installation is simple::

    curl https://raw.github.com/aezell/corndog/master/scripts/corndog > ~/bin/corndog && chmod u+x ~/bin/corndog

If you'd like an easier way to stay up-to-date, or you'd like to develop corndog do the following::

    fork on github
    clone your fork
    python setup.py develop

What it does
------------

* use some pre-built convenience methods that encapsulate multiple redis commands
* add your own commands to the command set so that you can quickly and easily perform entire command sets

What it will do
---------------

* allows you to run any of the built-in redis commands with pretty output