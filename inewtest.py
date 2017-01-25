#!/usr/bin/python
import calendar
import datetime
import operator
import random

__author__ = "Ericson Joseph"
__email__ = "ericsonjoseph@gmail.com"

# Class Line
class Line:
    def __init__(self, date, msisdn, balance):
        self.date = date
        self.msisdn = msisdn
        self.balance = balance
        
    def display_line(self):
        print self.date.strftime("%Y-%m-%d %H:%M:%S") + "|" + str(self.msisdn) + "|" + str(self.balance)
        
    def to_string(self):
        return self.date.strftime("%Y-%m-%d %H:%M:%S") + "|" + str(self.msisdn) + "|" + str(self.balance)
   
# Class Line Factory
class LineFactory:
    
    msisdnList = []

    def _get_msisdn(self):
        self.low = 573192510000
        self.msisdn = self.low + random.randint(0,1000000)
        while self.msisdn in LineFactory.msisdnList:
            self.msisdn = self.low + random.randint(0,1000000)
        LineFactory.msisdnList.append(self.msisdn)
        return self.msisdn

    def _get_balance(self):
        return random.randint(0,100000);
      
    def _get_datetime(self):
        self.year = 2016
        self.month = random.randint(1, 12)
        weekday, end_day = calendar.monthrange(2016, self.month)
        self.day = random.randint(1, end_day)
        self.hour = random.randint(0, 23)
        self.minute = random.randint(0, 59)
        self.seg = random.randint(0, 59)
        date = datetime.datetime(self.year, self.month, self.day, self.hour, self.minute, self.seg, 123000)
        return date
   
    def get_line(self):
        line = Line(self._get_datetime(), self._get_msisdn(), self._get_balance())
        return line
       
    def print_msisdnlist(self):
        print LineFactory.msisdnList

# Init process
numOfLines = 100000

print "INIT GENERATOR file.txt"

# Create lines
lines = []
factory = LineFactory()
for x in range(0, numOfLines):
    line = factory.get_line()
    lines.append(line)

# Order lines
lines.sort(key=operator.attrgetter('date'), reverse=True)

# Write files in file
file = open("file.txt", "w")
file.write("fecha|msisdn|saldo\n")
for line in lines:
    file.write("%s\n" % line.to_string())

print "END GENERATOR file.txt"
