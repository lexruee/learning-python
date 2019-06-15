# SQLAlechmy Tutorial


## Prerequisites

 * pipenv
 
 
## Setup

Install the necessary dependencies:

``` 
pipenv install
```

Next, create the sqlite db and populate it with data:

``` 
pipenv run python create_db.py
pipenv run python populate_db.py
```

## Querying

For querying run:

``` 
pipenv run python query_db.py
```