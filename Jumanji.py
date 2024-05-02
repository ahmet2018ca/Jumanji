
import random, math

def zero_lives_left_quit_game():   
    
    global format_nodes
    
    print(format_nodes)

    print("What an unfortunate series of events. I am sorry but this is where our journey ends.\n")
    print("You have made too many bad mistakes and now have 0 lives left meaning you lost the game and cant comeback to real life.\n")
    print("But you can still retry, if you want...\n")
    print("Would you like to restart the game?\n")

    print("Type 'yes' to restart the game or type 'no' or 'exit' to quit\n")

    user_restart_response = input("").lower()

    if user_restart_response == "yes":
        print("Alright I am restarting the game, good luck.\n")
        main()
    elif user_restart_response == "exit" or user_restart_response == "no":
        print("Alright, goodbye. Till next time we meet again.")
        exit()
    else:
        print("Could you please only type the answers given please? thanks.")
        zero_lives_left_quit_game()



def character_lives_left(lives_lost):

    global lives_left

    lives_left = lives_left - lives_lost

    if lives_left == 0:
        zero_lives_left_quit_game()
    
    if lives_left > 0:
        return lives_left



def show_inventory():

    global players_character_choice
    lives_left_in_game = character_lives_left(0)
    global gun_generator_per_situation
    global joker_token
    global pet_cheetah
    global cute_puppy
    global millions_in_game

    print(format_nodes)

    print("Here Are The Things In Your Inventory\n")
    
    if players_character_choice == "":

        print("Character = You don't have a charcter yet\n")
    else:
        print(f"Character = {players_character_choice}\n")
    
    if gun_generator_per_situation == True:
        print("Gun Generator Per Situation = Meaning the game will give you a gun when you go against an enemy.\n")
    if joker_token == True:
        print("A Joker Token  //  This Token Helps you get out of any bad situation\n")
    if pet_cheetah == True:
        print("You Have A Pet Cheetah  //  This Cheetah will help to protect you against dangerous things.\n")
    if cute_puppy == True:
        print("You Have A Cute Puppy   //  I dont know how a cute puppy will come in handy but, lets see...\n")
    if millions_in_game == True:
        print("Millions Of In Game Currency //  This much in game currency might help you to pay some people off so they leave you alone...\n")

    print(f"You Have {lives_left_in_game} lives left\n")
    print("This is your current Inventory, If you read and understood what you have in your inventory, than press 'Enter' to continue from where you left off")

    press_enter_to_continue = input("")

    if press_enter_to_continue == "":
        return None
    else:
        print("You might have pressed another key before pressing Enter, please try again to continue to the game")
        show_inventory()



def exit_or_see_inventory(user_input):

    global format_nodes
    
    if user_input == "exit":
        print("\nGoodbye, I hope you enjoyed my game")
        exit()

    elif user_input == "inventory":
        show_inventory()

    else:
        return None




def instructions_for_game():
    

    global format_nodes

    print(format_nodes)
    
    print("Welcome to Jumanji\n")
    print("Before starting to play this game there are some keybinds you should know, to help you have a better time.\n")
    print("If at any point you would like to quit the game, just type 'exit' to terminal, but be careful to write it in all lowercase.\n")
    print("To pick an option, either type the letter that represents the option or type the full option\n")
    print("example, A) run away. You could either type 'A' at any case or type 'run away' to pick that option.\n")
    print("The 2nd case only works when the choice is short, since sometimes the choices are a lot more longer for user to understand the choice better.\n")
    print("That is why I will mostly encourage you to use the letter that represents the choice. That will always work.\n")
    print("You can also type 'inventory' into the console to see your current inventory, but be careful to write it in all lowercase.\n")
    print("If you understood all of that, and want to start the game just press 'Enter'\n")
    print("I hope you enjoy Jumanji, Good Luck\n")
    pressed_enter = input("").lower()
    

    if pressed_enter == "":     
        prologue() 

    elif pressed_enter == "exit" or pressed_enter == "inventory":
        exit_or_see_inventory(pressed_enter)
        instructions_for_game()

    else:
        print("\nYou might have pressed another button, try to press Enter only next time to continue\n")
        instructions_for_game()



def prologue():

    global format_nodes

    print(format_nodes)

    print("You are playing a choose your own adventure video game. In this game there are a lot of probability and math questions that can decide your future.\n")
    print("Whenever you go against an enemy, the game will give you 3 guns to use in that situation or you can use the things in your inventory that you have collected before\n")
    print("While you are playing your body suddenly  gets sucked into the game, and you are now inside the game.\n")
    print("Finish the game without losing your 3 lives and get back to the real world. And dont forget, its an adventure game, dont think so logically :)\n")
    print("Good Luck!\n")
    print("\npress Enter to continue\n")

    pressed_enter = input("").lower()
    
    if pressed_enter == "":
        character_selection()

    elif pressed_enter == "exit" or pressed_enter == "inventory":
        exit_or_see_inventory(pressed_enter)
        prologue()

    else:
        print("\nCould You Pleaseee Press Enter Only?")
        prologue()


