def usr_summary():
    
    usr_location = raw_input("""Please choose the number for the corresponding location 
(defaults to blank location)
[1] BlackBerry
[2] AtHoc
[3] Good Tech
[4] WatchDox
""")

    if usr_location == "1":
        location = "BlackBerry "
    elif usr_location == "2":
        location = "AtHoc "
    elif usr_location == "3":
        location = "Good Tech "
    elif usr_location == "4":
        location = "WatchDox "
    else: 
        location = ""

    usr_sum = raw_input("Please enter summary of the issue: ")

    return location + usr_sum
issue_sum = usr_summary()
print issue_sum