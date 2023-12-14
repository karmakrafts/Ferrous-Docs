Imaginary Types
===============

Imaginary types are types which cannot be materialized into a runtime type
directly. These types are a major component of the const programming model,
and they allow passing around more abstract compile-time constructs like strings,
literals, expressions and more.

The following table describes all currently implemented imaginary types
and their usages:

.. list-table:: Imaginary Types
	:header-rows: 1

	* - Name
	  - Literal
	  - Summary
	* - ``string``
	  - ``""``, ``#""#`` or ``/""/``
	  - A sequence of characters.
    * - ``literal``
      - ``literal()``
      - A string, integer, real, boolean or character literal.
    * - ``expr``
      - ``expr()``
      - Any expression.
    * - ``ident``
      - ``ident()``
      - Any qualified or unqualified identifier.
    * - ``token``
      - ``token()``
      - Any single token.
    * - ``vaargs``
      - none
      - Used to define a local va_list for C-interop.