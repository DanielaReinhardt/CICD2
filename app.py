2.	import time
3.	import logging
4.	
5.	logging.basicConfig(level=logging.WARNING)
6.	
7.	# Loop every 10 seconds
8.	while True:
9.	    logging.warning("Hello, world!")
10.	    time.sleep(10)
