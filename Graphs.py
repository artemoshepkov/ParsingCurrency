from bs4 import BeautifulSoup
import requests
from datetime import timedelta
import datetime

from Currency import *

def parsingAllCurrencies(currencies):
    pageCurrency = requests.get('https://cbr.ru/currency_base/daily/?UniDbQuery.Posted=True&UniDbQuery.To=' + str(datetime.date.today())) 

    soup = BeautifulSoup(pageCurrency.text, 'html.parser')

    allCurrencies = soup.find('table', class_='data').find_all('td')

    for i in range(1, len(allCurrencies) - 2, 5):
        currencies.append(Currency(allCurrencies[i].text, allCurrencies[i + 1].text, allCurrencies[i + 2].text, allCurrencies[i + 3].text))

def findOptionValue(title):
    page = requests.get('https://cbr.ru/currency_base/dynamics/')

    soup = BeautifulSoup(page.text, 'html.parser')

    optionsValues = soup.find('label', class_='input_label').find_all('option')

    for item in optionsValues:
        if item.text.strip() == title:
            return item.get('value')

    return 0

def parsingChosenCurrency(chosenCurrency, dataChosenCurrency, periodFrom, periodTo):

    if chosenCurrency == None:
            return -1

    optionValue = findOptionValue(chosenCurrency)

    if optionValue == 0:
        return -1

    page = requests.get('https://cbr.ru/currency_base/dynamics/?UniDbQuery.Posted=True&UniDbQuery.so=1&UniDbQuery.mode=1&UniDbQuery.date_req1=&UniDbQuery.date_req2=&UniDbQuery.VAL_NM_RQ=' + optionValue + '&UniDbQuery.From=' + periodFrom + '&UniDbQuery.To=' + periodTo)

    soup = BeautifulSoup(page.text, 'html.parser')

    allData = None
    try:
        allData = soup.find('table', class_='data').find_all('td')
    except:
        print("No data for this period")
        return -1

    dataChosenCurrency.clear()
    for i in range(1, len(allData) - 2, 3):
        dataChosenCurrency.append(Currency(chosenCurrency, allData[i + 1].text, chosenCurrency.title, allData[i + 2].text, allData[i].text))

    return 0
