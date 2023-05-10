def getdate():
    import datetime
    return datetime.datetime.now()
print(getdate())
c = input("W - Write | R - Retrieve")
n = input("H - Harry | R - Rohan | HD - Hamad")
sl = input("D - Diet | E - Exercise")
if c == "W" and n == "H" and sl == "D":
    o = open("HD.txt","w")
    s = o.write(input("Kuch Likho Bhai"))
    print("Kaam ho Gya Bhai at", getdate())
    o.close()
elif c == "W" and n == "H" and sl == "E":
    o = open("HE.txt","w")
    s = o.write(input("Kuch Likho Bhai"))
    print("Kaam ho Gya Bhai at", getdate())
    o.close()
elif c == "W" and n == "R" and sl == "D":
    o = open("RD.txt","w")
    s = o.write(input("Kuch Likho Bhai"))
    print("Kaam ho Gya Bhai at", getdate())
    o.close()
elif c == "W" and n == "R" and sl == "E":
    o = open("RE.txt","w")
    s = o.write(input("Kuch Likho Bhai"))
    print("Kaam ho Gya Bhai at", getdate())
    o.close()
elif c == "W" and n == "HD" and sl == "D":
    o = open("HDD.txt","w")
    s = o.write(input("Kuch Likho Bhai"))
    print("Kaam ho Gya Bhai at", getdate())
    o.close()
elif c == "W" and n == "HD" and sl == "E":
    o = open("HDE.txt","w")
    s = o.write(input("Kuch Likho Bhai"))
    print("Kaam ho Gya Bhai at", getdate())
    o.close()
elif c == "R" and n == "H" and sl == "D":
    o = open("HD.txt")
    print(getdate(),o.read())    
    o.close()
elif c == "R" and n == "H" and sl == "E":
    o = open("HE.txt")
    print(getdate(),o.read())    
    o.close()
elif c == "R" and n == "R" and sl == "D":
    o = open("RD.txt")
    print(getdate(),o.read())    
    o.close()
elif c == "R" and n == "R" and sl == "E":
    o = open("RE.txt")
    print(getdate(),o.read())    
    o.close()
elif c == "R" and n == "HD" and sl == "D":
    o = open("HDD.txt")
    print(getdate(),o.read())    
    o.close()
elif c == "R" and n == "HD" and sl == "E":
    o = open("HDE.txt")
    print(getdate(),o.read())    
    o.close()
else:
    print("Aaram se Beta")