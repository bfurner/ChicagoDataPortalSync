import datetime
from pytz import timezone

BASE_METADATA_URI = "https://data.cityofchicago.org/api/views/metadata/v1"
BASE_RESOURCE_URI = "https://data.cityofchicago.org/resource/"
LAST_RUN =  datetime.datetime(2023, 10, 28, 0, 0, tzinfo=timezone('UTC'))
OUTPUT_DIR = "/Users/bfurner/Projects/Sociome/ChicagoDataPortalSync/downloads/"