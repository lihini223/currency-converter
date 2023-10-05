import requests

def get_url(url: str):

    try:
        response = requests.get(url)
        return response.status_code, response.text
    except Exception as e:
        return 500, str(e)
