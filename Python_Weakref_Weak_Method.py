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
# class weakref.WeakMethod(method): 
# A custom ref subclass which simulates a weak reference to a bound method (i.e., a method defined on a class and looked up on an instance).
# Since a bound method is ephemeral, a standard weak reference cannot keep hold of it.
# WeakMethod has special code to recreate the bound method until either the object or the original function dies:
# 

class C:
      def method(self):

           print("method called!")

c = C()

r = weakref.ref(c.method)
r()

r = weakref.WeakMethod(c.method)

r()

# OUTPUT: '<bound method C.method of <__main__.C object at 0x7fc859830220>>'

r()()

# OUTPUT: 'method called!'

del c
gc.collect()

# OUTPUT: '0'

r()
