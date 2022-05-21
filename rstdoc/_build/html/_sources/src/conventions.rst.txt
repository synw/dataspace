Conventions
===========

All functions that end with an underscore return an object.

.. highlight:: python

::

   ds.cols_()
   
The functions without an underscore return nothing

.. highlight:: python

::

   ds.sort("col1")
   
   
Note: some functions without underscore can still return something: ex: ``ds.show()``
returns a dataframe's head