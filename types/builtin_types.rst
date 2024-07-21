Builtin Types
=============

Builtin types are types which cannot be modeled as a UDT but are
required as the most primitive form of representing a value.
That's why builtin types are also called primitive types in a lot
of languages.

The table below is a complete list of all available builtin types.

.. list-table:: Builtin Types
	:header-rows: 1

	* - Name
	  - Category
	  - Size (in bits)
	  - Min Value/Exponent Bits
	  - Max Value/Significant Bits

	* - ``void``
	  - `Void Type`_
	  - 0
	  - none
	  - none

	* - ``char``
	  - `Unsigned Integer`_
	  - 32
	  - :math:`0`
	  - :math:`4,294,967,295`

	* - ``bool``
	  - `Truth Type`_
	  - 8
	  - :math:`0`
	  - :math:`1`

	* - ``i<n>``
	  - `Signed Integer`_
	  - n
	  - :math:`-(2^{n-1})`
	  - :math:`2^{n-1}-1`

	* - ``isize``
	  - `Signed Size Type`_
	  - GPR Width (w)
	  - :math:`-(2^{w-1})`
	  - :math:`2^{w-1}-1`

	* - ``u<n>``
	  - `Unsigned Integer`_
	  - n
	  - :math:`0`
	  - :math:`2^n`

	* - ``usize``
	  - `Unsigned Size Type`_
	  - GPR Width (w)
	  - :math:`0`
	  - :math:`2^w`

	* - ``f16``
	  - `IEEE-754`_
	  - 16
	  - 5 Bits
	  - 10 Bits

	* - ``f32``
	  - `IEEE-754`_
	  - 32
	  - 8 Bits
	  - 23 Bits

	* - ``f64``
	  - `IEEE-754`_
	  - 64
	  - 11 Bits
	  - 52 Bits

	* - ``f128``
	  - `IEEE-754`_
	  - 128
	  - 15 Bits
	  - 112 Bits

.. _Void Type:

Void Type
~~~~~~~~~

A sizeless type that indicates a function which does not return any value. Using ``void`` as a function return type makes that function a subroutine.

.. _Truth Type:

Truth Type
~~~~~~~~~~

A boolean value which can either be ``true`` (on, 1, etc.) or ``false``
(off, 0, etc.). 

This type may also be used as a type for bitfields.

.. _Signed Integer:

Signed Integer
~~~~~~~~~~~~~~

A signed integer is an integer which may be negative or positive, but
has half the numeric range of its unsigned counterpart.

If an unsigned value is assigned to a signed integer, the literal value
will be converted to the numeric range of the given signed type and may under-/overflow. This means
a value of ``-1`` assigned to a ``u32`` will result in an underflow, setting all binary digits in the value to ``1``.

This type may also be used as a type for bitfields.

.. _Signed Size Type:

Signed Size Type
~~~~~~~~~~~~~~~~

A signed size type is guaranteed to be the size of a general-purpose
register on the target architecture, and has half the numeric range
of its unsigned counterpart since it can be negative.

If an unsigned value is assigned to a signed size value, the literal value
will be converted to the numeric range of the given signed size type and may under-/overflow. This means
a value of ``-1`` assigned to a ``usize`` will result in an underflow, setting all binary digits in the value to ``1``.

This type may also be used as a type for bitfields.

.. _Unsigned Integer:

Unsigned Integer
~~~~~~~~~~~~~~~~

An unsigned integer is an integer which may only be positive, but
has double the numeric range of its signed counterpart.

This type may also be used as a type for bitfields.

.. _Unsigned Size Type:

Unsigned Size Type
~~~~~~~~~~~~~~~~~~

An unsigned size type is guaranteed to be the size of a general-purpose
register on the target architecture, and has double the numeric range
of its signed counterpart since it cannot be negative.

This type may also be used as a type for bitfields.

.. _IEEE-754:

IEEE-754
~~~~~~~~

A half-, single-, double- or quadruple-precision floating point number.
For more information see `the IEEE 754 Wikipedia page <https://en.wikipedia.org/wiki/IEEE_754>`_.