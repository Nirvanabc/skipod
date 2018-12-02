import itertools
import os

nThreadsList = [8, 16, 32, 64, 120, 160]
# sizesList = [512, 1024, 1536, 2048, 2560]
sizesList = [64, 512, 1024, 1536]

# os.system("rm *.out *.err")
# os.system("rm main")

ITER_NUM = 4

for nThreads in nThreadsList:
    for sz in sizesList:
        for v in range(ITER_NUM):
            # echo 100 10 60 | ./a.out
            os.system("echo " + str(sz) + " " + 
                      str(sz//10) +  " " + 
                      str(nThreads) + " | ./a.out")
