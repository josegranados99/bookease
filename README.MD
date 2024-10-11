# Install Local

## Install MongoDB 

## Create venv
```bash
python -m  venv venv         
```

## Activate venv windows
```bash
venv\Scripts\activate
```
## Install dependencies
```bash
pip install -r requirements.txt
```

## Run app
```bash
uvicorn main:app --reload
```