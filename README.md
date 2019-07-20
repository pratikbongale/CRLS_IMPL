### CRLS implementation in python 

#### Create a virtual environment 
```
sudo apt-get install python-virtualenv
virtualenv --python=/usr/bin/python3.6 env_crls_impl
source env_crls_impl/bin/activate
```

#### Clone repository
```
git clone https://github.com/pratikbongale/CRLS_IMPL.git
cd active_learning_label_distributions
pip install -r requirements.txt
```
---------
#### How to run
```
python filename.py [arg1] [arg2] ...
```

#### How to test

##### Simply run the program
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
    
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
```


##### Command
```
python -m unittest -v insertion_sort.py
```

[Organizing Tests in a program](https://docs.python.org/3/library/unittest.html#organizing-tests)

- A test fixture is created by inheriting unittest.TestCase and having methods setUp, tearDown, and test_*.
- Use assert*() methods from unittest.TestCase for evaluating results.
- Calling unittest.main() will collect all the module’s test cases and execute them.
- We can also build a testsuite and add tests to it
- recommended to create a separate module for test cases (eg. test_widget.py)



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
    def version(self): return "1.0"
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

- For multiple inheritance, follow order left to right to find a method
```python
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
