# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> List and tuples are both ways to store multiple pieces of information (objects) such as numerical values or strings.  The stored information can be retrieved by index number for both.
>>
>> LIsts are mutable, so the stored values can change, while tuples are immutable, so the stored values cannot change.  Tuples take less memory, and they can be used as keys in dictionaries.  Syntax-wise, lists are created by brackets, tuples are created with parentheses (or nothing).
>>
>> A dictionary key is found by a hash value.  If the key is changed, so would the hash value, and it could no longer be used to find the dictionary values associated with the previous key/hash value.  Thus, dictionary keys need to be immutable, which tuples are.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets both used to store multiple objects such as strings or numerical values.  Unlike lists, sets are unordered so you can't refer to objects by index position, and sets cannot hold duplicate objects.  They also have very different operations, largely because of the different characteristics of sets and lists.
>>
>> As an example, you can add two lists together (let's call them `A` and `B`) by the operation `A + B`.  This will return a new list that contains all the elements of `A` and `B`, including duplicates.  But to combine two sets (let's call them X and Y), you can't make a new set that retains the duplicate elements, and you can't use the operation `+`.  But you can find the union of the two sets by `X | Y` which will return a set containing all elements in X and Y but no duplicates.  Or you can find the intersection of the two sets by `X & Y`, which will return a set of elements in both X and Y.
>>
>> Sets are faster when searching for an element.  When you add an object to a set, a hash is used to record its position in memory.  So if you want to know if that object is a member of a set, the hash table will tell you where to look in memory.  Since a list isn't hashable, you have to search throughout the list to know if an object is a member.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> The lambda is used to make anonymous functions.  It behaves the same as a function, and returns a value (although, without using a `return`), but it can be used without assigning a variable to the function being performed.  They take the form of `lambda <arguments>: <expressions>`.  Lambdas are useful for making functions that can be used as arguments for other functions, such as `map()`, `filter()`, or `reduce()`.
>>
>> As an comparison to [list comprehension](https://github.com/andrewkruger/dsp/blob/master/05a-python.md#q4-list-comprehension-map--filter), we can use the following:

```
$ a = [4, 5, 6, 7]
$ b = [x**2 for x in a]
$ print(b)
[16, 25, 36, 49]
```

>> The `[x**2 for x in a]` returns the square of each element in `a`, which it does by temporarily calling each element `x` and performing the function `x**2`.  Similarly, we can do the following: 

```
$ c = list(map(lambda x : x**2, a))
$ print(c)
[16, 25, 36, 49]
```

>> This again calls each element of `a`, using the elements as the parameter `x` for the function `x**2`.
>> 
>> You can also save a lambda function to a variable.  The following creates the function `f()` that returns the even values from a list, `my_list`:

```
$ f = lambda my_list: [x for x in my_list if x%2==0]
$ my_evens = f(a)
$ print(my_evens)
[4, 6]
```

>> An example of using a `lambda` function as a `key` argument for `sorted` is [when sorting a list of tuples by the last number in each tuple](https://github.com/andrewkruger/dsp/blob/master/python/q7_lists.py#L73):

```
$ sorted(tuples, key=lambda tup: (tup[-1]))
```


---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> If you want to create a filter that returns the numbers in a list that are divisible by 10 to a list called `tens_list`, you can use:

```
$ tens_list = filter(lambda x: x%10==0, xlist)
```

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> [937 days](https://github.com/andrewkruger/dsp/blob/master/python/q5_datetime.py#L3)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> [513 days](https://github.com/andrewkruger/dsp/blob/master/python/q5_datetime.py#L13)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> [7850 days](https://github.com/andrewkruger/dsp/blob/master/python/q5_datetime.py#L23)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





