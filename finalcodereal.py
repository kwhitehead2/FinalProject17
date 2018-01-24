import sys

#Starting the game with an introduction. This tells the player what the game is about and sets up the theme o the game.
print("""You are walking alone at night when you hear a fall of footsteps behind you. You turn but see no one. You quicken your pace and continue to glance behind you. Just when you think you must have been just hearing things, you see a shadow. Before you can turn to get a good look your feel a cloth over your mouth and your vision goes black.""")

#this input asks the player his/her name and makes the answer the variable character so it can be used in the story line later
character = input("What is your name? ")

#more introduction to the game as the character learns the object of the game
print(f"{character} wakes up in a room blindfolded and tied to a chair. The room is empty and there is a door on the other side of the room. This is your chance to escape. The first thing you have to do is take off your blindfold.")

#In the game there are 18 total questions the player is asked. This part of the code sets up two variables for each question
#there is a variable for the question and a variable for the answer
#Once these variables are set there the riddle diccionary is created for each question where the key question is paired with the specific question
#and the key answer is paired with a specific answer (the variables created for each question)
#each diccionary also includes an escape sentence, which instructs the player what to do next once they get the question right

question1 = 'What is the capital of New Jersey? '
answer1 = 'trenton'
riddle1 = {'question' : question1 , 'answer' : answer1 , 'escapesentence' : 'That is correct!! You have successfully taken off the blindfold. It is time to untie the ropes.'}

question2 = 'Who won the 2001 superbowl? '
answer2 = 'ravens'
riddle2 = {'question' : question2 , 'answer' : answer2, 'escapesentence' : 'You are correct! you have now untied the ropes. You can see the key to the door on a table. You pick up the key. The final task is to oopen the door'}

question3 = 'Who starred as Belle in Disney/s live action Beauty and the Beast? '
answer3 = 'emma watson'
riddle3 = {'question' : question3 , 'answer' : answer3, 'escapesentence' : 'You have successfully opened the door. But stepping through the door, you find yourself in another room. This room is filled with doors. The first step is to try to open the doors'}

question4 = 'Who is the Marvel superhero played by Chris Hemsworth? '
answer4 = 'thor'
riddle4 = {'question' : question4 , 'answer' : answer4, 'escapesentence' : 'Unfortunately all the doors are locked, you need to find the key. Looking around, you see a pair of keys hanging from a hook just above your reach. Will you be able to reach them?'}

question5 = 'Who created Carpool Karaoke? '
answer5 = 'james corden'
riddle5 = {'question' : question5 , 'answer' : answer5, 'escapesentence' : 'You successfully reached the keys! The final step is to get out of this room? But what door do you pick?'}

question6 = 'where was the 2016 summer olympics held?'
answer6 = 'rio'
riddle6 = {'question' : question6 , 'answer' : answer6, 'escapesentence' : 'You picked the right door! As you walk into the next room, you realized something is weird. The entire room is covered in mirrors. There are no doors in sight! You started to search the room'}

question7 = 'The character Jar Jar Binks first appears in which star wars movie?'
answer7 = 'the phantom menace'
riddle7 = {'question' : question7 , 'answer' : answer7, 'escapesentence' : 'While searching the room you come across a small crack in a mirror. Will this be a way out?'}

question8 = 'What late night comedy show first aired in 1975?'
answer8 = 'saturday night live'
riddle8 = {'question' : question8 , 'answer' : answer8, 'escapesentence' : 'Just as you are about to give up, you realize you have a pin on your shirt that will fit into the crack!. You take it off and try to push it into the crack'}

question9 = 'Tony winner Ben Platt starred in what Broadway Show in the last year? '
answer9 = 'dear evan hansen'
riddle9 = {'question' : question9 , 'answer' : answer9, 'escapesentence' : 'The pin is a perfect fit! You jump back as the mirror wall swings open to reveal yet another room!'}

question10 = 'What is the biggest country in the world? '
answer10 = 'russia'
riddle10 = {'question' : question10 , 'answer' : answer10, 'escapesentence' : 'You step into yet another room and the door slams shut behind you. You are in pitch dark. YOu hold your hand up to your face and can not see it through the darkness. The first step is to find any source of light.'}

question11 = 'True or False- Rome has never hosted the Summer Olympic Games. '
answer11 = 'false'
riddle11 = {'question' : question11 , 'answer' : answer11, 'escapesentence' : 'As you fumble around in the dark you stub your toe on something. As you reach down you realize its a flashlight!'}

question12 = 'What is the name of Nemos dad in Finding Nemo? '
answer12 = 'merlin'
riddle12 = {'question' : question12 , 'answer' : answer12, 'escapesentence' : 'As you scan the room with a flashlight you find the door! You turn the knob and are realized to find its not locked. you are safe... for now.'}

question13 = 'How many Harry Potter books are there? '
answer13 = '7'
riddle13 = {'question' : question13 , 'answer' : answer13, 'escapesentence' : 'You can hear rain from outside! You must be getting close to getting out!! This room is filled with trap wires. You have to be careful to make sure you do not activate one!'}

question14 = 'Who is the current queen of England? '
answer14 = 'elizabeth'
riddle14 = {'question' : question14 , 'answer' : answer14, 'escapesentence' : 'You take a step forward and almost fall! You look down and see the the floor is covered in holes falling into a darkness. You have to make your way around without falling! can you do it?'}

question15 = 'What is Jay Gatsbys real name? '
answer15 = 'james gatz'
riddle15 ={'question' : question15 , 'answer' : answer15, 'escapesentence' : 'You have successfully made it through almost the entire room. There is just one more hole before the door. SPanning across it is a single piece of wood beam that you need to cross. Can you make it?'}

