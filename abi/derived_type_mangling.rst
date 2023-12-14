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

Type modifiers are also taken into account when mangling
derived types. The following table denotes all valid type modifiers
and their mangled symbol counterparts:

.. list-table:: Mangled Modifier Symbols
	:header-rows: 1

	* - Keyword
	  - Mangled Symbol
	* - ``mut``
	  - =
	* - ``tls``
	  - ^
	* - ``atomic``
	  - $
	* - ``volatile``
	  - !

A simple example of this would be the following type alias:

.. code-block::

	type MyRefType = atomic i32&

Where the mangled name of the type would be ``$S32&`` where the ``$``
precedes the derived type attribute ``&`` and the type itself. This applies to all mangled modifiers.

.. note::
	
	While the order in which the attribute appears after the modifiers is always
	fixed, the order of the modifiers itself does not have to be and modifiers may
	appear in any order.

If the modifier applies to the attribute like in the example below

.. code-block::

	type MyPtrType = i32 mut atomic*

The mangled name of the above type would be ``S32=$*``, since the modifiers always apply to 
whatever is on their righthand side.