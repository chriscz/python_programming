Title: Advanced Programming (Day 5)
Date: 2016-7-01 23:30 
Category: Exercises

Hey guys, it was a really awesome time, and we hope you make the best of the skills you have learnt!
Remember that perseverance will make the difference, and that this is what will make you a better programmer.
There is no place for arrogance.

1. On to the more important information. Remember what we said about writing files? There's one last thing
that I would like to add to that discussion: remember to **flush** before closing.

    *What is flushing?* you ask. Harddisks are slow and a computer's memory is fast. For this reason OS designers
    had files be written to RAM before writing them to disk. Flushing takes what's in memory and
    writes it to disk. You don't need to do it manually, since Python executes a flush before actually closing
    the file.


        #!python
        f = open('data.txt', 'w')
        f.write("My awesome string\n")
        # This is implied py close 
        # f.flush()
        f.close()


    Alternatively, you could use a more pythonic approach to reading files, which ensures that the files are
    always closed, even if an error occurs:

        #!python
        with open('data.txt', 'w') as f:
            f.write("My awesome string\n")
        # Here the file-handle (f) can no longer be used, since the file has been closed

2. **BUG** Saving of your drawings to file by calling the **save** method of stddraw did not produce
a valid image. The cause for this was trying to pass a **file** object to the method. 
It should instead be used with a filename string.

        
        #!python
        # Supported types: bmp, jpg, png
        stddraw.save("filename.jpg")

3. The cypher problem. Your task as code-breaker is to decipher a message in the given text file.
To complete this task you need knowledge of the following: basic loops, dictionaries and files.
Here's the [archive]({attach}/resources/cypher.zip) containing the cypher assignment. If you've solved it, post your answers in the comments!
**HINT**: How do you read a file character by character, instead of line by line?

4. Links to useful Python resources, if you have any others, post in the comments!
    1. Our documentation and installations: [Website](https://goo.gl/3ZvPYJ)
    2. [The Python Documentation](https://docs.python.org/3.4/) also included in WinPython.   
    3. [Think Python 2e](http://greenteapress.com/wp/think-python-2e/)
    4. [Dive into Python 3](http://www.diveintopython3.net/)
    5. [A Byte of Python](http://python.swaroopch.com/)
    6. [Making Games with Python](https://inventwithpython.com/makinggames.pdf)

   
5. The snake game. This isn't ready for you yet. When it is,
you can download the skeleton and begin completing the different sections of the code. 

6. **BUG** Fixed issue with stdlib imports when using IDLE. Here's the [updated stdlib]({attach}/resources/stdlib_updated_1.zip). 
You no longer need to save your files inside the stdlib directory! There are two options to
using stddraw. 
        
    Option1

    
        #!python
        from stdlib import stddraw
        stddraw.line(0,0,1,1)

    And Option 2    


        #!python
        import stdlib.stddraw
        stdlib.stddraw.line(0,0,1,1)



## Request    
Please leave comments if something is missing, or if you would like us to discuss something specific in 
more detail.
