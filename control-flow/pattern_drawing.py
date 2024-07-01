N=int(input("Enter the size of the pattern:"))
i=1
j=1
while i <= N:
    i=i+1
    j=0
    if i>2:
        print()
    while j <= N:
        print("*",end="")
        j=j+1