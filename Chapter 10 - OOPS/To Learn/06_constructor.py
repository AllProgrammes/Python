import time  # something new


class clock:
    def __init__(self):  # this is how a contructor is made in python
        zone = time.localtime()  # store the local time in variable zone
        current_time = time.strftime(f"%H hrs:%M mins", zone)
        todays_date = time.strftime("%m-%d-%Y", zone)
        print("Todays date is ->", todays_date)
        print("Current Time is ->", current_time)


class start:
    @staticmethod
    def __init__(os_name, os_version):
        print("Welcome to your operating system ^_^")
        print(f"OS Name -> {os_name}\nVersion -> {os_version}")


os_details = start("Windows 11 Home Single Language", "21H2")
data = clock()  # making an object with name [data]
