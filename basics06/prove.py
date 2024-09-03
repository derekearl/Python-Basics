# This is an assignment that will demostrate an adventure game
# That is made of choices given to the user

input ('Welcome to the Cave of Doom, press ENTER to continue ')

print()

print ('You have entered the Cave of Doom, it is a dark gloomy\n'
       'cave where there is little light and the darkness gets more and more\n'
       'hard to see the deeper you go in. You remember that a flashlight is in your\n'
       'backpack and quickly get it out to go deeper in the cave. Suddenly you hear a loud\n'
       'crash behind you.  You look back to realize that the door behind you has shut.\n'
       'You have no choice but to continue deeper in the cave. Your stomach starts to growl\n'
       'and you are really hungry, but you see a weird colored mushroom. You can choose to EAT the\n'
       'mushroom, you STORE the mushroom, or you can LEAVE it alone.')
print ()

choice1 = input ('Will you EAT, STORE, or LEAVE the Mushroom? ')
print ()
if choice1.upper() == 'EAT':
    print ()
    print ('You suddenly start to get really sick and your vision and balance\n'
           'starts to affect you poorly, but you continue to the next room. You\n'
           'see a dog that has been caught in a trap quietly wimpering in pain\n'
           'The dog looks at you scared with huge teary eyes for help.\n'
           'You are given three choices; will you HELP the dog get out of the trap,\n'
           'will you LEAVE the dog alone in the trap, or will you KILL the dog?')
    print ()

    choice2 = input ('Will you HELP, LEAVE, or KILL the dog? ')
    print ()
    if choice2.upper() == 'HELP':
        print ('The dog exits the trap and licks your face with excitement and joins you\n'
               'as the two of you enter the final room. You come across an evil Necromancer\n'
               'who has caused the darkness and injured the trapped dog. You and the dog work together\n'
               'to defeat the Necromancer and even in your weak state you and your brave companion\n'
               'turns to you as you fall exhausted and retrieves a plant in the Necromancers pack and brings\n'
               'it to you.  Your sickness leaves and a hole opens in the cave.  You and your furry companion\n'
               'leave the cave and live happily ever after')
        print ()
        
    elif choice2.upper() == 'LEAVE':
        print ('The dog continues to wimper in pain and vanishes in the darkness as you continue\n'
               'to the final room. You come across an evil Necromancer who sees you in an weak state\n'
               'The Necromancer turns you into a berry and feeds you to the dog you decided to leave behind')
        
    elif choice2.upper() == 'KILL':
        print ('The dog lays dead taking its last breath and you become more lost in darkness both\n'
               'in the cave and in your soul as well. And you continue in the final room. You come\n'
               'across an evil Necromancer that is not nearly as evil as you have become. But in his\n'
               'power that he has and with a point to prove he turns you into roll of never ending toilet\n'
               'paper and you will live out the rest of eternity living as the cleaning of rear ends of trolls')
        
elif choice1.upper() == 'STORE':
    print ('You pick the mushroom and open your backpack to store it for now.\n'
           'You continue into the next room and as you walk deeper in the room you\n'
           'see a dog that has been caught in a trap quietly wimpering in pain\n'
           'The dog looks at you scared with huge teary eyes for help.\n'
           'You are given three choices; will you HELP the dog get out of the trap,\n'
           'will you LEAVE the dog alone in the trap, or will you KILL the dog?')
    print ()

    choice2 = input ('Will you HELP, LEAVE, or KILL the dog? ')
    print ()

    if choice2.upper() == 'HELP':
        print ('The dog exits the trap and licks your face with excitement and joins you\n'
               'as the two of you enter the final room. You come across an evil Necromancer\n'
               'who has caused the darkness and injured the trapped dog. You and the dog work together\n'
               'to defeat the Necromancer. You and the dog stand in triumph over your victory. The dog\n'
               'turns to the mushroom that you have in your bag and expresses that he wants it. Turns\n'
               'out it is a very delicious treat for dogs that is poison for humans, you give the dog the mushroom.\n'
               'a hole opens in the cave. You and your furry companion leave the cave and live happily ever after')
        
    elif choice2.upper() == 'LEAVE':
        print ('The dog continues to wimper in pain and vanishes in the darkness as you continue\n'
               'to the final room. You come across an evil Necromancer who sees you in an weak state\n'
               'The Necromancer turns you into a berry and feeds you to the dog you decided to leave behind')
        
    elif choice2.upper() == 'KILL':
        print ('The dog lays dead taking its last breath and you become more lost in darkness both\n'
               'in the cave and in your soul as well. And you continue in the final room. You come\n'
               'across an evil Necromancer that is not nearly as evil as you have become. But in his\n'
               'power that he has and with a point to prove he turns you into roll of never ending toilet\n'
               'paper and you will live out the rest of eternity living as the cleaning of rear ends of trolls')

elif choice1.upper() == 'LEAVE':
    print ('You ignore the mushroom and continue into the next room as you walk deeper in the room you\n'
           'see a dog that has been caught in a trap quietly wimpering in pain\n'
           'The dog looks at you scared with huge teary eyes for help.\n'
           'You are given three choices; will you HELP the dog get out of the trap,\n'
           'will you LEAVE the dog alone in the trap, or will you KILL the dog?')
    print ()

    choice2 = input ('Will you HELP, LEAVE, or KILL the dog? ')

    print ()

    if choice2.upper() == 'HELP':
         print ('The dog exits the trap and licks your face with excitement and joins you\n'
               'as the two of you enter the final room. You come across an evil Necromancer\n'
               'who has caused the darkness and injured the trapped dog. You and the dog work together\n'
               'to defeat the Necromancer. You and the dog stand in triumph over your victory.a hole opens\n'
                'in the cave. You and your furry companion leave the cave and live happily ever after')
    
    elif choice2.upper() == 'LEAVE':
         print ('The dog continues to wimper in pain and vanishes in the darkness as you continue\n'
               'to the final room. You come across an evil Necromancer who sees you in an weak state\n'
               'The Necromancer turns you into a berry and feeds you to the dog you decided to leave behind')
         
    elif choice2.upper() == 'KILL':
        print ('The dog lays dead taking its last breath and you become more lost in darkness both\n'
               'in the cave and in your soul as well. And you continue in the final room. You come\n'
               'across an evil Necromancer that is not nearly as evil as you have become. But in his\n'
               'power that he has and with a point to prove he turns you into roll of never ending toilet\n'
               'paper and you will live out the rest of eternity living as the cleaning of rear ends of trolls')
        

print()

print ('You can guess by now that if you saved the dog, you will exit the cave and if you did not\n'
       'then met with a terrible fate')

print ()

final_choice = input ('Did you save the dog from the trap? YES or NO: ')

print ()
if final_choice.upper() == "YES":
    outcome = True
else:
    outcome = False

if outcome:
    print ('You see Dogs are amazing and you should always help them.')

else:
    print ('I am disappointed in you.')