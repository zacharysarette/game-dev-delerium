# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("Ellie")
define j = Character("Jake")
define cto = Character("The CTO")
define lead = Character("The Tech Lead")
define ceo = Character("The CEO")

# The game starts here.

label start:
    $ pooped_pants = False
    $ made_team_leader_laugh = False
    $ computer = "old MacBookPro"
    $ has_eaten_pizza = False
    $ is_full_of_pizza = False
    $ first_thing_done = False
    $ got_fired = False
    $ pizza_party = False
    $ boss_impressed = False
    $ boss_dissapointed = False
    $ boss_furious = False
    $ live_another_day = False
    $ CTO_disappointed = False
    $ arrested = False


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    scene office morning

    play sound "sounds/greatestgame.ogg"

    "Congratulations! You are now a game developer!"

    "It's your first day on the job!"

    "You arrive at the office. After a few introductions you set up your computer and passwords."

label before_meeting_message:
    scene office general room
    if first_thing_done == False:
        $ message = "What shall we do first?"
        $ first_thing_done = True
    else:
        $ message = "Okay, now what do we do?"
    menu before_meeting_menu:
        "[message]"

        "Let's eat pizza":

            $ is_full_of_pizza = True
            $ has_eaten_pizza = True
            play sound "sounds/pizza.ogg"

            "You eat pizza and it makes you sick. Maybe we should use the restroom..."
            jump before_meeting_message

        "Use the employees' restroom.":

            if is_full_of_pizza == True:
                "Yes, that was a good idea. Let's stick to healthy food, okay?"
                $ is_full_of_pizza = False
                jump before_meeting_message
            else:
                "Oh, nice! The seat is heated! But you don't really need to go now."
                jump before_meeting_message

        "Go to the meeting":
            scene office meeting room
            show ceo
            show cto at left
            show lead at right
            if is_full_of_pizza == True:
                menu:
                    "You didn't go to the bathroom? Are you sure?"
                    "Yes":
                        "You feel the sensation of a thousand thunderous gorrilas evacuating your bowels."
                        "The stench dampens the air as your co-workers slowly turn their heads toward the source of that fowl odor."
                        "You excuse yourself and head out of the office to buy a fresh pair of trousers."
                        play sound "sounds/ohno.ogg"
                        "So much for first impressions, eh?"
                        $ pooped_pants = True
                        jump after_meeting
                    "No, I should go.":
                        "You walk into the meeting room and walk out awkwardly..."
                        jump before_meeting_message
            else:
                play sound "sounds/mumble.ogg"
                "The meeting goes well. Your boss talks about block chain technologies and future projects."
                jump after_meeting

label after_meeting:
    hide ceo
    hide cto at left
    hide lead at right
    $ git_setup = False
    $ godot_setup = False
    "Time to go back to the desk."
    scene office desk
    show mac old at left
    if pooped_pants == True:
        jump new_computer


label do_you_understand_the_instructions:
    show lead normal at right with moveinright
    "Your lead dev tells you to fork the project, clone it and set up Godot."
    menu:
        "Do you understand?"

        "Yes. Of course!":
            menu setting_up_the_project:
                "Great!"
                "What shall we do now?"
                "Setup Git, fork and clone the project.":
                    if git_setup == True:
                        "You already set up Git. Do you need to download extra memory?"
                        jump setting_up_the_project
                    "It takes .035 seconds. Ah the efficiency of the terminal!"
                    $ git_setup = True
                    if godot_setup:
                        jump start_project
                    else:
                        jump setting_up_the_project
                "Setup Godot":
                    if godot_setup == True:
                        "You already set up Godot. Did you accidently 79mb rar files?"
                        jump setting_up_the_project
                    "It takes two seconds. Only 20mb! Wow!"
                    $ godot_setup = True
                    if git_setup:
                        jump start_project
                    else:
                        jump setting_up_the_project


        "No eye deer.":
            menu:
                "Do you think this is a joke?"
                "...yes?":
                    "You can't have fun here! This is a game company!"
                    menu:
                        "Sorry, I didn't know.":
                            "That was a joke. Please work on your humour for tomorrow."
                        "You are hilarious.":
                            "Glad to see you have a sense of humour."
                "...no...":
                    "Hahaha, okay. You're funny."
                    $ made_team_leader_laugh = True
                    jump do_you_understand_the_instructions
        "No.":
            "Git is a source control tool."
            "It's basically magic that lets us work together on the same project and fix things easily."
            "Godot is an open source game engine."
            "Download it and read over the docs to get started."
            jump start_project

