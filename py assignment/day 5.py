'''
#creation of set
set1={1,2,3,4,3,5}
print(set1)
set2={}
print(type(set2))
set3=set()
print(type(set3))

#set with different element types
set4={6,7.8,"hi",(3,4)}
print(set4)
set5=set([4,5,6])
print(set5)
set6={[4,5],6}
print(set6)

#adding elements to set
set2=set()
set2.update([3,4])
set2.update((23,56))
set2.update("hello")
print(set2)

set2=set()
set2.add("hello")
set2.add(3)
print(set2)
set2.update(2,6)
print(set2)

#remove elements from set
set2={1,2,"hello",45.7,10,"bye"}
print(set2)
set2.discard(2)
print(set2)
set2.remove(10)
print(set2)
set2.discard(7)
print(set2)
set2.remove(5)
print(set2)

#set mutation operations
set1={1,2,3,5}
set2={2,5,6,4}
print('set 1',set1)
print('set 2',set2)
print('Union : set1 | set2',set1|set2)
print('Union : set1.union(set2)',set1.union(set2))
print('Intersection: set1 & set2',set1&set2)
print('Intersection: set1.intersection(set2)',set1.intersection(set2))
print('Difference : set1 - set2',set1-set2)
print('Difference : set1.difference(set2)',set1.difference(set2))
print('Symmetric Difference : set1 ^ set2',set1^set2)
print('Symmetric Difference : set1.symmetric_difference(set2)',
      set1.symmetric_difference(set2))

# dictionary creation
d={}
print(d,type(d))
d={'english':20,'maths':40,'science':30}
print(d)

# Accessing items from dictionary 
print(d['maths'])
print(d.get('maths'))
print(d.get('hindi'))
print(d['hindi'])

# adding/chnaging items in a dictionary 
d={'english':20,'maths':40,'science':30}
print(d)
d['maths']=45  #changing
print(d)
d['hindi']=35  #adding
print(d)

# deleting elements from a dictionary 
d={'english':20,'maths':40,'science':30,'hindi':35}
print(d)
del d['maths']
print(d)
d.pop('hindi')
print(d)
d.popitem()
print(d)
d.clear()
print(d)

#iterating through a dictionary
d={'english':20,'maths':40,'science':30,'hindi':35}
print(d)

for x in d:
    print(x)

for x in d:
    y=d[x]
    print('{}:{}'.format(x,y))

#iterating through a dictionary
d={'english':20,'maths':40,'science':30,'hindi':35}
print(d)
print(d.keys())
print(d.values())

for x,y in d.items():
    print('{}:{}'.format(x,y))
    
#multiple values per key
d={'India':['AP','MP','UP'],
    'America':['Newyork','California','Florida']}
print(d)
print(d.keys())
print(d.values())

#Dictionary of dictionaries
students={'501':{'name':'tom','branch':'cse'},
          '201':{'name':'sam','branch':'eee'}}
print(students)
print(students['201'])
print(students['201']['branch'])
'''