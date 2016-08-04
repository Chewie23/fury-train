import pickle

def get_budget():
    while True:
        prompt = "Please enter your monthly salary after tax (as an integer. Round down if necessary): "
        try:
            income = int(raw_input(prompt))
        except ValueError:
            print "Please enter an integer!"
        else:
            return income

income = get_budget()    
pickle.dump(income, open("income.obj", "wb"))        