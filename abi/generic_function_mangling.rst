Generic Function Mangling
=========================

Just like with generic type mangling, the angle brackets ``<>`` are used to denote
generic parameters on a function when its name is mangled.

The following function

.. code-block::

	// Function in foo.fe
	pub fun testing<T>(value: T&, flag: bool): f32 {
		// ...
	}

with a usage of 

.. code-block::

	let x: f32 = foo::testing<i32>(100, true)

would have a mangled name of ``foo.testing<'S32>('S32&'B)`` after monomorphization.