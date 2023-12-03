Builtin Type Mangling
=====================
Builtin types are treated specially during mangling to save some
space in the identifier strings of types and functions.
The following table denotes all valid mangled builtin type names:

.. list-table:: Mangled Type Names
	:header-rows: 1

	* - Type
	  - Mangled Name
	* - ``i<width>``
	  - S<width>
	* - ``isize``
	  - SZ
	* - ``u<width>``
	  - U<width>
	* - ``usize``
	  - UZ
	* - ``f16``
	  - H
	* - ``f32``
	  - F
	* - ``f64``
	  - D
	* - ``f128``
	  - Q
	* - ``void``
	  - V
	* - ``char``
	  - C
	* - ``bool``
	  - B