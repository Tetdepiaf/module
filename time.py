# -*- coding: utf-8 -*-

import time
import datetime

temps = time.localtime()
time.sleep(3)
temps2 = time.mktime(temps)
temps3 = time.time()
date = time.strftime("%A %d %B %Y %H:%M:%S")
date2 = datetime.date.today()
date3 = datetime.date.fromtimestamp(time.time()) 
date4 = datetime.datetime.now()