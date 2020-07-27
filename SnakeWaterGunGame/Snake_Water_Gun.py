import random


def getRandomChoice(Opt_List):
    comp_Choice = random.choice(Opt_List)
    return comp_Choice


def getUserChoice():
    user_Choice =  input("Enter your Choice: \n 1.S \n 2.W \n 3.G\n")
    return  user_Choice

def game(comp_Choice,user_Choice,gamecounter = 0):
    user_point= 0
    comp_point= 0
    if comp_Choice != user_Choice :
        if comp_Choice == 'S' and user_Choice == 'G':
            print('You WIN Game no : '+str(gamecounter))
            user_point += 1
        elif comp_Choice == 'S' and user_Choice == 'W':
            comp_point += 1
            print('Computer WIN Game no : '+str(gamecounter))
        elif comp_Choice == 'W' and user_Choice == 'S':
            print('You WIN Game no : '+str(gamecounter))
            user_point += 1
        elif comp_Choice == 'W' and user_Choice == 'G':
            print('Computer WIN Game no : '+str(gamecounter))
            comp_point += 1
        elif comp_Choice == 'G' and user_Choice == 'S':
            print('Computer WIN Game no : '+str(gamecounter))
            comp_point += 1
        elif comp_Choice == 'G' and user_Choice == 'W':
            print('You WIN Game no : '+str(gamecounter))
            user_point += 1
    else:
        print('No Points')
    return user_point,comp_point





final_userpoint=0
final_comppoint=0
counter = 1
while counter < 11:
    print(f"===================Game No. - {counter}============================")
    comp_Choice=getRandomChoice(['S','W','G'])
    user_Choice=getUserChoice()
    user_point,comp_point = game(comp_Choice,user_Choice,counter)
    final_userpoint =final_userpoint + user_point
    final_comppoint =final_comppoint + comp_point
    counter += 1

if final_userpoint> final_comppoint:
    print(f'Winner is YOU with point :{final_userpoint} against Computer with Points :{final_comppoint}')
elif final_userpoint< final_comppoint:
    print(f'Winner is COMPUTER with point :{final_comppoint} against You with Points :{final_userpoint}')
else:
    print(f"Its a TIE with points {final_comppoint}")

