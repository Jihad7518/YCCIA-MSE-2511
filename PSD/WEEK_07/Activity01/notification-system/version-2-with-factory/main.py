from factory import NotificationFactory

def main():
    notification_type = input("Enter notification type (email/sms/push): ").lower()
    notification = NotificationFactory.create_notification(notification_type)
    notification.send("Hello! This is WITH Factory Pattern.")

if __name__ == "__main__":
    main()
