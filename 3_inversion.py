#Ashwal Neelakanta Kalgodu

num_list = raw_input("Enter the elements to sort: ").split()
#print num_list
#print len(num_list)
def divide_con(num_list):
	n = len(num_list)
	if n <= 1:
		return 0 , num_list
	elif n > 1:
		k = int(n/2)
		list1 = num_list[:k]
		list2 = num_list[k:]
		#print list1, list2

		#list1= sorted(list1)
		#list2= sorted(list2)
		n1 , L1 = divide_con(list1)
		n2 , L2 = divide_con(list2)
		n3 , L = merge(L1, L2)
		n = n1 + n2 + n3
		#print n1, n2, sorted_list
		return n ,L
	else:
		print "No inputs!!!"

def merge(l1,l2):
	p = len(l1)
	q = len(l2)
	count = 0
	#print l1,l2
	i = j = 0
	sorted_list=[]
	#### for sorting
	while (i < p and j < q):
		if l1[i] > l2[j]:
			sorted_list.append(l2[j])
			j = j + 1
			
		else:
			sorted_list.append(l1[i])
			i = i + 1
	if i < p:
		sorted_list = sorted_list + l1[i:]
	if j < q:
		sorted_list = sorted_list + l2[j:]


	i = j = 0
	#### for counting significant inversions
	while (i < p and j < q):
		if int(l1[i]) > 2*int(l2[j]):
			count += p - i
			j = j + 1
			
		else:
			i = i + 1	
	return count , sorted_list

	
result = divide_con(num_list)
print " "
print "Sorted elemets are as follows: "
print result[1]
print " "
print "Significant inversion is : "
print result[0]
