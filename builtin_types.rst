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
	* - ``isize``
	  - Signed Integer
	  - 8 on 64-bit, 4 on 32-bit
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
	* - ``usize``
	  - Unsigned Integer
	  - 8 on 64-bit, 4 on 32-bit
	* - ``f32``
	  - IEEE-754
	  - 4
	* - ``f64``
	  - IEEE-754
	  - 8