str = '  Hello Srinivas Kolaparthi!  '
print (str)
print (str[0])
print (str[2:5])
print (str[2:])
print (str * 2)
print(str + "TEST")
print (str)
print(str.lower())
print(str.upper())
print(str.strip()) #removes spaces
print(str.replace('a','z'))
print(str.count('a'))
print(str.find('s'),'th position')
print (str[:-5])

#--------------------------
print ("My name is %s and weight is %d kg!" % ('srini', 22))

#triple quotes
para_str = """Reason:
Violation Of Capgemini Policy (Hyderabad). This Websense category is filtered: Social Web - Facebook.
URL:
http://fb.com/
You Are:
skolapar
In Domain:
10.109.32.189 OU=IN-HYD-ITPARKPL,OU=IN,OU=Employees,DC=corp,DC=capgemini,DC=com
With IP:
10.109.81.136
Workstation:
din66005928
And Today Is:
Wednesday, March 22, 2017 2:57 PM
"""
print(para_str)

#-------------------
str = "Srinivas Kolaparthi"
print (str.swapcase())
print (str.swapcase())

#Title case
str = "srinivas kolaparthi"
print (str.title())
#Join
s = "";
seq = ("cococola", "disc", "scope")
print (s.join( seq ))