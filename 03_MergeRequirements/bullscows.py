import sys


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
    pass


if __name__ == "__main__":
    print(bullscows("ропот", "полип"))
