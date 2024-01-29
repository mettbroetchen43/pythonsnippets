import random

def get_random_fortune():
    with open('fortunes.txt', 'r') as f:
        fortunes = f.read().split('%')[:-1]  # Cut off the last element which might be an empty string.

    return random.choice(fortunes).strip()

if __name__ == "__main__":
    random_fortune = get_random_fortune()
    print(random_fortune)