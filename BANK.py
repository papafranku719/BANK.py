# BANK: A Text-Based Robbery

import sys
import time
import random

print("Chicago, 2006. You're a small-time crook looking to make a big score.")
time.sleep(1)
print("Since moving to the Windy City, a certain bank has attracted your eye: Northern Trust.")
time.sleep(1)
print("Since Chief Executive Harris' promotion in '03, Northern Trust's profits haven't been higher.")
time.sleep(1)
print("After casing the headquarters on 50 LaSalle Street, it's time to gather a crew.")
time.sleep(1)
print("")

member1 = input("Enter the name of a crew member: ")
member2 = input("Enter the name of a crew member: ")
member3 = input("Enter the name of a crew member: ")

print("")
print(f'What will {member1} do?')
role1 = input(''' 
A. Crowd control
B. Drill operation

'''
              )
if role1 == "A":
    role1 = "crowd control"
    print(member1, "is on", role1)
    print("")
elif role1 == "B":
    role1 = "drill operation"
    print(member1, "is on", role1)
    print("")
else:
    print("If you can't assign someone a role, how can you rob a bank?")
    sys.exit()

print(f'What will {member2} do?')
role2 = input(''' 
A. Crowd control
B. Drill operation

'''
              )
if role2 == "A":
    role2 = "crowd control"
    print(member2, "is on", role2)
    print("")
elif role2 == "B":
    role2 = "drill operation"
    print(member2, "is on", role2)
    print("")
else:
    print("If you can't assign someone a role, how can you rob a bank?")
    sys.exit()

if role1 == "crowd control" and role2 == "crowd control":
    role3 = "drill operation"
    print(member3, "is on", role3)
elif role1 == "drill operation" and role2 == "drill operation":
    role3 = "crowd control"
    print(member3, "is on", role3)
elif role1 != role2:
    print(f'What will {member3} do?')
    role3 = input('''
A. Crowd control
B. Drill operation

'''
                  )
    if role3 == "A":
        role3 = "crowd control"
        print(member3, "is on", role3)
    elif role3 == "B":
        role3 = "drill operation"
        print(member3, "is on", role3)
    else:
        print("If you can't assign someone a role, how can you rob a bank?")
        sys.exit()

if role1 == role2:
    you = role3
    print("You will go with", member3, "and do", role3)
elif role1 == role3:
    you = role2
    print("You will go with", member2, "and do", role2)
elif role2 == role3:
    you = role1
    print("You will go with", member1, "and do", role1)

