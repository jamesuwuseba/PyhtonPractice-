# This program is meant to add name of an animal on a list if it is elaready existing, 
# but if it existing, already, it will be removed

def list_o_matic (animalList,animalNames):
    if animalNames not in animalList:
        return animalList.append(animalNames)
    elif animalNames in animalList:
        return animalList.remove(animalNames)
    elif animalNames==str():
        return animalList.pop()

animalList=[]
animalNames=str(input('Enter the name of animal here: '))
if ainimal !='Quit':
    print(list_o_matic)
else:
    print("Goodbye")
    
   
animalList=['Cow','Sheep','Goat']
animalNames=str('Bird')
a=list_o_matic
print(list_o_matic(['Cow','Sheep','Goat'],'Bird'))


if animalNames not in animalList:
    animalList.append(animalNames)
    print(animalList)
elif animalNames in animalList:
    animalList.remove(animalNames)
    print(animalList)
elif animalNames is str():
    animalList.pop()
    print(animalList)


for i in range(10):
    animalNames=input('Enter the name of the animal')
    if animalNames!="Quit":
        print(list_o_matic)
    else:
        print(animalList)
    

        

