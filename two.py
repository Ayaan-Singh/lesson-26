class pair ():
 def tsum (self , nums , target):
  lookup = {}
  for i,num in enumerate(nums):
   if target - num in lookup:
    return (lookup[target-num],i)
   lookup [num] = i
value = int(input("enter a number you want to make"))
print ("index1=%d index2=%d"% pair().tsum((10,20,30,40,50,60,70),value))
  