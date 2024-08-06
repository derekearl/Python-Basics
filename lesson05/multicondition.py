# This is an extra demo to show multiple conditions

state = input ('What state are you from? ')

if state.capitalize() == 'Louisiana':
    town = input ("What part of Louisiana are you from? ")
    if town.capitalize() in ('Mangham', 'Baskin', 'Rayville', 'Winnsboro'):
        print ('Hey that is a good place to grow up!')
    
    elif town.capitalize() in ('Oak Grove', 'Columbia'):
        print ('Eww')

    elif town.capitalize() in ('Shreveport', 'Bossier City'):
        print ('Well you guys do have a little Vegas vibe going on.')

    elif town.capitalize() in ('New Orleans', 'Morgan City'):
        print ('You guys party hard when it comes to Mardi Gras!')

    elif town.capitalize() in ('Lafayette', 'Natchitoches'):
        print ('The food is so good!')

    else:
        print ('Cool')
else:
    print ('You should move to Louisiana!')