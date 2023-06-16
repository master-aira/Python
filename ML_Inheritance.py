class Electronic_Gadgets:
    charge_required = 1
class Pocket_Devices(Electronic_Gadgets):
    Mobility = "Possible"
class Mobile_Phone(Pocket_Devices):
    wireless = "Available"
    charge_required = 9
EG = Electronic_Gadgets()
PD = Pocket_Devices()
MP = Mobile_Phone()
# print(MP.charge_required)
print(MP.Mobility)