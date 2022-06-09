import datetime

class Currency(object):
    def __init__(self, code, unit, title, rate, date=datetime.date.today()):
        self.code = code
        self.unit = unit
        self.title = title
        self.date = date
        
        if isinstance(rate, str):
            rate = rate.replace(',', '.')
        self.rate = float(rate)

    def showInfo(self):
        print(self.code, self.unit, self.title, self.rate)

    def showInfoTable(self):
        print(self.date, self.unit, self.rate, sep='    ')

def convertCurrencies(currencies, codeFirstCurrency, codeSecondCurrency):
    firstCurrency = None
    secondCurrency = None
    for item in currencies:
        if item.code == codeFirstCurrency:
            firstCurrency = item
        if item.code == codeSecondCurrency:
            secondCurrency = item

    if firstCurrency == None or secondCurrency == None:
        print("Error. Invalid codes")
        return

    print(codeFirstCurrency, 'to', codeSecondCurrency, '=', firstCurrency.rate / secondCurrency.rate)

def showCurrencies(currencies):
    for item in currencies:
        item.showInfo()

def showTableChosenCurrency(dataChosenCurrency):
    print('--------------------------')
    print('Date         Unit   Rate')
    for item in dataChosenCurrency:
        item.showInfoTable()
    print('--------------------------')