# number of rows in a matrix
N = 1024

f1 = open("mdata1.inp", "w")
f2 = open("mdata2.inp", "w")

f1.write(str(N) + " " + str(N) + "\n") 
for i in range(N):
    for j in range(N):
        f1.write("1 ")
    f1.write("\n")

f1.write(str(N) + " " + str(N) + "\n") 
for i in range(N):
    for j in range(N):
        f2.write("1 ")
    f2.write("\n")

f1.close()
f2.close()
