ABI
===

The application binary interface or ABI mainly defines a standard
way of how the compiler mangles names of types and functions.
If a compiler implementation implements the ABI correctly, it produces
modules which are binary compatible to Ferrous modules.

.. toctree::
   :maxdepth: 4
   :caption: Mangling:

   builtin_type_mangling
   derived_type_mangling
   generic_type_mangling
   function_mangling
   generic_function_mangling
   operator_mangling