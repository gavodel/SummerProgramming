from ex3 import	max

def  max_in_list(n):
	big = 0
	for i in range(0,len(n)):
		big = max(n[i],big)
	return big
		
	
if __name__ == "__main__":
	print max_in_list([8641,92,63,46,44,10])

