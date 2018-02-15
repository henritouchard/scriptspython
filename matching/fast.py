import csv
import sys
import os


## As the explicit name of this function explains : the aim of this function is to import content of the csv file data.csv
## it returns a list where each part is an array of characteristics
def importCSV(name):
    with open(name) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        data = list(readCSV)
        row_count = len(data)
        people = [None] * len(data)
        it = 0
	print "hello"
        for i in data:
            people[it] = i
            it += 1
    return people

################################################### CSV handeling END #################################################

## This global variables just allow to simplify reading of the code.
## (I know : we will lose juste a bit of efficiency but it will clearly be easier to read and understand code)
index = {'UID': 0, 'Sex': 1, 'Birth': 2, 'Children' : 3, 'Religion': 4, 'environnement': 5, 'Politic': 6, 'reading': 8, 'lovLang' : 9 , 'job' : 12 , 'extraversion' : 20 ,'sSex': 32, 'sReligion' : 33 , 'sEnvironnement' : 34 , 'Wish': 38, 'WishValue': 39}


# this function search in the maching area of lovers (different sex and corresponding to most important expectation)
def getCandidateRate(client, match):
    # this condition allow to set client's sexual orientation and propose him only people which correspond to it
    if match[index['Sex']] != client[index['sSex']] or match[index['sSex']] != client[index['Sex']]:
        return 0

    #we considere that 5 years age difference isn't a big deal
    if abs(int(client[index['Birth']])- int(match[index['Birth']])) < 5:
        return 0

    # if one want children and the other not we won't propose this match
    if match[index['Children']] != client[index['Children']]:
        return 0

    rank = 0

    # A hight part of people considere as hard to be with someone with a different religion
    # because of life thinking and family. That's why we give a particular rate for it
    # for this reason we chose to give lot of points if the religions are the same
    if client[index['sReligion']] == match[index['Religion']]:
        rank += 150

    # this loop will iterate in important caracteristics and check if it's the same
    clientIdx = index['sEnvironnement']
    matchIdx = index['environnement']
    while matchIdx < index['lovLang']:
        if client[clientIdx] == match[matchIdx]:
            rank += 40
        matchIdx += 1
        clientIdx += 1

    #special price
    if match[int(client[index['Wish']])] == client[index['WishValue']]:
        rank += 15

    # this loop will iterate in less important caracteristics and check if it's the same
    while matchIdx < index['job']:
        if client[matchIdx] == match[matchIdx]:
            rank += 10
        matchIdx += 1

    # this loop will iterate in almost not important caracteristics at all and check if it's the same
    while matchIdx < index['extraversion']:
        if client[matchIdx] == match[matchIdx]:
            rank += 3
        matchIdx += 1

    # About qualities rates we considere that this is not because you are shy that you want a shy love
    # that's why we add each rates value as a small part of global rating.
    # What's more, we considere that all life's aim, especially in love is to become better where we are not.
    # Each quality is rated from 0 to 20, the rank result is given by rate / 10
    while matchIdx < 32:
        rank += int(match[matchIdx])/10
        matchIdx += 1
    return rank

# This function allow to iterate on each candidate for one client
def findSomeLovers(client, people):
    StandardWish = int(client[index['Wish']])
    standardValue = client[index['WishValue']]
    winnerVal = 0
    winner = -1
    ## this loop iterates on the array of clients, try to find someone corresponding to wishes and fill the array criteria with people who match with criteria asked
    for love in people:
        # if unique id is the same so we would compare someone with himself which makes no sense
        if client[index['UID']] == love[index['UID']]:
            continue
        ## this condition eliminates candidates which doesn't correspond to the special wish if there is
        # if love[StandardWish] == standardValue or StandardWish == 0:
        ## if we are here so love guy correspond a bit to the wishes of the client
        tmpVal = getCandidateRate(client, love)
        # if matching value is upper, the canidate is the best matched at the moment
        if tmpVal > winnerVal:
            winnerVal = tmpVal
            winner = int(love[index['UID']])
            # A big difference between fast and good, except for the precision is that if the rank reach 170 we considère it as a good maching and allow to stop search and take this one as a winner
            if winnerVal >= 220:
                break
    # Every data are randomely generated. with hasard i let this case which
    # will write "NONE" instead of winner unique id in file result.csv
    if winner == 0:
        return -1
    else :
        return winner

#####################################################################################################################
################################################## MAIN #############################################################
#####################################################################################################################
# check if usage as been respected and exit if it's not
if len(sys.argv) < 2:
    print("Usage : python3 fast.py [name of input file]")
    sys.exit()
dataFile = sys.argv[1]
#check if file exits
if os.path.isfile(dataFile):
    people = importCSV(dataFile)
else:
    print("Error : File doesn't exit")
    sys.exit()

# for faster maching algorythme we could considere that if x match y, so y match x
# but as i decided to considere as really important the choice of our clients, i won't take this method but choose to give theme only people who matches there wishes
# the only way it wouldn't be the case will be in case there would not be anyone who fill creteria asked. in this case only we propose someone close to criterias.
# w, h = 40, 1000
# criteria = [[0 for x in range(w)] for y in range(h)]
## this loop iterates on the array of clients interpreting their wishes
with open("result.csv", 'w') as data:
    result = csv.writer(data, delimiter=';')
    if result != -1 :
        for client in people:
            winner = findSomeLovers(client, people)
            if winner != -1:
                result.writerow([client[0], people[winner][0]])

                ## if you want comparison between two people directly written in the result file comment line above
                ## and uncoment next three lines
                # result.writerow(client)
                # result.writerow(people[winner])
                # result.writerow([""])

            # this line allow to write errors if there was no maching
            else :
                result.writerow(["NONE"])
