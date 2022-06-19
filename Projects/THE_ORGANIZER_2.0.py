import os
from time import sleep

# ALL THE EXT DATABASES
img_ext = [".img", ".png", ".jpg", ".jpeg", ".raw"]
doc_ext = [
    ".doc",
    ".htm",
    ".odt",
    ".pdf",
    ".xls",
    ".xlsx",
    ".ods",
    ".ppt",
    ".txt",
]
video_ext = [
    ".webm",
    ".mpg",
    ".mp2",
    ".mpeg",
    ".mpe",
    ".mpv",
    ".ogg",
    ".mp4",
    ".m4p",
    ".m4v",
    ".avi",
    ".wmv",
    ".mov",
    ".qt",
    ".flv",
    ".swf",
]
audio_ext = [".m4a", ".flac", ".mp3", ".wav", ".wma", ".aac"]

# FILE LIST
files = os.listdir()

# ALL FUNCTIONS
def arrange_images():
    try:
        print("\nSearching for 'Images' directory", end="")
        for i in range(10):
            print(".", end="")
            sleep(0.2)
        if os.path.exists("Images") == False:
            print("Not Found !!\nSo creating", end="")
            for i in range(10):
                print(".", end="")
            sleep(0.2)
            os.mkdir("Images")
            print("Done!!")
        else:
            print("Found !!")
        images = [
            file for file in files if os.path.splitext(file)[1].lower() in img_ext
        ]
        for item in images:
            os.replace(item, f"Images/{item}")
        print(f"Successfully Moved {len(images)} image files in 'Images' folder")
    except Exception as error:
        print(f"\nI have encountered an unexpected error :(\nError : {error}")


def arrange_docs():
    try:
        print("\nSearching for 'Documents' directory", end="")
        for i in range(10):
            print(".", end="")
            sleep(0.2)
        if os.path.exists("Documents") == False:
            print("Not Found !!\nSo creating", end="")
            for i in range(10):
                print(".", end="")
            sleep(0.2)
            os.mkdir("Documents")
            print("Done!!")
        else:
            print("Found !!")
        documents = [
            file for file in files if os.path.splitext(file)[1].lower() in doc_ext
        ]
        for item in documents:
            os.replace(item, f"Documents/{item}")
        print(
            f"Successfully Moved {len(documents)} document files in 'Documents' folder"
        )
    except Exception as error:
        print(f"\nI have encountered an unexpected error :(\nError : {error}")


def arrange_videos():
    try:
        print("\nSearching for 'Videos' directory", end="")
        for i in range(10):
            print(".", end="")
            sleep(0.2)
        if os.path.exists("Videos") == False:
            print("Not Found !!\nSo creating", end="")
            for i in range(10):
                print(".", end="")
            sleep(0.2)
            os.mkdir("Videos")
            print("Done !!")
        else:
            print("Found !!")
        videos = [
            file for file in files if os.path.splitext(file)[1].lower() in video_ext
        ]
        for item in videos:
            os.replace(item, f"Videos/{item}")
        print(f"Successfully Moved {len(videos)} videos files in 'Videos' folder")
    except Exception as error:
        print(f"\nI have encountered an unexpected error :(\nError : {error}")


def arrange_audios():
    try:
        print("\nSearching for 'Audios' directory", end="")
        for i in range(10):
            print(".", end="")
            sleep(0.2)
        if os.path.exists("Audios") == False:
            print("Not Found !!\nSo creating", end="")
            for i in range(10):
                print(".", end="")
            sleep(0.2)
            os.mkdir("Audios")
            print("Done !!")
        else:
            print("Found !!")
        audios = [
            file for file in files if os.path.splitext(file)[1].lower() in audio_ext
        ]
        for item in audios:
            os.replace(item, f"Audios/{item}")
        print(f"Successfully Moved {len(audios)} audios files in 'Audios' folder")
        print(audios)
    except Exception as error:
        print(f"\nI have encountered an unexpected error :(\nError : {error}")


def arrange_other():
    file_to_be_skipped = ["THE_ORGANIZER_2.0.exe", "DumpStack.log.tmp"]
    try:
        print("\nSearching for 'Others' directory", end="")
        for i in range(10):
            print(".", end="")
            sleep(0.2)
        others_ext = []
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if (
                (ext not in img_ext)
                and (ext not in doc_ext)
                and (ext not in video_ext)
                and (ext not in audio_ext)
                and os.path.isfile(file)
                and (os.path.basename(file) not in file_to_be_skipped)
            ):
                others_ext.append(file)
        if os.path.exists("Others") == False:
            print("Not Found !!\nSo creating", end="")
            for i in range(10):
                print(".", end="")
            sleep(0.2)
            os.mkdir("Others")
            print("Done !!")
        else:
            print("Found !!")
        for item in others_ext:
            os.replace(item, f"Others/{item}")
        print(f"Successfully Moved {len(others_ext)} others files in 'Others' folder")
    except Exception as error:
        print(f"\nI have encountered an unexpected error :(\nError : {error}")


be_organised_text = (
    "\n\n\t\t\t\t THANKS FOR CHOOSING ORGANIZER ^_^\n\t\t\t\t\t #be_organized ✌️"
)
if __name__ == "__main__":
    print(
        "\n\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx WELCOME TO ORGANIZER xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    )
    print("\t\t\t\t\t\t\t\t\t\t   Made by Biswajit Mishra")
    print(
        "\n\nWhat is does --> This is a organizer program which will orgranize all the mess in your system\n"
    )
    print("Note : Press 'q' to exit anytime\n")
    print(f"ATTENTION !!\nCurrent working directory is : {os.getcwd()}\n")
    while True:
        user_choice = input(
            "Options Available :- \n1. Arrange Images\n2. Arrange Documents\n3. Arrange Videos\n4. Arrange Audio Files\n5. Arrange Other Files\n6. Arrange All File Type\n\nSo BOSS !! What you wanna do ?\nAns : "
        )
        if user_choice.lower() == "q":
            print(be_organised_text)
            break
        elif user_choice == "1":
            arrange_images()
            print(be_organised_text)
        elif user_choice == "2":
            arrange_docs()
            print(be_organised_text)
        elif user_choice == "3":
            arrange_videos()
            print(be_organised_text)
        elif user_choice == "4":
            arrange_audios()
            print(be_organised_text)
        elif user_choice == "5":
            arrange_other()
            print(be_organised_text)
        elif user_choice == "6":
            arrange_images()
            arrange_docs()
            arrange_videos()
            arrange_audios()
            arrange_other()
            print(be_organised_text)
        else:
            print("Please enter a valid input !!")
