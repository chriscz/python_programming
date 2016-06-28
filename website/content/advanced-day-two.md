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

3. Write a function :python:`swop` that takes a list and two positions in the 
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



Using pass inside a function
-----
You'll see that I used :python:`pass` in the above functions.
That just tells python that there is nothing to do inside this function.
So when you actually write your solutions, you can remove :python:`pass` and then
write your solution.


Next problems coming in a bit..



