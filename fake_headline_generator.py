#import random module
import random 

#create list of subjects

subjects = [
    "Helios", 
    "Shahrukh Khan",
    "5",
    "Iron Man",
    "Thor",
    "The Prime Minister",
    "A Mumbai Cat",
    "Auto Rikhsaw Driver from Delhi"
]
           
actions=[
    "Launches",
    "cancels",
    "eats",
    "dances with",
    "orders",
    "celebrates",
    "declare war on"
]


places_or_things=[
    "at Red Fort",
    "in Mumbai Local Train",
    "inside parliament",
    "at Ganga Ghat",
    "during an ipl match",
    "at india gate"
]
            
# start the headline generator 
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)
 
    headline = print("BREAKING NEWS :", subject , action , place_or_thing )
    
    print("\n",headline)

    user_input = input("\nDo you want another headline? (yes/no)").strip().lower()

    if user_input == "no":
        break

# print a good bye message
print("\nThanks for using the fake news headline generator . Have a fun day")

           
            

            
            
             