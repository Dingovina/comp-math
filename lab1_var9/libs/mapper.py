from decimal import Decimal
def string_to_decimal(string):
    try:
        return Decimal(float(string))
    except ValueError:
        try:
            string = string.replace(",", ".")
            return Decimal(float(string))
        except ValueError:
            return None