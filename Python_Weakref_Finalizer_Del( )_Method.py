# Python Weakref
# weakref — Weak references.
# The weakref module allows the Python programmer to create weak references to objects.
# 
# In the following, the term referent means the object which is referred to by a weak reference.
# A weak reference to an object is not enough to keep the object alive: when the only remaining references to a referent are weak references, garbage
# collection is free to destroy the referent and reuse its memory for something else.
# However, until the object is actually destroyed the weak reference may return the object even if there are no strong references to it.
# A primary use for weak references is to implement caches or mappings holding large objects, where it’s desired that a large object not be kept alive
# solely because it appears in a cache or mapping.
#

#
# Handling of __del__() methods is notoriously implementation specific, since it depends on internal details of the interpreter’s garbage collector
# implementation.
# 
# A more robust alternative can be to define a finalizer which only references the specific functions and objects that it needs, rather than having access
# to the full state of the object:
# 

class TempDir:

    def __init__(self):
        self.name = tempfile.mkdtemp()

        self._finalizer = weakref.finalize(self, shutil.rmtree, self.name)

    def remove(self):
        self._finalizer()

    @property

    def removed(self):
        return not self._finalizer.alive
