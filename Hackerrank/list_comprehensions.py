#receiving 3 int coordinates x, y and z, as well as a int n, print all the possibilities
#of the coordinates x, y and z for wich the sum of the combinations are different than n
#the coordinates combinations goes from 0 to the value defined by x, y and z

if __name__ == '__main__':
    x = int(input("x coordinate: "))
    y = int(input("y coordinate: "))
    z = int(input("z coordinate: "))
    n = int(input("value of n: "))

    coord_list = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
    print(coord_list)