label start_project:
    "Let's get started on the project."
    hide lead
    "What shall we do now?"
    menu:
        "Fix some bugs.":
            "Okay, time to fix some bugs."
            jump fixing_bugs
        "Implement a new feature.":
            "Let's see if we can build a new feature."
            jump implementing_a_new_feature
        "Nothing.":
            "Let's do nothing..."
            jump doing_nothing

label new_computer:
    scene office desk
    show mac old at left
    show cto normal at right
    "The CTO asks you which computer you want."

    menu:
        "Mac":
            "You get a brand new iMac!"
            $ computer = "new iMac"
            show mac new 
        "PC":
            "You get a mid-range gaming PC!"
            $ computer = "new PC"
            hide mac
            show pc at left
        "No thanks! My old Mac Book is good enough!":
            "He shakes his head and walks away."
            $ CTO_disappointed = True
            show mac old fire 
    hide cto
    jump do_you_understand_the_instructions

label fixing_bugs:
    "Let's take a look at the bug list."
    "Oh, there are many bugs. Each have their own priorities."
    "Let's take a better look."
    menu bug_list:
        "Blocker: The game freezes at the inventory screen.":
            "The game freezes when you select the sword in your inventory."
            menu:
                "Fix this.":
                    jump fix_blocker
                "Look at the other bugs":
                    jump bug_list
        "Critical:":
            "The power up menu doesn't work."
            menu:
                "Fix this.":
                    jump fix_critical
                "Look at the other bugs":
                    jump bug_list
        "High:":
            "WHen I pick up a power up, the player freezes for a second."
            menu:
                "Fix this.":
                    jump fix_high
                "Look at the other bugs.":
                    jump bug_list
        "Cosmetic:":
            "The scrollbar doesn't auto hide in the power up menu."
            menu:
                "Fix this.":
                    jump fix_cosmetic
                "Look at the other bugs.":
                    jump bug_list
        "Do nothing":
            "Looks a bit hard..."
            jump doing_nothing

label fix_blocker:
    $ fixed_blocker = renpy.random.choice([True,False])
    if fixed_blocker == True:
        "You work hard and manage to get the program up and running!"
        "Nice work!"
        $ boss_impressed == True
        jump going_home
    else:
        "You work tirelessly on the blocker to get the machine up and running."
        "But alas the code is too much for you."
        jump going_home



label fix_critical:
    $ fixed_critical = renpy.random.choice([True, False])
    if fixed_critical == True:
        "You hack away at your keyboard for a few hours."
        "And at the end you fix the bug."
        $ boss_impressed == True
        jump going_home
    else:
        "You stumble around your keyboard for a few hours..."
        "and fail to fix the critical error today..."
        jump going_home

label fix_high:
    $ fixed_high = renpy.random.choice([True, False])
    if fixed_high == True:
        "Your fingers run through the keys like a treadmill."
        "And vioala! Fixed!"
        jump going_home
    else:
        "You try a bunch of solutions."
        "And the game keeps on breaking each time."
        jump going_home

label fix_cosmetic:
    $ fixed_cosmetic = renpy.random.choice([True, False])
    if fixed_cosmetic == True:
        "So you click the auto hide check box."
        "Done!"
        jump going_home
    else:
        "You try a bunch of solutions."
        "And the scrollbar keeps on breaking."
        jump going_home

label implementing_a_new_feature:
    "Let's look at the feature list."
    menu:
        "Build a god mode for the player to activate with a cheat code.":
            "You work for a few hours implementing the new feature."
            "The code is JUMP JUMP JUMP LEFT RIGHT LEFT ROLL."
            "Good job!"
            $ boss_impressed = True
            jump going_home
        "Build a pizza ordering system right into the game.":
            "You get on the phone with the local pizza chain to collaborate."
            if  has_eaten_pizza == True:    
                "They give you the okay and you start to work on the code."
                "After a few hours, the pizza ordering system works in game!"
                play sound "sounds/pizza.ogg"
                "Excellent!"
                $ boss_impressed = True
                jump going_home
            else:
                "They ask you if you have ever tried their pizza before."
                menu:
                    "Tell them the truth.":
                        "You tell them that sadly you have not."
                        "And then they agree to send 20 boxes of pizza straight to the office."
                        "Excellent!"
                        play sound "sounds/pizza.ogg"
                        "Pizza Party!"
                        $ pizza_party = True
                    "Lie.":
                        "Oh! What is your favorite topping?"
                        menu liar_liar:
                            "Banana flowers.":
                                "This is not such a fancy chain."
                                "They call you a dirty liar."
                                "You have lost the trust of the local pizza chain."
                            "Apples and corn.":
                                "Nothing is more american than a pizza with apples and corn!"
                                "You work on the ordering system for a few hours."
                                "Done! Nice work!"
                                $ boss_impressed = True
                                jump going_home

                            "Pepperoni and cheese":
                                "They don't have Pepperoni and cheese."
                                "They call you a dirty liar."
                                "You have lost the trust of the local pizza chain."
                        $ boss_dissapointed = True
                        jump going_home

                    


    jump going_home


