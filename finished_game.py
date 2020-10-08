import random
questions = [["According to Euler, e^(i*π) + 1 = " , "0"],["How many studio albums does Metallica have as of 2020?","10","Ten","ten","TEN"],["How many countries exist within Britain?","4","four","Four","FOUR"],["How many states are in the USA?" , "50" , "fifty" , "FIFTY" , "Fifty"] , ["Kathmandu is the capital of " , "NEPAL" , "Nepal" , "nepal"] , ["Constantinople was conquered by the ottomans in what year " , "1453"] , ["Nintendo is a company from " , "japan" , "Japan" , "JAPAN"] , ["Tupac was a rapper from the _ coast of the USA", "west" , "West" , "WEST" , "Western" , "WESTERN" , "western"] ]
security_code = random.randrange(1000)
security_code = str(security_code)
completed_areas=[]
level=0
items=[]
areas=["TOWN", "MOUNTAIN", "MINE" , "FOREST" , "BEACH"]
def mine (level):
       for i in range (level,4):
              print (" "*(4-i), "*"*(2*i+1))
def error():
       print ("Error")
       print ("Please type in capital letters one of the presented choices")
def comp():
       print ("There is nothing left to do here!")
def adddynamite():
       global level
       level=level+1
       print ("You won some extra dynamite, that can be used to open up the mine even further")
def blackjack():
       cards=[2,3,4,5,6,7,8,9,10,'J','Q','K','A']
       draw=input("Draw? (answer with YES or NO) ")
       value=0
       while draw!="YES" and draw!="NO":
              draw=input("Draw? (answer with YES or NO) ")
       while value<=21 and draw=="YES":
              pick=random.randrange(0,12)
              if type(cards[pick])!=str:
                     value=value+cards[pick]
              elif cards[pick]=='A' and value+11>21:
                     value=value+1
              elif cards[pick]=='A' and value+11<=21:
                     value=value+11
              else:
                     value=value+10
              print ("You picked", cards[pick],"your total value",value)
              if value>21:
                     break
              draw=input("Draw? (answer with YES or NO) ")
              while draw!="YES" and draw!="NO":
                     draw=input("Draw? (answer with YES or NO) ")
       if value>21:
              print ("You lost your value is",value)
       else:
              computer=random.randrange(10,21)
              print ("Computer has",computer)
              if computer>value:
                     print ("You lost")
                     return False
              if value>computer:
                     print ("You won")
                     return True
              if value==computer:
                     print ("It's a draw")
                     return False

