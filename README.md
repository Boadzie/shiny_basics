# Shiny Basics

> Repository for learning Shiny Python Basics

## Dependencies

1. Shiny Python
2. Polars
3. Lets-plot

## Setup

1. Create a virtual env

```bash
python -m venv .myenv
```

2. Activate the virtual environment

```bash
source .myenv/bin/activate
```

3. Install dependencies from the requirements.txt

```bash
pip install -r requirements.txt
```

## Run the app

```bash
shiny run --reload app.py
```

Then visit `localhost:8000`
