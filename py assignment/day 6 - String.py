'''
#string creation
str1='hi'
str2="hello"
print(str1,str2)
print(type(str1))
multiStr="""Hello
How are you?"""
print(multiStr)    

#accessing characters in string
str1='Hi,How are you?'
print(str1[3])
print(str1[-2])
print(str1[:3])
print(str1[3:])
print(str1[7:10])
print(str1[15])

#Immutability in string
str1='Hi,How are you?'
#str1[2]='t'
del str1[2]

#justifying string
String="Python"
print("Left,centre and right alignment by formatting:")
print("|{:<10}|{:^10}|{:>10}|".format(String,'is','fun'))

#formatting string
#using f-string
name="Tom"
print(f"His name is {name}")
father="Ram"
mother="Sita"
print(f"His father's name is {father} and his mother is {mother}")
#using format
print("His father's name is {} and his mother is {}".format(father,mother))
#using %
print("His father's name is %s and his mother is %s"%(father,mother))

#String functions
str1="Hello,how are you"
print(str1.casefold())
print(str1.lower())
print(str1.upper())
print(str1.capitalize())
print(str1.find('are'))
print(str1.index('are'))
print(str1.split())
print(str1.endswith("you"))
print(str1.startswith('you'))

#String functions
str1="Hello,how are you"
print("*".join(str1))
x="*".join(str1)
print(x.split("*"))
print(str1.split("o"))

#String functions
str1=" ********  "
print(str1,"hi")
print(str1.lstrip(),"hi")
print(str1.rstrip(),"hi")
print(str1.strip(),"hi")
str1="@@@hello@@"
print(str1)
print(str1.strip("@"))

#String functions
str1="hi,how are you?"
print(str1)
print(str1.replace(',','-'))
print(str1.count('h'))
'''
#String functions
print('A123&'.isalnum())
print('Aaab'.isalpha())
print('123'.isnumeric())
print('Hello'.isupper())
print('2sad'.isidentifier())




