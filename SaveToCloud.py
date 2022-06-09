import yadisk

yDisk = None

def saveAll(currencies, dataChosenCurrency):
    saveAllCurrency(currencies)
    saveHistoryOfCurrency(dataChosenCurrency)

def initDisk():
    global yDisk
    if yDisk == None:
        yDisk = yadisk.YaDisk(token='AQAAAABFRhaFAAfdcmmDZPATUEJcuHiawl9EqN4')

def saveAllCurrency(currencies):
    initDisk()
    saveAllCurrencyToFile(currencies)
    try:
        yDisk.remove('/AllCurrency.txt', permanently=True)
    except Exception:
        pass
    yDisk.upload('AllCurrency.txt', '/AllCurrency.txt')

def saveAllCurrencyToFile(currencies):
    f = open('AllCurrency.txt', 'w')

    try:
        for item in currencies:
            f.write(f'{item.code}\t{item.unit}\t{item.title}\t{item.rate} rub\t{item.date}\n')
    except Exception:
        print('Error')
    finally:
        f.close()

def saveHistoryOfCurrency(dataChosenCurrency):
    initDisk()
    saveHistoryOfCurrencyToFile(dataChosenCurrency)
    try:
        yDisk.remove(f'/{dataChosenCurrency[0].code}.txt', permanently=True)
    except Exception:
        pass
    yDisk.upload(f'{dataChosenCurrency[0].code}.txt', f'/{dataChosenCurrency[0].code}.txt')

def saveHistoryOfCurrencyToFile(dataChosenCurrency):
    f = open(f'{dataChosenCurrency[0].code}.txt', 'w')

    try:
        f.write('Date\t     Unit\tRate (rub)\n')
        for item in dataChosenCurrency:
            f.write(f'{item.date}\t{item.unit}\t{item.rate}\n')
    except Exception:
        print('Error')
    finally:
        f.close()