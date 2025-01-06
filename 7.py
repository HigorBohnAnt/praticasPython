import os
import time
from random import randint

def rgb_show():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[1m🎨 Bem-vindo ao Show de Cores RGB! 🎨\033[0m")
    time.sleep(1)

    while True:
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        print(f"\033[38;2;{r};{g};{b}mEssa é uma cor incrível: RGB({r}, {g}, {b})!\033[0m")
        time.sleep(0.3)

try:
    rgb_show()
except KeyboardInterrupt:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("🌈 Show de cores encerrado! Até a próxima!")
