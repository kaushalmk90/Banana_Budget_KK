# Functions to calculate budget, validate input parameters, and create get request are defined here


import requests
from datetime import datetime
from datetime import timedelta
from config.environment import ENDPOINTS

#url = "https://bananabudget.azurewebsites.net/"

def calculateBudget(startDate, numberOfDays):
    startDate = validateDate(startDate)
    numberOfDays = validateNumOfDays(numberOfDays)

    i = 0
    sum = 0
    while i < numberOfDays:
        if startDate.weekday() < 5:
            if startDate.day in range(1,8):
                sum = sum + 0.05
            elif startDate.day in range(8,15):
                sum = sum + 0.10
            elif startDate.day in range(15, 22):
                sum = sum + 0.15
            elif startDate.day in range(22, 29):
                sum = sum + 0.20
            else:
                sum = sum + 0.25

        startDate = startDate + timedelta(days=1)
        i = i+1

    return round(sum,2)

def validateDate(date):
    for fmt in ('%m-%d-%Y', '%m.%d.%Y', '%m/%d/%Y'):
        try:
            return datetime.strptime(date, fmt)
        except ValueError:
            pass
    raise ValueError("Invalid Date or Incorrect data format, should be MM-DD-YYYY or MM/DD/YYYY or MM.DD.YYYY")

def validateNumOfDays(num):
    try:
        if num in range(1,365):
            return num
    except ValueError:
        pass
    raise ValueError("Number of Days invalid")

#print(calculateBudget1("2/2/2017",100))

def getReq(startDate, numOfDays):
    payload = {'startDate': startDate, 'numberOfDays': numOfDays}
    #r = requests.get(url, params=payload)
    r = requests.get(ENDPOINTS['banana_budget'],params=payload)
    return r