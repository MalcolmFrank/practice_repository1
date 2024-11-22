#malcolm nov 21

#create a dictionary called rooms
rooms = {"1":[("E", "2")],
         "2":[("E", "5"), ("S", "3"), ("W", "1")],
         "3":[("N", "2"), ("E", "6"), ("W", "4")],
         "4":[("E", "4")],
         "5":[("W", "2")],
         "6":[("W", "3")]
         }

#draw a map and connect the rooms

def choose_direction(room):
    print("You are in a room. there are doors in the followong directions")
    for direction in rooms[room]:
        print(direction[0])
    #ask the user to choose direction
    user_choice = input("choose a direction: ")
    if user_choice == direction[0] :
        return pass
    #if user inputs invalid direction, tell the user no, and ask again

    #func should return a new room
choose_direction("1")
