# Python Weakref
# weakref � Weak references.
# The weakref module allows the Python programmer to create weak references to objects.
# 
# In the following, the term referent means the object which is referred to by a weak reference.
# A weak reference to an object is not enough to keep the object alive: when the only remaining references to a referent are weak references, garbage
# collection is free to destroy the referent and reuse its memory for something else.
# However, until the object is actually destroyed the weak reference may return the object even if there are no strong references to it.
# A primary use for weak references is to implement caches or mappings holding large objects, where it�s desired that a large object not be kept alive
# solely because it appears in a cache or mapping.
#

#
# Weak Reference Objects
# Weak reference objects have no methods and no attributes besides ref.__callback__.
# A weak reference object allows the referent to be obtained, if it still exists, by calling it:
# 

import weakref

class Object:
        pass

o = Object()

r = weakref.ref(o)

o2 = r()
o is o2

# OUTPUT: 'True'
