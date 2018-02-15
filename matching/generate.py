import csv
import sys
from random import randint
# this function is used to import csv files data and store it in memory
# it will return a bidirectional array of string containing each possible
# caracteristics
def readCSV() :
    # Creates a list containing 40 lists, each of 60 items, all set to 0
    cat, car = 60, 38
    caract = [[0 for x in range(cat)] for y in range(car)]
    with open('caract.csv', encoding='utf-8') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        it = 0
        for i in readCSV:
            idx = 0
            for x in i :
                caract[idx][it] = x
                idx += 1
            it += 1
        return caract

#counter allow to give the random number maximum
def counter(tab) :
    cnt = 0
    for i in tab :
        if i == '':
            break
        cnt+=1
    if cnt == 1 and tab[0] == "20":
        cnt = 0
    #print(cnt)
    cnt -= 1
    return cnt

# this function create a list of people with caracteristics taken randomely in csv file
def genPeople(caract) :
    #print(len(caract))
    #sys.exit()
    caracteristics, peopleNum = 40 , 1000
    people = [[0 for x in range(caracteristics)] for y in range(peopleNum)]
    pidx = 0
    while pidx < peopleNum :
        persCol = 0
        #i is the column of caracteristics so i[x] is one characteristic in particular theme
        for i in caract :
            #generate a random number n range of the number of different possible caracteristics
            maximumValue = counter(i)
            #print("max = ", maximumValue, "v")
            # 0 index is reserved to the unique id
            if persCol == 0:
                people[pidx][persCol] = pidx
                persCol +=1
            ##this condition allow to give preference of the users.
            ## i take a random number which shows what category is important for the client.
            ## and attribute next column to the value the client wants.
            if persCol >= 38:
                # choice can't be 0 because of unique id field, and cannot be higher than 37 because it's the choice himself
                choice = randint(9,19)
                people[pidx][persCol] = choice
                #count the possible number of different values
                MaximumChoiceValue = counter(caract[choice-1])
                # if MaximumChoiceValue is -1 the rand range is always a rate between 0 or 20
                if MaximumChoiceValue != -1:
                    rd = randint(0, MaximumChoiceValue)
                    people[pidx][persCol + 1] = caract[choice-1][rd]

                # if MaximumChoiceValue is -1 the rand range is always a rate between 0 or 20
                else:
                    people[pidx][persCol + 1] = randint(0, 20)

            #introduce some exceptions about religion wishes
            elif persCol > 32:
                #introduce some exceptions in religion
                if persCol == 33:
                    if pidx % 14 == 0 :
                        rand = randint(0, maximumValue)
                        people[pidx][persCol] = i[rand]
                    else :
                        people[pidx][persCol] = people[pidx][4]
                else:
                    people[pidx][persCol] = people[pidx][persCol - 29]
            # all cases
            else :
                if maximumValue != -1 :
                    rand = randint(0, maximumValue)
                    #print ("RAND= ",rand, i[rand], i)
                    people[pidx][persCol] = i[rand]
                # if MaximumChoiceValue is -1 the rand range is always a rate between 0 or 20
                else :
                    people[pidx][persCol] = randint(0, 20)
            persCol += 1
        pidx += 1
    return people

#generate the csv file containing each people
def genfile(people):
    with open("data.csv", 'w', newline='\n', encoding='utf-8') as data:
        wr = csv.writer(data, delimiter=';')
        uniqueId = 0
        for i in people:
            wr.writerow(i)
            uniqueId += 1

caract = readCSV()
people = genPeople(caract)
genfile(people)
