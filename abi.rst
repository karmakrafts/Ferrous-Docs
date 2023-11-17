ABI
===
The application binary interface or ABI mainly defines a standard
way of what CPU registers to use for which parameters when calling
a function, as well as conventions for name mangling in the Ferrous
programming language which is required for things like function 
overloading and structure monomorphization.

By default the Ferrous ABI relies on the standard ``cdecl`` calling
convention for simplicity purposes.

Mangling
--------
Mangling is the process of transforming the name of a type or function
during compile time, mainly to avoid possible collissions.

Type Mangling
~~~~~~~~~~~~~

Function Mangling
~~~~~~~~~~~~~~~~~