def is_divisible_by_k(i, k): 
    ''' 
    Checks whether x is divisible by k. 
    ''' 
    return i % k == 0 

''' 
Store all the integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000 (excluding 
doubles) 
''' 
x = set()
#x = [] 
for i in range(1, 1001): 
    if is_divisible_by_k(i, 2) or is_divisible_by_k(i, 5) or is_divisible_by_k(i, 7): 
        #x.append(i) have to use list if don't wanna change append
        x.add(i)
     
''' 
Sum all the integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000 (excluding 
doubles) 
''' 
#x = sum(x)
print(sum(x))