secret_number = 7
i=1
print("Find the secret number (1-10) ")
while i <= 3 :
    got = int(input("Guess : "))
    if got == secret_number :
        print("You win")
        break
    else :
        print("Oop's wrong number")
    i = i+1
print("Game over")