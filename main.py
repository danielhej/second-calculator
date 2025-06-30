def main():
    while(True):
        print(f"""
    Welcom to second Calculator!

    1. SecondS to Minents
    2. SecondS to Hours
    3. SecondS to Days
    4. SecondS to Weeks
    5. SecondS to Months 
    6. SecondS to Years
            
    7. Exit
            
    """)
        user_input = input("Enter Option: ")
        
        if user_input == "1":

            sec = int(input("what is the Second: "))
            res = second2min(sec)

            print(f"{sec} second is {res} minients")
            input("press Enter...")

        elif user_input == "2":

            sec = int(input("what is the Second: "))
            res = second2hour(sec)

            print(f"{sec} second is {res} hours")
            input("press Enter...")

        elif user_input == "3":

            sec = int(input("what is the Second: "))
            res = second2day(sec)

            print(f"{sec} second is {res} days")
            input("press Enter...")

        elif user_input == "4":

            sec = int(input("what is the Second: "))
            res = second2week(sec)

            print(f"{sec} second is {res} weeks")
            input("press Enter...")

        elif user_input == "5":

            sec = int(input("what is the Second: "))
            res = second2month(sec)

            print(f"{sec} second is {res} months")
            input("press Enter...")

        elif user_input == "6":

            sec = int(input("what is the Second: "))
            res = second2year(sec)

            print(f"{sec} second is {res} years")
            input("press Enter...")
        
        else:
            print("Exiting...")



def second2min(sec):
    # min = 60 sec
    return round(sec / 60, 1)

def second2hour(sec):
    # hour = 60 / 60 sec
    return round(sec / 60 / 60, 1)

def second2day(sec):
    # day = 60 / 60 / 24
    return round(sec / 60 / 60 / 24, 1)

def second2week(sec):
    # week = 60 / 60 / 24 / 7
    return round(sec / 60 / 60 / 24 / 7, 1)

def second2month(sec):
    # month = 60 / 60 / 24 / 7 / 4
    return round(sec / 60 / 60 / 24 / 7 / 4, 1)

def second2year(sec):
    # years = 60 / 60 / 24 / 7 / 4 / 12
    return round(sec / 60 / 60 / 24 / 7 / 4 / 12, 1)

main()