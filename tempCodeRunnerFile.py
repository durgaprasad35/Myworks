
# def comb1(n,l):
#     if n<=0:
#         yield [] 
#         return 
#     for i in range(len(l)):
#         c_num = [l[i]] 
#         for j in comb1(n-1,l[i+1:]):
#               yield c_num+j 
# n = 3 
# l = [1,2,3,4,5,6]
# res = comb1(n,l) 
# for k in res:
#     print(k,end=" ")