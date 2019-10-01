### CRLS implementation in python 

#### set up

##### Create a virtual environment 
```
sudo apt-get install python-virtualenv
virtualenv --python=/usr/bin/python3.6 env_crls_impl
source env_crls_impl/bin/activate
```

##### Clone repository
```
git clone https://github.com/pratikbongale/CRLS_IMPL.git
cd active_learning_label_distributions
pip install -r requirements.txt
```

##### How to run
```
python filename.py [arg1] [arg2] ...
```

#### How to test

##### How to read test results
- Test frameworks generate/raise AssertionError
- They write the outputs as [..F..FF..] where dots'.' represent passed tests, and F is for Fail 

##### Built-in test features
```python
assert sum([1,2,3]) == 6, "Sum should be 6"
assert sum([1,1,1]) == 6, "Sum should be 6"  # will print the error message
```

##### Python test runners:
- unittest (offered with python std library, defines its own assert methods)
- pytest (easy, allows use of built-in assert statements)

##### Unittest

Requires you to: 
- Inherit class TestClass and put your tests into methods of this class
- Use special assert_*() methods
- [Ref: Testing for beginners](https://realpython.com/python-testing/#testing-your-code)

- A test fixture is created by inheriting unittest.TestCase and having methods setUp, tearDown, and test_*.
- Use assert*() methods from unittest.TestCase for evaluating results.
- Calling unittest.main() will collect all the module’s test cases and execute them.
- We can also build a testsuite and add tests to it
- recommended to create a separate module for test cases (eg. test_widget.py)
- [Ref: Organizing Tests in a program](https://docs.python.org/3/library/unittest.html#organizing-tests)

```python
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
    
        
        with self.assertRaises(TypeError):      # expecting TypeError
            s.split('2222')   


if __name__ == '__main__':
    
    # dont need this when running code as: python -m unittest -v module_name
    # Need this when running code as: python module_name.py
    unittest.main()     # run all tests in this module 
```

```
python -m unittest -v insertion_sort.py
```

##### Pytest

- Needs to be installed: pip install pytest
- Easy to use, define simple functions with assert statements
- output provides detailed explanations, but we can suppress those in quiet mode
- runs all files with test_*.py or *_test.py filenames

```python
class TestSum:
    def test_sum(self):
        assert sum([1,2,3]) == 6
        assert sum([1,1,1]) == 6

def test_sum1():
    assert 1 == 1, "Are you kidding? I am unreachable comment"
```

Run pytest:
```
 $ pytest           # default mode
 $ pytest -q        # quiet mode
```

Output:
```
================ FAILURES ==================================
_____________ TestSum.test_sum _____________________________

self = <hello_world.TestSum object at 0x7f918befc4a8>

    def test_sum(self):
        assert sum([1,2,3]) == 6
>       assert sum([1,1,1]) == 6
E       assert 3 == 6
E        +  where 3 = sum([1, 1, 1])

hello_world.py:6: AssertionError

```

@pytest.fixture: 
- allow us to set up some helper code that should run before any test.
- utilize it if you see any duplicate code in multiple tests
- they can be parameterized as below:
```python
# content of conftest.py
import pytest
import smtplib

# below function will be run once using every parameter
# each test will be run on all parameters in params
# params can be accessed by a special 'request' object
@pytest.fixture(scope="module", params=["smtp.gmail.com", "mail.python.org"])
def smtp_connection(request):

    # similar to setUp()
    smtp_connection = smtplib.SMTP(request.param, 587, timeout=5)
    yield smtp_connection

    # similar to tearDown(), only executed after the last test using this fixture executes
    print("finalizing {}".format(smtp_connection))
    smtp_connection.close()
```
- parameterizing test function with different arguments
- means checking a function with different values of inp/exp
```python
# content of test_expectation.py
import pytest

@pytest.mark.parametrize(
    "test_input,expected",
    [("3+5", 8), ("2+4", 6), pytest.param("6*9", 42, marks=pytest.mark.xfail)],
)
def test_eval(test_input, expected):
    assert eval(test_input) == expected


# you can stack multiple arguments
@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_foo(x, y):
    # this will check:
    # x = 0, y = 2
    # x = 0, y = 3
    # x = 1, y = 2
    # x = 1, y = 3
    pass
```

- the 3rd parameter is marked to `xfail`
- which means `expected to fail`, so output will show as below:
```
> **..x**
> === 2 passed, 1 xfailed in 0.12s ===
```
- there are more such markers (skip, skipif, parametrize)
- and we can also define our own markers

Following command prints the docstrings in fixtures.
```pytest --fixtures```


#### Python Idiosyncrasies

##### Q. How does python pass values? 
- uses Pass-by-object: each parameter is first passed by reference, however, if a new object is assigned to that reference, it switches to Pass-by-value.
- def foo(*args) defines variable number of arguments. it is received in the function as a tuple of values
- to pass a list instead of several numbers as arguments, we call foo as: lst = [1,2,4] foo(*lst) Here we unpack lst into 3 values
- def foo(**kwrds) is used for passing (k,v) pairs.
- [Reference](https://www.python-course.eu/python3_passing_arguments.php)

```
Variable number of arguments (*)
In function definitions:
>>> def foo(*args):
        print(args)
>>> foo(1,4,3,2,5)
(1, 4, 3, 2, 5)

In function calls:
>>> def foo(a,b):
        print(a, b)
>>> l = [1,3]
>>> foo(*l)    

------------------------------------
Keyword arguments (**)
In function definition
>>> def foo(**kwrds):
        print(kwrds)
>>> foo(x=1, y=2)
    {'x':1, 'y':2}

In function calls     
>>> def f(a,b,x,y):
...     print(a,b,x,y)
...
>>> d = {'a':'append', 'b':'block','x':'extract','y':'yes'}
>>> f(**d)
('append', 'block', 'extract', 'yes')
```


```
mixture of *, **
>>> t = (47,11)
>>> d = {'x':'extract','y':'yes'}
>>> f(*t, **d)
(47, 11, 'extract', 'yes')
>>> 
```

##### Q. How does python support interfaces? how to declare private members?

Private members:
- No concept of private members in python, we call them non-public.
- We use naming conventions to differentiate btw public / non-public
- Add an 'Underscore' before variable name: non-public 
- This is not enforced, they should be treated as private

Interfaces:
- python doesnt have interfaces as it supports multiple inheritance
- we do have abstract base classes(cannot be instantiated)
```python
from abc import ABCMeta, abstractmethod

class IInterface:
    __metaclass__ = ABCMeta

    @classmethod
    def version(cls): return "1.0"
    
    @abstractmethod
    def show(self): raise NotImplementedError
    
class MyServer(IInterface):
    def show(self):
        return "Hellow world"

class MyClient(object):

    def __init__(self, server):
        if not isinstance(server, IInterface): raise Exception('Bad interface')
        if not IInterface.version() == '1.0': raise Exception('Bad revision')

        self._server = server


    def client_show(self):
        self._server.show()

MyClient(MyServer()).client_show()
```

- For multiple inheritance, follow order left to right to find a method, also called MRO(Method Resolution Order)
```python
class First:
    def show(self):
        pass

class Second:
    def show(self):
        pass

class Third(First, Second):
    def show(self):
        pass
    
class Main(Third):
    def __init__(self):
        self.show()  # here order followed will be [Third, First, Second]
```  

- when the case is ambiguous, python raises an exception

##### Q. difference between 'is' and '=='?
- 'is' will return True if two variables point to the same object
- '==' if the objects referred to by the variables are equal

##### Q. How does python compare two objects?
- using __eq__() and __ne__() methods
- there are many others [here](https://devinpractice.com/2016/11/29/python-objects-comparison/)

##### Q. how should we name python modules/packages/classes/functions/variables?
- everything except class names should have short, all-lowercase names
- Python module: source file (ex. foobar.py)
- Python package: directory (ex. bst)
- class names should have __CapWords__ format.

##### Q. How do we define class methods in python? static methods vs class methods?
- we use `@staticmethod` / `@classmethod` builtin decorator to define them
```python
class Demo:
    def __init__(self, x, y):
        pass

    @classmethod
    def class_method(cls, a1, a2):
        return cls(a1, a2) 

    @staticmethod
    def static_method(a1, a2):
        return a1 < a2
```
- static methods cannot access/modify the state of class, they are utility functions
- static methods take some parameters, work on them and return some result
- class methods can access/modify class state, they are used mostly as factory methods
- class methods take class as first parameter always. 
- Example for both -> [geeksforgeeks.org](https://www.geeksforgeeks.org/class-method-vs-static-method-python/)

##### Q. duck typing, type hints and static checking in python?
- "if it walks like a duck and it quacks like a duck, then it must be a duck"
- In normal typing, the type declaration is checked to see if an object can do a particular task/func
- In duck typing, the presence of certain methods and properties is checked to determine objs' suitability.
- example:
```python
class TheHobbit:
    def __len__(self):
        return 95022

the_hobbit = TheHobbit()
print(len(the_hobbit))   # 95022     

# this works because len() checks only for presence of __len__ method in the object the_hobbit 
def len(obj):
    return obj.__len__()
```

- _Type hints_: not enforced by python, its just a hint
```python
def headline(text: str, align: bool = True) -> str:
    pass
```
- for primitive types, we can directly use them, however, for complex types, we use module typing:
- [documentation](https://docs.python.org/3/library/typing.html#newtype)
- [cheatsheet](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html)

```python
from typing import List
def foo(l1: List[str]) -> None:
    pass

# we can also assign alias
Vector = List[float]
def foo1(v: Vector) -> None:
    pass
``` 

_Static Typing_: use `mypy abc.py`, you need to do `pip install mypy` before using it. 
