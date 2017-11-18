def printList(lst):
	print("Shopping list is: ")
	for i in lst:
		print(i)
	print ""

shopping_list = ['kale', 'spinach', 'chicken', 'celery', 'half n half']

printList(shopping_list)

shopping_list.append("Apple cider vinegar")
shopping_list.sort()
printList(shopping_list)

del(shopping_list[1])
printList(shopping_list)
