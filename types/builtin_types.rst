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
	  - Sizeless
	  - 0
	  - none
	  - none
	* - ``char``
	  - Signed Integer
	  - 8
	  - :math:`-128`
	  - :math:`127`
	* - ``bool``
	  - Truth Value
	  - 1 (8)
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
	  - `IEEE-754 Half-Precision`_
	  - 16
	  - 5 Bits
	  - 10 Bits
	* - ``f32``
	  - `IEEE-754 Single-Precision`_
	  - 32
	  - 8 Bits
	  - 23 Bits
	* - ``f64``
	  - `IEEE-754 Double-Precision`_
	  - 64
	  - 11 Bits
	  - 52 Bits
	* - ``f128``
	  - `IEEE-754 Quadruple-Precision`_
	  - 128
	  - 15 Bits
	  - 112 Bits

.. _Signed Integer:

Signed Integer
~~~~~~~~~~~~~~

A signed integer is an integer which may be negative or positive, but
has half the numeric range of its unsigned counterpart.

.. _Signed Size Type:

Signed Size Type
~~~~~~~~~~~~~~~~

A signed size type is guaranteed to be the size of a general-purpose
register on the target architecture, and has half the numeric range
of its unsigned counterpart since it can be negative.

.. _Unsigned Integer:

Unsigned Integer
~~~~~~~~~~~~~~~~

An unsigned integer is an integer which may only be positive, but
has double the numeric range of its signed counterpart.

.. _Unsigned Size Type:

Unsigned Size Type
~~~~~~~~~~~~~~~~~~

An unsigned size type is guaranteed to be the size of a general-purpose
register on the target architecture, and has double the numeric range
of its signed counterpart since it cannot be negative.

.. _IEEE-754 Half-Precision:

IEEE-754 Half-Precision
~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html
	:file: ../_images/IEEE754-HP.svg

.. _IEEE-754 Single-Precision:

IEEE-754 Single-Precision
~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html
	:file: ../_images/IEEE754-SP.svg

.. _IEEE-754 Double-Precision:

IEEE-754 Double-Precision
~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html
	:file: ../_images/IEEE754-DP.svg

.. _IEEE-754 Quadruple-Precision:

IEEE-754 Quadruple-Precision
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html
	:file: ../_images/IEEE754-QP.svg