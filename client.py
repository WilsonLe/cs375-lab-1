import sys

import requests


def main(host="127.0.0.1", port="7345", filename=""):
    response = requests.get(f"http://{host}:{port}/{filename}")
    print(response.text)


if __name__ == "__main__":
    assert len(sys.argv) == 4
    host = sys.argv[1]
    port = sys.argv[2]
    filename = sys.argv[3]
    main(host=host, port=port, filename=filename)
