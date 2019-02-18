# Author: Kaushal Kulkarni
# This file needs to be run to execute the test suite (python3 test.py)

import unittest
from core.calculateBudget import calculateBudget
from core.calculateBudget import getReq

# define startDate parameters
startDate = {
    1:"02-16-2019",
    2:"12-31-1990",
    3:"02-28-2016",
    4:"08/17/2019",
    5:"02-27-2019",
    6:"13-01-2018",
    7:""
}

# define  numOfDays parameters
numOfDays = {
    1:2,
    2:61,
    3:8,
    4:"a",
    5:366,
    6:"1a",
    7:""
}


class TestBananaBudget(unittest.TestCase):

    def testValidScenario(self):

        # This test makes sure Bob get the correct response when start date is on weekend

        date = startDate[1]
        days = numOfDays[1]
        r = getReq(date,days)
        try:
            self.assertEqual(r.status_code,200)
            # self.assertRaises(Exception) as context: broken_function()
        except:
            print('Failed to Connect. Response Code is not 200')
            exit(1)
        actualCost = float(r.json()['totalCost'].replace('$',''))
        expectedCost = calculateBudget(date, days)
        print('Total Cost returned by API',actualCost,' Expected Total Cost',expectedCost,'\n')
        self.assertEqual(actualCost,expectedCost)

    def testTwoMonths(self):

        # This test makes sure Bob get the correct response when date range covers a period of 61 days

        date = startDate[2]
        days = numOfDays[2]
        r = getReq(date, days)
        try:
            self.assertEqual(r.status_code, 200)
        except:
            print('Failed to Connect. Response Code is not 200')
            exit(1)
        actualCost = float(r.json()['totalCost'].replace('$',''))
        expectedCost = calculateBudget(date, days)
        print('Total Cost returned by API',actualCost,' Expected Total Cost.',expectedCost,'\n')
        self.assertEqual(actualCost,expectedCost)

    def testLeapYear(self):

        # This test makes sure Bob get the correct response when start date is Feb 28 in a leap year

        date = startDate[3]
        days = numOfDays[3]
        r = getReq(date, days)
        try:
            self.assertEqual(r.status_code, 200)
        except:
            print('Failed to Connect. Response Code is not 200')
            exit(1)
        actualCost = float(r.json()['totalCost'].replace('$',''))
        expectedCost = calculateBudget(date, days)
        print('Total Cost returned by API',actualCost,' Expected Total Cost',expectedCost,'\n')
        self.assertEqual(actualCost,expectedCost)

    def testInvalidDays(self):

        # This test tests the scenario when Bob enters a string as Number of Days

        date = startDate[4]
        days = numOfDays[4]
        r = getReq(date, days)
        try:
            print("Expected Response Code = 400"," Actual Response Code = ",r.status_code,'\n')
            self.assertEqual(r.status_code, 400)
        except:
            print('Failed. Response Code is not 400')
            exit(1)


    def testDayOutOfRange(self):

        # This test tests the scenario when Bob enters Number of Days > 365

        date = startDate[5]
        days = numOfDays[5]
        r = getReq(date, days)
        try:
            self.assertEqual(r.status_code, 200)
        except:
            print('Failed. Response Code is not 200')
            #exit(1)
        actualCost = float(r.json()['totalCost'].replace('$',''))
        expectedCost = calculateBudget(date, days)
        print('Total Cost returned by API',actualCost,' Expected Total Cost',expectedCost,'\n')
        self.assertEqual(actualCost,expectedCost)

    def testBothInvalidParams(self):

        # This test tests the scenario when Bob enters invalid Number of Days and an invalid Date

        date = startDate[6]
        days = numOfDays[6]
        r = getReq(date, days)
        try:
            print("Expected Response Code = 400", " Actual Response Code = ", r.status_code,'\n')
            self.assertEqual(r.status_code, 400)
        except:
            print('Failed. Response Code is not 400')



    def testBlankParams(self):

        # This test tests the scenario when Bob enters invalid Number of Days and an invalid Date

        date = startDate[7]
        days = numOfDays[7]
        r = getReq(date, days)
        try:
            print("Expected Response Code = 400", " Actual Response Code = ", r.status_code,'\n')
            self.assertEqual(r.status_code, 400)
        except:
            print('Failed. Response Code is not 400')


if __name__ == '__main__':
    unittest.main()

