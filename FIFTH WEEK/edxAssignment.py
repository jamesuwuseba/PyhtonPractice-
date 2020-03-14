# This program is meant to add name of an animal on a list if it is elaready existing, 
# but if it existing, already, it will be removed
# animalList=[]
# def list_o_matic():
#     for p in range(20):
#         animalNames=input("Enter the animal name here")
#         print(animalNames)
#         if animalNames not in animalList:
#             animalList.append(animalNames) 
#             print(animalList)  
#         elif animalNames in animalList:
#             animalList.remove(animalNames)
#             print(animalList)
#         elif animalNames=='':
#             animalList.pop()
#             print("This is the final animal list",animalList)
#         else:
#             print('Goodbye')

# print("This is the list", a)

def list_o_matic (animalList,animalNames):
    if animalNames not in animalList:
        return animalList.append(animalNames)
    # elif animalNames in animalList:
    #     return animalList.remove(animalNames)
    # elif animalNames=="":
    #     return animalList.pop()
    # elif animalNames in animalList:
    #     return animalList.remove(animalNames)
    # elif animalNames not in animalList:
    #     return animalList.append(animalNames)
   
animalList=['Cow','Sheep','Goat']
animalNames=str('Bird')
a=list_o_matic
print(list_o_matic(['Cow','Sheep','Goat'],'Bird'))
# if animalNames not in animalList:
#     animalList.append(animalNames)
#     print(animalList)
# elif animalNames in animalList:
#     animalList.remove(animalNames)
#     print(animalList)
# elif animalNames is str():
#     animalList.pop()
#     print(animalList)


# animalList=[]

# for i in range(10):
#     animalNames=input('Enter the name of the animal')
#     if animalNames!="Quit":
#         print(list_o_matic)
#     else:
#         print(animalList)
    

        
    

    
# newAddition=animalList.append("Cow")
# print(newAddition)


# print(b)
# for animals in range(10):
#     x=input("Enter the name of the animal you with check here")
#     x=list_o_matic
#     print(x)

