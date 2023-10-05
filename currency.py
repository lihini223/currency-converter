
def round_rate(rate):

    # Function that will round an input float to 4 decimals places.

    return round(rate, 4)

 

def reverse_rate(rate):

    # Function that will calculate the inverse rate from the provided input rate.

    if rate != 0:
        return round_rate(1/rate)
    else:
        return 0
    


def convert_currency(amount, rate):

    # Function that will convert the amount from from_currency to to_currency using the provided rate(latest or historical)

    return round_rate(amount * rate)



def format_output(date, from_currency, to_currency, rate, amount):

    """Function that generates the string that will be displayed by the web app once the user has selected his choices.\
        output string convention: The conversion rate on <date> from <from currency> to <to currency> was <rate> \
        So <from amount> in <from currency> correspond to <to amount> in <to currency> 
        The inverse rate was <inverse rate>."""

    return f"The conversion rate on {date} from {from_currency} to {to_currency} was {round_rate(rate)} \
            So {amount} in {from_currency} correspond to {convert_currency(amount, rate)} in {to_currency} \
            The inverse rate was {reverse_rate(rate)}"

   