# cd dropbox/cusp/pui/pui2015_ds2455_hw3
import pandas as pd
from sys import argv

csv = argv[1]

if __name__=='__main__':
	print "Working--this might take a while (approx 2 seconds per MB in CSV). Please be patient..."
	bikes = pd.read_csv(csv)
	#below is WAAAAAAAAAY faster than first version. Like 30x faster.
	bikes['ts'] = pd.to_datetime(bikes.starttime, format = '%m/%d/%Y %H:%M:%S')
	#values 5,6 are Saturday and Sunday
	days = bikes['starttime'].dt.dayofweek
	bikes['dayvals'] = days

	weekends = bikes[(bikes.dayvals == 5) | (bikes.dayvals == 6)] 
	weekdays = bikes[(bikes.dayvals != 5) & (bikes.dayvals != 6)]

	custWknds = weekends[weekends.usertype == 'Customer']
	subWknds = weekends[weekends.usertype == 'Subscriber']

	custWkday = weekdays[weekdays.usertype == 'Customer']
	subWkday = weekdays[weekdays.usertype == 'Subscriber']

	print 'Weekend customer rides = %.2f' % (len(custWknds))
	print 'Weekend subscriber rides = %.2f' % (len(subWknds))
	print "Weekend subscriber: weekend customer ratio = %.2f" % (float(len(subWknds))/float(len(custWknds)))

	print 'Weekday customer rides = %.2f' % (len(custWkday))
	print 'Weekday subscriber rides = %.2f' % (len(subWkday))
	print "Weekday subscriber: weekday customer ratio = %.2f" % (float(len(subWkday))/float(len(custWkday)))

