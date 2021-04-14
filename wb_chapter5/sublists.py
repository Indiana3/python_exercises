# Find the number of sublists for a list of n elements
# sublists = 1 + n + (n-1) + (n-2) + (n-3) + (n-4) ...(n-x) | x Ꜫ (1,n)
n = 10
sublists = 1 + n
for x in range(1, n):
    sublists += (n-x)
print(sublists)


    
    

