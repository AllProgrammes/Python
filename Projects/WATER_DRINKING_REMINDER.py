import time
from plyer import notification

if __name__ == "__main__":
    for count in reversed(range(9)):
        if count == 0:
            break
        notification.notify(
            title="DRINK WATER",
            message=f"{count} glasses of water left to drink",
            app_icon="D:\BISWAJIT GITHUB\Python\Projects\icon.ico",
            app_name="WATER MAN",
            ticker="test test",
            # display time on the screen in seconds
            timeout=2,  # default is 10
        )

        # wait time till next notification
        time.sleep(60 * 60)  # equivalent to 60 mins
