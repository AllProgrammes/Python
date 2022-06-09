# importing required modules
from time import sleep
import fontstyle


def covert_to_float(data):
    try:
        print("\nTrying to convert", end="")
        for i in range(10):
            sleep(0.2)
            print(".", end="")
        data = float(data)
        print(fontstyle.apply("Done !! ψ(｀∇´)ψ", "red"))

    except Exception:
        print("\nYou gave an input which couldn't be typecasted into float ＞﹏＜")

    else:  # This will be executed only if [try] is executed successfully
        print(fontstyle.apply(f"\nYour float number is {data}", "bold/YELLOW_BG/blink"))

    finally:  # This will be executed everytime irrespective of what we do in any of the conditions
        # print("\nThanks for using my program (●'◡'●)")
        print(
            fontstyle.apply(
                "\nThanks for using my program (●'◡ '●)", "bold/black/italic/underline"
            )
        )


data = input(
    fontstyle.apply(
        "\n\nGive me a number and I'll convert it into float for you ^_^ !\n", "blue"
    )
)
covert_to_float(data)
