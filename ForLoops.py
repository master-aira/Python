'''
L1 = [["Rajesh",43] ,["Rahul",56],["Raj",4], ["Rohit",0]]
for item,Money in L1:
    print(item ,"and He has", Money , "$")
'''
#Check if element in List is a no. or not then check if it is greater than 6
L2 = [ "Mohit" , 4 , 45 ,"Burger","Delhi"]
for item in L2:
    if type(item) == int and item > 6:
        print("Shi Khel Rhe Ho Bhai",item)
    else:
        print("Ky kr rhe ho Yaar")