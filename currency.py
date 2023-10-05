
def round_rate(rate):

    return round(rate, 4)

 

def reverse_rate(rate):

    if rate != 0:
        return round_rate(1/rate)
    else:
        return 0
    


def convert_currency(amount, rate):

    to_amount = amount * rate

    return round_rate(to_amount)



def format_output(date, from_currency, to_currency, rate, amount):
 
    return f"The conversion rate on {date} from {from_currency} to {to_currency} was {round_rate(rate)} \
            So {amount} in {from_currency} correspond to {convert_currency(amount, rate)} in {to_currency} \
            The inverse rate was {reverse_rate(rate)}"

   