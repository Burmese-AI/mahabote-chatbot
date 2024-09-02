from datetime import date

import mmcalendar

HOUSE_OF_BOARD_MM = {
    "House of Leader": "အဓိပတိ",
    "House of Fame": "အထွန်း",
    "House of Wealth": "သိုက်",
    "House of Kingly Position": "ရာဇ",
    "House of Extremity": "မရဏ",
    "House of Impermanence": "ဘင်္ဂ",
    "House of Sickly": "ပုတိ"
}

BOARD_ORDER = (
    "House of Impermanence",
    "House of Extremity",
    "House of Fame",
    "House of Wealth",
    "House of Kingly Position",
    "House of Sickly",
    "House of Leader")

PLANET_ORDER = (1, 4, 7, 3, 6, 2, 5)
# Sun - Mercury - Saturn - Mars - Venus - Moon - Jupiter

def getHouse(birth_date):
    # convert input string to date
    day, month, year = (int(i) for i in birth_date.split("-"))
    dob = date(year, month, day)

    # get day of week
    mmday = mmcalendar.getMMDayOfWeek(dob)

    # get day index
    # add 1 to align with planet
    day_index = int(dob.strftime("%w")) + 1

    # convert to myanmar year
    mmyear = mmcalendar.getMMYear(dob)

    # find remainder
    rem = mmyear % 7
    r = rem if rem != 0 else 7 # make remainder 0 to 7

    # make board
    board = PLANET_ORDER[PLANET_ORDER.index(r):] + PLANET_ORDER[:PLANET_ORDER.index(r)]

    # get born house
    house = BOARD_ORDER[board.index(day_index)]

    # return in burmese
    return mmday, HOUSE_OF_BOARD_MM.get(house)

