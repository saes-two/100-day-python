print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")

left_or_right = input('Type "left" or "right"\n').lower()

if left_or_right == "left":
    print("You're come to a lake. There is an island in the middle of the lake.")
    wait_or_swim = input(' Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    
    if wait_or_swim == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        doors = input(" One red, one yellow and one blue. Which colour do you choose?\n").lower()

        if doors == "yellow":
            print("You found the treasure! You Win!")
        elif doors == "red":
            print("It's a room full of fire. Game Over.")
        elif doors == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("Game Over.")
            
    else:
        print("You get attacked by an angry trout. Game Over.")
        
else:
    print("You fell into a hole. Game Over.")