o = open("College.txt")
print(o.tell()) #It gives the Location of the pointer
o.readline()
print(o.tell())
o.readline()
print(o.tell())
o.readline()
o.seek(0) #It moves the pointer Jaha hm chahe
print(o.tell())
o.close()