def character_selection():
    
    global two_lines_down 
    global format_nodes

    print(format_nodes)

    print("Luckily, you hadn't picked your character before getting sucked into the game.\n")
    print("Be careful of which character you choose, it will greatly affect your future.\n")
    print("So, which one will you choose?\n")

    #Character 1
    print(f"{two_lines_down} A) Mr. Lucky \n")
    print("Mr. Lucky gives you a 25% more chance of being more favorable during a tough situation.")

    #Character 2 
    print(f"{two_lines_down} B) MEGAMIND \n")
    print("MEGAMIND makes the math problems you get after getting into rough situations a lot easier.")
    print("It might save your life. Who knows.")

    #Character 3
    print(f"{two_lines_down} C) Animal Andy \n")
    print("Animal Andy is able to communicate with animals and be friends with them.")
    print("This will probably get you out of bad situations such as walking into a hungry predator")

    print(f"{two_lines_down}To pick your character, type the letter that represents the character or the characters name\n")

    character_choice = input("").lower()

    if character_choice == "a" or character_choice == "mr. lucky":
        which_character("mr. lucky")
        check_the_cave()

    elif character_choice == "b" or character_choice == "megamind":
        which_character("megamind")  
        check_the_cave()

    elif character_choice == "c" or character_choice == "animal andy":
        which_character("animal andy")
        check_the_cave()   
    elif character_choice == "exit" or character_choice == "inventory":
        exit_or_see_inventory(character_choice)
        character_selection() 
    else:
        print("\nOops, you might have pressed another button than the ones given to you.\n")
        character_selection()



def which_character (character_name):
    
    global players_character_choice
    
    if character_name == "mr. lucky":
        players_character_choice = "Mr. Lucky"
    
    elif character_name == "megamind":
        players_character_choice = "MEGAMIND"
    
    else:
        players_character_choice = "Animal Andy"
    
    return players_character_choice

    

def check_the_cave():
    
    global format_nodes
    global players_character_choice
    global two_lines_down
    characters_name = players_character_choice
   
    print(format_nodes)

    print(f"Great Choice, to be honest I would have also picked {characters_name}\n")
    print("Alright, now you spawn  a bit further away from the first event that is going to happen.\n")
    print("You are on your way to the first event but you see a mysterious Cave on your way to the first checkpoint.\n")
    print("Would you like to check the cave out? I don't know, something valuable might be in there ;D ")

    print(two_lines_down)
    print("A) Nope I am fine\n")
    print("B) Oh yes, I would love to\n")

    go_into_cave = input("").lower()

    if go_into_cave == "a" or go_into_cave == "Nope I am fine":
        sure_not_to_check_cave()
        
    elif go_into_cave == "b" or go_into_cave == "Oh yes, I would love to":
        walk_into_cave()
    
    elif go_into_cave == "exit" or go_into_cave == "inventory":
        exit_or_see_inventory(go_into_cave)
        accepted_joker_token_now_wish()
    
    else:
        print("\nOops, you might have pressed another button than the ones given to you. Retry with the ones that have been given\n")
        check_the_cave()


def sure_not_to_check_cave():
    
    global two_lines_down
    global format_nodes


    print(format_nodes)

    print("Are you reaaally sure that you don't want to check it out?")

    print(two_lines_down)

    print("A) Nope I dont want to check it out. I want to lose out on valuable things.\n")
    print("B) Alright, I will check out the cave\n")


    are_u_sure = input("").lower()


    if are_u_sure == "a" or are_u_sure == "nope i dont want to check it out. i want to lose out on valuable things.":
        didnt_go_in_cave_or_no_joker()
    
    elif are_u_sure == "b" or are_u_sure == "alright, i will check out the cave":
        walk_into_cave()
    elif are_u_sure == "exit" or are_u_sure == "inventory":
        exit_or_see_inventory(are_u_sure)
        accepted_joker_token_now_wish()
    else:
        print("\nOops, you might have pressed another button than the ones given to you. Retry with the ones that have been given\n")
        sure_not_to_check_cave()


def walk_into_cave():
    
    global two_lines_down
    global format_nodes

    print(format_nodes)

    print("You walk into the cave without fear and see a lamp on the rock.\n")
    print("It looks interesting, would you like to get a closer look at it?")

    print(two_lines_down)

    print("A) Oh Yes, I would love to get a closer look at the lamp.\n")
    print("B) Nope I am a total coward\n")
    
    closer_look = input("").lower()

    if closer_look == "a" or closer_look == "Oh Yes, I would love to get a closer look at the lamp":
        genie_offers_special_token()
    
    elif closer_look == "b" or closer_look == "Nope I am a total coward":
        genie_is_mad_for_cowardness()
    elif closer_look == "exit" or closer_look == "inventory":
        exit_or_see_inventory(closer_look)
        accepted_joker_token_now_wish() 
    else:
        print("\nOops, you might have pressed another button than the ones given to you. Retry with the ones that have been given\n")
        walk_into_cave()


def genie_is_mad_for_cowardness():
    
    global two_lines_down
    global format_nodes
    global players_character_choice
    
    print(format_nodes)

    print("It seems like there is a genie inside the lamp and has sensed your cowardness. Genie's that are from here dont like non-adventorus cowards.\n")
    print("There is a '70%' chance the Genie will calm down and greet you normally,\n")
    print(" but there is a '30%' chance he will come out of the lamp and break your spine in half\n")
    print("and will make you lose 1 life and lose your chance with the genie.\n")
    
    print(two_lines_down)
    print("Or you can solve a math question and make the genie come out all happy,\n")
    print("but if you get the question wrong you lose 1 life and lose your chance with the genie.\n")
    
    print(two_lines_down)
    print("Will you hope and take that '70%' chance or will you solve the math question?\n")

    if players_character_choice == "Mr. Lucky":
        print(two_lines_down)
        print("A) I wont need to hope because I am Mr. Lucky. I have a '95%' chance to win!\n")
        print("C) Send over the math question, I got this \n")

    elif players_character_choice == "MEGAMIND":
        print(two_lines_down)
        print("D) Send over that easy question, I am MEGAMIND!\n")
        print("B) I will pray and take the '70%' chance please\n")
    
    else: 
        print(two_lines_down)
        print("C) Send over the math question, I got this\n")
        print("B) I will pray and take the '70%' chance please\n")

   
    genie_mad = input("").lower()

    if genie_mad == "a" or genie_mad == "b":
        genie_is_mad_gamble()
    
    elif genie_mad == "c" or genie_mad == "d":
        genie_is_mad_math()
    
    elif genie_mad == "exit" or genie_mad == "inventory":
        exit_or_see_inventory(genie_mad)
        accepted_joker_token_now_wish()
    
    else:
        print("Can you try answering it again? Your answer wasnt expected")
    

