#!/usr/bin/env python3
score = input("How much did you score: ")

score = int(score)

if (90<=score<=100):
    print("You have got a Grade A: ")
elif (80<=score<=89):
    print("You have got a Grade B:" )
elif (70<=score<=79):
    print("You have got a Grade C:")
elif (60<=score<=69):
    print("You have a Grade D: ")
elif(score<=59):
    print("You have an F:")


