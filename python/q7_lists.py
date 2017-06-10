# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    """
    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same.

    >>> match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
    3
    >>> match_ends(['', 'x', 'xy', 'xyx', 'xx'])
    2
    >>> match_ends(['aaa', 'be', 'abc', 'hello'])
    1
    """
    #List comprehension
    return len([w for w in s if (len(w)>1) and (w[0]==w[-1])])
    #Or, using lambda:
    '''
    return len(list(filter(lambda w: (len(w)>1) and (w[0]==w[-1]), s)))
    '''
    #Or, more basic:
    '''cnt = 0
    for word in s:
      if len(word) > 1 and word[0] == word[-1]:
        cnt+=1
    return cnt'''

print('match_ends:')
print(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']))
print(match_ends(['', 'x', 'xy', 'xyx', 'xx']))
print(match_ends(['aaa', 'be', 'abc', 'hello']))


def front_x(words):
    """
    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].

    >>> front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
    ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
    >>> front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
    ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    """
    #List comprehension:
    return sorted([w for w in words if w[0]=='x'])+sorted([w for w in words if w[0]!='x'])
    #Or, using lambda:
    '''return sorted(list(filter(lambda w: w[0]=='x', words))) +\
        sorted(list(filter(lambda w: w[0]!='x', words)))
    '''
    #Or, more basic:
    '''xwords = []
    swords = []
    for word in words:
      if word[0] == 'x':
        xwords.append(word)
      else:
        swords.append(word)
    return sorted(xwords)+sorted(swords)
    '''
    
print('\nfront_x:')
print(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']))
print(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']))
print(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']))


def sort_last(tuples):
    """
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].

    >>> sort_last([(1, 3), (3, 2), (2, 1)])
    [(2, 1), (3, 2), (1, 3)]
    >>> sort_last([(2, 3), (1, 2), (3, 1)])
    [(3, 1), (1, 2), (2, 3)]
    >>> sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
    [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    """
    return sorted(tuples, key=lambda tup: (tup[-1]))

print('\nsort_last:')
print(sort_last([(1, 3), (3, 2), (2, 1)]))
print(sort_last([(2, 3), (1, 2), (3, 1)]))
print(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]))


def remove_adjacent(nums):
    """
    Given a list of numbers, return a list where all adjacent equal
    elements have been reduced to a single element, so [1, 2, 2, 3]
    returns [1, 2, 3]. You may create a new list or modify the passed
    in list.

    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([2, 2, 3, 3, 3])
    [2, 3]
    >>> remove_adjacent([3, 2, 3, 3, 3])
    [3, 2, 3]
    >>> remove_adjacent([])
    []
    """
    n_out = [nums[0]]
    for i in range(1,len(nums)):
      if nums[i] != nums[i-1]:
        n_out.append(nums[i])
    return n_out

print('\nremove_adjacent:')
print(remove_adjacent([1, 2, 2, 3]))
print(remove_adjacent([2, 2, 3, 3, 3]))
print(remove_adjacent([3, 2, 3, 3, 3]))


def linear_merge(list1, list2):
    """
    Given two lists sorted in increasing order, create and return a
    merged list of all the elements in sorted order. You may modify
    the passed in lists. Ideally, the solution should work in "linear"
    time, making a single pass of both lists.

    >>> linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
    ['aa', 'aa', 'aa', 'bb', 'bb']
    """
    out_list = []
    while list1 and list2:
      if list1[0] < list2[0]:
        out_list.append(list1.pop(0))
      else:
        out_list.append(list2.pop(0))
    return out_list+list1+list2

print('\nlinear_merge:')
print(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']))
print(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']))
print(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']))
