#!/ust/bin python3
def triangle(height):
    for i in range(1,height+1):
        print(" "*(height-i)+" *"*(i))

def elgnairt(height):
    for i in range(1,height+1):
        print(" "*(i)+"* "*(height-i+1))

if __name__ == "__main__":
    n = int(input("Please input the height of the pyramid: "))
    triangle(n)
    elgnairt(n)