label doing_nothing:
    "Okay... what kind of nothing shall we do?"
    menu:
        "Take a nice long walk for a few hours":
            scene office noon
            "The air is cool and crisp."
            "You find a park after walking for 10 minutes."
            scene park
            "You sit down and feed the pidgeons some of your lunch."
            show police with dissolve
            play sound "sounds/hey.ogg"
            "A policeman notices you feeding the pidgeons."
            "He walks up to you and points to a sign."
            menu:
                "What do you do?"
                "Talk to the police officer":
                    "You apologize and head back to work."
                "Run away.":
                    "The officer chases after you."
                    play sound "sounds/no.ogg"
                    "You try to run, but it's no use."
                    "The officer calls in for back up."
                    "They have you cornered."
                    "They arrest you."
                    "Just in time for the 6 o'clock news."
                    jump arrested
        "Pretend to be working":
            show ceo normal
            "Your boss comes to your desk."
            "He asks you what you're doing."
            menu:
                "You tell him you are filing a few TPS reports.":
                    "He tells you that those aren't due till next month and walks away."
                    hide ceo
                    jump going_home
                "Nothing! Absolutely Nothing!":
                    $ boss_furious = True
                    jump fired


label going_home:
    scene office general room night with dissolve
    "At last, it's time to go home."
    "Your coworkers are still working on a few things before they leave."
    menu say_goodbye:
        "Goodnight everyone!":
            "Good night!"
            $ live_another_day = True
            jump achievements
        "See ya suckers!":
            jump fired

label arrested:
    scene jail with dissolve
    $ arrested = True
    "After spending the night in jail you go to work."
    "The boss asks you where you went yesterday."
    scene office general room with dissolve
    show ceo at right with moveinright
    "What do you do?"
    menu:
        "You tell him the truth.":
            jump fired
        "You tell him you had a family emergency.":
            "He believes you, and tells you to let him know next time."
            "You work hard for 6 hours."
            jump going_home


label fired:
    scene office meeting room fired
    show ceo
    "The boss calls you into an empty meeting room."
    play sound "sounds/ohno.ogg"
    "You are fired. GOOD DAY SIR!"

    "I SAID GOOD DAY!"
    $ got_fired = True

    jump achievements

label achievements:
    scene achievements
    label achievement_block:
        "Congratulations!"
        "Let's see what you managed to do on your first day as a game developer!"
        if got_fired == True:
            "First day Flunkie:"
            play sound "sounds/ohno.ogg"
            "You were fired!"
            "Nice!"
        if pooped_pants == True:
            "Fresh Pair:"
            play sound "sounds/pizza.ogg"
            "You managed to soil yourself!"
            "Remember to pick up some bleach at the store on your way home."
        if arrested == True:
            "Arrested Developer:"
            "If you can't do the time."
            "Don't do the crime."
            "But seriously did you see that guy?"
            "That cop was scary looking!"
        if CTO_disappointed == True:
            "Save the Fire Wire!"
            "You managed to keep your mac book long enough to see it explode."
            "And the CTO is dissapoint"
        if made_team_leader_laugh == True:
            "Funny guy!"
            "You made your team leader laugh."
        if boss_impressed == True:
            "Impressive. Most Impressive."
            "You managed to impress the boss."
            "Good work!"
        if boss_dissapointed == True:
            "Dissapoint"
            "Boss is very dissapoint..."
            "Try again?"
        if boss_furious == True:
            "Flippin Furious."
            "You've managed to hit it out of the park with this one."
            "The boss is incredibly furious with you."
            "Look, he's turning into a green muscled monster right now."
        if live_another_day == True:
            "You get to come back tomorrow!"
            "Perhaps you'll even get paid soon."
            "What are you going to buy?"
            menu:
                "a boat":
                    "You should buy a boat."
                "a goat":
                    "You should buy a boat"
                "a moat":
                    "You should buy a boat"
        if pizza_party == True:
            play sound "sounds/pizza.ogg"
            "Pizza Party!"
            "Pizza Party!"
        

label rolling_credits:
    "This game was made in a week."
    "All characters and portrayals of a real working environment are fictional."
    "(Including YOU!)"
    "It was made by Zachary Sarette in 2018."
    "If you liked my game give me a comment and rate it!"
    "Thank you for playing."


# This ends the game.

return
