import os
import json
from rich import print

os.system("title quizly")

LOGO = """
             _     _       
  __ _ _   _(_)___| |_   _ 
 / _` | | | | |_  / | | | |
| (_| | |_| | |/ /| | |_| |
 \__  |\____|_/___|_|\__  |
    |_|              |___/ 
"""

cls = lambda: os.system("cls")

c = 0
w = 0
n = 0

def main():
    global c
    global w
    global n
    os.system("")
    print("[medium_purple1]" + LOGO + "[/medium_purple1]")
    jsonFile = input("JSON File: ")
    try:
        cls()
        with open(jsonFile, "r") as file:
            data = json.load(file)
        for item in data:
            print("[medium_purple1]" + item["question"] + "[/medium_purple1]")
            print("(A) - " + item["A"])
            print("(B) - " + item["B"])
            print("(C) - " + item["C"])
            print("(D) - " + item["D"])
            x = input(">>> ")
            print("")
            if x.casefold() == item["answer"].casefold():
                c += 1
                print("[green1]Correct Answer![/green1]")
                print("")
            elif x == "" or x.isspace():
                n += 1
                print("")
            else:
                w += 1
                print(f"[red3]Wrong Answer! The Correct Answer is {item['answer']}[/red3]")
                print("")
        print("[green1]Correct Answers:[/green1] " + str(c))
        print("[red3]Wrong Answers:[/red3] " + str(w))
        print("Unanswered Questions: " + str(n))
        os.system("pause >nul")  
    except FileNotFoundError:
        print("")
        print("[red3]File not found, press any key to try again.[/red3]")
        os.system("pause >nul")
        cls()
        return main()

if __name__ == "__main__":
    main()