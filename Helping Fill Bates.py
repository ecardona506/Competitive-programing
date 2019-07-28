from sys import stdin

def binary_search(array,low,hi,index,letter):
	global key, key_index
	mid = (low+hi)>>1
	if low == hi:
		return -1
	if low+1 == hi:
		if array[low] >= index:
			key_index[ord(letter)] = hi
			return array[low]
		elif hi < len(array):
			key_index[ord(letter)] = hi + 1
			return array[hi]
		else:
			return -1
	if array[mid] >= index: return binary_search(array,low,mid,index,letter)
	else: return binary_search(array,mid,hi,index,letter)

def solve(string,pattern):
	global key, key_index
	n = len(pattern)
	index,i = 0,0
	key_index = [0 for _ in range(123)]
	while i < n and index != -1:
		m = len(key[pattern[i]])
		array = key[pattern[i]]
		if m: 
			index = binary_search(array,key_index[ord(pattern[i])],m,index,pattern[i])
		else: index = -1
		if i == 0:
			init = index
		i+=1
	if index == -1: return "Not matched"
	else: return "Matched {} {}".format(init,index)

def main():
	global key, key_index
	string = stdin.readline().strip()
	n = len(string)
	key = {}
	for i in range(65,91):
		key[chr(i)] = []
	for i in range(97,123):
		key[chr(i)] = []
	for i in range(n):
		key[string[i]].append(i)
	n_patterns = int(stdin.readline().strip())
	while n_patterns:
		pattern = stdin.readline().strip()
		ans = solve(string,pattern)
		print(ans)
		n_patterns -= 1
	
main()