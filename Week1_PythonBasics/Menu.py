import sys
def black_current():
    print("You chose Blackcurrent flavour!")

def vanilla():
    print("You chose Vanilla flavour!")

def chocobar():
    print("You chose Chocobar flavour!")

def strawberry():
    print("You chose Strawberry flavour!")

def mango_candy():
    print("You chose Mango Candy !")

def butterscotch():
    print("You chose Butterscotch flavour!")

def cone_icecream():
    print("You chose Cone IceCream!")

def invalid():
    print("Invalid Choice entered")
    
def end():
    print("End of Program")
    sys.exit()

menu = {
    1: black_current,
    2: vanilla,
    3: chocobar,
    4: butterscotch,
    5: strawberry,
    6: mango_candy,
    7: cone_icecream,
    8: end
}
print("CoolCool Ice Creams")
print("Menu : 1.Black Current 2. Vanilla 3.Chocobar 4.ButterScotch 5.Strawberry " \
    "6.Mango candy 7.Cone IceCream 8.Exit")
while True:
    choice = int(input("Enter choice: "))
    menu.get(choice,invalid)()
