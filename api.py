import requests

def get_url(url: str):
    """
    Function that will call a provide GET API endpoint url and return its status code and either its content or error message as a string

    Parameters
    ----------
    url : str
        URL of the GET API endpoint to be called

    Returns
    -------
    int
        API call response status code
    str
        Text from API call response
    """

    try:
        response = requests.get(url)
        return response.status_code, response.text
    except Exception as e:
        return 500, str(e)
