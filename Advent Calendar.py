import tkinter as tk
from datetime import datetime

class AdventCalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advent Calendar")
        self.message_label = tk.Label(root, text="Welcome to your Advent Calendar!", font=("Helvetica", 14), padx=20, pady=20, fg="#0000FF")  
        self.message_label.pack()
        self.update_button = tk.Button(root, text="View Calendar", command=self.update_calendar, bg="#228B22", fg="white")
        self.update_button.pack()
        self.messages = [
            "Merry Christmas!",
            "Start a holiday puzzle with family.",
            "Write a letter of gratitude to someone special.",
            "Craft a DIY ornament for your tree.",
            "Enjoy a cozy night by the fireplace.",
            "Visit a local holiday light display.",
            "Try a new festive recipe in the kitchen.",
            "Watch a heartwarming Christmas movie.",
            "Donate to a charitable cause.",
            "Create a holiday playlist and share it with friends.",
            "Send virtual holiday wishes to loved ones.",
            "Read a classic winter tale.",
            "Organize a virtual Secret Santa with friends.",
            "Decorate your living space with festive decor.",
            "Bundle up and take a winter stroll.",
            "Host a virtual game night with holiday-themed games.",
            "Make a list of your favorite moments from the year.",
            "Share a favorite holiday tradition with others.",
            "Create a scrapbook of holiday memories.",
            "Practice mindfulness with a winter meditation.",
            "Express appreciation for the people in your life.",
            "Reflect on personal growth in the past year.",
            "Plan a small act of kindness for someone else.",
        ]
        self.show_message()

    def show_message(self, day=None):
        if day is None or day < 1 or day > len(self.messages):
            self.message_label.config(text="Welcome to your Advent Calendar!")
        else:
            self.message_label.config(text=f"Day {day}\n{self.messages[day - 1]}")

    def update_calendar(self):
        today = datetime.today().date()
        current_day_in_december = today.day
        self.show_message(current_day_in_december)

if __name__ == "__main__":
    root = tk.Tk()
    app = AdventCalendarApp(root)
    root.mainloop()
