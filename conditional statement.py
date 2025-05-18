# conditional statement (making decision in code )
# if this happen(true) do this,otherwise do somthing else 
my_age=10
if my_age>30:
    print("you are old ")
elif 20<=my_age<=30:
    print("you are an adult")
elif 10<=my_age<20: # IF if condition is not true.elif mean check next condition 
    print('you are a "teenager"')
elif 0<=my_age<10:
    print('you are a "child"') 
else:
    print("you are not born yet haha ") 
    # (if) means IF 1st condition true then print this 
    #(elif) means if 1st condition is not true then check 2nd condition and  if 2nd condition true then print this 
    # again (elif) means if 1st and 2nd condition is not true  then check 3rd condtion and if 3rd condition true then print this
    # so on.......
    #(else) means if all above conditions are not then print this 
    # important note (if two consecutive condition are true then it will print 1st one )
