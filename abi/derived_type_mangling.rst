Derived Type Mangling
=====================
Type mangling is applied to derived types, that is types which are either
any depth of pointer or a reference, as well as any UDT with generic parameters.

If the given type is a pointer, a single ``*`` will be appended during
mangling for every level of pointer. On the other hand, if the given type 
is a reference, a single ``&`` will be appended to the mangled name.

For example, if the type is

.. code-block::

	type MyType = i32**&

the resulting mangled type name will be ``S32**&``.
The same applies for derived types whose backing type is a UDT.