

#!/usr/bin/python
import csv
import random
import time

def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%m/%d/%Y %I:%M %p', prop)

records = 100000
print("Making %d records\n" % records)

fieldnames = ['id', 'Context', 'Sentiment Score', 'Operator', 'Circle', 'Channel', 'Date']
writer = csv.DictWriter(open("people.csv", "w"), fieldnames = fieldnames)

operators = ['Airtel', 'Vodafone-Idea', 'BSNL', 'Jio', 'Aircel', 'Reliance', 'Telenor', 'Docomo', 'MTS', 'MTNL']
circles = ['Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Goa','Gujarat','Haryana',
	'Himachal Pradesh','Jammu & Kashmir','Karnataka','Kerala','Madhya Pradesh','Maharashtra',
	'Manipur','Meghalaya','Mizoram','Nagaland','Orissa','Punjab','Rajasthan','Sikkim','Tamil Nadu',
	'Tripura','Uttar Pradesh','West Bengal','Chhattisgarh','Uttarakhand','Jharkhand','Telangana']
contexts = ['Data', 'Calls', 'Roaming', 'Charges', 'VAS', 'Customer Support']
channels = ['Facebook', 'Twitter', 'Instagram', 'LinkedIn']

writer.writerow(dict(zip(fieldnames, fieldnames)))
for i in range(0, records):
  writer.writerow(dict([
    ('id', i),
    ('Context', random.choice(contexts)),
    ('Sentiment Score', str(random.randint(0,5))),
    ('Operator', random.choice(operators)),
    ('Circle', random.choice(circles)),
    ('Channel', random.choice(channels)),
    ('Date', randomDate("1/1/2008 12:00 AM", "3/1/2008 12:00 AM", random.random()))
    ]))
