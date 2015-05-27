import re

def binary(num):
    return re.match(r"[01]+", num)

def binary_even(num):
    """String must be a binary number and be even."""
    return re.match(r"[01]+0$", num)

def hex(txt):
    return re.match(r"\A[0-9A-Fa-f]+\Z", txt)
    assert v.hex("CAFE")
    assert v.hex("9F9")
    assert v.hex("123")
    assert v.hex("6720EB3A9D1")
    assert not v.hex("")
    assert not v.hex("COFFEE")

def word(txt):
    return re.match(r"\A[\d]*[A-Za-z-]+\Z", txt)

def words(txt, count=0):
    if count == 0:
        return re.match(r"\A[\d]*[A-Za-z-\s]+\Z", txt)

    else:
        txt_list = txt.split()
        if len(txt_list) != count:
            return False
        else:
            return re.match(r"\A[\d]*[A-Za-z-\s]+\Z", txt)


def phone_number(num):
    """US phone numbers only."""
    return re.match(r"\(?\d{3}[\.\)]?[.\- ]?\d{3}[.\-]?\d{4}", num)


def money(num):
    """We are just concerned with dollars here."""
    return re.match(r"""\$  #find dollar sign
                        ((\d{1,3} # one to three digits
                        (,\d{3})*) #find comma and 3 digits as many times
                        | #or
                        \d+)#zero or more digits
                        (\.\d{2})?$ #finds a decimal and zero or 1 digits
                        """, num, re.VERBOSE)

def zipcode(num):
    return re.match(r"""\d{5} #five digit zipcode
                    (-\d{4} #can also have dash
                    | #or
                    $ #has to end, no more number allowed
                    )""", num, re.VERBOSE)


def date(num):
    return re.match(r"""\A(\d{1}|\d{2}|\d{4})
                    [/-]
                    \d{1,2}
                    [/-]
                    (\d{2}|d{4})
                    """, num, re.VERBOSE)