print ("You spawn in an island. An old man approaches you. He immediatly starts talking:")
print ("Hello, I'm Mr Exposition. My job is to explain how the game works, so pay attention.")
print ("You can visit any location you want in the island. One of them is a mine that is shaped like this:")
mine(0)
print ("However if you visit it with a bar of dynamite, the first level of the mine will explode, leaving it looking like this:")
mine(1)
print ("Similarly if you visit the mine with 2 bars of dynamite, the first two levels will explode, leaving it looking like this:")
mine(2)
print ("The goal of the game is to access the heart of the mine, by collecting 4 different pieces of dynamite from around the island.")
print("Every time you visit the mine without 4 bars of dynamite you will be able to check how much of the mine is still left. Have fun.")
print ("(Mr Exposition explodes into a cloud of smoke)")
print("----------------------------------------------------------")
while True:
       visit=input ("Do you want to visit TOWN, MOUNTAIN, MINE ,BEACH or the FOREST? ")
       while visit not in areas:
              error()
              visit=input ("Do you want to visit TOWN, MOUNTAIN, MINE or the FOREST? ")
       if visit=="TOWN":
              while True:
                     print("----------------------------------------------------------")
                     print ("Do you want to enter the pub, explore the town square or exit the town?")
                     key=input("Type PUB, SQUARE or EXIT ")
                     while key!="PUB" and key!="SQUARE" and key!="EXIT":
                            error()
                            key=input()
                     if key=="PUB":
                            key = input("Would you like to engage in a game of blackjack? (answer with YES or NO) " )
                            while key!="YES" and key!="NO":
                                   error()
                                   key=input()
                            if key=="YES":
                                   print ("You pick cards one by one. If you get an overall score higher than the CPU one you win, although if you surpass 21 you instantly lose. ")
                                   check=False
                                   while check==False:
                                          x=blackjack()
                                          if x==True:
                                                 print("Victory is yours")
                                                 if "TOWN" not in completed_areas:
                                                        adddynamite()
                                                        completed_areas.append("TOWN")
                                                 check=True
                                          else:
                                                 print ("You lost. Do you want to play again?")
                                                 key=input("Type YES or NO ")
                                                 while key!="YES" and key!="NO":
                                                        Error()
                                                        key=input()
                                                 if key=="NO":
                                                        check=True
                     elif key=="SQUARE" and "SQUARE" not in completed_areas:
                            print ("You find an orange goblin, living a life of crime due to video games and atheism that is looking to sell marijuana.")
                            if "gold" in items:
                                   key = input ("Do you trade your gold for weed? (YES or NO) ")
                                   while key!="YES" and key!="NO":
                                          Error()
                                          key=input()
                                   if (key=="YES"):
                                          items.append("weed")
                                          print("You obtained some weed")
                                          completed_areas.append("SQUARE")
                            else:
                                   print ("Unfortunately you lack the required gold needed to obtain a joint to blaze up")
                     elif key=="SQUARE" and "SQUARE" in completed_areas:
                            comp()
                     elif key=="EXIT":
                            break
              print ("You leave the town")
              print("----------------------------------------------------------")
       elif  visit=="FOREST":
              print ("You enter the island's massive forest")
              q=input("You come across a cave. Do you enter it? (type either YES or NO) ")
              while q!="YES" and q!="NO":
                     Error()
                     q=input()
              if q=="YES":
                     print ("You enter the dark cave and find a secret underground city like the ones in Cappadocia (google that shit)")
                     kappa=["EXIT", "CASTLE", "TEMPLE"]
                     while True:
                            print("----------------------------------------------------------")
                            go=input("Type CASTLE or TEMPLE to enter those locations or type EXIT to leave the cave ")
                            while go not in kappa:
                                   error()
                                   go=input()
                            if go=="EXIT":
                                   break
                            elif go=="TEMPLE":
                                   if "TEMPLE" not in completed_areas:
                                          if "gold" not in items:
                                                 print ("A purple goblin offers you an optional side quest because the programmer thinks he is hot shit")
                                                 print ("'Visit the Town Square in the capital and buy me some weed'")
                                                 print ("(the goblin hands you some golden coins)")
                                                 items.append("gold")
                                          elif "weed" in items:
                                                 print ("The goblin says:")
                                                 print ("'Thank you. You are quite helpful. But are you really deserving of my love and trust? '")
                                                 print ("I'm gonna present you with a riddle. Be careful, you only have one try.")
                                                 print ("Wikipedia defines the Monty Hall Problem like this: ")
                                                 print("------------------------------------------------------------------")
                                                 print ("Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats.")
                                                 print ("You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat.")
                                                 print ("He then says to you, 'Do you want to pick door No. 2?' Is it to your advantage to switch your choice?")
                                                 print("------------------------------------------------------------------")
                                                 q3 = input("Type your answer (YES or NO) ")
                                                 while q3!="YES" and q3!="NO":
                                                        error()
                                                        q3=input()
                                                 if q3=="YES":
                                                        items.append("Endgame")
                                                        print("You got it right (QUEST COMPLETED)")
                                                        print("This will result in getting the better ending")
                                                 else:
                                                        print("You are a complete loser, don't ever come here again")
                                                 completed_areas.append("TEMPLE")
                                          elif "gold" in items and "weed" not in items:
                                                 print ("The goblin complains that you didn't bring his allegedly medical marijuana")
                                   else:
                                          comp()
                                   print ("You leave the temple")
                            elif go=="CASTLE":
                                   if "boots" in items :
                                          comp()
                                   else:
                                          print ("You come across a chest.")
                                          q2= input("Do you want to open it? (YES or NO) ")
                                          while q2!="YES" and q2!="NO":
                                                 error()
                                                 q2=input()
                                          if q2=="YES":
                                                 print ("You just acquired some magical boots that allow you to run on water")
                                                 items.append("boots")
                                          else:
                                                 print("You are a boring person")
              print("----------------------------------------------------------")
              if "secret" and "key" not in items:
                     print("You continue walking through the forest")
                     print ("You find a blue goblin that gives you a simple challenge")
                     print ("These are the rules of the fibonacci sequence: A(0)=1, A(1)=1, A(i+1)= A(i) + A(i-1)")
                     print ("Type the first 6 elements of the fibonacci sequence with no spaces in between, for example 11XXXX where the Xs are numbers")
                     guess=input("Type your answer or EXIT to leave the challenge ")
                     while guess!="112358"and guess!="EXIT" and guess!= security_code:
                            error()
                            guess=input("Try again ")
                     if guess == "112358":
                            print ("You obtained a key")
                            items.append("key")
                     elif guess == security_code:
                            print ("Congratulations, you accessed the most obscure part of the game")
                            if "FOREST" not in completed_areas:
                                   adddynamite()
                                   completed_areas.append("FOREST")
                                   items.append("secret")
              else:
                     comp()
              print("You leave the forest")
              print("----------------------------------------------------------")
       elif visit == "BEACH":
              print ("You arrive at the beach.")
              if "boots" in items:
                     q = input("Use your boots to run on the water? (YES or NO) ")
                     while q!="YES" and q!="NO":
                            error()
                            q=input()
                     if q=="YES":
                            print("You reach an island with a chest lying in the sand.")
                            if "key" in items:
                                   HELP = input ("Use your key to open the chest? (YES or NO) ")
                                   while HELP!="YES" and HELP!="NO":
                                          error()
                                          HELP = input()
                                   if HELP == "YES":
                                          print ("You found a piece of dynamite!")
                                          if "BEACH" not in completed_areas:
                                                 adddynamite()
                                                 completed_areas.append("BEACH")
                                          else:
                                                 print("The chest is empty")
                                   else:
                                          print("The chest is locked")
                                          print ("The programmer could have just as easily made it so you didn't need a key but they love making you run around hunting for items to satisfying they sadism")
                                          print("You leave the island")
                     else:
                            print("You leave the beach")
              print("----------------------------------------------------------")
       elif visit == "MINE":
              if level == 4:
                     break
              print ("The mine looks like this:")
              mine(level)
              print("----------------------------------------------------------")
       elif visit=="MOUNTAIN" and "MOUNTAIN" in completed_areas:
              print ("We are very sorry but the government has rendered the mountain inaccessible for reasons definetily not related to rural terrorism")
       elif visit == "MOUNTAIN":
              print("Visiting the mountain would be a long and tiring process as you will need to ride the train for many hours")
              q1 = input("Board the train (YES or NO)? ")
              while q1!="YES" and q1!="NO":
                     error()
                     q1=input()
              if q1=="YES":
                     print("----------------------------------------------------------")
                     print ("Many hours pass while you wait for the train to arrive to its destination")
                     print ("You finally arrive at the mountain and climb to the top.")
                     print ("You come across your old friend Mr Exposition.")
                     print("'I assume you are here to access the tree of knowledge from the bible'")
                     print ("You nod positively, pretending you are aware of all the lore of this universe and its theological themes")
                     print ("'But first you must answer correctly 1 arbitrary question.'")
                     print("----------------------------------------------------------")
                     while True:
                            question = random.randrange(len(questions))
                            print(questions[question][0])
                            answer = input("(type the answer) ")
                            if answer in questions[question]:
                                   break
                     used_question = question
                     print("----------------------------------------------------------")
                     print ("You obviously are a fellow intellectual")
                     print ("But before you access the tree of knowledge you have to confess your most embarrasing secret")
                     secret = input ("Type your most embarrassing secret ")
                     while True:
                            q2 = input("Are you ready to talk to the tree of knowledge? (YES or NO) ")
                            while q2!="YES" and q2!="NO":
                                   error()
                                   q2=input()
                            if q2=="NO":
                                   print ("Okay I guess we can waste all day doing this")
                            elif q2=="YES":
                                   break
                     print("----------------------------------------------------------")
                     print ("The wise tree of knowledge exclaims:")
                     print ("Among these lands, there is another of blue color individual that may offer you another riddle")
                     print ("Apart from the initial correct answer, there is a second valid answer which holds a different reward")
                     print("You should remember this code: " , security_code , " for that occasion")
                     continuE = input("Type anything to move on once you understand all this information and memorize the code ")
                     q3 = input ("Board the train to return? (YES or NO) ")
                     if q3!="YES" and q3!="Yes" and q3!="yes":
                            print ("Eat shit you are boarding it anyway")
                     print("----------------------------------------------------------")
                     print ("The train slowly pass through a forest while you try to sleep")
                     print ("Suddenly you hear an explosion and the train lands on its side")
                     print ("'I PLEDGE MY SOUL TO GOD DEATH TO THE RULING ELITE OF THIS ISLAND' exclaims a rather enthusiastic and heavily armed fellow ")
                     print ("One of the guerrilla warriors puts a gun to your head ")
                     print("'The only wait we will let you go is if you answer another question correctly, for arbitrary game reasons'")
                     while True:
                            question = random.randrange(len(questions))
                            while (question==used_question):
                                   question = random.randrange(len(questions))
                            print(questions[question][0])
                            answer = input("(type the answer here) ")
                            if answer in questions[question]:
                                   break
                     print ("You ran away crying like a bitch, swearing to never talk about with the authorities")
                     print ("But you also managed to grab some dynamite of their arsenal")
                     adddynamite()
                     completed_areas.append("MOUNTAIN")
                     print("----------------------------------------------------------")
for i in range (10000):
       print("*"*i)
print ("Congratulations! You have accessed the heart of the mine and won the game!")
if "Endgame" in items:
       print("Because of the optional quest you did earlier on, normally you would access an extra part the I found funny.")
       print("Unfortunately my friends told me it was too risque and provocative for github so you got the lame clean version where there's no de facto difference between the endings.")
else:
       print("However you didn't complete everything so you get the bad ending.")
q=input("Type anything to terminate the game")
