from data import Data
from config import Config
from num import Num
from operator import itemgetter
import re
import math

def super(data):
    rows = data.rows
    goal = len(rows[1])-1
    enough = len(rows)**Config().superEnough
    most = 0

    cut_var_n = []
    col_split_val = []
    def band(c, lo, hi):
        """
        band takes the low and hi value along with the index and return the string to be printed

        Param:
            int c for index of rows
            int lo for the lowest cut
            int hi for the highest cut

        Return:
            String
        """
        if (lo == 0):
            return ".." + str(rows[hi][c])
        elif (hi == most):
            return str(rows[lo][c]) + ".."
        else:
            return str(rows[lo][c]) + ".." + str(rows[hi][c])


    def argmin(c, lo, hi):
        """
        finds the cut index for the min sd returns that. If cut is not found, returns None

        Param:
            int c for index of rows
            int lo for the lowest cut
            int hi for the highest cut

        Return:
            int cut index or None
        """

        mu = 0
        cut = None
        if (hi - lo > 2 * enough):

            xl = Num()
            xr = Num()
            yl = Num()
            yr = Num()


            for i in range(lo, hi + 1):
                xr.numInc(rows[i][c])
                yr.numInc(rows[i][goal])

            bestx = xr.sd
            besty = yr.sd
            mu = yr.mu

            for i in range(lo, hi + 1):
                x = rows[i][c]
                y = rows[i][goal]

                xl.numInc(x)
                xr.numDec(x)
                yl.numInc(y)
                yr.numDec(y)

                if (xl.n >= enough and xr.n >= enough):
                    tempx = Num.numXpect(xl, xr) * Config().superMargin
                    tempy = Num.numXpect(yl, yr) * Config().superMargin
                    if (tempx < bestx) and (tempy < besty):
                        cut = i
                        bestx = tempx
                        besty = tempy
        return cut, mu

    def cuts(c, lo, hi, pre):
        """
        calls the cut function recursively and gets the text to print

        Param:
            int c for index of rows
            int lo for the lowest cut
            int hi for the highest cut
            String pre for the text to print
        Return:
            Void
        """
        txt = pre + str(rows[lo][c]) + ".. " + str(rows[hi][c])
        cut,mu = argmin(c, lo, hi)

        if cut is not None:
            print(txt)
            cuts(c, lo, cut, pre + "|.. ")
            cuts(c, cut + 1, hi, pre + "|.. ")
        else:
            b = band(c, lo, hi)
            rounded_mu = math.floor(100*mu)
            print(txt + " ==> " + str(rounded_mu))
            if(rounded_mu > 0):
                cut_var_n.append((get_var(c, lo, hi), rounded_mu))
            for r in range(lo, hi + 1):
                rows[r][c] = b


    def get_var(c, lo, hi):
        numx = Num()
        for i in range(lo, hi + 1):
            numx.numInc(rows[i][goal])
        return (numx.sd)**2

    def stop(c, t):
        """
        ignores the undefined data and also calculates the most variable
       Param:
           int c for the index
           list c is the rows
       Return:
           int most

        """
        for i in range(len(t) - 1, -1, -1):
            if (t[i][c] != Config().garbageValue):
                return i
        return 0

    def splitter():
        n = 0
        split_val = 0
        for itm in cut_var_n:
            x, y = itm
            n += y
        for itm in cut_var_n:
            x, y = itm
            split_val += y/n*x

        return split_val

    for i in range(len(data.name)):
        if("$" in data.name[i]):
            data.name[i] = data.name[i].split("$")[1]

    for i, _ in data.indeps.items():
        cut_var_n = []
        if (data.nums.get(i, 0) == 0):
            continue

        for row in rows:
            if isinstance(row[i], str):
                row[i] = Config().garbageValue

        rows.sort(key=itemgetter(i))
        most = stop(i, rows)
        print("\n-- " + str(data.name[i]) + "---------")
        cuts(i, 0, most, "|.. ")
        col_split_val.append([i, round(splitter(), 4)])

    print ("\nSplitting Value:\n[columNum, expectedVal]")
    print(col_split_val)

