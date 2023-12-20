#1 Bubble sorting by pairs (1 by 1)(O(n**2))

def bubblesort(a):
	#turn swapped to True for start
	swapped = True
	while swapped:
		swapped = False
		for i in range(len(a) - 1):
			if a[i] > a[i + 1]:
				#change elements
				a[i], a[i + 1] = a[i + 1], a[i]
				#turn swapped to True for next iteration
				swapped = True

x = [2,3,7,1,23,4,5,6]

bubblesort(x)
print(x)

#2 Selection sorting (O(n**2)
#Lowest element moving from unsorted pile of List to sorted 1 by 1 

def selectsort(a):
	#i = number of sorted elements
	for i in range(len(a)):
		#for default first element is lowest
		lowindex = i
		#this cycle check unsorted elements
		for j in range(i + 1, len(a)):
			if a[j] < a[lowindex]:
				lowindex = j
		#lowest element change with first in List
		a[i], a[lowindex] = a[lowindex], a[i]
x2 = [2,6,4,9,16,8,20]
selectsort(x2)
print(x2)

#3 Inserting sorting (O(n**2))
#From unsorted pile taking current element and insert in sorted pile

def insertsort(a):
	#sorting start by second element (coz first element is sorted)
	for i in range(1, len(a)):
		itinsert = a[i]
		#Save link to index last element
		j = i - 1
		#Elements of sorted pile  moving forward, 
		#if they r bigger than element for insert
		while j >= 0 and a[j] > itinsert:
			a[j + 1] = a[j]
			j -= 1
		#insert element
		a[j + 1] = itinsert

x3 = [2,6,8,12,3,24,16,4,1]
insertsort(x3)
print(x3)

#4Pyramind sorting (O(n log n)). Two piles (sorted and unsorted)
#
