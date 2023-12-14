Function Mangling
=================
Function mangling is always applied to prevent collissions for overloaded
functions and monomorphized functions with generic parameters.

In any case, the parameter types of the functions are mangled and concatinated
before they're appended to the mangled function name between a pair of parentheses ``()``.
For example, the function

.. code-block::

	// Function in foo.fe
	fun test_function(offset: isize, value: std::String): void* {
		// ...
	}

will have a mangled name of ``foo.test_function('SZ@std.String)``.

.. note:: 

	Note that builtin types are always preceded by a single ``'``
	while user defined types are always preceded by a single ``@``
	within the parentheses of a mangled function parameter list.