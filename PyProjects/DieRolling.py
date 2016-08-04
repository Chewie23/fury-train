from random import randrange
#Has to be a better way to go through the choices of the die
def die_roll():
    done = False

    while not done:   
        n = randrange(0, 60000)
        
        if n <= 10000:
            print "You got 1"
        elif n <= 20000:
            print "You got 2"
        elif n <= 30000:
            print "You got 3"
        elif n <= 40000:
            print "You got 4"
        elif n <= 50000:
            print "You got 5"
        else:
            print "You got 6"
                
        roll_die = raw_input("""Again? Y/N
>""")
        if roll_die in ["N", "n", "No", "no", "q", "quit", "Q", "Quit"]:
            done = True
            print "Goodbye"
             

def coin_flip():
    done = False
    
    while not done:
        
        n = randrange(0, 100000)
        
        if n <= 50000:
            print "Heads"
        else:
            print "Tails"
                
        flip_coin = raw_input("""Again? Y/N
>""")
        if flip_coin in ["N", "n", "No", "no", "q", "quit", "Q", "Quit"]:
            done = True
            print "Goodbye"

def coin_or_die():
    choice = raw_input("""Do you want to flip a C(oin) or toss a D(ie)? C/D/Q(uit)
>""")
    if choice in ["Q", "q", "quit", "Quit"]:
        print "Goodbye"
        exit()
    elif choice in ["C", "coin", "Coin", "c"]:
        coin_flip()
    elif choice in ["D", "d", "Die", "die"]:
        die_roll()
    else:
        print "I don't understand"
        coin_or_die()
        
coin_or_die()
    