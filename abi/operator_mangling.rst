Operator Mangling
=================

Operators also require some form of mangling to allow overloading them in
user defined types. Ferrous simply looks up operators by their symbol and
retrieves their mangled name from an enum. 

Every operator function in Ferrous
uses the ``fe.op.`` prefix to uniquely identify them without colliding with
the user definable identifier range.

The following lists contain all valid overloadable operators in Ferrous:

.. list-table:: Arithmetic Operators
	:header-rows: 1

	* - Symbol
	  - Name
	  - Mangled Name
	* - ``+``
	  - Plus
	  - ``fe.op.plus``
	* - ``-``
	  - Minus
	  - ``fe.op.minus``
	* - ``*``
	  - Times
	  - ``fe.op.times``
	* - ``/``
	  - Divide
	  - ``fe.op.div``
	* - ``%``
	  - Modulo
	  - ``fe.op.mod``
	* - ``+|``
	  - Saturating Plus
	  - ``fe.op.splus``
	* - ``-|``
	  - Saturating Minus
	  - ``fe.op.sminus``
	* - ``*|``
	  - Saturating Times
	  - ``fe.op.stimes``
	* - ``/|``
	  - Saturating Divide
	  - ``fe.op.sdiv``
	* - ``%|``
	  - Saturating Modulo
	  - ``fe.op.smod``
	* - ``+=``
	  - Plus Assign
	  - ``fe.op.plus.assign``
	* - ``-=``
	  - Minus Assign
	  - ``fe.op.minus.assign``
	* - ``*=``
	  - Times Assign
	  - ``fe.op.times.assign``
	* - ``/=``
	  - Divide Assign
	  - ``fe.op.div.assign``
	* - ``%=``
	  - Modulo Assign
	  - ``fe.op.mod.assign``
	* - ``+|=``
	  - Saturating Plus Assign
	  - ``fe.op.splus.assign``
	* - ``-|=``
	  - Saturating Minus Assign
	  - ``fe.op.sminus.assign``
	* - ``*|=``
	  - Saturating Times Assign
	  - ``fe.op.stimes.assign``
	* - ``/|=``
	  - Saturating Divide Assign
	  - ``fe.op.sdiv.assign``
	* - ``%|=``
	  - Saturating Modulo Assign
	  - ``fe.op.smod.assign``
	* - ``&``
	  - Bitwise AND
	  - ``fe.op.and``
	* - ``&&``
	  - Short Circuit AND
	  - ``fe.op.scand``
	* - ``|``
	  - Bitwise OR
	  - ``fe.op.or``
	* - ``||``
	  - Short Circuit OR
	  - ``fe.op.scor``
	* - ``^``
	  - Bitwise XOR
	  - ``fe.op.xor``
	* - ``<<``
	  - Left Shift
	  - ``fe.op.shl``
	* - ``>>``
	  - Right Shift
	  - ``fe.op.shr``
	* - ``~``
	  - Bitwise Inverse
	  - ``fe.op.inv``
	* - ``&=``
	  - Bitwise AND Assign
	  - ``fe.op.and``
	* - ``|=``
	  - Bitwise OR Assign
	  - ``fe.op.or``
	* - ``^=``
	  - Bitwise XOR Assign
	  - ``fe.op.xor``
	* - ``<<=``
	  - Left Shift Assign
	  - ``fe.op.shl``
	* - ``>>=``
	  - Right Shift Assign
	  - ``fe.op.shr``
	* - ``~~x``
	  - Bitwise Pre-Inverse Assign
	  - ``fe.op.inv``
	* - ``x~~``
	  - Bitwise Post-Inverse Assign
	  - ``fe.op.inv``