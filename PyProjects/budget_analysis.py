import pickle

income = pickle.load(open("income.obj", "rb"))
week_income = income / 4
#may need to use sqlite3 to have persistent data for budget. Will continue this later