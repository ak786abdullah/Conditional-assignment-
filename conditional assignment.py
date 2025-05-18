# task 1 check age 
age =23 
if age>=18: # if means If condition true then print this 
    print("you are an adult") # condition is true so(out put=you are an adult) 
else:
    print("you are not an adult") # else means If all above conditions are not true then print 'you are not an adult' 
marks=76 
if marks>=90:
    print('grade:A')
elif marks>=70:
    print("grade:B") # elif means if above conditions are not true then check this If true then print this 
elif marks>=50:
    print("grade:C")
else:
    print("congratulation your are failed ") # hahaha 
# out put=grade:B (76>70 true )
# weather advice 
weather="sunny"
if weather is "rainy":
    print("take an umberalla")
elif weather is "cloudy":# we can use '==' instead of is 
    print("it might rain later")
elif weather is "sunny": # this condition is true 
    print("wear sunglasses") 
else:
    print("please enter right input")
    # out put =wear sunglasses 
    # feeling hungry 
    hungry=True 
    if hungry is True :
        print("go eat something!")
    else:
        print("may be have a snack later") 
        # out put =go eat something! ( becouse condition is true )
        #mini chat boot
        mood=input("how are you feeling today?:")
        if mood == "happy":
            print("That's great to hear!")
        elif mood== 'sad':
            print("I hope your day gets better.")
        elif mood=='bored':
            print("Try reading a book or going for a walk.")
        else:
            print("Thanks for sharing your mood!")
            #output depend on user input 