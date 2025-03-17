#print_triangular_numbers function.
def print_triangular_numbers(n):
    #intialize s as 0
    s = 0
    #iterate from 1 to n.
    for i in range(1,n+1):
        #increment s by i
        s = s + i
        #print i and s with space in between.
        print(i, "   " , s)

#call print_triangular_numbers with 5 as parameter.       
print_triangular_numbers(5)
