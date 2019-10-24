#labtest 1
#Pascals triangle
#Jake Bolger C18395341

#Part 1 and Part 2
def make_new_row(old_row): #function

    #declaring first row as [1] etc.
    First_row = [1]
    Second_row = [1, 1]

    #declaring Triangle_master
    Triangle_master = [First_row, Second_row]

    # row = []
    r = []

    #if user inputs 1
    if old_row == 1:
        First_row[0] = str(First_row[0])

        #output will be 1
        print(' '.join(First_row))
    #if user inputs 2
    elif old_row == 2:
        for j in Triangle_master:
            for a in range(len(j)):
                j[a] = str(j[a])

            #output will be [1,1]
            print((' ')*(2-(a+1)), (' '.join(j)))
    else:
        #for numbers above 1 and 2
        for i in range(2, old_row):
            Triangle_master.append([1]*i)
            for n in range(1, i):
                Triangle_master[i][n] = (Triangle_master[i-1][n-1]+Triangle_master[i-1][n])
            Triangle_master[i].append(1)

        for x in range(len(Triangle_master)):
            for y in Triangle_master[x]:
                s = str(y)
                r.append(s)
            print((' ')*(old_row-(x+1)), (' ' .join(r)))
            r = []

#taking the users input of rows entered
old_row = int(input("Enter the amount of rows you wish to have"))

#passing function
make_new_row(old_row)