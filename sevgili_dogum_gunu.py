
import time
import os

heart = [
    "  ***     ***  ",
    "******* *******",
    "***************",
    " ************* ",
    "  ***********  ",
    "   *********   ",
    "    *******    ",
    "     *****     ",
    "      ***      ",
    "       *       "
]

def print_heart():
    os.system('cls' if os.name == 'nt' else 'clear')
    for line in heart:
        print("\033[91m" + line + "\033[0m")
    print("\n")

def birthday_message(Melike):
    messages = [
        f"Canım {Melike},",
        "Bugün senin doğum günün!",
        "Seninle her gün bir hediye gibi 🎁",
        "İyi ki varsın, iyi ki hayatımdasın 💖",
        "Nice mutlu, sağlıklı, birlikte senelere!",
        "Seni çok seviyorum 💕"
    ]
    for msg in messages:
        print_heart()
        print("\033[95m" + msg + "\033[0m")
        time.sleep(2)

if __name__ == "__main__":
    sevgilinin_ismi = "Meleğim"  # Buraya sevgilinin ismini yazabilirsin
    birthday_message(sevgilinin_ismi)