def genie_gamble_others():
    
    random_num = random.randint(1, 100) 
    
    if random_num < 76:
        won_genie_gamble()
    
    else:
        lost_genie_gamble()


def genie_gamble_mr_lucky():
    
    random_num = random.randint(1, 100) 
    
    if random_num < 96:
        won_genie_gamble()
    
    else:
        lost_genie_gamble()



def genie_is_mad_gamble():
    
    global players_character_choice
    
    
    if players_character_choice == "Mr. Lucky":
        genie_gamble_mr_lucky()
    
    elif players_character_choice == "MEGAMIND" or players_character_choice == "Animal Andy":
        
        genie_gamble_others()
        
        
def math_question_megamind():
    
    global format_nodes

    print(format_nodes)

    a = random.randint(1, 13)
    b = random.randint(1, 13)
    multiplication_total_integer = a * b
    
    multiplication_total = str(multiplication_total_integer)
    
    print(f"what is {a} * {b} \n")
    
    print(multiplication_total)

    user_answer = input("")
        
    if user_answer == multiplication_total:
        won_genie_math()
    
    elif user_answer.isalpha() == True:
        print("Could you please type in a number?\n")
        genie_is_mad_math()
    
    elif user_answer == "exit" or user_answer == "inventory":
        exit_or_see_inventory(user_answer)
        accepted_joker_token_now_wish()
    
    else:
        lost_genie_math()
     
    

def math_question_others():
    
    global format_nodes
    
    print(format_nodes)

    a = random.randint(1, 13)
    b = random.randint(1, 13) 
    exponent_total_integer = a ** b  #or math.pow()

    print(exponent_total_integer)

    exponent_total = str(exponent_total_integer)

    print(f"what is {a} ^ {b} \n")

    user_answer = input("")

    if user_answer == exponent_total:
        won_genie_math()
        
    elif user_answer.isalpha() == True:
        print("Could you please type in a number?\n")
        genie_is_mad_math()
    
    elif user_answer == "exit" or user_answer == "inventory":
        exit_or_see_inventory(user_answer)
        accepted_joker_token_now_wish()
    
    else:
        lost_genie_math()
  

def genie_is_mad_math():

    global players_character_choice
    global lives_left
    
    if players_character_choice == "MEGAMIND":
        math_question_megamind()
    
    elif players_character_choice == "Mr. Lucky" or players_character_choice == "Animal Andy":
        math_question_others()


def genie_offers_special_token():

    global joker_token
    global format_nodes

    print(format_nodes)

    print("Nice job for not being so scared. The Genie kind of likes you. And he wants to offer you something special.\n")
    print("This special thing is better than all of the other options.\n")
    print("It is a Joker Token, helping you move onto the next chapter without losing anything.\n")
    print("It is basically a free pass out of trouble.\n")
    print("Would you like to have it?\n")

    print("A) Yes I would love to\n")
    print("B) No its ok, I like to miss out on great oppurtunities.\n")

    user_token_decision = input("").lower()

    if user_token_decision == "a" or user_token_decision == "Yes I would love to":
        joker_token = True
        accepted_joker_token_now_wish()

    elif user_token_decision == "b" or user_token_decision == "No its ok, I like to miss out on great oppurtunities":
        didnt_go_in_cave_or_no_joker()

    elif user_token_decision == "exit" or user_token_decision == "inventory":
        exit_or_see_inventory(user_token_decision)
        genie_offers_special_token()
    
    else:
        print("Your answer wasn't expected, could you retry again please?")
        genie_offers_special_token()



def accepted_joker_token_now_wish():
    
    global format_nodes
    
    print(format_nodes)

    print("Alright Nice, the genie has given you a Joker Token,\n")
    print("now wish for something that could be useful to you in the story\n")
    print("Here are the things you can wish for\n")

    print("A) Hungry Grizzly Bear\n")
    print("B) Pet Cheetah\n")
    print("C) Cute Puppy\n")
    print("D) Millions of In game Currency\n")

    user_wish = input("").lower()

    if user_wish == "a" or user_wish == "hungry grizzly bear":
        chose_hungry_grizzly_bear()   
    
    elif user_wish == "b" or user_wish == "pet cheetah":
        chose_pet_cheetah()
    
    elif user_wish == "c" or user_wish == "cute puppy":
        chose_cute_puppy()
    
    elif user_wish == "d" or user_wish == "millions of in game currency":
        chose_millions_currency()
    
    elif user_wish == "exit" or user_wish == "inventory":
        exit_or_see_inventory(user_wish)
        accepted_joker_token_now_wish()
    
    elif user_wish == "exit" or user_wish == "inventory":
        exit_or_see_inventory(user_wish)
        accepted_joker_token_now_wish()
    
    else:
        print("Could you retry typing your answer? You accidentally pressed another button or wrote something unexpected.")
        accepted_joker_token_now_wish()


def lost_genie_math():

    global lives_left
    global format_nodes

    character_lives_left(1)
    
    print(format_nodes)

    print("Im sorry, you got it incorrect\n")
    print("Oh no, it seems like you have given the wrong answer. How unfortunate.\n")
    print("You lose one of your lives but don't worry, the story hasn't ended yet. You can still win. Keep your head up.\n")
    print("Press Enter To Continue")

    press_enter = input("").lower()

    if press_enter == "":
        spawn_outside_cave_lost_a_life()

    elif press_enter == "exit" or press_enter == "inventory":
        exit_or_see_inventory(press_enter)
        lost_genie_math()

    else:
        print("You might have pressed another key before enter, could you try again?")
        lost_genie_math()


