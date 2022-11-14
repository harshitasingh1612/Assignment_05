#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# Harshita Singh, 2022-Nov-11, Modified File
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of dict to hold data
dictRow = {}  # dict of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        #  Exit the program if the user chooses so
        break

    if strChoice == 'l':
        # loading existing data from file to in-memory
        lstTbl.clear()
        with open(strFileName,'r') as f:
            for line in f.readlines():
                val = line.strip().split(',')
                dictRow = {'ID':int(val[0]), 'Title':val[1], 'Artist':val[2]}
                lstTbl.append(dictRow)

    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        #  Add data to the table (2d-list) each time the user wants to add data
        intID = int(input('Enter an ID: '))
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        dictRow = {'ID': intID, 'Title': strTitle, 'Artist':strArtist}
        lstTbl.append(dictRow)

    elif strChoice == 'i':
        #  Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ')

    elif strChoice == 'd':
        # delete CD from inventory based upon the user data
        key_to_be_deleted = int(input("Enter the CD you want to delete: "))
        index = -1
        for idx, line in enumerate(lstTbl):
            # if the ley matches with the user key, then delete the data from list of dict
            if key_to_be_deleted == line['ID']:
                index = idx
                break
        if index != -1:
            lstTbl.pop(index)
              
    elif strChoice == 's':
        #  Save the data to a text file CDInventory.txt if the user chooses so
        with open(strFileName, 'w') as f:
            for row in lstTbl:
                val = ''
                for item in row.values():
                    val += str(item) + ','
                val = val[:-1] + '\n'
                f.write(val)

    else:
        print('Please choose either l, a, i, d, s or x!')

