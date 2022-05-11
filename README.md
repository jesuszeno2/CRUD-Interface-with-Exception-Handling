# CRUD Interface with Exception Handling
Custom exceptions have been introduced for the Model class. Note that it is not really necessary since Model could raise the same exceptions as basic_backend.py. However, this was an assignment to get some experience with exception writing, using and handling. The Model class raises its own exceptions that convey useful error messages.

Basic_backend.py is equipped to handle file IO errors and do the appropriate exception handling for this code. In addition there are exceptions at other critical points in the code. 

ModelBasic handles any basic_backend.py exceptions raised as well as its own.
