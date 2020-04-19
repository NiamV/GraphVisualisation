def graphInput(fname):
    f = open(fname)
    data = [ x.rstrip("\n") for x in f.readlines() ]

    mat = []

    for row in data:
        rowMat = []
        rowSplit = row.split(" ")
        for elem in rowSplit:
            if elem == 'MAX':
                rowMat.append("MAX")
            else:
                rowMat.append(int(elem))
        mat.append(rowMat)

    return mat