n = 13
i = 0
while i < 11:
    g = int(input("Please Enter Your Guess No."))
    print("No. of trials Left : ", 10 - i)
    i = i + 1
    if g < n:
        print("Kam Hai Tera No.")
    elif g > n:
        print("Jyada Hai Bhai")
    else:
        print("Are Waah!")
        break