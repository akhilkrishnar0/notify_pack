import platform
from plyer import notification

def send_notification(title="Task Completed", message="Your script has finished running!", timeout=10):
    system = platform.system()
    notification.notify(
        title=title,
        message=message,
        timeout=timeout
    )

if __name__ == "__main__":
    send_notification()