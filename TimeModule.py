import time
o = time.time()
for i in range(10):
    print("Hello")
    time.sleep(2) #2 second ke liye samay ruk jayega
print("For ran in", time.time() - o)
k = 0
while k < 10:
    print("Bye")
    k = k + 1
print("While ran in", time.time() - o)
timenow = time.asctime(time.localtime(time.time()))
print(timenow)