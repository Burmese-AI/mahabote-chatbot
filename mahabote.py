from datetime import date

day_of_week_mm = {
    "Sunday": "တနင်္ဂနွေ",
    "Monday": "တနင်္လာ",
    "Tuesday": "အင်္ဂါ",
    "Wednesday": "ဗုဒ္ဓဟူး",
    "Thursday": "ကြာသပတေး",
    "Friday": "သောကြာ",
    "Saturday": "စနေ"
}

day_of_week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

house_of_board_mm = {
    "House of Leader": "အဓိပတိ",
    "House of Fame": "အထွန်း",
    "House of Wealth": "သိုက်",
    "House of Kingly Position": "ရာဇ",
    "House of Extremity": "မရဏ",
    "House of Impermanence": "ဘင်္ဂ",
    "House of Sickly": "ပုတိ"
}

board_order = (
    "House of Impermanence",
    "House of Extremity",
    "House of Fame",
    "House of Wealth",
    "House of Kingly Position",
    "House of Sickly",
    "House of Leader")

planet_order = (1, 4, 7, 3, 6, 2, 5)
# Sun - Mercury - Saturn - Mars - Venus - Moon - Jupiter

def getHouse(birth_date):
    # convert input string to date
    day, month, year = (int(i) for i in birth_date.split("-"))
    dob = date(year, month, day)

    # get day of week
    born_dow = dob.strftime("%A")
    born_dow_index = day_of_week.index(born_dow) + 1

    # convert to myanmar year
    year_dif = 639 if dob.month < 4 else 638
    mm_year = dob.year - year_dif

    # find remainder
    rem = mm_year % 7
    r = rem if rem != 0 else 7 # make remainder 0 to 7

    # make board
    board = planet_order[planet_order.index(r):] + planet_order[:planet_order.index(r)]

    # get born house
    house = board_order[board.index(born_dow_index)]

    # return in burmese
    return day_of_week_mm.get(born_dow), house_of_board_mm.get(house)