def lost_genie_gamble():
    
    global lives_left
    global format_nodes

    character_lives_left(1)

    print(format_nodes)

    print("You Lost The Gamble\n")
    print("Oh No, unfortunatly you are not a very lucky person, you did not win the gamble.\n")
    print("This means that you have lost 1 life and you didnt get to talk to the genie. But hey its all good. You can still win, I believe you.\n")
    
    
    press_enter = input("").lower()

    if press_enter == "":
        spawn_outside_cave_lost_a_life()

    elif press_enter == "exit" or press_enter == "inventory":
        exit_or_see_inventory(press_enter)
        lost_genie_math()

    else:
        print("You might have pressed another key before enter, could you try again?")
        lost_genie_math()



def won_genie_gamble():

    global format_nodes

    print(format_nodes)

    print("Nice You Won the Gamble\n")
    print("Lucky you, you have won the gamble and the genie has came out of the lamp all calm.\n")
    print("Genie will give you 4 different options. Make sure to wish for something that will help you throughout the game.\n")
    
    print("A) Hungry Grizzly Bear\n")
    print("B) Pet Cheetah\n")
    print("C) Cute Puppy\n")
    print("D) Millions of In game Currency\n")

    user_wish = input("").lower()
    
    if user_wish == "a" or user_wish == "hungry grizzly bear":
        chose_hungry_grizzly_bear()   
    elif user_wish == "b" or user_wish == "pet cheetah":
        chose_pet_cheetah()
    elif user_wish == "c" or user_wish == "cute puppy":
        chose_cute_puppy()
    elif user_wish == "d" or user_wish == "millions of in game currency":
        chose_millions_currency()
    elif user_wish == "exit" or user_wish == "inventory":
        exit_or_see_inventory(user_wish)
        accepted_joker_token_now_wish()
    else:
        print("Could you retry typing your answer? You accidentally pressed another button or wrote something unexpected.")
        won_genie_gamble()



def won_genie_math():

    global format_nodes

    print(format_nodes)

    print("Your Answer Was Correct\n")
    print("Correct answer Einstein. Great job with the math work. The genie is all yours.\n")
    print("Genie will give you 4 different options. Make sure to wish something well.\n")

    print("A) Hungry Grizzly Bear\n")
    print("B) Pet Cheetah\n")
    print("C) Cute Puppy\n")
    print("D) Millions of In game Currency\n")

    user_wish = input("").lower()
    
    if user_wish == "a" or user_wish == "hungry grizzly bear":
        chose_hungry_grizzly_bear()   
    elif user_wish == "b" or user_wish == "pet cheetah":
        chose_pet_cheetah()
    elif user_wish == "c" or user_wish == "cute puppy":
        chose_cute_puppy()
    elif user_wish == "d" or user_wish == "millions of in game currency":
        chose_millions_currency()
    elif user_wish == "exit" or user_wish == "inventory":
        exit_or_see_inventory(user_wish)
        accepted_joker_token_now_wish()
    else:
        print("Could you retry typing your answer? You accidentally pressed another button or wrote something unexpected.")
        won_genie_math()




def chose_hungry_grizzly_bear():

    global format_nodes

    character_lives_left(1)

    print(format_nodes)

    print("Uhhhh, did you not read the option? It says A 'HUNGRY GRIZZLY BEAR''.\n")
    print("The bear hungry grizzly bear spawns right beside you.\n")
    print("And breaks all of your bones and pulls all of your organs out. A horrible way to go, not gonna lie.\n")
   
    spawn_outside_cave_lost_a_life()



def chose_pet_cheetah():

    global pet_cheetah 
    global format_nodes
    
    pet_cheetah = True

    print(format_nodes)

    print("Oh nice, interesting choice.\n")
    print("I guess if you ever need to outrun something,\n")
    print("you can hop on the pet cheetah and you will be fine. Good luck.\n")
    
    walkout_with_new_item()


def chose_cute_puppy():
    
    global cute_puppy 
    global format_nodes

    cute_puppy = True

    print(format_nodes)

    print("Uhhh, I'm not sure if a cute puppy will help you")
    print("against the dangerous lands of a  adventure game.\n")
    print("But you never know. It might come in handy.\n")
    walkout_with_new_item()

def chose_millions_currency():

    global millions_in_game 
    global format_nodes

    millions_in_game = True

    print(format_nodes)

    print("Oh I see I guess You like big money in your pockets\n")
    print(" Well hopefully it pays off. (Pun intended)")
    
    walkout_with_new_item()

#---------------------------------


def spawn_outside_cave_lost_a_life():
    
    global format_nodes

    print(format_nodes)

    print("So u spawn outside of the cave after losing 1 life.\n")
    print("U get back on the road to checkpoint number 1.\n")
    
    print("Press Enter To Continue")

    press_enter = input("").lower()

    if press_enter == "":
        pick_chimpanzee_or_lion_event()

    elif press_enter == "exit" or press_enter == "inventory":
        exit_or_see_inventory(press_enter)
        spawn_outside_cave_lost_a_life()

    else:
        print("You might have pressed another key before enter, could you try again?")
        spawn_outside_cave_lost_a_life()



    
def didnt_go_in_cave_or_no_joker():

    global format_nodes

    print(format_nodes)

    print("So u walk out of the cave with nothing new in your inventory.\n")
    print("Maybe you should have been more adventurous.\n")
    
    print("Press Enter To Continue")

    press_enter = input("").lower()

    if press_enter == "":
        pick_chimpanzee_or_lion_event()

    elif press_enter == "exit" or press_enter == "inventory":
        exit_or_see_inventory(press_enter)
        didnt_go_in_cave_or_no_joker()

    else:
        print("You might have pressed another key before enter, could you try again?")
        didnt_go_in_cave_or_no_joker()



