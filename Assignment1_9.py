
def even():
    for i in range(1,21):
        if (i%2==0):
            print(i, end='  ')

def main():
    print("Function to display first ten even numbers")
    even()

if __name__=="__main__":
    main()