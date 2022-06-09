import os

from Currency import *
from Parsing import *
from Graphs import *
import SaveToCloud as sc

currencies = []
dataChosenCurrency = []

def menu():
    chosenCurrency = None

    while(True):
        os.system('cls')

        print('1 - Show all currencies')
        print('2 - Choose currency')
        print('3 - Save to YANDEX')
        valueMenu = input()

        os.system('cls')

        if valueMenu == '1':
            showCurrencies(currencies)
            convertCurrencyMenu()

        elif valueMenu == '2':
            chooseCurrencyMenu()
        elif valueMenu == '3':
            saveToYandexMenu()
        else:
            print("Error")

def convertCurrencyMenu():
    while(True):
        print('--------------------')
        print('1 - Convert currency')
        print('2 - Exit to menu')
        valueMenu = input()
        print('--------------------')
        if valueMenu == '1':
            print('Choose currencies (example: USD EUR)')
            print('From')
            codeFirstCurrency = input()
            print('To')
            codeSecondCurrency = input()
            convertCurrencies(currencies, codeFirstCurrency, codeSecondCurrency)

        elif valueMenu == '2':
            break

def chooseCurrencyMenu():
    showCurrencies(currencies)
    print('--------------------------------------')
    while(True):
        print('Type title of currency')
        chosenCurrency = input()
        print('Type time period (example: "From 20.04.2022 to 26.04.2022")')
        print('From')
        periodFrom = input()
        print('To')
        periodTo = input()

        if parsingChosenCurrency(chosenCurrency, dataChosenCurrency, periodFrom, periodTo) == 0:
            showTableChosenCurrency(dataChosenCurrency)
            break
        else:
            print('Error')
    print('To continue, close the winddow with graphs')
    showGraphs(chosenCurrency, dataChosenCurrency)

def saveToYandexMenu():
    while(True):
        print('1 - save all currency')
        print('2 - save history of chosen currency (only when currency was selected)')
        print('3 - save all currency and history of chosen currency (only when currency was selected)')
        print('4 - exit to main menu')
        valueMenu = input()
        os.system('cls')
        if valueMenu == '1':
            sc.saveAllCurrency(currencies)
        elif valueMenu == '2':
            if len(dataChosenCurrency) > 0:
                sc.saveHistoryOfCurrency(dataChosenCurrency)
            else:
                print('Error. Only when the currency was selected')
        elif valueMenu == '3':
            if len(dataChosenCurrency) > 0:
                sc.saveAll(currencies, dataChosenCurrency)
            else:
                print('Error. Only when the currency was selected')
        elif valueMenu == '4':
            break
                
def main():
    parsingAllCurrencies(currencies)
    menu()   


if __name__ == "__main__":
    main()