def walkout_with_new_item():
    
    global format_nodes

    print(format_nodes)

    print("So u walk out the cave with a new item in your inventory.\n")
    print("How EXCITING!!!\n")
    
    print("Press Enter To Continue")

    press_enter = input("").lower()

    if press_enter == "":
        pick_chimpanzee_or_lion_event()

    elif press_enter == "exit" or press_enter == "inventory":
        exit_or_see_inventory(press_enter)
        walkout_with_new_item()

    else:
        print("You might have pressed another key before enter, could you try again?")
        walkout_with_new_item()



def pick_chimpanzee_or_lion_event():

    events_list = ["lion", "chimpanzee"]

    random_selection = random.choice(events_list)

    if random_selection == "chimpanzee":
        chimpanzee_event()
    
    elif random_selection == "lion":
        lion_event()


def chimpanzee_event():

    global format_nodes
    global two_lines_down
    global players_character_choice
    global pet_cheetah
    global joker_token

    print(format_nodes)

    print("After a pretty long walk, you get in front of a pretty big wooden bridge,\n")
    print("but for some reason start to hear loud noises coming behind you.\n")
    print("And oh my god, if it isnt the angry chimpanzee horde itself.\n")
    print("They are coming to tear you apart.\n")

    print(two_lines_down)
    print("What will you do to deal with this Monkey Horde?\n")

    print(two_lines_down)

    print("A) Hide Behind A Bush\n")
    print("B) Use Zap Gun  /// Zap gun throws out a very powerful that can kill anyone, and bounces between close enemies.\n")
 

    if pet_cheetah == True:
        print("C)Run Away With Pet Cheetah\n")
    
    if players_character_choice == "Animal Andy":
        print("D) Try To Talk To The Horde\n")

    if joker_token == True:
        print("E) Use Joker Token\n")
    
    if players_character_choice == "Mr. Lucky":
        print("F) Since you are Mr. Lucky, get Into The Helicopter but have a '75%' chance to be able to fly it\n")
    
    else:
        print("F) Get Into The Helicopter but have a '50%' chance to be able to fly it\n")


    user_choice = input("").lower()

    
    if user_choice == "a":
        chimpanzee_event_hide_behind_bush()
    
    elif user_choice == "b":
        chimpanzee_event_zap_gun()
    
    elif pet_cheetah == True and user_choice == "c":
        chimpanzee_event_pet_cheetah()

    elif players_character_choice == "Animal Andy" and user_choice == "d":
        chimpanzee_event_talk_to_horde()
    
    elif joker_token == True and user_choice == "e":
        chimpanzee_event_joker_token()

    elif user_choice == "f":
        chimpanzee_event_helicopter()
    
    elif user_choice == "exit" or user_choice == "inventory":
        exit_or_see_inventory(user_choice)
        walkout_with_new_item()
    
    else:
        print("Could you retry typing your answer? You accidentally pressed another button or wrote something unexpected.")
        chimpanzee_event



def chimpanzee_event_hide_behind_bush():
    
    global format_nodes
    
    character_lives_left(1)

    print(format_nodes)

    print("Oh no...\n")
    print("Chimpanzees are very smart animals, they know you are behind the bush...\n")
    print("You died in a pretty stupid way.\n")
    
    print("Press Enter To Continue\n")

    press_enter = input("").lower()

    if press_enter == "":
        chimpanzee_event_died()

    elif press_enter == "exit" or press_enter == "inventory":
        exit_or_see_inventory(press_enter)
        chimpanzee_event_hide_behind_bush()

    else:
        print("You might have pressed another key before enter, could you try again?")
        chimpanzee_event_hide_behind_bush()




def chimpanzee_event_zap_gun():
    
    global format_nodes

    print(format_nodes)

    print("The Zap Of The Zap gun bounced around between the enemies\n")
    print("and eliminated all of the chimpanzees. \n")
    print("Nice job.\n")
   
    print("Press Enter To Continue\n")

    press_enter = input("").lower()

    if press_enter == "":
        chimpanzee_event_alive()

    elif press_enter == "exit" or press_enter == "inventory":
        exit_or_see_inventory(press_enter)
        chimpanzee_event_zap_gun()

    else:
        print("You might have pressed another key before enter, could you try again?")
        chimpanzee_event_zap_gun()


def chimpanzee_event_pet_cheetah():
    
    global format_nodes

    print(format_nodes)

    print("Great Thinking\n")
    print("You succesfully escaped\n")
    print("Your Pet Cheetah was more than happy to help you.\n")
   
    print("Press Enter To Continue\n")

    press_enter = input("").lower()

    if press_enter == "":
        chimpanzee_event_alive()

    elif press_enter == "exit" or press_enter == "inventory":
        exit_or_see_inventory(press_enter)
        chimpanzee_event_pet_cheetah()

    else:
        print("You might have pressed another key before enter, could you try again?")
        chimpanzee_event_pet_cheetah()



def chimpanzee_event_talk_to_horde():

    global format_nodes
    
    character_lives_left(1)

    print(format_nodes)

    print("I dont think a horde of angry chimpanzees will listen to you...\n")
    print("You died in a horrible way.")
   
    print("Press Enter To Continue\n")

    press_enter = input("").lower()

    if press_enter == "":
        chimpanzee_event_died()

    elif press_enter == "exit" or press_enter == "inventory":
        exit_or_see_inventory(press_enter)
        chimpanzee_event_talk_to_horde()

    else:
        print("You might have pressed another key before enter, could you try again?")
        chimpanzee_event_talk_to_horde()