print("")
print("With the crew assembled, you gather into a Ford Transit and head to the bank.")
time.sleep(1)
print("Masks on, guns out, you storm into the lobby.")
time.sleep(1)
print("")
if you == "drill operation":
    print("While crowd control is established, you head to the vault to set up the drill.")
    if role1 == "drill operation":
        partner = member1
    elif role2 == "drill operation":
        partner = member2
    elif role3 == "drill operation":
        partner = member3
    time.sleep(1)
    print("")
    roll_one = random.randint(1,10)
    if roll_one <= 1:
        print("While trying to assemble the drill, you find a drillbit missing.")
        print("Because of this, you can't drill open the vault and you fail the heist.")
        sys.exit()
    elif roll_one >= 2:
        print("You successfully assemble the drill.")
        print("At the current rate, it should be about 4 minutes before the vault door opens.")
    time.sleep(1)
    print("")
    roll_two = random.randint(1,10)
    if roll_two <= 4:
        print("About a minute into the drilling, a guard that happened to be on break sees your drill.")
        time.sleep(1)
        print("The guard shouts at you: 'Hey, what the hell are you doing?!'")
        persuasion = input('''
A. We're repairmen, here to fix the vault door?
B. We're guards too, some dick got into the vault?
C. We're lost, and thought this was the bathroom?
D. We're bank robbers, and you won't stop us?
'''
                  )
        roll_two2 = random.randint(1,10)
        if roll_two2 <= 8:
            print("The guard clearly isn't convinced, and starts to pull out his gun.")
            time.sleep(1)
            roll_two3 = random.randint(1,10)
            if roll_two3 <= 2:
                print("The guard shoots you in the chest. Incapacitated, you fail the heist.")
                sys.exit()
            elif roll_two3 >=3:
                print(partner, "pulls out their gun and shoots the guard before he can fire, saving you.")
                print("")
        elif roll_two2 >= 9:
            print("The guard seemingly buys whatever you said, and walks away content.")
    elif roll_two >= 5:
        print("Nothing out of the ordinary yet.")
    print("Three minutes left on the drill.")
    time.sleep(1)
    print("")
    roll_three = random.randint(1,10)
    if roll_three <= 6:
        print("While you're drilling, a guard that just clocked in sees your drill.")
        time.sleep(1)
        print("The guard shouts at you: 'Hey, what the hell are you doing?!'")
        persuasion3 = input('''
A. We're janitors, here to clean the vault?
B. We're guards too, we left our lunches in there?
C. We're cops, looking into a potential robbery?
D. We're bank robbers, and you won't stop us?
'''
                  )
        roll_three2 = random.randint(1,10)
        if roll_three2 <= 8:
            print("The guard clearly isn't convinced, and starts to pull out his gun.")
            time.sleep(1)
            roll_three3 = random.randint(1,10)
            if roll_three3 <= 2:
                print("The guard shoots you in the chest. Incapacitated, you fail the heist.")
                sys.exit()
            elif roll_three3 >=3:
                print(partner, "pulls out their gun and shoots the guard before he can fire, saving you.")
                print("")
        elif roll_three2 >= 9:
            print("The guard seemingly buys whatever you said, and walks away content.")
    elif roll_three >= 7:
        print("Situation normal.")    
    print("About two minutes left on the drill.")
    time.sleep(1)
    print("")
    roll_four = random.randint(1,10)
    if roll_four <= 1:
        print("You feel a twinge in your stomach, and come to realize you need to shit.")
        time.sleep(1)
        print("You leave the drill to go look for a bathroom.")
        print("")
        roll_fourI = random.randint(1,10)
        if roll_fourI <= 1:
            print("You're not fast enough; you shit your pants.")
            time.sleep(3)
            print("You waddle back to the drill, reeking of shit the rest of the heist.")
            print("")
        elif roll_fourI >= 2:
            print("You finesse into a bathroom and void your bowels.")
            time.sleep(1)
            print("You make it back to the vault feeling refreshed.")
            print("")
    if roll_four >= 2 and roll_four <=5:
        print("While you're drilling, a guard that was walking by sees your drill.")
        time.sleep(1)
        print("The guard shouts at you: 'Hey, what the hell are you doing?!'")
        persuasion3 = input('''
A. We're annoyed, and tired of guards?
B. We're guards too, we wanted to make a deposit?
C. We're blind, we thought this was a church?
D. We're bank robbers, and you won't stop us?
'''
                  )
        roll_four2 = random.randint(1,10)
        if roll_four2 <= 8:
            print("The guard clearly isn't convinced, and starts to pull out his gun.")
            time.sleep(1)
            roll_four3 = random.randint(1,10)
            if roll_four3 <= 2:
                print("The guard shoots you in the chest. Incapacitated, you fail the heist.")
                sys.exit()
            elif roll_four3 >=3:
                print(partner, "is able to pull out a gun and shoots the guard before he can fire.")
        elif roll_four2 >= 9:
            print("The guard seemingly buys whatever you said, and walks away content.")
    if roll_four >= 6:
        print("You twiddle your thumbs in anticipation.")
    print("One minute left on the drill.")
    time.sleep(1)
    print("")
    roll_five = random.randint(1,10)
    if roll_five <= 7:
        print("You get a call from your mom.")
        time.sleep(1)
        roll_fiveI = random.randint(1,10)
        if roll_fiveI <= 7:
            print("Instead of hanging up on her, you accidentally answer the phone.")
            print("")
            time.sleep(1)
            print("Your mom shrieks into the phone: 'HEY HONEY, WHY HAVEN'T YOU CALLED ME?'")
            persuasion4 = input('''
A. Answer earnestly
B. Answer rudely
C. Answer in a foreign language
'''
                                )
            roll_fiveII = random.randint(1,10)
            if roll_fiveII <= 5:
                print("She gets annoyed with your answer and continues to shriek at you.")
                desperation = input('''
A. Try to say the connection is bad and hang up
B. Hang up the phone outright
C. Hand the phone to your partner
'''
                                    )
                roll_fiveIII = random.randint(1,10)
                if roll_fiveIII <= 1:
                    print("You somehow get stuck in the phonecall. It takes 40 minutes.")
                    time.sleep(1)
                    print("The police arrive and arrest you, giving you a twisted sense of relief.")
                    print("You fail the heist.")
                    sys.exit()
                elif roll_fiveIII >= 2:
                    print("This seems to sort the problem out, and you can resume drilling.")
            elif roll_fiveII >= 6:
                print("Your mom understands, and asks you to call later. She hangs up.")
        elif roll_fiveI >= 8:
                print("You successfully hang up the call and dodge a bullet.")
    elif roll_five >= 8:
        print("Almost there.")
    print("The drill is finished.")
    print("")
    time.sleep(1)
    print(f'The vault door swings open; you and {partner} rush in, and start bagging the money.')
    time.sleep(1)
    print("You meet up with the other crew members in the lobby and make your way out of the bank.")
    print("")
    roll_finalI = random.randint(1,3)
    if roll_finalI == 1:
        traitor = member1
        partner1 = member2
        partner2 = member3
    elif roll_finalI == 2:
        traitor = member2
        partner1 = member3
        partner2 = member1
    elif roll_finalI == 3:
        traitor = member3
        partner1 = member1
        partner2 = member2
    print(f'As you all exit the front doors, {traitor} shoots {partner1} in the leg and knocks down {partner2}.')
    time.sleep(1)
    print(f'{traitor} is betraying you!')
    react = input('''
What do you do?

A. Try to disarm them
B. Try to talk to them
C. Try to shoot them
D. Try to run away
'''
                      )
    if react == "A":
        roll_dis = random.randint(1,10)
        if roll_dis <= 2:
            print("You attempt to disarm", traitor, "but they shoot you in the abdomen.")
            time.sleep(1)
            print("You are incapacitated, and you fail the heist.")
            sys.exit()
        elif roll_dis >= 3:
            print("You are able to wrestle the gun out of " + traitor + "'s hands, taking them down in the process")
            print("")
            print("Despite there being a traitor, you gather your crew in the van, money in tow.")
            time.sleep(1)
            print("You have successfully robbed the Northern Trust Bank.")
            print("YOU WIN!")
    elif react == "B":
        roll_talk = random.randint (1,10)
        if roll_talk <= 2:
            print("You try to convince", traitor, "to stand down, but you're shot and killed for your efforts.")
            time.sleep(1)
            print("You fail the heist.")
            sys.exit()
        elif roll_talk >= 3 and roll_talk <= 6:
            print("What you say to", traitor, "confuses them enough for you to execute a desperate leg sweep.")
            time.sleep(1)
            print("With", traitor, "grounded, you are able to gather", partner1, "and", partner2, "into the van.")
            downed_man = traitor
        elif roll_talk >= 7:
            print("You are able to give a rousing speech, stopping", traitor, "in their tracks.")
            time.sleep(1)
            print(traitor, "puts the gun away, shaken to their core by your words.", traitor, "is back on your side.")
            print("")
            print("With your entire crew in the van, money in tow, you have successfully robbed the Northern Trust Bank.")
            time.sleep(1)
            print("YOU WIN!")
            sys.exit()
    elif react == "C":
        roll_gun = random.randint(1,10)
        if roll_gun <= 2:
            print("As you go to unholster your weapon,", traitor, "fires off at you, killing you.")
            time.sleep(1)
            print("You fail the heist.")
            sys.exit()
        elif roll_gun >= 3:
            print("You are able to unholster your gun, shooting", traitor, "in the chest.")
            time.sleep(1)
            print("")
            print("Despite", traitor, "'s death, you gather your crew in the van, money in tow.")
            time.sleep(1)
            print("You have successfully robbed the Northern Trust Bank.")
            print("YOU WIN!")
            sys.exit()
    elif react == "D":
        roll_run = random.randint(1,10)
        if roll_run <= 8:
            print("You try to run, but", traitor, "shoots you in the back.")
            time.sleep(1)
            print("Incapacitated, you fail the heist.")
            sys.exit()
        elif roll_run >= 9:
            print("You successfully escape, but you left your crew and the money behind.")
            time.sleep(1)
            print("By making such a foolish move, you fail the heist.")
            sys.exit()

