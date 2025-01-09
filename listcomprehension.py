#LIST COMPREHENSIONS
my_list = [1,2,3,4,5,6,7,8,9,10] 
new_list = [i*i for i in my_list] 
even_list1 = [i for i in my_list if i%2==0] 
even_list2 = [i for i in new_list if i%2==0] 
odd_list1 =  [i for i in my_list if i%2!=0] 
odd_list2 = [i for i in new_list if i%2!=0] 
print(f"my original list {my_list}") 
print(f"squares of the my_list{new_list}") 
print(f"The even numbers of my_list is {even_list1}") 
print(f"The even numbers of new_list is {even_list2}") 
print(f"The odd numbers of my_list are {odd_list1}") 
print(f"The odd numbers of new_list are {odd_list2}") 
#DICTIONARY COMPREHENSION 
d = {i:i*i for i in my_list} 
d_even = {i:i for i in my_list if i%2==0} 
d_odd = {i:i for i in my_list if i%2!=0} 
print(f"The new dictionary is {d}") 
print(f"The even numbers dictionary is {d_even}") 
print(f"The odd number dictionary is {d_odd}") 
#SET COMPREHENSION 
s = set() 
s = {1,2,3,4,5,6,7,8,9} 
s1 = {i*i for i in s } 
s1_even = {i for i in s if i%2==0} 
s1_odd = {i for i in s if i%2!=0}  
print(f"The squares of the set s is {s1}") 
print(f"The even numbers set is {s1_even}") 
print(f"The odd number set is {s1_odd}") 
#GENERATOR COMPREHENSION 
gene = (i*i for i in my_list)
for j in gene:
    print(j,end=" ") 
gene_even = (i for i in my_list if i%2==0) 
for k in gene_even:
    print(k,end=" ") 
gene_odd = (i for i in gene if i%2!=0) 
for m in gene_odd:
    print(m,end=" ") 