def chimpanzee_event_joker_token():
    
    global format_nodes
    global joker_token

    joker_token = False

    print(format_nodes)

    print("Great Use Of The Joker Token, You Succesfully Pass\n.")

    print("Press Enter To Continue\n")

    press_enter = input("").lower()

    if press_enter == "":
        chimpanzee_event_alive()

    elif press_enter == "exit" or press_enter == "inventory":
        exit_or_see_inventory(press_enter)
        chimpanzee_event_joker_token()

    else:
        print("You might have pressed another key before enter, could you try again?")
        chimpanzee_event_joker_token()



def chimpanzee_event_helicopter():

    global players_character_choice

    if players_character_choice == "Mr. Lucky":
        chimpanzee_event_helicopter_mr_lucky()
    
    else:
        chimpanzee_event_helicopter_others()


def chimpanzee_event_helicopter_mr_lucky():
    
    random_number = random.randint(1, 100)

    if random_number < 76:
        chimpanzee_event_helicopter_won()

    elif random_number > 75:
        chimpanzee_event_helicopter_lost()


def chimpanzee_event_helicopter_others():
    
    random_number = random.randint(1, 100)

    if random_number < 51:
        chimpanzee_event_helicopter_won()

    elif random_number > 50:
        chimpanzee_event_helicopter_lost()


def chimpanzee_event_helicopter_won():
    
    global format_nodes

    print(format_nodes)

    print("Oh wow, I guess believing in your luck is a good thing.\n")
    print("And you escape with the helicopter.\n")

    print("Press Enter To Continue\n")

    press_enter = input("").lower()

    if press_enter == "":
        chimpanzee_event_alive()

    elif press_enter == "exit" or press_enter == "inventory":
        exit_or_see_inventory(press_enter)
        chimpanzee_event_helicopter_won()

    else:
        print("You might have pressed another key before enter, could you try again?")
        chimpanzee_event_helicopter_won()




def chimpanzee_event_helicopter_lost():
    
    global format_nodes
    
    character_lives_left(1)

    print(format_nodes)

    print("You are a very unlucky person.\n")
    print("And you lose your life in a helicopter crash\n")

    print("Press Enter To Continue\n")

    press_enter = input("").lower()

    if press_enter == "":
        chimpanzee_event_died()

    elif press_enter == "exit" or press_enter == "inventory":
        exit_or_see_inventory(press_enter)
        chimpanzee_event_helicopter_lost()

    else:
        print("You might have pressed another key before enter, could you try again?")
        chimpanzee_event_helicopter_lost()


def chimpanzee_event_died():
    
    global format_nodes

    print(format_nodes)

    print("Better Luck Next Time\n")
    print("So you were unsecsesful with dealing with the horde of angry chimpanzees,\n")
    print("and have lost 1 life.\n")

    print("Press Enter To Continue\n")

    press_enter = input("").lower()

    if press_enter == "":
        final_mighty_midas_event()

    elif press_enter == "exit" or press_enter == "inventory":
        exit_or_see_inventory(press_enter)
        chimpanzee_event_died()

    else:
        print("You might have pressed another key before enter, could you try again?")
        chimpanzee_event_died()



def chimpanzee_event_alive():

    global format_nodes

    print(format_nodes)

    print("Nice Job\n")
    print("So you are succesfully able to cross the bridge and escape\n")
    print("from the horde of angry chimpanzees without losing a life.\n")

    print("Press Enter To Continue\n")

    press_enter = input("").lower()

    if press_enter == "":
        final_mighty_midas_event()

    elif press_enter == "exit" or press_enter == "inventory":
        exit_or_see_inventory(press_enter)
        chimpanzee_event_alive()

    else:
        print("You might have pressed another key before enter, could you try again?")
        chimpanzee_event_alive()




def lion_event():

    global format_nodes
    global two_lines_down
    global joker_token
    global pet_cheetah

    print(format_nodes)

    print("After a pretty long walk, you get in front of a pretty big wooden bridge\n")
    print("but there is a very muscular hungry lion waiting for you.\n")

    print("How will you deal with this Lion?\n")

    print(two_lines_down)


    print("A) Hide Behind A Bush\n")
    print("B) Use Taser  /// The Taser that polices use\n")
    print("C) Use Bazooka  ///  A big bazooka that makes things go boom!!! And vanish into the air\n")

    if joker_token == True:
        print("D) Use Joker Token\n")
    
    if pet_cheetah == True:
        print("E) Send Pet Cheetah To Fight Lion\n")
    
    
    
    user_choice = input("").lower()

    if user_choice == "a":
        lion_event_hide_in_bush()
    
    elif user_choice == "b":
        lion_event_use_taser()
    
    elif user_choice == "c":
        lion_event_use_bazooka()
    
    elif joker_token == True and user_choice == "d":
        lion_event_joker_token()
    
    elif pet_cheetah == True and user_choice == "e":
        lion_event_pet_cheetah()
    
    elif user_choice == "exit" or user_choice == "inventory":
        exit_or_see_inventory(user_choice)
        lion_event()

    else:
        print("Could you retry typing your answer? You accidentally pressed another button or wrote something unexpected.")
        lion_event()



    
def lion_event_hide_in_bush():
    
    global format_nodes
    
    character_lives_left(1)
    
    print(format_nodes)
    
    print("You should have known better...\n")
    print("Lions have amazing senses.\n")
    print("I dont think hiding away from a predator that\n")
    print("is known to be the greatest predator is a great idea.\n")
    print("You died just from the fear alone.\n")

    print("Press Enter To Continue\n")
    
    press_enter = input("").lower()

    if press_enter == "":
        lion_event_died()

    elif press_enter == "exit" or press_enter == "inventory":
        exit_or_see_inventory(press_enter)
        lion_event_hide_in_bush()

    else:
        print("You might have pressed another key before enter, could you try again?")
        lion_event_hide_in_bush()

    

