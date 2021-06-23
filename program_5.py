def method(y):
    print ("Bonus is {}". format (int ((5/100)*y)))


y=int (input ())
x=int (input ())
if x<=5:
    print ("No Bonus")
elif x>5:
    method (y)
   