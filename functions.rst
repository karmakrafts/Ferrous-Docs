Functions
=========

Functions are reusable blocks of code which make up your program.
Some people may refer to certain functions as methods, procedures or subroutines
depending on the programming language and context.

A function may be defined using the ``fun`` keyword in Ferrous.
The following illustrates an example of a simple function which prints the
text ``Hellord!`` if the given value is less than 10.

.. code-block::

	fun do_the_thing(value: i32) {
		if(value >= 10) return
		println("Hellord!")
	}

A function may be invoked (or called) by referring to it by its identifier
and passing the required parameters.
The following example illustrates a call of the ``do_the_thing`` function:

.. code-block::

	do_the_thing(8)

Every function call is an expression whose type is the return type of the 
called function. In this case the expression would be of the type ``void``
which is referred to as a statement.