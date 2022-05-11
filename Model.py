"""
Jesus Zeno SIE 508 Assignment 5. This ModelBasic class sets up the object for the CRUD system.
"""

import basic_backend
import mvc_exceptions as mvc_exc


class ModelBasic(object):
    def __init__(self, application_items):
        self._item_type = 'product'
        self.create_items(application_items)

    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, new_item_type):
        self._item_type = new_item_type

    def create_item(self, name, price, quantity):
        self._name = name
        # We make an if statement to read the item we want to create first. If we can read it, then we know
        # it's already stored. We can then raise the custom exception for the class.
        try:
            if basic_backend.read_item(self._name)['name'] == self._name:
                raise mvc_exc.ModelItemAlreadyStored(self._name)
        except:
            basic_backend.create_item(self._name, price, quantity)

    def create_items(self, items):
        basic_backend.create_items(items)

    def read_item(self, name):
        self._name = name
        # If we can read the item then we will return the message of what the item is. Otherwise, we will
        # raise the custom Model class exception.
        try:
            if basic_backend.read_item(self._name)['name'] == self._name:
                msg = basic_backend.read_item(name)
        except:
            raise mvc_exc.ModelItemNotStored(self._name)
        return msg

    # Note that due to class design, we wouldn't be able to instantiate the object without passing a list
    # of item(s) as a parameter. Therefore, a custom exception for this method wasn't created for reading
    # items in a file that doesn't exist.
    def read_items(self):
        return basic_backend.read_items()

    def update_item(self, name, price, quantity):
        self._name = name
        # If we can read the item then we will update the item. Otherwise, we will
        # raise the custom Model class exception.
        try:
            if basic_backend.read_item(self._name)['name'] == self._name:
                basic_backend.update_item(self._name, price, quantity)
        except:
            raise mvc_exc.ModelItemNotStored(self._name)
        return

    def delete_item(self, name):
        self._name = name
        # If we can read the item then we will update the item. Otherwise, we will
        # raise the custom Model class exception.
        try:
            if basic_backend.read_item(self._name)['name'] == self._name:
                basic_backend.delete_item(self._name)
        except:
            raise mvc_exc.ModelItemNotStored(self._name)
        return
