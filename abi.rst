ABI
===
The application binary interface or ABI mainly defines a standard
way of how the compiler mangles names of types and functions.
If a compiler implementation implements the ABI correctly, it produces
modules which are binary compatible to Ferrous modules.

Builtin Mangling
----------------
Builtin types are treated specially during mangling to save some
space in the identifier strings of types and functions.
The following table denotes all valid mangled builtin type names:

.. list-table:: Mangled Builtin Type Names
	:header-rows: 1

	* - Type
	  - Mangled Name
	* - ``i8``
	  - sB
	* - ``i16``
	  - sS
	* - ``i32``
	  - sI
	* - ``i64``
	  - sL
	* - ``isize``
	  - sZ
	* - ``u8``
	  - uB
	* - ``u16``
	  - uS
	* - ``u32``
	  - uI
	* - ``u64``
	  - uL
	* - ``usize``
	  - uZ
	* - ``f32``
	  - F
	* - ``f64``
	  - D
	* - ``void``
	  - V
	* - ``char``
	  - C
	* - ``bool``
	  - T

Type Mangling
-------------
Type mangling is applied to derived types, that is types which are either
any depth of pointer or a reference, as well as any UDT with generic parameters.

If the given type is a pointer, a single ``P`` will be appended during
mangling for every level of pointer. On the other hand, if the given type 
is a reference, a single ``R`` will be appended to the mangled name.

For example, if the type is

.. code-block:: Ferrous

	&**i32

The resulting mangled type name will be ``sIPPR``.
The same applies for derived types whose backing type is a UDT.

Another case which involes mangling of the type name is when
the given type has any number of generic parameters.
The compiler will append a single ``$`` to the mangled type name
followed by the concatinated list of mangled generic parameter
types during monomorphization of the given UDT.

For example, if the type is

.. code-block:: Ferrous

	struct Foo<T, U> { /* ... */ }

And its usage looks as follows

.. code-block:: Ferrous

	Foo<bool, usize>

The resulting mangled type name will be ``Foo$TuZ``.

Function Mangling
-----------------
Function mangling is always applied to prevent collissions for overloaded
functions and monomorphized functions with generic parameters.

