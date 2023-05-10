#Designing a calculator which solves all the Problems except :- 45 * 3 = 555 , 56 + 9 = 77 , 56 / 6 = 4
f1 = int(input("Pehla No. Daale"))
o = input("Please Sirf Operator(+,-,*,/)hi daale DADA")
f2 = int(input("Dusra No. Daale"))
if f1 == 45 and f2 == 3 and o == "*":
    print("555")
elif f1 == 56 and o == "+" and f2 == 9:
    print("77")
elif f1 == 56 and o == "/" and f2 == 6:
    print("4")
elif o == "+":
    print(f1+f2)
elif o == "*":
    print(f1*f2)
elif o == "-":
    print(f1-f2)
elif o == "/":
    print(f1/f2)
else:
    print("Please Enter Valid Operator DADA")