#Die roll simulator
#Also look into how to multiples like 4d6
import random

def Dice_Bag(dice):
    
    dice = [*dice]
    number = dice[0]
    number = int(number)
    die = dice[2:]
    #print(f"this is the die {die} and this is the number {number}")
    
    #d4  OMG this works!!!!
    if die == ['4']:
        roll_history = []
        while number > 0:
            value = random.randint(1,4)
            roll_history.append(value)
            print(f"You rolled a {value}!")
            number = int(number)-1
        
        print(f"\nYour total roll is {sum(roll_history)}")
        roll_history = []
    
    #d6
    if die == ['6']:
        roll_history = []
        while number > 0:
            value = random.randint(1,6)
            roll_history.append(value)
            print(f"You rolled a {value}!")
            number = int(number)-1
        
        print(f"\nYour total roll is {sum(roll_history)}")
        roll_history = []    
        
    #d8
    if die == ['8']:
        roll_history = []
        while number > 0:
            value = random.randint(1,8)
            roll_history.append(value)
            print(f"You rolled a {value}!")
            number = int(number)-1
        
        print(f"\nYour total roll is {sum(roll_history)}")
        roll_history = []   
        
    #d10
    if die == ['1', '0']:
        roll_history = []
        while number > 0:
            value = random.randint(1,10)
            roll_history.append(value)
            print(f"You rolled a {value}!")
            number = int(number)-1
        
        print(f"\nYour total roll is {sum(roll_history)}")
        roll_history = [] 
        
    #d12
    if die == ['1', '2']:
        roll_history = []
        while number > 0:
            value = random.randint(1,12)
            roll_history.append(value)
            print(f"You rolled a {value}!")
            number = int(number)-1
        
        print(f"\nYour total roll is {sum(roll_history)}")
        roll_history = []     
        
    #d20
    if die == ['2', '0']:
        roll_history = []
        while number > 0:
            value = random.randint(1,20)
            roll_history.append(value)
            print(f"You rolled a {value}!")
            number = int(number)-1
        
        print(f"\nYour total roll is {sum(roll_history)}")
        roll_history = [] 
            
    #d100
    if die == ['1', '0', '0']:
        roll_history = []
        while number > 0:
            value = random.randint(1,100)
            roll_history.append(value)
            print(f"You rolled a {value}!")
            number = int(number)-1
        
        print(f"\nYour total roll is {sum(roll_history)}")
        roll_history = []     

Roll = input("What die do you need and how many (2d6)? ")
print("\n")    
Dice_Bag(Roll) 
print("\n Job Done")   



