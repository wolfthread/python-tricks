"""
This modules contains Python Tricks I enjoy from Dan Bader at Real Python (https://realpython.com/).

"""

from collections import namedtuple


def print_formatted_message(message):
    print(f"\n{'-' * len(message)}\n{message}\n{'-' * len(message)}\n")

def merge_dicts(a, b):
    """
    Merges two dicts in Python 3.5+ with a single expression.
    Python merges dictionary keys in the order listed in the expression, overwriting duplicates from left to right.

    :param a: dict
    :param b: dict
    :return: dict
    """
    merged = {**x, **y}
    return merged


def sort_dict_by_value(d):
    """
    Yields a dict representation of a dict sorted by value

    :param d: dict
    :return: list
    """
    sorted_d = sorted(d.items(), key=lambda x: x[1])
    return sorted_d

def get_method_on_dict(d, value):
    """
    When "get()" is called it checks if the given key exists in the dict.
    If it does exist, the value for that key is returned.
    If it does not exist then the value of the default argument is returned instead.

    :param d: dict
    :param value: key to look for in d
    :return: d[value] or default
    """
    return d.get(value, None)

def named_tuples_as_class(name, attributes):
    # make sure to import namedtuple from collections
    """
    Uses an alternative to manual class definition with named tuples.

    :param name: String starts with capital
    :param attributes: String separated by space
    :return: namedtuple
    """
    # checks format of name
    return namedtuple(name, attributes)

def addition(a, b):
    return a + b

def substraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def entire_division(a, b):
    return a // b

def division(a, b):
    return a / b

def modulo(a, b):
    return a % b


def dispatch_dict(fn, x, y):
    """
    Use a dictionary to emulate switch/case statements.

    :param operator: Function
    :param x: int or float
    :param y: int or float
    :return: int or float
    """
    operator = fn.__name__
    return {
        operator: lambda: fn(x,y)
    }.get(operator, lambda: None)()


name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}

def greeting(userid):
    return f"Hi {name_for_userid.get(userid, 'there')}!"


if __name__ == "__main__":
    print_formatted_message("Python Tricks from Dan Bader All Regrouped In A Single Module")
    print("We have got to start with import this:\n")
    import this
    print_formatted_message("Now get on with the Python Tricks...")
    x = {'a': 1, 'b': 2}
    y = {'b': 3, 'c': 4}
    print(f"Merging dictionaries {x} and {y} with merge_dicts function yields: {merge_dicts(x, y)}")
    xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
    print(f"\nSorting by value dictionary {xs} with sort_dict_by_value function yields: {sort_dict_by_value(xs)}")
    name_for_userid = {
        382: "Alice",
        590: "Bob",
        951: "Dilbert",
    }
    print(f"\nGetting item by value 382 from dictionary {name_for_userid} with get_method_on_dict function yields: {get_method_on_dict(name_for_userid, 382)}")
    Car = named_tuples_as_class('Car', 'color mileage')
    my_car = Car('red', 3812.4)
    print(f"\nUsing alternative to manual class definition with named tuples ('Car', 'color mileage') yields: {named_tuples_as_class('Car', 'color mileage')}")
    print(f"This class behaves as such: for example my_car = Car('red', 3812.4) yields object: {my_car}")
    print(f"Which can give us my_car.color as: {my_car.color} and my_car.mileage as: {my_car.mileage}")
    # to show that functions are first-class citizens in Python
    # passed as arguments to other functions, returned as values from other functions and assigned to variables and stored in data structure:
    funcs = [addition, substraction, multiplication, entire_division, division, modulo]
    print(f"\nMy functions are put in a list: \n{funcs}")
    print("And I can pass them as arguments to other functions, return them as values from other functions and assign them to variables.")
    a, b = (2, 3)
    print(f"For example, running all my operations for numbers {a} and {b}:")
    for fn in funcs:
        print(f"Running {fn.__name__} function: {fn(a, b)}")
    print(f"\nOr I can also use a dictionary to emulate switch/case statements by using the functions list just created:")
    for fn in funcs:
        print(f"I am calling the dispatch_dict function on numbers {a} and {b} by sending the function {fn.__name__} to it, which yields: {dispatch_dict(fn, a, b)}")
    print("\nThe get() method on dicts with its default argument is also quite awesome!")
    print(f"For example, I can simply call  greeting(382) and greeting(333333) and the first will return a name whereas the second the default argument.")
    print(greeting(382))
    print(greeting(333333))