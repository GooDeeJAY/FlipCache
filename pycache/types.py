from enum import Enum


ONE_MINUTE = 60
ONE_HOUR = 3600
ONE_DAY = 86400
ONE_WEEK = 604800
ONE_MONTH = 2592000
ONE_YEAR = 31536000

THIRTY_MINUTES = 1800

TWO_DAYS = 2 * ONE_DAY
THREE_DAYS = 3 * ONE_DAY
FOUR_DAYS = 4 * ONE_DAY
FIVE_DAYS = 5 * ONE_DAY
SIX_DAYS = 6 * ONE_DAY


class DataType(Enum):
    STRING = 0
    INTEGER = 1
    JSON = 2