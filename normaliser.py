def normalize_ticker(ticker):
    """
    Convert company ticker to uppercase
    Remove spaces and new lines
    """

    if ticker is None:
        return ""

    return str(ticker).strip().upper()


def normalize_year(year):
    """
    Convert Mar-24 to 2024
    Convert Mar-23 to 2023
    """

    if year is None:
        return ""

    year = str(year).strip()

    if "-" in year:
        parts = year.split("-")

        if len(parts) == 2:
            yy = parts[1]

            if len(yy) == 2:
                return "20" + yy

    return year


# Testing

print(normalize_ticker(" tcs "))
print(normalize_ticker("infy"))

print(normalize_year("Mar-24"))
print(normalize_year("Mar-23"))