if you == "crowd control":
    print("While the drill is being set up, you gather the hostages.")
    if role1 == "crowd control":
        partner = member1
    elif role2 == "crowd control":
        partner = member2
    elif role3 == "crowd control":
        partner = member3
    time.sleep(1)
    print("")
    roll_one = random.randint(1,10)
    if roll_one <= 1:
        print("While trying to secure the hostages, you forgot the zip ties back at your apartment.")
        print("Because of this, you can't control the hostages and you fail the heist.")
        sys.exit()
    elif roll_one >= 2:
        print("You successfully restrain the hostages.")
        print("At the current rate, it should be about 4 minutes before the vault door opens.")
    time.sleep(1)
    print("")
    roll_two = random.randint(1,10)
    if roll_two <= 5:
        print("About a minute after securing the hostages, a large man enters the bank.")
        time.sleep(1)
        roll_two2 = random.randint(1,10)
        if roll_two2 <= 7:
            print("The man's a a police officer!")
            time.sleep(1)
            roll_two3 = random.randint(1,10)
            if roll_two3 <= 2:
                print("The officer pulls out a gun and shoots you in the chest. Incapacitated, you fail the heist.")
                sys.exit()
            elif roll_two3 >=3:
                print(partner, "pulls out their gun and shoots the cop before he can act, saving you.")
                print("")
        elif roll_two2 >= 8:
            print("The man's a civilian, who you restrain quickly.")
    elif roll_two >= 6:
        print("Nothing out of the ordinary yet.")
    print("Three minutes left on the drill.")
    time.sleep(1)
    print("")
    roll_three = random.randint(1,10)
    if roll_three <= 5:
        print(f'While you are waiting, a guard clocks in and sees you and {partner}.')
        time.sleep(1)
        print("The guard shouts at you: 'Hey, what the hell are you doing?!'")
        persuasion3 = input('''
A. We're tourists, trying to get some money?
B. We're guards too, we're also clocking in?
C. We're cops, looking into a potential robbery?
D. We're bank robbers, and you won't stop us?
'''
                  )
        roll_three2 = random.randint(1,10)
        if roll_three2 <= 8:
            print("The guard clearly isn't convinced, and starts to pull out his gun.")
            time.sleep(1)
            roll_three3 = random.randint(1,10)
            if roll_three3 <= 2:
                print("The guard shoots you in the chest. Incapacitated, you fail the heist.")
                sys.exit()
            elif roll_three3 >=3:
                print(partner, "shoots the guard before he can fire, saving you.")
                print("")
        elif roll_three2 >= 9:
            print("The guard seemingly buys whatever you said, and walks away content.")
    elif roll_three >= 6:
        print("Situation normal.")    
    print("About two minutes left on the drill.")
    time.sleep(1)
    print("")
    roll_four = random.randint(1,10)
    if roll_four <= 1:
        print("The hostages are trying to stage a revolt!")
        roll_fourI = random.randint(1,10)
        if roll_fourI <= 2:
            print(f'The hostages succeed and brutalize you and {partner}!')
            print("You fail the heist.")
            sys.exit()
        elif roll_fourI >= 3:
            print(f'You and {partner} easily subdue the unarmed and restrained hostages.')
            print("")
    if roll_four >= 2 and roll_four <= 7:
        print("While you're waiting, you see a hostage trying to get their phone out of their pocket.")
        think_fast = input('''
A. Politely ask them for their phone
B. Threaten to break their legs
C. Speak in a foreign language
D. Point your gun at them
'''
                  )
        if think_fast == "A":
            roll_pol = random.randint(1,10)
            if roll_pol <= 2:
                print("Your persuasion attempt failed, and the hostage dials the police.")
                time.sleep(1)
                print("With the police on the way, you fail the heist.")
                sys.exit()
            elif roll_pol >= 3:
                print("The hostage sees how charming you are, and hands you the phone.")
                print("")
        elif think_fast == "B":
            roll_thr = random.randint (1,10)
            if roll_thr <= 2:
                print("They don't seem particularly frightened, and dial the police.")
                time.sleep(1)
                print("With the police on the way, you fail the heist.")
                sys.exit()
            elif roll_thr >= 3:
                print("The hostage sees how 'persuasive' you are, and hands you the phone.")
        elif think_fast == "C":
            roll_for = random.randint(1,10)
            if roll_for <= 6:
                print("You spout off random gibberish, confusing the hostage. They dial the police.")
                time.sleep(1)
                print("With the police on the way, you fail the heist.")
                sys.exit()
            elif roll_for >= 7:
                print("The hostage, startled by your fluency, hands you the phone.")
        elif think_fast == "D":
            roll_poi = random.randint(1,10)
            if roll_poi <= 2:
                print(f'The hostage somehow disarms you, and shoots {partner}')
                time.sleep(1)
                print("They then shoot you, and you fail the heist.")
                sys.exit()
            elif roll_poi >= 3:
                print("The gun does the talking for you, and the hostage hands you the phone.")
    if roll_four >= 8:
        print("You rack your gun while you wait.")
    print("One minute left on the drill.")
    time.sleep(1)
    print("")
    roll_five = random.randint(1,10)
    if roll_five <= 6:
        print("One of the hostages somehow recognizes you!")
        time.sleep(1)
        roll_fiveI = random.randint(1,10)
        if roll_fiveI <= 7:
            print("Despite the situation, the hostage seems offended you don't recognize them.")
            print("")
            time.sleep(1)
            print("They ask who you think they are?")
            guess = input('''
A. Old friend from high school
B. A distant relative
C. Old one night stand
D. Answer in a foreign language
'''
                                )
            roll_fiveII = random.randint(1,10)
            if roll_fiveII <= 5:
                print("They get upset about your answer, and ask you again.")
                guess2 = input('''
A. Stick to your first answer
B. Yell at them to get down
C. Punch them in the face
D. Answer in a foreign language
'''
                                    )
                roll_fiveIII = random.randint(1,10)
                if roll_fiveIII <= 1:
                    print("They get worked up and charge at you.")
                    time.sleep(1)
                    print(f'They knock you to the ground and hold {partner} up with your gun')
                    print("You fail the heist.")
                    sys.exit()
                elif roll_fiveIII >= 2:
                    print("This seems to sort the problem out, and you resume waiting.")
            elif roll_fiveII >= 6:
                print("They get excited about your answer, and lay back down.")
        elif roll_fiveI >= 8:
                print("You quickly yell at them to get down and salvage the situation.")
    elif roll_five >= 8:
        print("Still waiting.")
    print("The drill is finished.")
    print("")
    time.sleep(1)
    print("You can hear the vault door opening; you wait for the rest of your crew to grab the money.")
    time.sleep(1)
    print("You meet up with the other crew members in the lobby and make your way out of the bank.")
    print("")
    roll_finalI = random.randint(1,3)
    if roll_finalI == 1:
        traitor = member1
        partner1 = member2
        partner2 = member3
    elif roll_finalI == 2:
        traitor = member2
        partner1 = member3
        partner2 = member1
    elif roll_finalI == 3:
        traitor = member3
        partner1 = member1
        partner2 = member2
    print(f'As you all exit the front doors, {traitor} shoots {partner1} in the leg and knocks down {partner2}.')
    time.sleep(1)
    print(f'{traitor} is betraying you!')
    react = input('''
What do you do?

A. Try to disarm them
B. Try to talk to them
C. Try to shoot them
D. Try to run away
'''
                      )
    if react == "A":
        roll_dis = random.randint(1,10)
        if roll_dis <= 2:
            print("You attempt to disarm", traitor, "but they shoot you in the abdomen.")
            time.sleep(1)
            print("You are incapacitated, and you fail the heist.")
            sys.exit()
        elif roll_dis >= 3:
            print("You are able to wrestle the gun out of " + traitor + "'s hands, taking them down in the process")
            print("")
            print("Despite there being a traitor, you gather your crew in the van, money in tow.")
            time.sleep(1)
            print("You have successfully robbed the Northern Trust Bank.")
            print("YOU WIN!")
    elif react == "B":
        roll_talk = random.randint (1,10)
        if roll_talk <= 2:
            print("You try to convince", traitor, "to stand down, but you're shot and killed for your efforts.")
            time.sleep(1)
            print("You fail the heist.")
            sys.exit()
        elif roll_talk >= 3 and roll_talk <= 6:
            print("What you say to", traitor, "confuses them enough for you to land a desperate leg sweep.")
            time.sleep(1)
            print("With", traitor, "grounded, you are able to gather your crew into the van, money in tow.")
            time.sleep(1)
            print("You have successfully robbed the Northern Trust Bank.")
            print("YOU WIN!")
        elif roll_talk >= 7:
            print("You are able to give a rousing speech, stopping", traitor, "in their tracks.")
            time.sleep(1)
            print(traitor, "puts the gun away, shaken to their core by your words.", traitor, "is back on your side.")
            print("")
            print("With your entire crew in the van, money in tow, you have successfully robbed the Northern Trust Bank.")
            time.sleep(1)
            print("YOU WIN!")
            sys.exit()
    elif react == "C":
        roll_gun = random.randint(1,10)
        if roll_gun <= 2:
            print("As you go to unholster your weapon,", traitor, "fires off at you, killing you.")
            time.sleep(1)
            print("You fail the heist.")
            sys.exit()
        elif roll_gun >= 3:
            print("You are able to unholster your gun, shooting", traitor, "in the chest.")
            time.sleep(1)
            print("")
            print("Despite", traitor, "'s death, you gather your crew in the van, money in tow.")
            time.sleep(1)
            print("You have successfully robbed the Northern Trust Bank.")
            print("YOU WIN!")
            sys.exit()
    elif react == "D":
        roll_run = random.randint(1,10)
        if roll_run <= 8:
            print("You try to run, but", traitor, "shoots you in the back.")
            time.sleep(1)
            print("Incapacitated, you fail the heist.")
            sys.exit()
        elif roll_run >= 9:
            print("You successfully escape, but you left your crew and the money behind.")
            time.sleep(1)
            print("By making such a foolish move, you fail the heist.")
            sys.exit()
