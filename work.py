import re


def find_date(text):
    """ find date in string and return as datetime,
        works only for specific text structure """

    months = ['sty', 'lut', 'mar', 'kwi', 'maj', 'cze', 'lip', 'sie', 'wrz', 'paź', 'lis', 'gru']

    reg = re.compile(
        r"\d{1,2}\s\w{5,12}\s\d{2,4}|\s\d{1,2}[.-]\s?\d{1,2}[.-]\s?\d{2,4}|^\d{1,2}[.-]\s?\d{1,2}[.-]\s?\d{2,4}")

    try:
        date = reg.findall(text)[0].strip()
    except IndexError:
        return 'b.d.'
    if date.count('.') == 2:
        date = [int(i) for i in date.split('.')]
        day, month, year = date
    else:
        date = date.split(' ')
        for i, j in enumerate(months, 1):
            if j in date[1].lower():
                month = i
        day, year = int(date[0]), int(date[2])

    return f'{year}-{month:02}-{day:02}'
