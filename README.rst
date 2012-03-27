jsonshelve
==========

A `shelve`_-like key/value persistence API that uses JSON instead of `pickle`_.
This means that stored data structures cannot be arbitrary (pickleable) objects
but must instead be simple data structures (lists, dicts, strings, ints, floats,
null). But it also means that it's easy to use the data files from languages
other than Python.

Backends currently exist for flat JSON files, pickle blobs (which is really
useless), and SQLite. Backends *should* exist for `LevelDB`_ and `DBM`_.

Goals include:

* Many backends. Applications can choose based on performance and other
  constraints and switch later without pain.
* Concurrency management & naive ACID in some form.
* Single-codebase Python 2 and 3 compatibility.
* Unicode keys?
* Extra niceness for indexing and such?

.. _DBM: http://docs.python.org/library/dbm.html
.. _shelve: http://docs.python.org/library/shelve.html
.. _leveldb: http://code.google.com/p/leveldb/
.. _pickle: http://docs.python.org/library/pickle.html

Related Projects
----------------

* `sqlite3dbm`_
* `sqlitedict`_
* `y_serial`_
* `json-store`_

.. _json-store: https://github.com/brainsik/json-store
.. _sqlite3dbm: https://github.com/Yelp/sqlite3dbm
.. _y_serial: http://yserial.sourceforge.net/
.. _sqlitedict: http://pypi.python.org/pypi/sqlitedict
