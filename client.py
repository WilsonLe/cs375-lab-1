import requests


def main():
    response = requests.get("http://127.0.0.1:7345")
    print(response.text)


if __name__ == "__main__":
    main()
