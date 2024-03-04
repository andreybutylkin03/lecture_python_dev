import sys
import random
import urllib.request
import os.path
from cowsay import cowsay, list_cows

def bullscows(guess: str, secret: str) -> (int, int):
    cow = 0
    s_m = dict()

    for i in secret:
        s_m.setdefault(i, 0)
        s_m[i] += 1
    
    for i in guess:
        if i in s_m.keys() and s_m[i] > 0:
            cow += 1
            s_m[i] -= 1

    bull = 0

    for i in range(len(guess)):
        if guess[i] == secret[i]:
            bull += 1

    return (bull, cow)


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    secret = words[random.randrange(0, len(words))]
    guess = None
    tr = 0

    while guess != secret:
        guess = ask("Введите слово: ", words)
        tr += 1

        bulls, cows = bullscows(guess, secret)

        inform("Быки: {}, Коровы: {}", bulls, cows)

    return tr 


def ask(prompt: str, valid: list[str] = None) -> str:
    fd = open('cow.txt', "r")
    cf = fd.read()
    fd.close()

    if valid is None:
        print(cowsay(prompt, cowfile=cf))
        return input()
    else:
        s = None

        while s not in valid:
            print(cowsay(prompt, cowfile=cf))
            s = input()

        return s


def inform(format_string: str, bulls: int, cows: int) -> None:
    idx_c = random.randrange(0, len(list_cows()))

    print(cowsay(format_string.format(bulls, cows), cow=list_cows()[idx_c]))


if __name__ == "__main__":
    try:
        d = urllib.request.urlopen(sys.argv[1]).read().decode().split('\n')
    except:
        if os.path.exists(sys.argv[1]):
            d = open(sys.argv[1], "r").read().split('\n')
        else:
            print("Invalid arguments")
            sys.exit()

    if len(sys.argv) == 3:
        len_of = int(sys.argv[2])
    else:
        len_of = 5

    d = list(filter(lambda x: len(x) == len_of, d))

    print(f"Попыток сделано: {gameplay(ask, inform, d)}")

