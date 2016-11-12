def print_lol(element):
	for ele in element:
		if isinstance(ele,list):
			print_lol(ele)
		else:
			print(ele)
