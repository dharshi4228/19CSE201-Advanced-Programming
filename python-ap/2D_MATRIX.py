matrix=[]
r=int(input())
c=int(input())
for i in range(r):
     row=[]
     for j in range(c):
         d=int(input())
         row.append(d)
     matrix.append(row)
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print("\n")
