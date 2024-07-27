Arithmetic
==========

Ferrous provides a standard set of arithmetic operators for
all applicable primitive types of the categories :ref:`Unsigned Integer`,
:ref:`Signed Integer`, :ref:`Unsigned Size Type`, :ref:`Signed Size Type` and 
:ref:`IEEE-754`.

The following is a complete list of all arithmetic operators
applicable on the aforementioned type categories:



Saturating Arithmetic
---------------------

Ferrous provides a feature inspired by `the Zig programming language <https://ziglang.org/>`_
called saturating arithmetic.

Saturating arithmetic automatically clamps the result of the computation to the numeric range
of the type it is used on. Take the following code as an example:

.. code-block::

	pub(mod) struct Color {
		r: u8
		g: u8
		b: u8
		a: u8
	}

	pub(mod) fun multiply_rgb(color: Color, factor: f32): Color {
		let r = clamp(color.r * factor, 0x00, 0xFF)
		let g = clamp(color.g * factor, 0x00, 0xFF)
		let b = clamp(color.b * factor, 0x00, 0xFF)
		return Color(r, g, b, color.a)
	}

This code can be rewritten using saturating arithmetic as follows:

.. code-block::

	pub(mod) fun multiply_rgb(color: Color, factor: f32): Color {
		let r = color.r *| factor
		let g = color.g *| factor
		let b = color.b *| factor
		return Color(r, g, b, color.a)
	}