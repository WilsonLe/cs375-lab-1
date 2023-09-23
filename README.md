# CS375 - Wilson Le & Krystal Ly

# Prerequisite

Setup python virtual environment (optional)

```sh
# On Linux/MacOS
python -m venv .venv
source .venv/bin/activate
```

Install all necessary dependencies
```sh
pip install -r requirements.txt
```

# Server

To start the web server:

```sh
python server.py
```

# Client

To run the client connecting to the web server:

```sh
python client.py "127.0.0.1" "7345" "foobar.html"
```

