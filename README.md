# Python Tricks

Tools, tips, tricks taken from Python Tricks by Dan Bader at Real Python

### Purpose

It contains Python Tricks I enjoy and use from Dan Bader at Real Python (https://realpython.com/).
I created this to regroup them in a single place for reference.

### Installing

Clone or download repository. Navigate to the folder. To see demo of functions run:

```
python pythontricks.py
```

And you should see something like this:

```
-------------------------------------------------------------
Python Tricks from Dan Bader All Regrouped In A Single Module
-------------------------------------------------------------

We have got to start with import this:

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

------------------------------------
Now get on with the Python Tricks...
------------------------------------

Merging dictionaries {'a': 1, 'b': 2} and {'b': 3, 'c': 4} with merge_dicts function yields: {'a': 1, 'b': 3, 'c': 4}

Sorting by value dictionary {'a': 4, 'b': 3, 'c': 2, 'd': 1} with sort_dict_by_value function yields: [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

Getting item by value 382 from dictionary {382: 'Alice', 590: 'Bob', 951: 'Dilbert'} with get_method_on_dict function yields: Alice

Using alternative to manual class definition with named tuples ('Car', 'color mileage') yields: <class '__main__.Car'>
This class behaves as such: for example my_car = Car('red', 3812.4) yields object: Car(color='red', mileage=3812.4)
Which can give us my_car.color as: red and my_car.mileage as: 3812.4

My functions are put in a list:
[<function addition at 0x015568E8>, <function substraction at 0x01556930>, <function multiplication at 0x01556978>, <function entire_division at 0x015569C0>, <function division at 0x01556A08>, <function modulo at 0x01556A50>]
And I can pass them as arguments to other functions, return them as values from other functions and assign them to variables.
For example, running all my operations for numbers 2 and 3:
Running addition function: 5
Running substraction function: -1
Running multiplication function: 6
Running entire_division function: 0
Running division function: 0.6666666666666666
Running modulo function: 2

Or I can also use a dictionary to emulate switch/case statements by using the functions list just created:
I am calling the dispatch_dict function on numbers 2 and 3 by sending the function addition to it, which yields: 5
I am calling the dispatch_dict function on numbers 2 and 3 by sending the function substraction to it, which yields: -1
I am calling the dispatch_dict function on numbers 2 and 3 by sending the function multiplication to it, which yields: 6
I am calling the dispatch_dict function on numbers 2 and 3 by sending the function entire_division to it, which yields: 0
I am calling the dispatch_dict function on numbers 2 and 3 by sending the function division to it, which yields: 0.6666666666666666
I am calling the dispatch_dict function on numbers 2 and 3 by sending the function modulo to it, which yields: 2

```

You can also import the module and use each functions upon your needs.
