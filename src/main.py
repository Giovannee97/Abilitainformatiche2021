import cmath
import math
a=math.sin(2)
b=math.tan(3)
z=complex(a,b)
print("Complesso:", type(z),z)

var1="fai cestil Giovanni! "
var2="stai per inciampare"
print("Slicing:", var1[0:10])
print("Somma:", var1+var2)

nome= "DOOM"

string = " Gosh! %s!!! I should have brought my autograph book!" %nome
print(string)
adjective= "AWESOME"
tool = "Flying guillotine"
status = "dead"

Bar1= " I been tossin, enforcing, my style is %s" %adjective

Bar2= " ,I cause more family feuds than Richard Dawson"
Bar3= " ,the survey says your %s" %status
Bar4= " ,Fatal %s chops off your head " %tool
print(Bar1+Bar2+Bar3+Bar4)
