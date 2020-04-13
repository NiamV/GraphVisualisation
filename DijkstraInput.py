def convert(fname):
    f = open(fname)
    data = f.readlines()
    iterations = []
    currentIter = []

    count = 0
    for x in data:
        count += 1
        if(x[0] == 'I'):
            if(len(currentIter) > 0):
                iterations.append(currentIter)
                currentIter = []
        else:
            if(len(x) > 0):
                toAdd = x.rstrip("\n")
                field = count % 7

                if(field == 2 or field == 3):
                    currentIter.append(int(x))

                elif(field == 4):
                    if x == "true\n":
                        currentIter.append(True)
                    else:
                        currentIter.append(False)

                elif(field == 5):
                    toAdd2 = toAdd.split()
                    for i in range(0, len(toAdd2)):
                        currentElem = toAdd2[i]
                        if currentElem == '2147483647':
                            toAdd2[i] = "\N{INFINITY}"
                        else:
                            toAdd2[i] = currentElem
                    currentIter.append(toAdd2)

                elif(field == 6):
                    toAdd2 = toAdd.split()
                    for i in range(0, len(toAdd2)):
                        currentElem = toAdd2[i]
                        if currentElem == '-1':
                            toAdd2[i] = "NIL"
                        else:
                            toAdd2[i] = int(currentElem)
                    currentIter.append(toAdd2)

    return iterations
