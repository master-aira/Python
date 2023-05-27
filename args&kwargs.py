# def name(a , b , c , d):
#     print(a , b , c ,d)
# name("Hello" , "Boy" , "Gord" , "Doobaaa")
def dargs(*args,**kwargs):
    #print(args[0])
    for item in args,kwargs:
        print(item)
Lid = ["Shimla","Delhi","Mumbai"]
Gid = {"naruto":"haikyu"}
dargs(*Lid , **Gid)