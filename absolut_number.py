def sum(a, b):
        if b < a:
            return(a-b)
        elif b > a:
            return(b-a)
        else:
            return(0)

print(sum(7,4))
print(sum(2,4))
print(sum(9,9))