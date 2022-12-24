import array

# define a function for insertion sort

def InsertionSort(arr): 
  
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
# end of insertion sort function


# Define array of integer numbers
a = array.array('i', [])

n = int(input('Enter Array size='))
# input n numbers in arry
for i in range(n):
    item= int(input("Enter number:"))
    a.append(item)

# call insertion sort function for sorting array
InsertionSort(a)

# print sorted array
print ("Sorted array is:")
for i in a:
    print (i, '\t')