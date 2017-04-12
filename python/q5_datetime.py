# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

from datetime import datetime
date_format = "%m-%d-%Y"
start = datetime.strptime(date_start, date_format)
stop = datetime.strptime(date_stop, date_format)
print (stop-start).days

####b)  
date_start = '12312013'  
date_stop = '05282015'  

date_format = "%m%d%Y"
start = datetime.strptime(date_start, date_format)
stop = datetime.strptime(date_stop, date_format)
print (stop-start).days


####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'

date_format = '%d-%b-%Y'
start = datetime.strptime(date_start, date_format)
stop = datetime.strptime(date_stop, date_format)
print (stop-start).days
