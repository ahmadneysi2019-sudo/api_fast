import requests

def get_all_items():
    url = 'http://127.0.0.1:8000/getitems/'

    response = requests.get(url)
    if response.status_code !=200:
        return 'error'
    else:
        response = response.json()
        return response

####################################
if __name__ == '__main__':
    result = get_all_items()
    print('result:',result)