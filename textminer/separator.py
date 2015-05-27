import re

def words(txt):
    match = re.findall(r"\b[\d]*[A-Za-z-]+", txt)
    if match:
        return match

def phone_number(num):
    match = re.match(r"\(?(?P<area_code>\d{3})[\.\)]?[.\- ]?(?P<first>\d{3})[.\-]?(?P<last>\d{4})", num)
    if match:
        temp_dict = match.groupdict()
        phone_dict = {}
        phone_dict["area_code"] = "{area_code}".format(**temp_dict)
        phone_dict["number"] = "{first}-{last}".format(**temp_dict)
        return phone_dict

def zipcode(num):
    match = re.match(r"""(?P<zip>\d{5}) #five digit zipcode
                    (-(?P<plus4>\d{4}) #can also have dash
                    | #or
                    $ #has to end, no more number allowed
                    )""", num, re.VERBOSE)
    if match:
        return match.groupdict()


def dates(num):
    match = re.match(r"""\A(?P<year>\d{4}) # YYYY
                    [/-]
                    (?P<month>\d{1,2}) #MM
                    [/-]
                    (?P<day>\d{2}) #DD
                    | #or
                    \A(?P<month2>\d{1,2}) # MM
                    [/-]
                    (?P<day2>\d{1,2}) #DD
                    [/-]
                    (?P<year2>\d{4}) #YYYY
                    """, num, re.VERBOSE)
    if match:
        match_dict = match.groupdict()
        if match_dict.get('month2') != None:
            match_dict['month'] = match_dict['month2']
            match_dict['day'] = match_dict['day2']
            match_dict['year'] = match_dict['year2']
        del(match_dict['month2'])
        del(match_dict['day2'])
        del(match_dict['year2'])
        match_dict['month'] = int(match_dict['month'])
        match_dict['day'] = int(match_dict['day'])
        match_dict['year'] = int(match_dict['year'])
        return match_dict

#
# ("9/4/1976", {"month": 9, "day": 4, "year": 1976}),
#     ("1976-09-04", {"month": 9, "day": 4, "year": 1976}),
#     ("2015-01-01", {"month": 1, "day": 1, "year": 2015}),
#     ("02/15/2004", {"month": 2, "day": 15, "year": 2004}),
#     ("9/4", None),
#     ("2015", None),
# ])