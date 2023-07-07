# This file is just an abstract example
# and not a concrete implementation nor 
# is it part of a project. 
# On July 7th of 2023, I asked ChatGPT 
# for an example of implementing Events 
# in Python.
# This was the output. I archived it 
# for learning purpose, since I want
# to understand the concept of Events
# in object-oriented languages.
# --------------------------------------


class Event:
    def __init__(self):
        self.handlers = []

    def add_handler(self, handler):
        self.handlers.append(handler)

    def remove_handler(self, handler):
        self.handlers.remove(handler)

    def fire(self, *args, **kwargs):
        for handler in self.handlers:
            handler(*args, **kwargs)


class Button:
    def __init__(self):
        self.click_event = Event()

    def click(self):
        self.click_event.fire()


def button_clicked():
    print("Button clicked!")


# Erstellen einer Button-Instanz
button = Button()

# Registrieren des Event-Handlers
button.click_event.add_handler(button_clicked)

# Auslösen des Events
button.click()