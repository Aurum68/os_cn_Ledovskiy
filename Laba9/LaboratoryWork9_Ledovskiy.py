import requests

def http_options(url):
    response = requests.options(url)
    print("\nOPTIONS Request:")
    print("Status Code:", response.status_code)
    print("Response Headers:", response.headers)
    print("Response Body:", response.text)

def http_get(url):
    response = requests.get(url)
    print("\nGET Request:")
    print("Request URL:", response.url)
    print("Request Method: GET")
    print("Status Code:", response.status_code)
    print("Response Headers:", response.headers)
    print("Response Body:", response.text)

def http_post(url, data):
    response = requests.post(url, data=data)
    print("\nPOST Request:")
    print("Request URL:", response.url)
    print("Request Method: POST")
    print("Request Data:", data)
    print("Status Code:", response.status_code)
    print("Response Headers:", response.headers)
    print("Response Body:", response.text)

if __name__ == "__main__":
    url = "https://httpbin.org"  # Можно заменить на нужный тебе URL

    # Выполнение метода OPTIONS
    http_options(url)

    # Выполнение метода GET
    http_get(url + "/get")  # пример использования GET

    # Выполнение метода POST
    data = {'key1': 'value1', 'key2': 'value2'}
    http_post(url + "/post", data)