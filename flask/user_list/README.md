# Basic Flask + SQLAlchemy Tutorial


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

## Running the app

For running the app use the following command:

``` 
pipenv run python app.py 
```