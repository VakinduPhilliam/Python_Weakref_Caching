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
# If the object never gets garbage collected the finalizer will still be called at exit.
#

# 
# One advantage of weakref based finalizers is that they can be used to register finalizers for classes where the definition is controlled by a third
# party, such as running code when a module is unloaded:
# 

import weakref, sys

def unloading_module():

    # implicit reference to the module globals from the function body

weakref.finalize(sys.modules[__name__], unloading_module)
 

#
# Note:
# 
# If you create a finalizer object in a daemonic thread just as the program exits then there is the possibility that the finalizer does not get called at
# exit.
# However, in a daemonic thread atexit.register(), try: ... finally: ... and with: ... do not guarantee that cleanup occurs either.
# 