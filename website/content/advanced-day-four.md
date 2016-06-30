Title: Advanced Programming (Day four)
Date: 2016-6-30 18:45
Category: Exercises

Right, so from class you should remember that we started implementing the Learner class
and that we completed the Date class. So here is the **skeleton**  for the file we
expect to see tomorrow. Finish the unfinished methods in the skeleton code below, but don't worry too much if you can't do all the exercises,
just do as many as you can. Tomorrow we plan to continue with Object-Oreintated programming, either by coding an electronic diary, or a game. 
To be adequately prepared for this, you should just review some of the input-output things that you know. Or, if you prefer, we could code a small game, but it is then very important that you finish the Point class from Day 3, and review some of the drawing we did previously. Good Luck!


        #!python
        class Date:
            def __init__(self, year, month, day):
                self.year = year
                self.month = month
                self.day = day
            
            def to_string(self):
                """
                returns a string
                >>> D = Date(2016, 6,30)
                >>> D.to_string()
                >>> '30 June 2016'
                """
                pass

            def less_than(D):
                """
                takes in a Date D, returns True if self is an earlier date than D, and returns false otherwise
                >>> D1 = Date(2016, 6, 30)
                >>> D2 = Date(2017, 7, 32)
                >>> D1.less_than(D2)
                True
                >>> D2 = Date(2016, 7, 32)
                >>> D1.less_than(D2)
                True
                >>> D2 = Date(2016, 6, 32)
                >>> D1.less_than(D2)
                True
                >>> D2 = Date(2016, 6, 30)
                >>> D1.less_than(D2)
                False
                """
                pass
            
       
        class Learner:
            def __init__(self, first_name, surname, date_of_birth, email, address):
                self.first_name = first_name
                self.surname    = surname
                self.date_of_birth = date_of_birth
                self.email = email
                self.address = address
                
            def display_details(self):
                """
                displays (prints) the details of the Learner, does NOT return anything.
                >>> D = Date(1872, 6, 30)
                >>> L = Learner("Bertrand", "Russell", D, "bertie@gmail.com", "Cambridge")
                >>> L.display_details()
                Name of Learner: Bertrand Russell
                Date of birth: 30 June 1872
                Email: bertie@gmail.completed
                Address: Cambridge
                """
                pass
                
            def is_younger_than(self, L):
                """this method takes in a Learner object L, and returns True if self is younger than L, returns false otherwise
                >>> D1 = Date(1872, 6, 30)
                >>> L1 = Learner("Bertrand", "Russell", D1, "bertie@gmail.com", "Cambridge") 
                >>> D2 = Date(1879, 6, 30)
                >>> L2 = Learner("Albert", "Einstein", D2, "uncle_albie@gmail.com", "Princeton")
                >>> L1.is_younger_than(L2)
                False
                pass
                """



            class ClassRoom:
            """this class is supposed to represent a classroom of learners.
            it has no other attributes, other than a list of learners."""
            def __init__(self):
                learner = []
                
            def add_learner(L):
                """adds a learner L to the class room by appending it to learner"""
                self.learner.append(L)


            def youngest(self):
                """returns the youngest learner in the class"""
                pass


            def sort_by_age(self):
                """this method sorts the list learner by age, from youngest to oldest."""
                pass 
        
            
            
            
            
