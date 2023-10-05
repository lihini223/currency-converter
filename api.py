import requests

def get_url(url: str):
    """
    Function that will call a provide GET API endpoint url and return its status code and either its 
    content or error message as a string
    """
    
    try:
        response = requests.get(url)
        return response.status_code, response.text
    except Exception as e:
        return 500, str(e)
