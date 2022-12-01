def star(num):
    for i in range(num):
        for j in range(num):
            print("*", end='  ')
        print()

def main():
    print("Function to print pattern star")
    no=int(input())
    star(no)

if __name__=="__main__":
    main()