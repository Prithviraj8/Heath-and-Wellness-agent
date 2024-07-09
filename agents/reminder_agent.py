import time
import threading


class ReminderAgent:
    def __init__(self, user_data):
        self.user_data = user_data
        self.reminders = []

    def add_reminder(self, message, delay):
        self.reminders.append((message, delay))

    def send_reminders(self):
        def reminder_thread(message, delay):
            time.sleep(delay)
            print(f"Reminder: {message}")

        for reminder in self.reminders:
            message, delay = reminder
            threading.Thread(target=reminder_thread, args=(message, delay)).start()


if __name__ == "__main__":
    # Example usage
    user_data = {"name": "John Doe", "age": 30}

    reminder_agent = ReminderAgent(user_data)
    reminder_agent.add_reminder("Time for your workout!", 5)
    reminder_agent.add_reminder("Time for your meal!", 10)
    reminder_agent.send_reminders()
