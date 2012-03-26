"""A simple key/value store API. Like shelve but uses JSON instead of
pickle (so data must be simple structures instead of arbitrary Python
objects).

Goals:

    * Multiple backends (flat JSON, SQLite, LevelDB, DBMs,
      wrapped-in-pickle, ...).
    * Concurrency management & naive ACID.
    * Single-codebase Python 2 and 3 compatibility.
"""
import json
import collections
import os
try:
    import cPickle as pickle
except ImportError:
    import pickle

class JSONShelf(collections.MutableMapping):
    # Object lifetime.

    def save(self):
        """Persist the current in-memory state of the mapping."""
        raise NotImplementedError

    def close(self):
        """Close any opened resources."""
        pass

    def __del__(self):
        self.close()


    # As a context manager, the shelf saves on exit.

    def __enter__(self):
        # Eventually, this might acquire a lock on the file.
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        self.save()


class MemoryShelf(JSONShelf):
    """A base class for shelves that keep all their data in memory and
    write everything to disk on save().
    """
    def __init__(self, filename):
        self.filename = filename
        self.data = {}
        if os.path.exists(self.filename):
            self.load()
        else:
            # Create an empty file. Good idea? Maybe not. It's how
            # SQLite works, anyway.
            self.save()

    def load(self):
        """Dump self.data to the file."""
        raise NotImplementedError

    # Pass mapping methods on to underlying store.
    def __getitem__(self, key):
        return self.data[key]
    def __setitem__(self, key, value):
        self.data[key] = value
    def __delitem__(self, key):
        del self.data[key]
    def __iter__(self):
        return iter(self.data)
    def __len__(self):
        return len(self.data)


class FlatShelf(MemoryShelf):
    """A shelf backed by a single flat JSON file.
    """
    def load(self):
        with open(self.filename) as f:
            self.data = json.load(f)

    def save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f)


class PickleShelf(MemoryShelf):
    """A shelf that stores data in a pickle file.
    """
    def load(self):
        with open(self.filename) as f:
            self.data = pickle.load(f)

    def save(self):
        with open(self.filename, 'w') as f:
            pickle.dump(self.data, f)
