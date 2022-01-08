# AUTOMATIKA TEST
### Requirements

Install
```
python 3.9
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```
Configure 
``` 
cp .env.sample .env
```
Modify ```.env``` file as you want.
#### Note
Database settings should be 'link-like' mode. For example
```DATABASE_URL=postgres://<user:root>:<password:password>@<host:127.0.0.1>:<port:5432>/<database:db>```