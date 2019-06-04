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
# Several built-in types such as list and dict do not directly support weak references but can add support through subclassing:
# 

class Dict(dict):
    pass

obj = Dict(red=1, green=2, blue=3)   # this object is weak referenceable
 

#
# Other built-in types such as tuple and int do not support weak references even when subclassed
# (This is an implementation detail and may be different across various Python implementations.).
#