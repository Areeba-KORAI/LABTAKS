shopping = []
for i in range(5):
 items = input("enter shopping items " + str(i + 1) + ": ")
 shopping.append(items)
 print ("shopping list:")
 for item in shopping:
     print ("-", items)
     print (shopping)
