import math
from datetime import date

DAY_OF_WEEK_MM = {
    "Sunday": "တနင်္ဂနွေ",
    "Monday": "တနင်္လာ",
    "Tuesday": "အင်္ဂါ",
    "Wednesday": "ဗုဒ္ဓဟူး",
    "Thursday": "ကြာသပတေး",
    "Friday": "သောကြာ",
    "Saturday": "စနေ"
}

DAY_OF_WEEK = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")


def calculateJDN(gregorian_date : date) -> int:
    a = math.floor((14 - gregorian_date.month)/12)
    y = gregorian_date.year + 4800 - a
    m = gregorian_date.month + 12*a - 3
    jdn = gregorian_date.day + math.floor((153*m + 2)/5) + 365*y + math.floor(y/4) - math.floor(y/100) + math.floor(y/400) - 32045
    return jdn


def convertJDNtoMMYear(jdn : int) -> int:
    SY = 1577917828/4320000
    MO = 1954168.0506
    mm_year = math.floor((jdn - 0.5 - MO)/SY)
    return mm_year


def getMMYear(gregorian_date: date) -> int:
    return convertJDNtoMMYear(calculateJDN(gregorian_date))


def getMMDayOfWeek(gregorian_date: date) -> str:
    dow = gregorian_date.strftime("%A")
    return DAY_OF_WEEK_MM.get(dow)
