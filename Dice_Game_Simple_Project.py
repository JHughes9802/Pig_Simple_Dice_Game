import random

# I initially thought of doing a high/low game with dice, but decided it was too close to creating a coin toss game.
# So Instead, I went with the Pig dice game listed under the suggestions. It was close enough to what I already had
# in mind and didn't have to deal with any immediate problems of working with cards (suits and duplicate cards),
# so I felt it was a good choice.

# Features I would add if I immediately knew how: the ability to set the number of players and adding unicode dice.

def main():
    player1 = 0 # Sets player totals to 0 when a new game starts.
    player2 = 0
    goal = 100 # Lower this number when testing.
    player_tracker = 1 # A number to keep track of the current player. With more players I'd probably try to use a queue.
    new_total = Player_Turn()
    play_again_message = Again("\nWould you like to play again? (enter y for yes or n for no) ")

    print("\nStarting new game...\n\nFirst to 100 wins!")

    # This will continuously loop until a player's total reaches the goal.
    while player1 < goal and player2 < goal:

        # I'd likely change this into a class with more players.
        if player_tracker == 1:
            print("\nPlayer one, it's your turn!")
            player1 = new_total.Dice_Roll(player1, goal) # This sends the player's current total and goal to Dice_Roll, then it sets the returned value as the player's new current total.
            print("\nPlayer one's current total: " + str(player1))
            player_tracker = 2

        elif player_tracker == 2:
            print("\nPlayer two, it's your turn!")
            player2 = new_total.Dice_Roll(player2, goal)
            print("\nPlayer two's current total: " + str(player2))
            player_tracker = 1
    
    if player1 >= goal:
        print("\nCongratulations player one!")
    
    elif player2 >= goal:
        print("\nCongratulations player two!")

    # An if statement that loops back to the beginning if the user enters y or Y to play again.
    if play_again_message.Response() == True:
        main()

# This class runs each time a player's new turn starts. It first receives the player's current total and the goal to reach.
# Then, it rolls and checks to see if it rolled a one. If it didn't, it'll enter the while loop and continue rolling until
# either it rolls a one or the user tells it to stop. If the user says to stop rolling or their current total plus rolled
# total reaches the goal, it'll combine the two and return them to Main to "bank" (set) the new player total. If a one
# ever gets rolled, the class will set the total that gets added to the player's current total to zero and return it to Main.
class Player_Turn:
    def Dice_Roll (self, player_total, goal):
        self.player_total = player_total
        self.goal = goal
        total = 0
        roll = random.randint(1, 6)
        roll_again_message = Again("\nWould you like to roll again? (enter y for yes or n for no) ")
        
        if roll != 1:
            print(f"\n{roll}, currently rolled total: {total + roll}, your banked total: {self.player_total}")

        else:
            print("\n" + str(roll))

        while roll != 1:
            total = total + roll

            # This will break out of the while loop if the player's rolled total plus current total reaches the goal.
            if total >= (self.goal - self.player_total):
                break

            # This part asks the user after each roll whether or not they want to roll again.
            elif roll_again_message.Response() == True:
                roll = random.randint(1, 6)

                if roll != 1:
                    print(f"\n{roll}, currently rolled total: {total + roll}, your banked total: {self.player_total}")

                else:
                    print("\n" + str(roll))

            else:
                break

        if roll == 1:
            print("\nOops, you rolled a one. Sorry!")
            total = 0

        total = total + self.player_total

        return total

# This class runs after each time the dice is rolled (if it didn't roll a one) and after the game is finished.
# It's a simple design that merely asks the user to input y or n (not case-sensitive) for the question asked.
# It sticks inside the while loop and will repeatedly ask its question until the user enters y or n, where
# it'll then return true or false based on the response given.
class Again:
    def __init__ (self, message):
        self.message = message

    def Response (self):
        another = input(self.message).strip()

        # I got the "not in" with curly brackets from Stack Overflow. I tried to use operators I knew in a combination of how I
        # thought they would interact, but could only manage to get the 'y' to break out. So, I gave in and looked for answers.
        # Link to the page: https://stackoverflow.com/questions/26578277/multiple-conditions-with-while-loop-in-python
        while another.lower() not in { 'y' , 'n' }:
            another = input(self.message)

        if another.lower() == "y":
            return True
        
        return False

main()