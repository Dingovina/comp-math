from decimal import Decimal
def string_to_decimal(string):
    """
    Converts a string to a Decimal object
    """
    try:
        return Decimal(string)
    except ValueError:
        try:
            string = string.replace(",", ".")
            return Decimal(string)
        except ValueError:
            return None
