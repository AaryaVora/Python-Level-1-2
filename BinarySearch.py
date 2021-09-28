# def binarySearch (arr, low, high, x):
#     if high >= low:
#         mid = (high+low)//2
#         if arr[mid]== x :
#             return mid
#         elif arr[mid] > x:
#             return binarySearch(arr, low, mid - 1, x)
#         else :
#             return binarySearch(arr, mid + 1, high, x)
#     else :
#         return -1
# arr = ['1','2','3','4','5','6','7','8','9']
# x = 8
# result = binarySearch(arr,0,len(arr)-1,x)
# if result != -1 :
#     print("Element is present at ",str(result))
# else :
#     print("Element not present!")



def binary_search(arr, low, high, x):


    if high >= low:

        mid = (high + low) // 2


        if arr[mid] == x:
            return mid

        elif arr[mid] < x:
            return binary_search(arr, low, mid - 1, x)


        else:
            return binary_search(arr, mid + 1, high, x)

    else:

        return -1


arr = [ 2, 3, 4, 10, 40 ]
x = 10

result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
  print("Element is present at index", str(result))
else:
  print("Element is not present in array")

