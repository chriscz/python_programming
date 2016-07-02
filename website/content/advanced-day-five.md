Title: Advanced Programming (Day 5)
Date: 2016-7-01 23:30 
Category: Revision

Hey guys, it was a really awesome time, and we hope that you make the best of the skills you have been taught!
Remember that perseverance will make the difference, and that this is what will make you a better programmer.
There is no place for arrogance.

1. Anyhow, on to the more important information. Remember what we said about writing files? There's one last thing
that I would like to add to that discussion, and that is to remember to **flush** before closing.

    *What is flushing?*, you ask. Harddisks are slow, but a computer's memory is faster. So what OS (operating system)
    designers did was to have files be written to RAM (computer memory) first, before writing them to disk. And 
    by following the **flush** and **close** approach you achieve just this.


        #!python
        f = open('data.txt', 'w')
        f.write("My awesome string\n")
        f.flush()
        f.close()

2. **BUG** Saving of your drawings to file by calling the save method of stddraw does not actually produce
a valid image. We will fix this as soon as possible.

3. The cypher problem. Your task as code-breaker is to decipher the message in the textfile. 
Your task requires the most basic of loops, dictionaries and files. Expect the exercise soon

4. References to useful resources
    1. Our documentation and installations: [Website](https://goo.gl/3ZvPYJ)
    2. [The Python Documentation](https://docs.python.org/3.4/) also included in WinPython.   
    3. [Think Python 2e](http://greenteapress.com/wp/think-python-2e/)
    4. [Dive into Python 3](http://www.diveintopython3.net/)
    5. [A Byte of Python](http://python.swaroopch.com/)
    6. [Making Games with Python](https://inventwithpython.com/makinggames.pdf)

5. I know I'm missing something, but now I don't remember...

Lastly... Leave comments if we made a typo, there's something's missing, or if there's
something you would like us to disucss.
We will get notified, and respond as soon as time permits.
