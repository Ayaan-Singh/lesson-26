class string():
    def __init__(self):
     self.str1 = ""
    def get_string(self):  
       self.str1 = str(input("enter a string "))
    def print_string(self):
       print ("the result is",self.str1.upper())
str1 = string()
str1.get_string()
str1.print_string()