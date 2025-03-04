A = {'a', 'g', 'd', 'f', 'b', 'c'}
B = {'b', 'l', 'm', 'o', 'c', 'h'}
C = {'h', 'i', 'j', 'k', 'c', 'd', 'f'}

print("a. How many elements are there in set A and B:", len(A | B))  
print("b. How many elements are there in B that is not part of A and C:", len(B - (A | C)))  

print("i.", list((C - (A | B)) | ((C & B) - A)))  
print("ii.", list(C & A))  
print("iii.", list((A & B) | (B & C)))  
print("iv.", list((A & C) - B))  
print("v.", list(A & B & C))  
print("vi.", list(B - (A | C)))  