def lion_event_use_taser():
    
    global format_nodes
    
    character_lives_left(1)
    
    print(format_nodes)
    
    print("The Taser kind of just tickled him.\n")
    print("A taser wont kill a lion...\n")
    print("You died in a pretty horrible way.")
    
    print("Press Enter To Continue\n")
    
    press_enter = input("").lower()

    if press_enter == "":
        lion_event_died()

    elif press_enter == "exit" or press_enter == "inventory":
        exit_or_see_inventory(press_enter)
        lion_event_use_taser()

    else:
        print("You might have pressed another key before enter, could you try again?")
        lion_event_use_taser()
    
    


def lion_event_use_bazooka():
    
    global format_nodes
    
    print(format_nodes)
    
    
    print("Oh wow, a bit too violent against an animal\n")
    print("but hey it gets the job done.\n")
    print("You have eliminated the lion and can now cross the bridge.\n")

    print("Press Enter To Continue\n")
    
    press_enter = input("").lower()

    if press_enter == "":
        lion_event_alive()

    elif press_enter == "exit" or press_enter == "inventory":
        exit_or_see_inventory(press_enter)
        lion_event_use_bazooka()

    else:
        print("You might have pressed another key before enter, could you try again?")
        lion_event_use_bazooka()
    



def lion_event_joker_token():
    
    global format_nodes
    global joker_token
    
    joker_token = False
    
    print(format_nodes)
    
    print("Great Use Of The Joker Token.\n")
    print("You succesfully cross the bridge.\n")

    print("Press Enter To Continue\n")
    
    press_enter = input("").lower()

    if press_enter == "":
        lion_event_alive()

    elif press_enter == "exit" or press_enter == "inventory":
        exit_or_see_inventory(press_enter)
        lion_event_use_bazooka()

    else:
        print("You might have pressed another key before enter, could you try again?")
        lion_event_use_bazooka()
        



def lion_event_pet_cheetah():

    global format_nodes
    global pet_cheetah
    
    pet_cheetah = False

    print(format_nodes)
    
    print("Even though the Lion Won the fight and your pet cheetah died.\n")
    print("It was a close fight and the lion is very tired.\n")
    print("He lets you go through the wooden bridge.\n")

    print("Press Enter To Continue\n")
    
    press_enter = input("").lower()

    if press_enter == "":
        lion_event_alive()

    elif press_enter == "exit" or press_enter == "inventory":
        exit_or_see_inventory(press_enter)
        lion_event_pet_cheetah()

    else:
        print("You might have pressed another key before enter, could you try again?")
        lion_event_pet_cheetah()



def lion_event_died():
    
    global format_nodes
    
    print(format_nodes)

    print("You were unsuccessful dealing with the Lion\n")
    print("and made it through the bridge with losing a life.\n")
    print("An important loss I would say.\n")

    print("Press Enter To Continue\n")
    
    press_enter = input("").lower()

    if press_enter == "":
        final_mighty_midas_event()

    elif press_enter == "exit" or press_enter == "inventory":
        exit_or_see_inventory(press_enter)
        lion_event_died()

    else:
        print("You might have pressed another key before enter, could you try again?")
        lion_event_died()



def lion_event_alive():
    
    global format_nodes
    
    print(format_nodes)

    print("So you were succesfull with dealing with the hungry Lion\n")
    print("and made it through the bridge without losing a life\n")

    print("Press Enter To Continue\n")

    press_enter = input("").lower()

    if press_enter == "":
        final_mighty_midas_event()

    elif press_enter == "exit" or press_enter == "inventory":
        exit_or_see_inventory(press_enter)
        lion_event_alive()

    else:
        print("You might have pressed another key before enter, could you try again?")
        lion_event_alive()







def final_mighty_midas_event():

    global format_nodes

    print(format_nodes)

    print("After going through that crazy event,\n")
    print("you are faced against the Final Boss named the Mighty Midas.\n")
    print("Midas is 30 meters tall giant that is covering the path to the finish line.\n")
    print("You need to somehow take him down.\n")
    print("And dont worry about dying if you have more than 1 life left.\n")
    print("If you die you will spawn back to this position to choose again.\n")
    print("But if you do have 1 life. Than this is your only chance so make it count.\n")
    print("What will you do get past this giant?\n")

    print("A) Ask The 'Mighty Midas' Nicely If He Can Let You Through\n")
    print("B) Try To Sneak By Midas\n")
    print("C) Use Bazooka  ///  A big bazooka that makes things go boom!!! And vanish into the air\n")


    if joker_token == True:
        print("D) Use Joker Token  /// This is a free way to victory my friend\n")
    

    if cute_puppy == True:
        print("E) Use Cute Puppy /// Who knows it might just work.\n")

    print(two_lines_down)

    user_choice = input("").lower()

    if user_choice == "a":
        final_event_ask_nicely()
    
    elif user_choice == "b":
        final_event_sneak_by()
    
    elif user_choice == "c":
        final_event_use_bazooka()
    
    elif joker_token == True and user_choice == "d":
        final_event_use_joker()
    
    elif cute_puppy == True and user_choice == "e":
        final_event_use_puppy()
    
    elif user_choice == "exit" or user_choice == "inventory":
        exit_or_see_inventory(user_choice)
        final_mighty_midas_event()

    else:
        print("Could you retry typing your answer? You accidentally pressed another button or wrote something unexpected.\n")
        final_mighty_midas_event()