question16 = 'What is the largest organ in your body? '
answer16 = 'skin'
riddle16 = {'question' : question16 , 'answer' : answer16, 'escapesentence' : 'You made without falling! You find yourself in the final room. THere are windows showing the outside but they are covered in iron bars. There are 3 locks on the door! Can you get them undone?'}

question17 = 'Who is the richest man in the world currently? '
answer17 = 'jeff bozos'
riddle17 = {'question' : question17 , 'answer' : answer17, 'escapesentence' : 'You successful got off the first 2 locks! Only 1 to go and you will be free!'}

question18 = 'who is the current prime minister of Canada? '
answer18 = 'justin trudeau'
riddle18 = {'question' : question18 , 'answer' : answer18, 'escapesentence' : 'You got the final lock off!! You are free!! The sun is shining bright and you take a second to revel in your freedom.'}

#in order to reference each question and answer without running a specific code for each one, this list is made up of all the diccionaries
#that way by referencing just a number in the list question, a specific diccionary and question and answer set can be called
question = [riddle1 , riddle2 , riddle3 , riddle4 , riddle5 , riddle6 , riddle7 , riddle8 , riddle9 , riddle10 , riddle11 , riddle12 , riddle13 , riddle14 , riddle15 , riddle16 , riddle17 , riddle18]

#in the game if a player gets a question wrong they will be required to begin from the first question
#the variable counter represents which question the player is on. This counter begins at zero to represent the position of 'riddle1' in the question list
counter = 0

#if a player gets a question wrong they return to the begginning but they will only be allowed to get 5 wrong before losing the game
#the variable 'tries' is set at 5 to represent the number of attempts the player has at the beginning of the game
tries = 5

#The while loop is being used to ask the questions set up in the diccionaries in a loop. It is set as 'while true' so after a question
#is asked the loop will continue
while True:
#the first thing that will happen each time is a sentence will print to tell the player how many tries they have left
    print(f"you have {tries} attempts left")
#if the counter number (aka the question number) reaches higher then 17 it means that the plaey has passed this level in the game
#this if statement will break the loop if this is the case so the player can move on to the next part
    if counter > 17:
        break
#the elif following concerns the amount of tries the player has used
#if the player has used up all their tries the game will be over and the code will end with sys.exit()
    elif tries <= 0:
        print("Sorry you have lost the game!")
        sys.exit()
#if the player has enough tries and the counter is less than 17 then the player will be prompted to answer a question
#this answer is set as a variable answer using the input function below
    else:
        answer = input(question[counter]['question']).lower()
#If the answer is correct the 'escape sentence' from the dictionaries above will be printed and 1 will be added to the counter variable
#this means that when the loop begins again the next question will be asked
        if answer == question[counter]['answer']:
            print(question[counter]['escapesentence'])
            print("---")
            counter += 1
#if the player gives the wrong answer then then the following sentance will be printed and the counter is set to 0
#this means that the player has to start from the beginning of the game
        else:
            print('oh no! you have answered wrong! You turn around to see the hooded person behind you! They drag you back into the original room ')
            counter = 0
#one is also subtracted from tries so that when the loops goes back it will print one less try
            tries -= 1

#once the player has answered all the questions correctly they will be set into the second section of the game
print("""---
Unfortunately your problems are not over yet. As you look up you are frightented to see the thing that captured you standing in the front yard. He turns and looks right at you. You feel a chill run through your bones. What will you do?""")

#because the function later uses random integers this first imports randint function so I can use it later
from random import randint

#this class is used to set temporary names and lives for the characters. The characters will be fighting and losing life so the class is needed
class Character(object):
    def __init__(self,name, life):
        self.name = name
        self.life = life

#these two variables define the player and the opponent as part of the class above
#Both characters begin with lives at 100
player = Character("you", 100)
opponent = Character("opponent", 100)

#This is defining an attack function
#when this function is called the player will lose life of a random value from 0-20
#the opponent will lose life of a random value from 0-25
def attack1():
        player.life -= randint(0,20)
        opponent.life -= randint(0,25)
        print(f"{opponent.name}'s life is now {opponent.life}! You haven't defeated him yet! Keep attacking!")
        print(f"{player.name}'s life is now {player.life}! Be careful! You have to defeat your opponent before you die!")

#this function allows the player to run instead of attack. If the player chooses not to attack they will lose life
def run1():
    player.life -=20
    print(f"{player.name} tried to run and fell! You get back up, but now {player.name}r life is {player.life}")

#This while loop will continue the attack until either the player or the opponent loses
while True:
#if the players life reaches 0 the player loses and the games ends
    if player.life <= 0:
        print(f"Oh no it looks like your {opponent.name} got the best of you! You have lost the game")
        break
#if the opponents life reaches 0 the player wins the game
    elif opponent.life <= 0:
        print(f"Congrats! You have defeated your {opponent.name}! You rush by him and run home safe and sound! Be more careful walking around alone next time")
        break
#if both the player and opponents life is greater then 0 an imput asks if the player wants to attack and sets this answer as the action variable
#if the answer is yes then the attack function above is called
#if the answer is no the player will try to run and lose life
#if the player does no put yes or no the player will be asked to put a valid input of yes or no
    else:
        action = input("Do you want to attack. (yes or no)")
        if action == "yes":
            attack1()
        elif action == "no":
            run1()
        else:
            print("invalid input please answer yes or no")








