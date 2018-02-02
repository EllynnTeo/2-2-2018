class CUser():
    def __init__(self,name,loanId,amount, interestRate, years, monthsPaid, loanName, dueDate, startDate, daysLeft,
                  payamount, totalpayable, overdate):
        self.__name = name
        self.__loanId = loanId
        #self.__month = month
        #self.__type = type
        self.__amount = amount
        self.__interestRate = interestRate
        self.__years = years
        self.__monthsPaid = monthsPaid
        self.__loanName = loanName
        self.__dueDate = dueDate
        self.__startDate = startDate
        self.__daysLeft = daysLeft
        self.__payamount = payamount
        self.__totalpayable = totalpayable
        self.__overDate = overdate
        #self.__extraAmt = extraAmt

   # def __str__(self):
    #    return self.get_payamount()

    def get_name(self):
        return self.__name
    def get_loanId(self):
        return self.__loanId
    '''
    def get_month(self):
        return self.__month
    def get_type(self):
        return self.__type
        '''
    def get_amount(self):
        return self.__amount
    def get_interestRate(self):
        return self.__interestRate
    def get_years(self):
        return self.__years
    def get_monthsPaid(self):
        return self.__monthsPaid
    def get_loanName(self):
        return self.__loanName
    def get_dueDate(self):
        return self.__dueDate
    def get_startDate(self):
        return self.__startDate
    def get_daysLeft(self):
        return self.__daysLeft
    def get_payamount(self):
        return self.__payamount
    def get_totalpayable(self):
        return self.__totalpayable
    def get_overdate(self):
        return self.__overDate
   # def get_extraAmt(self):
    #    return self.__extraAmt

    def set_name(self, name):
        self.__name = name
    def set_loanId(self,loanId):
        self.__loanId = loanId
        '''
    def set_month(self, month):
        self.__month = month
    def set_type(self, type):
        self.__type = type
        '''
    def set_amount(self, amount):
        self.__amount = amount
    def set_interestRate(self, interestRate):
        self.__interestRate = interestRate
    def set_year(self, year):
        self.__year = year
    def set_monthsPaid(self, monthsPaid):
        self.__monthsPaid = monthsPaid
    def set_loanName(self, loanName):
        self.__loanName = loanName
    def set_dueDate(self, dueDate):
        self.__dueDate = dueDate
    def set_startDate(self,startDate):
        self.__startDate = startDate
    def set_daysLeft(self, daysLeft):
        self.__daysLeft = daysLeft
    def set_payamount(self, payamount):
        self.__payamount = payamount
    def set_totalpayable(self,totalpayable):
        self.__totalpayable = totalpayable
    def set_overdate(self,overdate):
        self.__overDate = overdate
  #  def set_extraAmt(self,extraAmt):
   #     self.__extraAmt = extraAmt

