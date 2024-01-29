import random

def get_random_fortune():
    with open('fortunes.txt', 'r') as f:
        fortunes = f.read().split('%')[:-1]  # Cut off last element which might be an empty string.

    return random.choice(fortunes).strip()

if __name__ == "__main__":
    print("This file is not meant to be run directly.")
    print("Please run 'main.py' instead.")
