"""
Jesus Zeno
We will have all the custom exceptions for our basic_backend and Model files.
Please note that ItemNotStored doesn't have a custom exception written for the class. This was to show
how custom error messages can be made in the functions of basic_backend. In contrast, I made custom
messages for the functions (ItemAlreadyStored) and the class ModelBasic (ModelItemAlreadyStored). The former
shows only the one error message from the ModelBasic class when there is an error with the object while
the latter shows both bascic_backend function and ModelBasic class errors. Both ways might be important
depending on the type of messages and programs being written. I would likely prefer the former method so
only one error message shows each time."""

class Error(Exception):
    """Base parent class for our defined exceptions"""
    pass

class IOError(Exception):
    pass

"""These will be children classes of Error class"""
# Meant to be raised by the basic_backend.py file
class ItemAlreadyStored(Error):
    def __init__(self, name):
        super().__init__()
        self._name = name
        print("'{}' item is already stored. Basic Backend function error.".format(self._name))

# Meant to be raised by the ModelBasic class
class ModelItemAlreadyStored(Error):
    def __init__(self, name):
        super().__init__()
        self._name = name
        print("'{}' item is already stored Model class error".format(self._name))


class ItemNotStored(Error):
    pass

# Meant to be raised by ModelBasic class
class ModelItemNotStored(Error):
    def __init__(self, name):
        super().__init__()
        self._name = name
        print("'{}' item is not stored. Model class error".format(self._name))

# Excpetion handling for input value types
class NotNumber(TypeError):
    pass

class NotString(TypeError):
    pass
