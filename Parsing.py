import matplotlib.pyplot as plt

from Parsing import *

def showGraphs(currency, dataChosenCurrency):
    ratesDataGraph = []
    datesDataGraph = []
    calculationDataGraph(dataChosenCurrency, ratesDataGraph, datesDataGraph)

    ratesForecast = []
    datesForecast = []
    calculationForecast(currency, ratesForecast, datesForecast)

    plt.figure(figsize=(13,5))

    plt.subplot(1,2,1)
    plt.title('Data of date period')
    plt.xlabel('date')
    plt.ylabel('rate')
    plt.plot(datesDataGraph, ratesDataGraph, marker='o')

    plt.subplot(1,2,2)
    plt.title('Forecast')
    plt.xlabel('date')
    plt.ylabel('rate')
    plt.plot(datesForecast, ratesForecast, marker='o')

    
    plt.show()

def calculationDataGraph(dataChosenCurrency, rates, dates):
    for i in range(len(dataChosenCurrency) - 1, -1, -1):
        rates.append(dataChosenCurrency[i].rate)
        dates.append(dataChosenCurrency[i].date)

def calculationForecast(currency, rates, dates):
    dataChosenCurrencyLastDays = []

    amountLastDaysForForecast = 3
    dateFrom = datetime.date.today() - datetime.timedelta(days=amountLastDaysForForecast)
    dateTo = datetime.date.today()
    
    parsingChosenCurrency(currency, dataChosenCurrencyLastDays, dateFrom.strftime('%d.%m.%Y'), dateTo.strftime('%d.%m.%Y'))
    while len(dataChosenCurrencyLastDays) < 3:
        dateFrom -= datetime.timedelta(days=1)
        parsingChosenCurrency(currency, dataChosenCurrencyLastDays, dateFrom.strftime('%d.%m.%Y'), dateTo.strftime('%d.%m.%Y'))


    daysForecast = 5
    for i in range(daysForecast):
        dates.append((datetime.date.today() + datetime.timedelta(days=i)).strftime('%d.%m.%Y'))

    for i in range(daysForecast):
        rates.append(0)
        for j in range(i, len(dataChosenCurrencyLastDays)):
            rates[i] += dataChosenCurrencyLastDays[j].rate
        rates[i] /= amountLastDaysForForecast

        dataChosenCurrencyLastDays.append(Currency(dataChosenCurrencyLastDays[0].code,dataChosenCurrencyLastDays[0].unit,dataChosenCurrencyLastDays[0].title,rates[i],dataChosenCurrencyLastDays[0].date))