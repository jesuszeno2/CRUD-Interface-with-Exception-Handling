"""
Jesus Zeno SIE 508 Assignment 5.
Basic_backend with exception handling. We have modified the original basic_backend CRUD file to allow for
exception handling around critical code blocks.
basic_backend.py: simple CRUD backend to store inventory items
"""



import Model
import mvc_exceptions as mvc_exc
import csv

item_type = "product"

## Function reads specified file and outputs a list ##
def read_inv():
    try:
        with open("current_inv.txt", 'r') as file:
            items = []
            temp = csv.DictReader(file)
            for row in temp:
                items.append(row)
    except IOError:
        print("File not accessible. Please check that the file is in the proper directory or make a new one.")
        items = []
    return items


## Function writes list to specified file ##
def write_inv(items):
    try:
        with open("current_inv.txt", 'w', newline='') as file:
            headers = ['name', 'price', 'quantity']
            csv_file = csv.DictWriter(file, fieldnames=headers)
            csv_file.writeheader()
            csv_file.writerows(items)
            print("Inventory file updated!")
    except IOError:
        print("Unable to write file.")



# create item, add it to file
def create_item(name, price, quantity):
    # reference list created from reading file
    items = read_inv()
    # search first if that item already exists
    results = list(filter(lambda x: x['name'] == name, items))
    # if we find an existing item with the name, we raise an exception
    if results:
        raise mvc_exc.ItemAlreadyStored(name)
    # if not, we append the item to the dictionary
    else:
        items.append({'name': name, 'price': price, 'quantity': quantity})
        # appended dictionary is written to file
        write_inv(items)


# bulk create times
def create_items(app_items):
    items = app_items
    write_inv(items)


# read a particular item
def read_item(name):
    items = read_inv()
    myitems = list(filter(lambda x: x['name'] == name, items))
    if myitems:
        return myitems[0]
    else:
        raise mvc_exc.ItemNotStored(
            'Can\'t read "{}" because it\'s not stored'.format(name))


# read all items
def read_items():
    items = read_inv()
    return [item for item in items]


# update item in file
def update_item(name, price, quantity):
    items = read_inv()
    # Python 3.x removed tuple parameters unpacking (PEP 3113), so we have to do it manually (i_x is a tuple, idxs_items is a list of tuples)
    idxs_items = list(
        filter(lambda i_x: i_x[1]['name'] == name, enumerate(items)))
    if idxs_items:
        i, item_to_update = idxs_items[0][0], idxs_items[0][1]
        items[i] = {'name': name, 'price': price, 'quantity': quantity}
        write_inv(items)
    else:
        raise mvc_exc.ItemNotStored(
            'Can\'t update "{}" because it\'s not stored'.format(name))


# delete item from file
def delete_item(name):
    items = read_inv()
    # Python 3.x removed tuple parameters unpacking (PEP 3113), so we have to do it manually (i_x is a tuple, idxs_items is a list of tuples)
    idxs_items = list(
        filter(lambda i_x: i_x[1]['name'] == name, enumerate(items)))
    # print("index items", idxs_items)
    if idxs_items:
        i, item_to_delete = idxs_items[0][0], idxs_items[0][1]
        print("idxs_items[0][0], idxs_items[0][1]: ", idxs_items[0][0], " item in list, value:", idxs_items[0][1])
        del items[i]
        write_inv(items)
    else:
        raise mvc_exc.ItemNotStored(
            'Can\'t delete "{}" because it\'s not stored'.format(name))


