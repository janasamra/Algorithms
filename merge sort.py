import array
# define merge sort function
def mergeSort(arr):
    if len (arr)>1:
        mid=len(arr)//2
        right=arr[mid:]
        left=arr[:mid]
        # recursive call
        mergeSort(right)
        mergeSort(left)
        i=0
        j=0
        k=0

        while i<len(left) and j<len(right):
          if left[i]<right[j]:
            arr[k]=left[i]
            i+=1
          else:
            arr[k]=right[j]
            j+=1
            k+=1

            while i< len(left):
                arr[k]=left[i]
                i+=1
                k+=1
            while j<len(right):
                arr[k]=right[j]
                j+=1
                k+=1
#end of merge sort 
n = int(input("How many numbers in the list: "))
list=[int(input()) for x in range(n)]
# call imerge sort function for sorting array
mergeSort(list)
# print sorted array
print ("Sorted array is:",list)








    
