# Iske 5 levels han


#DEBUG

#INFO

#WARNING

#ERROR

#CRITICAL


import logging
logging.warning("This is warning")
logging.error("SomeTime went wrong")
logging.critical("System Crash")


import logging

logging.basicConfig(level=logging.INFO)

logging.debug("Debug")
logging.info("Info")
logging.warning("Warning")
logging.error("Error")
logging.critical("Critical")