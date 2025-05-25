import requests

def http_options(url):
    response = requests.options(url)
    with open("options.txt", "w") as f:
        f.write("\nOPTIONS Request:")
        f.write("Status Code: " + str(response.status_code))
        f.write("Response Headers: " + str(response.headers))
        f.write("Response Body: " + str(response.text))

def http_get(url):
    response = requests.get(url)
    with open("get.txt", "w") as f:
        f.write("\nGET Request:")
        f.write("Request URL: " + str(url))
        f.write("Request Method: GET")
        f.write("Status Code: " + str(response.status_code))
        f.write("Response Headers: " + str(response.headers))
        f.write("Response Body: " + str(response.text))

def http_post(url, data):
    response = requests.post(url, data=data)
    with open("post.txt", "w") as f:
        f.write("\nPOST Request:")
        f.write("Request URL: " + str(url))
        f.write("Request Method: POST")
        f.write("Request Data: " + str(data))
        f.write("Status Code: " + str(response.status_code))
        f.write("Response Headers: " + str(response.headers))
        f.write("Response Body: " + str(response.text))

if __name__ == "__main__":
    url = "https://httpbin.org"  # Можно заменить на нужный тебе URL

    # Выполнение метода OPTIONS
    http_options(url)

    # Выполнение метода GET
    http_get(url + "/get")  # пример использования GET

    # Выполнение метода POST
    data = {'key1': 'value1', 'key2': 'value2'}
    http_post(url + "/post", data)