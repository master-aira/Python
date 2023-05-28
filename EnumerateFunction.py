L1 = ["Bhindi","Aaloo","Chowmein","Chips"]
# i = 1
# for item in L1:
#     if i%2 != 0:
#         print(f"Jarvis Please Buy {item}")
#     i += 1
for index,item in enumerate(L1):
    if index % 2 == 0:
        print(f"Jarvis Please Buy {item}")