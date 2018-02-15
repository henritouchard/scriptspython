import csv
import sys
import os
import os.path


## As the explicit name of this function explains : the aim of this function is to import content of the csv file data.csv
## it returns a list where each part is an array of characteristics
def importCSV(name):
    with open(name) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        data = list(readCSV)
        row_count = len(data)
        people = [None] * len(data)
        it = 0
        for i in data:
            people[it] = i
            it += 1
    return people

################################################### CSV handeling END #################################################

## This global variables just allow to simplify reading of the code.
## (I know : we will lose juste a bit of efficiency but it will clearly be easier to read and understand code)
index = {'UID': 0, 'Sex': 1, 'Birth': 2, 'Children' : 3, 'Religion': 4, 'Env': 5, 'Politic': 7, 'Stud': 8, 'lovLang' : 9 , 'job' : 12 , 'extraversion' : 20 ,'sSex': 32, 'sReligion' : 33 , 'sEnvironnement' : 34 , 'Food' : 35, 'Wish': 38, 'WishValue': 39}
Religions = ["Catholicism", "Orthodox", "Anglicanism", "Protestantism", "Judaism" , "Islam",  "Gnosticism", "Deism", "Atheism",  "Buddhism", "Hinduism"]
Politics = ["FN", "SIEL", "LR", "RUMP", "UDI", "MoDem", "PS", "EELV", "PG", "PRG"]
Environnement = ["Capital", "Big City", "town near big cities", "countryside near big cities", "Deep countryside"]

###################################################### get[Category]Rate ################################################
## theses functions allow to attribute a rate for each parametre, considering their importance.
## the model is simple i check the distance between datas in the arrays and determmine when possible a value to closeness

# A hight part of people considere as hard to be with someone with a different religion
# because of life thinking and family. That's why we give a particular rate for it
# for this reason i chose to give lot of points if the religions are the same, and
# some points if they are close enough

def getReligionRate(clientR, matchR):
    cIdx = 0
    mIdx = 0
    for i in Religions:
        if i == clientR:
            break
        cIdx += 1
    for n in Religions :
        if n == matchR:
            break
        mIdx += 1
    rate = abs(cIdx-mIdx)
    if rate < 2 :
        rate = 150

    elif rate > 5 :
        rate = 0
    else :
        rate = 30
    return rate

## Attribute rate in function of environnement wher they want to live
def getEnvironementRate(clientE, matchE) :
    cIdx = 0
    mIdx = 0
    for i in Environnement:
        if i == clientE:
            break
        cIdx += 1
    for n in Environnement :
        if n == matchE:
            break
        mIdx += 1
    rate = abs(cIdx-mIdx)
    if rate < 2 :
        rate = 40
    elif rate > 4 :
        rate = 0
    elif rate < 3 :
        rate = 20
    return rate

## Attribute rate in function of their political ideas closeness
def getPoliticRate(clientP, matchP):
    cIdx = 0
    mIdx = 0
    for i in Politics:
        if i == clientP:
            break
        cIdx += 1
    for n in Politics :
        if n == matchP:
            break
        mIdx += 1
    rate = abs(cIdx-mIdx)
    if rate < 2 :
        rate = 40
    elif rate > 5 :
        rate = 0
    else :
        rate = 15
    return rate

## Attribute rate in function of their study level
def getStudiesRate(clientS, matchS):
    rate = abs(int(clientS)-int(matchS))
    if rate < 2 :
        rate = 30
    elif rate > 5 :
        rate = 0
    else :
        rate = 15
    return rate

############################################### End of functions get[Category]Rate #######################################

## this function search in the maching area of lovers (different sex and corresponding to most important expectation)
def getCandidateRate(client, match):
    # this condition allow to set client's sexual orientation and propose him only people which correspond to it
    if match[index['Sex']] != client[index['sSex']] or match[index['sSex']] != client[index['Sex']]:
        return 0
    # we considere that 5 years age difference isn't a big deal
    if abs(int(client[index['Birth']])- int(match[index['Birth']])) < 5:
        return 0
    # if one want children and the other not we won't propose this match
    if match[index['Children']] != client[index['Children']]:
        return 0
    #this variable aggragates every rates attributed in functions of candidates's caracteristics
    rank = 0
    # return a rate between 0 and 150
    rank += getReligionRate(client[index['sReligion']], match[index['Religion']])
    # return a rate between 0 and 40
    rank += getEnvironementRate(client[index['sEnvironnement']], match[index['Env']])
    # return a rate between 0 and 40
    rank += getPoliticRate(client[index['Politic']], match[index['Politic']])
    # return a rate between 0 and 30
    rank += getStudiesRate(client[index['Stud']], match[index['Stud']])

    # all is easier when we can eat the same things
    if match[index['Food']] == client[index['Food']] :
        rank += 50

    # this special rate is given in case where candidates get an important caracteristic for the client
    if match[int(client[index['Wish']])] == client[index['WishValue']]:
        rank += 40

    # this two loops allow to attribute a rank for each less important caracteristics
    matchIdx = index['lovLang']
    while matchIdx < index['job']:
        if client[matchIdx] == match[matchIdx]:
            rank += 10
        matchIdx += 1
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
    winnerVal = 0
    winner = -1

    ## this loop iterates on the array of clients, try to find someone corresponding to wishes and fill the array criteria with people who match with criteria asked
    for love in people:
        # if unique id is the same so we would compare someone with himself which makes no sense
        if client[index['UID']] == love[index['UID']]:
            continue

        # With this function each candidate will be attributed a rank. We will only accept this winner
        tmpVal = getCandidateRate(client, love)

        # if new candidate value is upper than previous candidates tested,
        # the candidate is the best matched at the moment
        if tmpVal > winnerVal:
            winnerVal = tmpVal
            winner = int(love[index['UID']])
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

# for faster maching algorythme we could considere that if x match y, so y match x and try to group people by similarity
# but as i decided to considere as really important the choice of our clients, i won't take this method but choose to
# give theme only people who matches as closely as possible there wishes.

# this line open our result csv file to write every data on it
with open("result.csv", 'w') as data:
    result = csv.writer(data, delimiter=';')
    if result != -1 :
        ## this loop iterates on the array of clients interpreting their wishes
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
