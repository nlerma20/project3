
import urllib.request
from datetime import datetime, date, time, timedelta
import re
import os

# this retrieves log file and saves it locally as local_copy.log

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_PATH = 'local_copy.log'

local_file, headers = urllib.request.urlretrieve(URL_PATH, LOCAL_PATH)

