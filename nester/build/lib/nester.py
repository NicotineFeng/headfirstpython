def print_lol(element):
	for ele in element:
		if isinstance(ele,list):
			for ele1 in ele:
				print(ele1)
		else:
			print(ele) 