def final_event_ask_nicely():

    global format_nodes
    
    print(format_nodes)
    
    
    print("Uhhhh.. I forgot to tell you but Mighty Midas isnt a very nice person...\n")
    print("and he doesnt know what empathy is.\n")
    print("Therefore he crushed you with his 5 meter long foot.\n")
    print("Dont worry though, you can still choose again if you have more lives.\n")

    character_lives_left(1) 
    
    #I call this here before the next step, so that when I deacrease 1 from his life count, and user has 0 lives left, it instantly cuts him off. 
    #But if user has more than 0 lives than they can continue, and pick again. Since in this case they picked the wrong choice and lost a life. Hopefully this makes sense.

    print("Press Enter To Continue\n")
    
    press_enter = input("").lower()

    if press_enter == "":
        final_mighty_midas_event()

    elif press_enter == "exit" or press_enter == "inventory":
        exit_or_see_inventory(press_enter)
        final_event_ask_nicely()

    else:
        print("You might have pressed another key before enter, could you try again?")
        final_event_ask_nicely()


def final_event_sneak_by():

    global format_nodes
    
    print(format_nodes)
    
    
    print("Oh wow, What an interesting turn of events.\n")
    print("You caught Midas wondering. He didnt notice you at all.\n")
    print("I guess he isnt so mighty after all.\n")
    print("Great Job being so stealthy.\n")
    print("You have earned to leave this place and get back to the real world.\n")


    print("Press Enter To Continue\n")
    
    press_enter = input("").lower()

    if press_enter == "":
        choosing_prologue()

    elif press_enter == "exit" or press_enter == "inventory":
        exit_or_see_inventory(press_enter)
        final_event_sneak_by()

    else:
        print("You might have pressed another key before enter, could you try again?")
        final_event_sneak_by()



def final_event_use_bazooka():

    global format_nodes
    
    print(format_nodes)
    
    
    print("Im so sorry to let you know, but that bazooka only tickled Mighty Midas.\n")
    print("He is Mighty after all.\n")
    print("You died in a horrific way.\n")
    print("Dont worry though, you can still choose again if you have more lives.\n")

    character_lives_left(1) 
    
    print("Press Enter To Continue\n")
    
    press_enter = input("").lower()

    if press_enter == "":
        final_mighty_midas_event()

    elif press_enter == "exit" or press_enter == "inventory":
        exit_or_see_inventory(press_enter)
        final_event_use_bazooka()

    else:
        print("You might have pressed another key before enter, could you try again?")
        final_event_use_bazooka()


def final_event_use_joker():

    global format_nodes
    global joker_token

    joker_token = False
    
    print(format_nodes)
    
    print("An awesome, awesome but an awesome way to use your Joker Token.\n")
    print("This was such a great way to use it.\n")
    print("Great job saving your token all the way this far.\n")
    print("You have earned to get out of this place. Nice job.\n")


    print("Press Enter To Continue\n")
    
    press_enter = input("").lower()

    if press_enter == "":
        choosing_prologue()

    elif press_enter == "exit" or press_enter == "inventory":
        exit_or_see_inventory(press_enter)
        final_event_use_joker()

    else:
        print("You might have pressed another key before enter, could you try again?")
        final_event_use_joker()


def final_event_use_puppy():

    global format_nodes
    global cute_puppy

    cute_puppy = False

    print(format_nodes)
    
    
    print("The puppy that you picked was Sooooooooo cuuute and addooooorable.\n")
    print("It rolled on the ground and opened its eyes big and wide. \n")
    print("It made even the Mighty Midas feel wholesome\n")
    print("You have earned to get out of this place. Nice job.\n")
    print("and he let you both go through.")
    print("This was an interesting choice that you picked.")
    print("This was an interesting choice that you picked. But it turned out to be a good one.")
    print("Nice job, You earned to leave this place.")

    print("Press Enter To Continue\n")
    
    press_enter = input("").lower()

    if press_enter == "":
        prologue_1()

    elif press_enter == "exit" or press_enter == "inventory":
        exit_or_see_inventory(press_enter)
        final_event_use_puppy()

    else:
        print("You might have pressed another key before enter, could you try again?")
        final_event_use_puppy()


def choosing_prologue():

    global millions_in_game 

    if millions_in_game == True:
        prologue_2()
    elif millions_in_game == False:
        prologue_1()


def prologue_1():

    global format_nodes
    global two_lines_down

    print(format_nodes)

    print("Nice job user, you succesfully made it through Jumanji.\n")
    print("I hope you had fun along the way but a more important thing is waiting for you now.\n")
    print("THE REAL LIFE, now go out there and get a fresh air of that real life.\n")
    print("You have earned it.")
    print("Until I see you next time, good bye friend :)\n")
    print("*Body gets sucked back into real life*\n")

    print("THE END")




def prologue_2():

    global format_nodes
    global two_lines_down

    print(format_nodes)

    print("Nice job user, you succesfully made it through Jumanji.\n")
    print("But that wasn't the only great thing you did.\n")
    print("You might not have noticed this but you never got to use your millions of in game currency option\n")
    print("Well I have great news for you!")
    print("All of those 24 karat (highest karat) gold is getting sent to real life with you\n")
    print("Since you finished the game without using it, its a nice little bonus for you, great job\n")
    print("Now go out there and enjoy real life, and spend all of that money you will get from selling the gold\n")
    print("I hope you enjoyed Jumanji and till I see you next time again, goodbye friend :)")
    
    print(two_lines_down)

    print("THE END")


#------------------------------- Global Variables and Main

global format_nodes 
global two_lines_down 
global players_character_choice
global lives_left
global gun_generator_per_situation
global joker_token
global pet_cheetah
global cute_puppy
global millions_in_game


#-------------------------------------  Values 

format_nodes = "-" * 150 + "\n" * 2
two_lines_down = "\n" * 2
players_character_choice = ""
lives_left = 3

gun_generator_per_situation = True
joker_token = False
pet_cheetah = False
cute_puppy = False
millions_in_game = False

def main ():
    instructions_for_game()

main()


