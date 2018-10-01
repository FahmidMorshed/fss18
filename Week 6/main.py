from testEngine import O
from unsuper import *

from num import Num
from sym import Sym
import sys, zipfile, codecs, re
from tabulate import tabulate
from data import Data

def addRow(data, cells):
    tempRows = []
    for i, use in data._use.items():
        if (use == True):
            x = cells[i]
            if ("?" not in x):
                if (data.nums.get(i, 0) != 0):
                    x = float(x)
                    data.nums.get(i).numInc(x)
                else:
                    data.syms.get(i).symInc(x)
            tempRows.append(x)
    data.rows.append(tempRows)


def lines(src=None, f=None):
    if src is None:
        # no string is given, read from standard input
        for line in sys.stdin:
            yield line
    elif src[-4:] == ".zip":
        # src ends with .zip, so unzip it first and then read
        # for zip, also give the filename inside the zip in arg f
        with zipfile.ZipFile(src, 'r') as z:
            with z.open(f, 'r') as f:
                for line in f:
                    yield codecs.decode(line, 'unicode_escape')
    elif src[-4:] in [".csv", ".dat"]:
        with open(src) as fs:
            for line in fs:
                yield line
    else:
        for line in src.splitlines():
            yield line


def rows(src):
    cache = []
    # the cache works nicely for joining with the next line
    for line in src:
        line = re.sub(r'([ \n\r\t]|#.*)', "", line)
        cache += [line]
        if len(line) > 0:
            if line[-1] != ",":
                line = ''.join(cache)
                cache = []
                yield line


def header(data, cells):
    for i, x in enumerate(cells):
        if "%?" not in x:
            data._use[i] = True
            data.name.append(x)
            if re.search(r"[<>$]", x):
                data.nums[i] = Num()
            else:
                data.syms[i] = Sym()

            if re.search(r"<", x):
                data.w[i] = -1
            elif re.search(r">", x):
                data.w[i] = 1
            elif re.search(r"!", x):
                data.clss = i
            else:
                data.indeps[i] = True
        else:
            data._use[i] = False


"""
Takes a csv file, reads through the data, creates the header and the rows using the Data object.
Then calculates the doms and sort them by the dom scores. Finally, prints the data.

Param:
    String csvFileName - name of the csv file to read data from

Return:
    Void
"""


def printResult(csvFilename):
    first = True
    data = Data()
    for x in rows(lines(csvFilename)):
        if (first):
            first = False
            header(data, x.split(","))
        else:
            addRow(data, x.split(","))

    print("#\tName\t\t n \t       mode \t       freq")
    for i, x in data.syms.items():
        print("%d   %15s \t %d \t %10s \t %10.2f" % (i, data.name[i], x.n, x.mode, x.most))
        # print(str(i) + "\t" + data.name[i][:7] + ".." + "\t" + str(x.n))

    print("\n#\tName\t\t n \t\t mu \t\t sd")
    for i, x in data.nums.items():
        print("%d   %15s \t %d \t %10.2f \t %10.2f" % (i, data.name[i], x.n, x.mu, x.sd))

    data.doms()

    data.rows.sort(key=sortByDom, reverse=True)

    for row in data.rows:
        row[-1] = round(row[-1], 2)

    unsuper(data)

    print("\n")
    decideAndPrint(data)


"""
Just a helper function for sort. Takes the last element of the row for comparing

Param:
    List row - the total row as a list item

Return:
    Float dom - last value of the list
"""


def sortByDom(row):
    return row[-1]


"""
Prints the data in tabular form. Decides if the table is large or not. If large, 
only prints the first 10 columns and the last 10 columns

Param:
    Data object having all the rows and names

Return:
    Void
"""


def decideAndPrint(data):
    if len(data.rows) < Config().maxRowsToPrint:
        print(tabulate(data.rows, headers=data.name))
        return
    newRows = data.rows[:10]
    dotRow = []
    for x in data.rows[0]:
        dotRow.append("-----")

    newRows.append(dotRow)
    for x in data.rows[0]:
        dotRow.append("-----")
    newRows.append(dotRow)

    newRows += data.rows[-10:]
    # print(newRows)
    print(tabulate(newRows, headers=data.name))
    return


@O.k
def test():
    print('=========Testing on "auto.csv"=============')
    printResult("input/weatherLong.csv")

    # print('\n\n')
    # print ('=========Testing on "weather.csv"==========')
    # printResult("weather.csv")

    print('\n\n')
    print('=======Testing on "weatherLong.csv"========')
    printResult("input/auto.csv")

    assert 1 == 1