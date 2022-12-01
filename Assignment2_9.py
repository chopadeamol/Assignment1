def digit(num):
    if num:
        print("Number of digits in the numbers are :", int(len(num)))

def main():
    print("Count of digits in the entered number")
    no=input()
    digi=digit(no)

if __name__=="__main__":
    main()