from CUser import CUser
import datetime


def payTotal(name):
    total = 0
    #print(name)
    l_file  = open('file/testCalculator.txt', 'r')
    for info in l_file:
        list = info.split(',')
        if list[0] == name:
            loanAmount = int(list[2])
            interestRate = float(list[3])
            loanTenor = int(list[4])
            payamount = (((loanAmount * (interestRate / 100) * loanTenor) + loanAmount) / (loanTenor * 12))
            twodpP = "%.2f" % payamount
            total += float(twodpP)


    print(total)
    return total

def processUser2(name):
    uList = []
    #print(name)
    l_file  = open('file/testCalculator.txt', 'r')
    for info in l_file:
        list = info.split(',')
        if list[0] == name:
            loanAmount = int(list[2])
            interestRate = float(list[3])
            loanTenor = int(list[4])
            extraInter = float(list[10])
            #print(list[3])
            year = int(list[7])
            month = int(list[8])
            date = int(list[9])

            payamount = (((loanAmount * (interestRate / 100) * loanTenor)+loanAmount)/(loanTenor*12))
            twodpP = "%.2f" %payamount
            totalpayable = (loanAmount * (interestRate / 100) * loanTenor)+loanAmount
            twodpT = "%.2f" %totalpayable
            #print(payamount)
            now = datetime.date.today()
            nowMonth = now.month
            todayDate = str(year)+ '-' + str(month) + '-' + str(date)
            pdate = datetime.date(year, nowMonth, date)
            printdate =  str(year)+ '-' + str(nowMonth) + '-' +str(date)
            #print(printdate)
            #print(now, 'now')
            if pdate<now:
                type = 'OverDue'
                daysLeft = 0
                extra = ((float(twodpP)*(extraInter/100))+ payamount)
                total = extra+float(twodpT)
                twodpT = '%.2f'%total
                print(twodpT)
                s = CUser(list[0], list[1], list[2], list[3], list[4], list[5], list[6], printdate,todayDate,daysLeft, twodpP,
                          twodpT, type)

            elif pdate == now:
                #print('hello')
                type = 'Due Today'
                daysLeft = 0
                s = CUser(list[0], list[1], list[2], list[3], list[4], list[5], list[6], printdate,todayDate, daysLeft, twodpP,
                          twodpT, type)

            else:
                type = 'Fine'
                daysLeft = (pdate - now).days
                #print('plab blah')
                s = CUser(list[0], list[1], list[2], list[3], list[4], list[5], list[6], printdate,todayDate, daysLeft, twodpP,
                          twodpT, type)

            uList.append(s)
    return uList

def overDueAmt(name):
    total = 0
    # print(name)
    l_file = open('file/testCalculator.txt', 'r')
    for info in l_file:
        list = info.split(',')
        if list[0] == name:
            loanAmount = int(list[2])
            interestRate = float(list[3])
            loanTenor = int(list[4])
            year = int(list[7])
            month = int(list[8])
            date = int(list[9])
            now = datetime.datetime.now()
            nowMonth = now.month
            extraInter = float(list[10])

            payamount = (((loanAmount * (interestRate / 100) * loanTenor) + loanAmount) / (loanTenor * 12))
            twodpP = "%.2f" % payamount
            # print(payamount)
            duedate = datetime.datetime(year, nowMonth, date)
            if duedate < datetime.datetime.now():
                type = 'OverDue'
                extra = (float(twodpP) * (extraInter / 100)) + payamount
                extraAmt = '%.2f' % extra
                total += float(extraAmt)
                return total

    print(total)
    return total

def reduceAfterpay(name,totalpayable,payamount):
    uList = []
    rAlist = []
    now = datetime.date.today()
    nowMonth = now.month
    #print(name)
    l_file  = open('file/testCalculator.txt', 'r')
    for info in l_file:
        list = info.split(',')
        year = int(list[7])
        month = int(list[8])
        date = int(list[9])
        printdate = datetime.date(year, nowMonth, date)
        todayDate = str(year) + '-' + str(month) + '-' + str(date)
        twodpP = payamount
        twodpT = float(totalpayable) - float(payamount)
        daysLeft = (printdate - now).days
        #print(payamount)
        newLine = list[0]+','+list[1]+','+list[2]+','+list[3]+','+list[4]+','+list[5]+','+list[6]+','+list[7]+','+list[8]+','+list[9]+','+list[10]+','+str(twodpT)+'\n'
        rAlist.append(newLine)
        s = CUser(list[0], list[1], list[2], list[3], list[4], list[5], list[6],printdate,todayDate, daysLeft,twodpP,
                  list[11], type)
        uList.append(s)

        newdata = name+','+ str(twodpP) +','+str(twodpT)+','+str(now)+'\n'
        writedata = open('file/trans.txt','a')
        writedata.write(newdata)
            
        userwrite_file = open('file/testCalculator.txt', 'w')
        for userwrite in rAlist:
            userwrite_file.write(userwrite)



def month_change(name):
    now = datetime.datetime.now()
    todayDate = str(now.day) + '-' + str(now.month) + '-' + str(now.year)
    nowMonth = now.month

    l_file  = open('file/testCalculator.txt', 'r')
    for info in l_file:
        list = info.split(',')
        if list[0] == name:
            year = int(list[7])
            month = int(list[8])
            date = int(list[9])
            dateDate = datetime.datetime(year,nowMonth,date)

            print(dateDate)
            return dateDate



#payAmount()
#payableAmount('John')
#info_loanAmount('John')
#datecall()
#month_change('John')
#reduceAfterpay('John',13160.20,215.67)
#processUser2('John')