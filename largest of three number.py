#largest of three numbers
a = float(input("enter the 1st number"))
b = float(input("enter the 2nd number"))
c = float(input("enter the 3rd number"))
if (a>=b) and (a>=c):
   print("the largest number is",a)
elif (b>=a) and (b>=c):
    print("the largest number is",b)
else:
  print("the largest number is", c)
