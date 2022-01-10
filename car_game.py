print("Enter help to start")
option = input(">")
if option == "help" :
    print('''
    start - To start the car
    stop  - To stop the car
    quit  - To exit the car
    ''')
   #  ssq_option = input(">")
    i = 0
    started = False
    stopped = False
    while i <= 5  :
     ssq_option = input(">")
     if ssq_option == "start" :
        if started :
           print("car is already started")
        else :  
            started = True
            print("car started ready to go")
     elif ssq_option == "stop" :
        if not started :
           print("car has already stopped")
        else :
            stopped = False
            print("car stopped")
        
     elif ssq_option == "help" :
          print('''
    start - To start the car
    stop  - To stop the car
    quit  - To exit the car
    ''')
       
     elif ssq_option == "quit" :
         print("Quiting game")
         break
    i = i+1 