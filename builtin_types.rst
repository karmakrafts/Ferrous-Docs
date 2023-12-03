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
	  - Size (in bytes)
	* - ``void``
	  - Sizeless
	  - 0
	* - ``char``
	  - Signed Integer
	  - 1
	* - ``bool``
	  - Truth Value
	  - 1
	* - ``i8``
	  - Signed Integer
	  - 1
	* - ``i16``
	  - Signed Integer
	  - 2
	* - ``i32``
	  - Signed Integer
	  - 4
	* - ``i64``
	  - Signed Integer
	  - 8
	* - ``i128``
	  - Signed Integer
	  - 16
	* - ``i256``
	  - Signed Integer
	  - 32
	* - ``i512``
	  - Signed Integer
	  - 64
	* - ``isize``
	  - Signed Integer
	  - GPR Width
	* - ``u8``
	  - Unsigned Integer
	  - 1
	* - ``u16``
	  - Unsigned Integer
	  - 2
	* - ``u32``
	  - Unsigned Integer
	  - 4
	* - ``u64``
	  - Unsigned Integer
	  - 8
	* - ``u128``
	  - Unsigned Integer
	  - 16
	* - ``u256``
	  - Unsigned Integer
	  - 32
	* - ``u512``
	  - Unsigned Integer
	  - 64
	* - ``usize``
	  - Unsigned Integer
	  - GPR Width
	* - ``f16``
	  - IEEE-754
	  - 2
	* - ``f32``
	  - IEEE-754
	  - 4
	* - ``f64``
	  - IEEE-754
	  - 8
	* - ``f128``
	  - IEEE-754
	  - 16