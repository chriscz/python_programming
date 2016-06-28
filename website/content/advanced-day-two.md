Title: Advanced Programming
Date: 2016-7-28 18:45
Category: Exercises

Ok, so as promised here is the website. You can expect more 
exercises to be uploaded in the next hour.


Problems
--------
1. **EXERCISE** Write a function called *printn* that has the following signature
and does what is described in the doc string.

        #!python
        def printn(string, count):
            """Prints the string `string`, `count` number of times.
               For example,

               >>> printn('Hello', 3)
               Hello
               Hello
               Hello
            """
            pass

2. **EXERCISE** Write a function *array_sum* that takes two lists of the same length
   as arguments, and returns a list that that is the element-wise 
   sum of the two lists.

        #!python
        def array_sum(list1, list2):
            """Takes two lists and returns a new list that is the 
               element-wise sum of the lists.

               For example,
               >>> array_sum([1,2,3], [1,2,3])
               [2, 4, 6]
            """
            pass

3. Write a function *swop* that takes a list and two positions in the 
   list as arguments, it then swops the values at the two positions.

        #!python
        def swop(L, x, y):
            """
            Takes two indexes and swops (switches) the values of L at that index
            Arguments
            ---------
            L: list
                A python list of elements
            x: int
                An index into the list L. x must satisfy x >= 0 and x < len(L)
            y: int
                An index into the list L. y must satisfy y >= 0 and y < len(L)

            Examples
            --------
            >>> L = [1,2,3,4,5]
            >>> swop(L, 0, 4)
            >>> print(L)
            [5, 2, 3, 4]


            >>> L = [1,2,3]
            >>> swop(L, 1, 1) # Swop element number two with itself
            >>> print(L)
            [1, 2, 3]

            """
            pass

            

7. **READING** Read about how python dictionaries work (See the introduction PDF written by me and Mike).
   After you understand this, go ahead and do the next dictionary exercises

8. **EXERCISE** Write a program that reads in the names and ages of
of your friends *N* friends (N is the number of friends whose names you want
 to read in). these should then be put inside a dictionary, mapping each user
 to his/her age. Look at the following example which shows
 you how to store the ages of two people.

        #!python
        >>> ages = {}
        >>> ages['bob'] = 16
        >>> ages['alice'] = 19
        >>> print(ages['alice'])
        19

9. **EXERCISE** Create a function *read_ages* that takes a single parameter **n** and then reads in 
the names and ages of **n** people into a dictionary and returns that dictionary.
for example:
        
        #!python
        >>> ages = read_ages(2)
        Please enter a person's name: 
        Janice
        Please enter their age:
        15
        Please enter a person's name: 
        Alice
        Please enter their age:
        14
        >>> print(ages['Janice'])
        15
        >>> print(ages['Alice'])
        14

10. **EXERCISE** Write a function *contains* that takes two arguments: a list and a number and 
returns True if the number is in the list or False otherwise. 

        #!python
        def contains(list, x):
            """Returns True if x is in list and False if it is not
            
                Examples
                --------
                >>> x = [1, 2, 3]
                >>> contains(x, 1)
                True
                >>> contains(x, 6)
                False
                >>> contains(x, -1)
                False
            """
            pass

11. **EXERCISE** Write a function *remove_dup* that takes a single list parameter and 
removes all duplicates from it. If there are duplicates, you should remove all of them.
*NOTE*: It doesn''t matter which of the duplicates you remove, as long as there
are no duplicates after usign remove_dup!


        #!python
        def remove_dup(L):
            """Removes all elements that are duplicates from L
               
               Examples
               --------
               >>> L = [1, 1, 2, 3, 1]
               >>> remove_dup(L)
               >>> L
               [1, 2, 3]
               # OR
               [2, 3, 1]
               >>> L = [1, 55, 6, 7, 7, 8, 7]
               >>> remove_dup(L)
               >>> L
               [1, 55, 6, 8, 7]
               >>> L = [2, 4, 6]
               >>> remove_dup(L)
               >>> L
               [2, 4, 6]
            """
            pass

12. **EXERCISE** Write a function *does_share* that takes two lists as arguments and
    returns True if the lists have at least one common element (an element that is in
    both of the lists).

        #!python
        def does_share(list1, list2):
            """Returns True if list1 and list2 share any elements, otherwise False

               Examples
               --------
               >>> does_share([1], [2])
               False
               >>> does_share([1, 2], [2])
               True
               >>> does_share([2, 3, 11, 55], [55, 3, 4])
               True
               >>> does_share([2, 3, 11, 55], [9, 9, 10])
               False
            """
            pass






Using pass inside a function
-----
You''ll see that I used **pass** in the above functions.
That just tells python that there is nothing to do inside this function.
So when you actually write your solutions, you can remove **pass** and then
write your solution.


Next problems coming in a bit..



