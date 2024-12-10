
#Write a Python program to find the sum and average of the list. The average of the list is defined as the sum of the elements divided by the number of the elements. Also, find the largest and the smallest number in the list.

num = [9,1,5,6,7,2]
print(num)

count = 0
for a in num:
    count += a

ave = count/len(num)
print(count,ave)

num.sort()
print('Smallest element:',num[0])
print('Largest element :',num[-1])
      
