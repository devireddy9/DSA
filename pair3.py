def pair (arr,target):
   arr.sort()
   num_and_index =[(num,index) for index, num in enumerate(arr)]
   left,right = 0,len(arr)-1
   while left<right:
       sum = num_and_index[left][0] + num_and_index[right][0]
       if sum == target:
           return [num_and_index[left][0] , num_and_index[right][0]]
       elif sum> target:
           right-=1
       else:
           left+=1
   return "NO"





arr = [2,6,5,8,11]
target = 17
print(pair(arr,target))