from datetime import date
import numpy as np

MULTIPLIERS = np.array((4, 3, 2, 7, 6, 5, 4, 3, 2, 1))

exceptions = (
    1965,
    1966,
    1970,
    1980,
    1984,
    1985,
    1986,
    1987,
    1988,
    1990
)

SERIES_MALE = np.array((7, 13, 9, 15, 11, 17))

SERIES_FEMALE = np.array((2, 10, 4, 8, 6, 12))


class CPRException(Exception):
    pass


class CPR(object):
    def __init__(self, cpr):
        cpr = self.as_tuple(cpr)

        day = self.nums_to_num(*cpr[0:2])
        month = self.nums_to_num(*cpr[2:4])
        year = self.nums_to_num(*cpr[4:6])

        year += 1900 if cpr[6] < 4 \
            else (2000 if year < 37 else 1900) if cpr[6] < 5 \
            else (2000 if year < 58 else 1800) if cpr[6] < 9 \
            else (2000 if year < 37 else 1900)

        self.__birthdate = date(year, month, day)
        self.__checksum = self.nums_to_num(*cpr[6:10])

        if sum(MULTIPLIERS * cpr) % 11 \
                and not (day == 1 and month == 1 and year in exceptions) \
                and not year >= 2007:
            raise CPRException()
        elif 0 not in ((SERIES_MALE[1::2] - self.checksum) % 6) \
                and 0 not in ((SERIES_FEMALE[1::2] - self.checksum) % 6):
            raise CPRException()

    @property
    def birthdate(self):
        return self.__birthdate

    @property
    def checksum(self):
        return self.__checksum

    @property
    def gender(self):
        return self.cpr[9] % 2

    @staticmethod
    def nums_to_num(*nums):
        return int("".join(map(str, nums)))

    @staticmethod
    def as_tuple(cpr):
        if type(cpr) is tuple:
            cpr = cpr
        if type(cpr) is str:
            cpr = tuple(map(lambda l: int(l), cpr))
        elif type(cpr) is list:
            cpr = tuple(cpr)
        return cpr

    def __str__(self):
        return "{0:%d%m%y}-{1}".format(self.birthdate, self.checksum)

