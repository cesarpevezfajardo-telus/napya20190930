#!/usr/bin/python3
### Zach show off shebang trick before this script ends
import sys

def main():
    # oldschool python way 2.7+
    myfile = open("example01.txt", "w")     # "w", "r", "a"
    print("Hola mundo", file=myfile, end="\n")
    myfile.write("Konnichiwa\n")
    myfile.close()

    with open("example02.txt", "w") as myfile:
        myfile.write("Salve mundi\n")
        print("Marhabaan bialealam", file=myfile)
        sys.stdout = myfile
        print("Does this work as well??")

if __name__ == "__main__":
    main()