def main():
    my_items = [
        {'name': 'bread', 'price': 2.5, 'quantity': 20},
        {'name': 'milk', 'price': 4.0, 'quantity': 10},
        {'name': 'eggs', 'price': 4.0, 'quantity': 5},
        {'name': 'juice', 'price': 5.75, 'quantity': 10},
        {'name': 'cake', 'price': 10.0, 'quantity': 2},
    ]

    ########################################################
    ## Statements to show functionality of program ##

    # Insert/create new item to the file #
    # create_item('apples', 1.55, 13)

    # Update item in the file #
    # update_item('apples', 1.0, 5)

    # Delete item from the file #
    # delete_item('apples')

    ########################################################

    """Read inventory works as intended"""
    # Read inventory. If we try to read inventory before it's created, we get an exception.
    print("Try to read items before file is written.")
    print(read_items())

    # # CREATE #
    create_items(my_items)

    # Read items. Now it will read items since they have been created from my items.
    print("Read items after file is written.")
    print(read_items())



    """Try to create an item and raise specific exception as to what is stored. This works as intended"""
    try:
        print("Create eggs:")
        create_item('eggs', price=10.0, quantity=10)
    except mvc_exc.ItemAlreadyStored as e:
        print(e)

    """Create item works as intended"""
    # if we try to re-create an object we get an ItemAlreadyStored exception
    try:
        print("Create wine:")
        create_item('wine', price=10.0, quantity=10)
    except Exception as e:
        print(e)

    try:
        print("Create bread:")
        create_item('bread', price=10.0, quantity=10)
    except Exception as e:
        print(e)

    # READ
    print('READ items')
    print(read_items())

    """Read item works as intended"""
    # if we try to read an object not stored we get an ItemNotStored exception
    try:
        print('READ meat')
        print(read_item('meat'))
    except mvc_exc.ItemNotStored as e:
        print(e)

    try:
        print('READ bread')
        print(read_item('bread'))
    except mvc_exc.ItemNotStored as e:
        print(e)

    """Update item works as intended"""
    # UPDATE
    try:
        print('UPDATE bread')
        update_item('bread', price=2.0, quantity=25)
    except mvc_exc.ItemNotStored as e:
        print(e)

    try:
        print("Update milk:")
        update_item('milk', price=2.0, quantity=24)
    except mvc_exc.ItemNotStored as e:
        print(e)

    # Check Updates
    print(read_item('bread'))
    print(read_item('milk'))
    # if we try to update an object not stored we get an ItemNotStored exception
    try:
        print('UPDATE chocolate')
        update_item('chocolate', price=10.0, quantity=20)
    except mvc_exc.ItemNotStored as e:
        print(e)


    """Works as intended"""
    # DELETE
    print(read_items())
    try:
        print('DELETE wine')
        delete_item('wine')
    except mvc_exc.ItemNotStored as e:
        print(e)
    # if we try to delete an object not stored we get an ItemNotStored exception
    try:
        print('DELETE chocolate')
        delete_item('chocolate')
    except mvc_exc.ItemNotStored as e:
        print(e)

    print('READ items')
    print(read_items())

    """Make ModelBasic object to test if things work."""
    print("\nInstantiate inventory_model object:")
    inventory_model = Model.ModelBasic(my_items)

    """Items can be read from object"""
    # Note that due to class design, we wouldn't be able to instantiate the object without passing a list
    # of item(s) as a parameter. Therefore, a custom exception wasn't created for reading items in a file
    # that doesn't exist.
    print("Read items from inventory model object:")
    print(inventory_model.read_items())

    """Create item in class works as intended"""
    # Create item for inventory model object. Throws class specific exception if item is already stored
    try:
        print("CREATE wine:")
        inventory_model.create_item('wine', price=15.5, quantity=15)
    # This one allows us know the type error and moves on
    except Exception as e:
        print(e)

    try:
        print("CREATE bread:")
        inventory_model.create_item('bread', price=15.5, quantity=15)
    # This one allows us know the type error and moves on
    except Exception as e:
        print(e)

    """Read item from class works as intended"""
    # We try to read the item cookies which doesn't exist, and it shows the class specific error.
    try:
        print("READ cookies:")
        print(inventory_model.read_item('cookies'))
    except Exception as e:
        print(e)
    # Works for items that exist
    try:
        print("READ milk:")
        print(inventory_model.read_item('milk'))
    except Exception as e:
        print(e)

    """Update item in class works as intended"""
    # Try to update an item. If it exists, then we can update it, if it doesn't then custom class exception
    # will show.
    try:
        print("UPDATE milk:")
        inventory_model.update_item('milk', price=2.0, quantity=24)
        # We are going to just check that milk updated properly.
        try:
            print("Check that milk was updated properly:")
            print(inventory_model.read_item('milk'))
        except Exception as e:
            print(e)
    # This one allows us know the type error and moves on
    except Exception as e:
        print(e)

    try:
        print("UPDATE chocolate")
        inventory_model.update_item('chocolate', price=15.5, quantity=15)
    # This one allows us know the type error and moves on
    except Exception as e:
        print(e)


    """Delete item in class works as intended"""
    # Try to delete an item. If it exists, then we can delete it, if it doesn't then custom class exception
    # will show.
    try:
        print("DELETE milk:")
        inventory_model.delete_item('milk')
        # We are going to just check that milk deleted properly.
        try:
            print("Check that milk was deleted properly:")
            print(inventory_model.read_item('milk'))
        except Exception as e:
            print(e)
    # This one allows us know the type error and moves on
    except Exception as e:
        print(e)

    try:
        print("DELETE chocolate")
        inventory_model.delete_item('chocolate')
    # This one allows us know the type error and moves on
    except Exception as e:
        print(e)

    print("Read inventory model object items:")
    print(inventory_model.read_items())


if __name__ == '__main__':
    main()