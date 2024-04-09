import sys
import os

def rens_terminal():
    if sys.platform == "Windows":
        os.system("cls")
    else:
        os.system("clear")

print(" -- Velkommen til Quiz -- ")

while True:
    rens_terminal()
    print(" Hvor mange studioalbum har The Beatles? ")
    print("1 - 13")
    print("2 - 14")
    print("3 - 15")
    print("4 - 16")
    brukervalg = input("> ")

    if brukervalg == "1":
        print(" RIKTIG")
    else:
        print("FEIL")

    break
