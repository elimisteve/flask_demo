# Flask Demo

Simple Flask app to show people who are new to programming!


## Getting Started

Install [uv](https://docs.astral.sh/uv/) (a fast Python package manager that
replaces `pip` and `virtualenv`):

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then, from this directory, install the dependencies and run the app:

```sh
uv sync
uv run python app.py
```

Open http://localhost:5000/ in your browser. Try also `/hello` and
`/hello/your-name`.

## Running the tests

```sh
uv run pytest
```

## Learn more

Flask quickstart: https://flask.palletsprojects.com/en/stable/quickstart/
