import os
from time import sleep

# ALL THE EXT DATABASES
img_ext = [".img", ".png", ".jpg", ".raw"]
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
    "mp2",
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
audio_ext = ["m4a", "flac", "mp3", "mp4", "wav", "wma", "aac"]

# CURRENT WORKING DIRECTORY
current_working_directory = os.getcwd()


# ALL FUNCTIONS
def Search_Files():
    files = []
    walk_db = os.walk(current_working_directory)
    for path in walk_db:
        for file_in_current_path in path[2]:
            print(file_in_current_path)
            files.append(os.path.join(path[0], file_in_current_path))
    return files
def arrange_images(files):
    print("Searching for 'Images' directory", end="")
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
    images = [file for file in files if os.path.splitext(file)[1].lower() in img_ext]
    for item in images:
        os.replace(item, f"Images/{os.path.basename(item)}")
    print(f"Successfully Moved {len(images)} image files in 'Images' folder\n")


def arrange_docs(files):
    print("Searching for 'Documents' directory", end="")
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
    documents = [file for file in files if os.path.splitext(file)[1].lower() in doc_ext]
    for item in documents:
        os.replace(item, f"Documents/{os.path.basename(item)}")
    print(f"Successfully Moved {len(documents)} document files in 'Documents' folder\n")


def arrange_videos(files):
    print("Searching for 'Videos' directory", end="")
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
    videos = [file for file in files if os.path.splitext(file)[1].lower() in video_ext]
    for item in videos:
        os.replace(item, f"Videos/{os.path.basename(item)}")
    print(f"Successfully Moved {len(videos)} videos files in 'Videos' folder\n")


def arrange_audios(files):
    print("Searching for 'Audios' directory", end="")
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
    audios = [file for file in files if os.path.splitext(file)[1].lower() in audio_ext]
    # print("Audios : ", audios)
    for item in audios:
        os.replace(item, f"Audios/{os.path.basename(item)}")
    print(f"Successfully Moved {len(audios)} audios files in 'Audios' folder\n")


def arrange_other(files):
    print("Searching for 'Others' directory", end="")
    for i in range(10):
        print(".", end="")
        sleep(0.2)
    others_ext = []
    for file in files:
        if os.path.isfile(file):
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
    # print("Others : ", others_ext)
    for item in others_ext:
        os.replace(item, f"Others/{os.path.basename(item)}")
    print(f"Successfully Moved {len(others_ext)} others files in 'Others' folder\n")


be_organised_text = "\n\n\t\t\t\t\t\t\t\t\t THANKS FOR CHOOSING ORGANIZER ^_^\n\t\t\t\t\t\t\t\t\t\t #be_organized ✌️"
if __name__ == "__main__":
    print(
        "\n\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx WELCOME TO ORGANIZER xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    )
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tMade by Biswajit Mishra")
    print(
        "\n\nThis is a organizer program which will orgranize all the mess in your system\n"
    )
    files = Search_Files()

    while True:
        user_choice = input("Press 'Enter' to start else press any key to exit : ")
        if user_choice == "":
            print(f"\nATTENTION !!\nCurrent working directory is : {os.getcwd()}\n")
            confirm = input("Press 'y\Y' to confirm : ")
            try:
                if confirm.lower() == "y":
                    print("OK BOSS\n")
                    arrange_images(files)
                    arrange_docs(files)
                    arrange_videos(files)
                    arrange_audios(files)
                    arrange_other(files)
                    print(be_organised_text)
                else:
                    continue
            except Exception as error:
                print(f"\nI have encountered an unexpected error :(\nError : {error}")
        else:
            print(be_organised_text)
            break
