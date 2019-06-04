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
# Testing that a weak reference object is still live should be done using the expression ref() is not None.
# Normally, application code that needs to use a reference object should follow this pattern:
# 

# r is a weak reference object

o = r()

if o is None:

    # referent has been garbage collected

    print("Object has been deallocated; can't frobnicate.")

else:
    print("Object is still live!")

    o.do_something_useful()
