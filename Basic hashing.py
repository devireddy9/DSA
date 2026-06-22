# bruite force
def counting_frequency(arr):
   n = len(arr)
   visted = [False]*n
   for i in range(n):
       if visted[i] == True:
           continue
       count = 1
       for j in range (i+1, n):
           if arr[i] == arr[j]:
               visted[j] = True
               count += 1

       print(f"{arr[i]} -> {count}")
arr = [10, 10 , 20, 10, 10, 20, 5, 20]
counting_frequency(arr)