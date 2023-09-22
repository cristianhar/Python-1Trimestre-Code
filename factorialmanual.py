def la_factoria(n):
    if n <2:
        return 1
    else :
        return n*la_factoria(n-1)

n = int(input("Factor de : "))
print(la_factoria(n))



