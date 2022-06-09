from time import sleep


def covert_to_float(data):
    try:
        print("Trying to convert", end="")
        for i in range(10):
            sleep(1)
            print(".", end="")
        data = float(data)
        print("Done !! ( •̀ ω •́ )✧")

    except Exception:
        print("\nYou gave an input which couldn't be typecasted into float ＞﹏＜")

    else:  # This will be executed only if [try] is executed successfully
        print("\nYour float number is", data)


data = input("Give me a number and I'll convert it into float for you ^_^ !\n")
covert_to_float(data)
