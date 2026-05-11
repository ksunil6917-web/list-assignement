# 1.write a program that takes an array as input from the user and find out the product of the elements
import numpy as np

a = np.array([1,2,3,4,5])
product = np.prod(a)
print(product)

# 2.Write a program which takes an array as input from the user and find out the sum of the array elements.     
a = np.array([1,2,3,4,5])
sum = np.sum(a)
print(sum)

#You are given an array A containing N integer elements and an integer K, and your task is to return the count of occurances of k in array a

a = np.array([3,3,3,1,2])
K = 3
count = np.count_nonzero(a == K)
print(count)
 
# find the sum of all even and odd elements
a = np.array([1,2,3,4,5,6,7])
even_sum = np.sum(a[a % 2 == 0])
odd_sum = np.sum(a[a % 2 != 0])

print("Sum of even elements:", even_sum)
print("Sum of odd elements:", odd_sum)

#Write a program which takes an array as input from the user and a number. Check whether the number is present or not. 
a = np.array([1,2,3,4,5,2])
number = 2
is_present = np.any(a == number)
print("Number is present:", is_present)

#You are given an array A containing the age of persons in your locality, and your task is to find and return an array 
#containing the age of persons that are over 1818 (18(18 included)). 

a = np.array([11,23,3,45,72,68])
over_18 = a[a >= 18]
print(over_18)

#You are provided an array of integers and you have to increment all array elements by 1 and then print whole array

a = np.array([1,2,3,4,5])
incremented_array = a + 1

print(incremented_array)

# find minimum and maximum elements.

a = np.array([3,1,4,6,2,7])
min_element = np.min(a)
max_element = np.max(a)

print("Minimum element:", min_element)
print("Maximum element:", max_element)

#Return "YES" (without quotes) if all the students pass in your class; other wise, print "NO" (without quotes). 

a = np.array([7,13,89,45,98,67,45,54])
passing_score = 40
all_passed = np.all(a >= passing_score)
if all_passed:
    print("YES")
else:
    print("NO")


#The first line of the input contains an integer N denoting the number of shirts in the wardrobe. The second line of the input 
#contains N integers C1,C2,C3,C4,...,CN1,2,3,4,..., color of shirts (separated by space).

a = np.array([3,2,4,1,2,3])
unique_colors = np.unique(a)
print("Unique colors of shirts:", unique_colors)
