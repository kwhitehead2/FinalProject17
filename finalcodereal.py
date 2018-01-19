#Starting the game with an introduction. This tells the player what the game is about and sets up the theme o the game.
print("""You are walking alone at night when you hear a fall of footsteps behind you. You turn but see no one. You quicken your pace and continue to glance behind you. Just when you think you must have been just hearing things, you see a shadow. Before you can turn to get a good look your feel a cloth over your mouth and your vision goes black.""")

#this input asks the player his/her name and makes the answer the variable character so it can be used in the story line later
character = input("What is your name? ")

#more introduction to the game as the character learns the object of the game
print(f"{character} wakes up in a room blindfolded and tied to a chair. The room is empty and there is a door on the other side of the room. This is your chance to escape. The first thing you have to do is take off your blindfold.")

class questions(object):
    def __init__(self, q_text, a_text):
        self.question == q_text
        self.answer == a_text

#In the game there are 18 total questions the player is asked. This part of the code sets up two variables for each question
#there is a variable for the question and a variable for the answer
#Once these variables are set there the riddle diccionary is created for each question where the key question is paired with the specific question
#and the key answer is paired with a specific answer (the variables created for each question)
#each diccionary also includes an escape sentence, which instructs the player what to do next once they get the question right
question1 = 'What is the capitol of New Jersey'
answer1 = 'trenton'
riddle1 = {'question' : question1 , 'answer' : answer1 , 'escapesentence' : 'That is correct!! You have successfully taken off the blindfold. It is time to untie the ropes.'}

question2 = 'Who won the 2001 superbowl'
answer2 = 'ravens'
riddle2 = {f'question' : question2 , 'answer' : answer2, 'escapesentence' : 'You are correct {character}! you have now untied the ropes. {character} can see the key to the door on a table. {character} picks up the key. The final task is to oopen the door'}

question3 = 'Who starred as Belle in Disney/s live action Beauty and the Beast'
answer3 = 'emma watson'
riddle3 = {'question' : question3 , 'answer' : answer3, 'escapesentence' : 'You have successfully opened the door. But stepping through the door, you find yourself in another room. This room is filled with doors. The first step is to try to open the doors'}

question4 = 'Who is the Marvel superhero played by Chris Hemsworth?'
answer4 = 'thor'
riddle4 = {'question' : question4 , 'answer' : answer4, 'escapesentence' : 'Unfortunately all the doors are locked, you need to find the key. Looking around, you see a pair of keys hanging from a hook just above your reach. Will you be able to reach them?'}

question5 = 'Who created Carpool Karaoke?'
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

question9 = 'Tony winner Ben Platt starred in what Broadway Show in the last year'
answer9 = 'dear evan hansen'
riddle9 = {'question' : question9 , 'answer' : answer9, 'escapesentence' : 'The pin is a perfect fit! You jump back as the mirror wall swings open to reveal yet another room!'}

question10 = 'Who was the first superhero created?'
answer10 = 'superman'
riddle10 = {'question' : question10 , 'answer' : answer10, 'escapesentence' : 'You step into yet another room and the door slams shut behind you. You are in pitch dark. YOu hold your hand up to your face and can not see it through the darkness. The first step is to find any source of light.'}

question11 = 'True or False- Rome has never hosted the Summer Olympic Games'
answer11 = 'false'
riddle11 = {'question' : question11 , 'answer' : answer11, 'escapesentence' : 'As you fumble around in the dark you stub your toe on something. As you reach down you realize its a flashlight!'}

question12 = 'What is the name of Nemos dad in Finding Nemo?'
answer12 = 'merlin'
riddle12 = {'question' : question12 , 'answer' : answer12, 'escapesentence' : 'As you scan the room with a flashlight you find the door! You turn the knob and are realized to find its not locked. you are safe... for now.'}

question13 = 'How many Harry Potter books are there?'
answer13 = '7'
riddle13 = {'question' : question13 , 'answer' : answer13, 'escapesentence' : 'You can hear rain from outside! You must be getting close to getting out!! This room is filled with trap wires. You have to be careful to make sure you do not activate one!'}

question14 = 'Who is the current queen of england?'
answer14 = 'elizabeth'
riddle14 = {'question' : question14 , 'answer' : answer14, 'escapesentence' : 'You take a step forward and almost fall! You look down and see the the floor is covered in holes falling into a darkness. You have to make your way around without falling! can you do it?'}

question15 = 'What is Jay Gatsbys real name?'
answer15 = 'james gatz'
riddle15 ={'question' : question15 , 'answer' : answer15, 'escapesentence' : 'You have successfully made it through almost the entire room. There is just one more hole before the door. SPanning across it is a single piece of wood beam that you need to cross. Can you make it?'}

question16 = 'what is the fastest mammel in the world?'
answer16 = 'cheetah'
riddle16 = {'question' : question16 , 'answer' : answer16, 'escapesentence' : 'You made without falling! You find yourself in the final room. THere are windows showing the outside but they are covered in iron bars. There are 3 locks on the door! Can you get them undone?'}

question17 = 'Who is the richest man in the world currently?'
answer17 = 'jeff bozos'
riddle17 = {'question' : question17 , 'answer' : answer17, 'escapesentence' : 'You successful got off the first 2 locks! Only two to go and you will be free!'}

question18 = 'who is the current prime minister of Canada?'
answer18 = 'justin trudeau'
riddle18 = {'question' : question18 , 'answer' : answer18, 'escapesentence' : 'You got the final lock off!! You are free!! The sun is shining bright and you take a second to revel in your freedom.'}

#in order to reference each question and answer without running a specific code for each one, this list is made up of all the diccionaries
#that way by referencing just a number in the list question, a specific diccionary and question and answer set can be called
question = [riddle1 , riddle2 , riddle3 , riddle4 , riddle5 , riddle6 , riddle7 , riddle8 , riddle9 , riddle10 , riddle11 , riddle12 , riddle13 , riddle14 , riddle15 , riddle16 , riddle17 , riddle18]

#in the game if a player gets a question wrong they will be required to begin from the first question
#the variable counter represents which question the player is on. This counter begins at zero to represent the position of 'riddle1' in the question list
counter = 0

#if a player gets a question wrong they return to the begginning but they will only be allowed to get three wrong before losing the game
#the variable 'tries' is set at 3 to represent the number of attempts the player has at the beginning of the game
tries = 3

#The while loop w
while True:
    print(f"you have {tries} attempts left")
    if counter > 17:
        break
    elif tries <= 0:
        print("Sorry you have lost the game!")
        break

    else:
        answer = input(question[counter]['question']).lower()
        if answer == question[counter]['answer']:
            print(question[counter]['escapesentence'])
            counter += 1
        else:
            print('oh no! you have answered wrong! You turn around to see the hooded person behind you! They drag you back into the original room ')
            counter = 0
            tries -= 1

print("""---
Unfortunately your problems are not over yet. As you look up you are frightented to see the thing that captured you standing in the front yard. He turns and looks right at you. You feel a chill run through your bones. What will you do?""")


