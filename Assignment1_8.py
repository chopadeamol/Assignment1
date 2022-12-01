def starred(star1):
    for i in range(star1):
        print("*", end='  ')

def main():
    print("Function to enter number star ")
    star=int(input())
    starred(star)

if __name__=="__main__":
    main()