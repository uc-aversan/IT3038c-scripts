import time

start_time = time.time()

print('What is your name?')
myName = str(input())

#while loop example
while myName != "Aaron":
    if myName == 'your name':
        print("Not funny, Dad. What's your real name?")
        myName = input()
    else:
        print("You are not authorized to run this.")
        myName = input()

#    print("This is not 'your name'. Please type 'your name'.")
#    myName = input()


print('Hello, ' + myName + '. That is a good name. How old are you?')
myAge = int(input())

#Sample is statements
if myAge < 13:
    print("Learning young, thant's good.")
elif myAge == 13:
    print("You're a teenager now... thats cool.")
elif myAge > 13 and myAge < 30:
    print("Adulting!")
elif myAge >= 30 and myAge < 65:
    print("Still young. Still learning.")
else:
    print("... you've lived a long life.")

time.sleep(1)
programAge = int(time.time() - start_time)
print("%s? That's funny, I am only %s secconds old." % (myAge, programAge))
print("I wish I was %s years old" % (myAge *2)) 

time.sleep(3) 
print("I'm tired. Shutting down now.")