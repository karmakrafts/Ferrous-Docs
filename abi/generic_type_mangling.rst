Generic Type Mangling
=====================

Another case which involes mangling of the type name is when
the given type has any number of generic parameters.
The compiler will append a pair of angle brackets (``<>``) to the mangled type name
which contain the concatinated list of mangled generic parameter
type names during monomorphization of the given UDT.

For example, if the type is

.. code-block::

	struct Foo<T, U> { 
	    // ...
	}

and its usage looks as follows

.. code-block::

	type MyType = Foo<bool, std::String>

the resulting mangled type name will be ``Foo<'B@std.String>``.

.. note:: 

	Note that builtin types are always preceded by a single ``'``
	while user defined types are always preceded by a single ``@``
	within the angle brackets of a mangled generic parameter list.