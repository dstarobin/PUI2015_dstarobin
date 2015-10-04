The python script in the hypothesis folder can be run on any citibike csv.

**Ha: The ratio of subscriber trips to customer trips is lower on weekends than on weekdays.**

**Ho: The ratio of subscriber trips to customer trips is the same or higher on weekends than on weekdays.**

Could be interesting to update Ho/ Ha to include an examination of difference between ratios
between low month (Feb) and peak (July). Lots of ways to look at it:

*Intra* month subscriber to customer ratios on weekdays vs subscriber to customer ratios on weekends

	For July 2015:
	cust wknds: 73035
	sub wknds: 156930
	ratio = 2.15
	
	cust wkdys: 107327
	sub wkdys: 748384
	ratio = 6.97
	
	For Feb 2015:
	cust wknds: 1054
	sub wknds: 39783
	ratio = 37.74
	
	cust wkdys: 1211
	sub wkdys: 154882
	ratio =  127.89

*Intra* month ratio of the ratios above

	July 2015 wkdys ratio of 6.97: wknds ratio of 2.15 = 3.24
	Feb 2015 wkdys ratio of 127.89: wknds ratio of 37.74 = 3.39

*Inter* month comparisons

	July customer weekends : Feb customer weekends
	July customer weekdays : Feb customer weekdays
	July subscriber weekends : Feb customer weekends
	July subscriber weekends : Feb customer weekends

	whatever else

(Potential) Tasks:
To do - Ensure Ho and Ha make sense. Select confidence level (.05 should be fine).
Done - Select a month’s worth of Citibike data to analyze (Citibike July 2015 csv (zipped) is in the same folder this document is in.). 
Done - Bin rides by weekday and weekend (this was done for both July and Feb 2015)
  (Weekend dates in July 2015 were: 4, 5, 11, 12, 18, 19, 25, 26)
Done - Bin each of the two groups in #3 by subscribers and customers
Done - Calculate totals for weekday subscriber rides, weekday customer rides, weekend subscriber rides and weekend customer rides.
To do - Identify most appropriate statistical tests and run. Reject or accept Ho.
To do - Create some visualizations.
