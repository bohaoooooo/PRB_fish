import os
from pathlib import Path

def GetLabelNum(pathName) :
    
    for imgName in sorted(os.listdir(pathName)) :
        if '.JPG' in imgName or '.jpg' in imgName :
            labelTxt = imgName[:-4] + '.txt'
            f = open(os.path.join(pathName, labelTxt))

            fish = False

            for line in f.readlines() :
                if line[0] == '0' or line[0] == '2' :
                    fish = True
            
            f.close()

            if fish == True :
                f = open('data/fish/true_result.txt', 'a')
                result = imgName + '\n'
                f.write(result)
                f.close()
            else :
                f = open('data/fish/false_result.txt', 'a')
                result = imgName + '\n'
                f.write(result)
                f.close()


if __name__ == '__main__' :
    pathName = './data/fish'
    GetLabelNum(pathName)
    print("\nComplete Classification !")

    posGt = []
    negGt = []
    posRes = []
    negRes = []

    f = open('./data/fish_true.txt')
    for line in f :
        posGt.append(line)

    f.close()

    f = open('./data/fish/true_result.txt')
    for line in f :
        posRes.append(line)

    f.close()

    f = open('./data/fish_false.txt')
    for line in f :
        negGt.append(line)

    f.close()

    f = open('./data/fish/false_result.txt')
    for line in f :
        negRes.append(line)

    f.close()


    correctNum = 0 

    for pos in posRes :
        if pos in set(posGt) :
            correctNum += 1

    for neg in negRes :
        if neg in set(negGt) :
            correctNum += 1

    print("Accuracy : " + str((correctNum/300.0) * 100) + "%")