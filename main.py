#print("welcome to python")
def fact(c):
  if c<0:
    print("0")
  elif c==0 or c==1:
    print("1")
  else:
    f=1
    while c>1:
      f=f*c
      c=c-1
    print(f)
fact(8)

year=int(input("enter the year u want : "))
if (year%4)==0:
  print("leap year")
else:
  print("not leap year")