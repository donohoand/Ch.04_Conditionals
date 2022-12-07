'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
score = 0
print("random quiz time")
#question 1
answer1 = input("who is the tallest person in the world in 2021? \na.Sultan Kösen \nB.Robert Wadlow \nc.Brahim Takioullah \nd.lebronjames \nAnswer:")
if answer1.upper() == "A" or answer1.upper() == "Sultan Kösen".upper():
    score = score+1
    print("correct!")
    print("score:", score)

else:
    print("incorrect! The answer was Sultan Kösen")
    print("score:",score)
    print()

#question 2
answer2 = input( "Who is the smallest person in the world in 2021? \na.Robert Wadlow \nB.Chandra Dangi \nc.Percy Jackson \nd.Philip Eno \nAnswer:")
if answer2.upper() == "B" or answer2.upper() == "Chandra Dangi".upper() :
    score = score + 1
    print("correct!")
    print("score:", score)
    p
else:
    print("incorrect! The answer was Chandra Dangi")
    print("score:", score)


#question 3
answer3 = input( "Who is the smartest person in 2021? \na.Walt Sing \nB.Terence Tao\nc.Margareta Johnson\nd.Oliver Brown \nAnswer:")
if answer3.upper() == "B" or answer3.upper() == "Terence Tao".upper() :
    score = score + 1
    print("correct!")
    print("score:", score)

else:
    print("incorrect! The answer was Terence Tao")
    print("score:", score)


#question 4
answer4 = input( "Who is the fastest man in the world 2021? \na.Hugh Raye \nB.Usain Bolt\nc.Drew Jackson\nd.Yohan Black \nAnswer:")
if answer4.upper() == "B" or answer4.upper() == "Usain Bolt".upper() :
    score = score + 1
    print("correct!")
    print("score:", score)

else:
    print("incorrect! The answer was Usain Bolt")
    print("score:", score)


#question 5
answer5 = input( "What is the fastest plane in world? \na.Mikoyan MiG-25 Foxbat \nB.Sukhoi Su-27 Flanker.\nc.Lockheed SR-71 Blackbird \nd.McDonnell Douglas F-15 Eagle. \nAnswer:")
if answer5.upper() == "C" or answer5.upper() == "Lockheed SR-71 Blackbird".upper() :
    score = score + 1
    print("correct!")
    print("score:", score)

else:
    print("incorrect! The answer was  Lockheed SR-71 Blackbird")
    print("score:", score)


#question 6
answer6 = input( "What is the biggest state in the US? \na.Iowa \nB.California\nc.Texas \nd Alaska \nAnswer:")
if answer6.upper() == "D" or answer6.upper() == "Alaska".upper() :
    score = score + 1
    print("correct!")
    print("score:", score)


else:
    print("incorrect! The answer was North American X-15")
    print("score:", score)

#question 7
answer7 = input("What is 33 plus 36 in scientific notation?\na.69\nb.6.9E2\nc.6.9E1\nd.tim caver\nAnswer:")
if answer7.upper() == "C" or answer7 == "6.9E1".upper():
    score = score + 1
    print("correct!")
    print("score:", score)


else:
    print("incorrect! The answer was 6.9E1")
    print("score:", score)


#question 8
answer8 = input("how many years did it take to build the great wall of China?\na 21 years\nb.14 years\nc.17 years\nd.15 years\nAnswer:")
if answer8.upper() == "D" or answer8 == "15 years".upper():
    score = score + 1
    print("correct!")
    print("score:", score)


else:
    print("incorrect! The answer was 15 years")
    print("score:", score)


Grade_Percent = score / 8 * 100

if Grade_Percent >= 100:
    Msg = "Awesome Job you got all questions correct for an A+"
elif  Grade_Percent > 90:
    Msg = "Great Job you Got an A"
elif  Grade_Percent >= 80:
    Msg = "Great Job you Got an B"
elif  Grade_Percent >= 70:
    Msg = "Great Job you Got an C"
elif  Grade_Percent >= 60:
    Msg = "You barely passed with an D"
else:
    Msg = "You failed you loser!! don't get a F again loser"

print(Msg)



