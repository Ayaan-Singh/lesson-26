class emp:
    def __init__(self):
     print ("created")
    def __del__(self):
       print("destructor called")
def create_obj():
       print ("making obj...")
       obj = emp()
       print("function end")
       return obj
print ("calling obj")
obj = create_obj()
print ("end")