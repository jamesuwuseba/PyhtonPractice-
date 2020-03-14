def printDictionary(dictList):
    for slip in dictList:
        print(slip,end=' :')
        listItems =dictList[slip]
        for item in listItems:
            print(item[0],item[1],end=' ,')
        print()

salepeople={'James':8099444252,'Seun':8093495808,'Ekene':80578787237,'Karo':8048988432}
string_salepeople=(salepeople.values())
for p in string_salepeople:
    print(p)
# print(string_salepeople)
# # print(string_salepeople)
# # print(salepeople.keys())
# products=['Panadol','Amala','Asprin','Phensic','Malarich']
# import datetime
# day_1=datetime.date(2020,3,1)
# day_1_sales_product={'day_1'}
slip_james_={'james':[["Panadol",5],["Amala",6],["Phensic",9]]}
slip_seun_={'seun':[["gala",5],["Amala",6],["Phensic",9]]}
printDictionary(slip_james_)
printDictionary(slip_seun_)
# for slip in slip_james_:
#     print(slip,end=' :')
#     listItems =slip_james_[slip]
#     for item in listItems:
#         print(item[0],item[1],end=' ,')
#     print()

slip_james=[[8099444252,"Panadol",5],[8099444252,"Amala",6],[8099444252,"Phensic",9]]
# slip_seun=[[8093495808,"Panadol",4],[8093495808,"Phensic",3],[8093495808,"Malarich",10]]
# slip_ekene=[[80578787237,"Asprin",6],[80578787237,"Phensic",13]]
# slip_karo=[[8048988432,"Asprin",4],[8048988432,"Malarich",8]]
for p in salepeople:
    sales_people_number=salepeople[p]
    print(p)
    for i in slip_james:
        if sales_people_number==i[0]:
            print(i[1],i[2])


# for i in slip_james:
#     a=(i[0])
#     print(a)
#     if a==string_salepeople:
    # print("Yes")
    # if p==i[0]:
    #     print("Yes")
#     if i[0]==string_salepeople:
#         print(i[1,2])'Asprin'
#     # for p in string_salepeople:
#     #     # print(p,end='')
#     #     if i[0]==p:
#     #         print(salepeople.keys(),i[1,2],end="")

        