from animalfile import*
import random 
Animals=["dog","cat","fish","bird","pig","elephant","sheep","chicken"]
age=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]
zoo=[]

for x in range(300):
	a = Animal("woof", Animals[random.randint(0,7)],age[random.randint(0,50)])
	a.eat("nutella")
	zoo.append(a)



dog = Animal("woof","Jeff",17)
cat = Animal("meow","lolo",4)

print(dog.sound)
dog.eat("bamba")
cat.eat("besli")
cat.sleep(" real madrid")



