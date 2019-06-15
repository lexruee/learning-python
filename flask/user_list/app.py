#!/usr/bin/env python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Flask
import model

app = Flask(__name__)
engine = create_engine('sqlite:///./db.sqlite')
Session = sessionmaker(bind=engine)
session = Session()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
<title>{title}</title>
</head>
<body>
<h1>{title}</h1>
{content}
</body>
</html>
"""


@app.route('/')
def hello():
    return HTML_TEMPLATE.format(title='Hello', content='Welcome to this simple page!')

@app.route('/users')
def users():
    users = session.query(model.User).all()
    html_nicknames = ["<li>{}</li>".format(user.nickname) for user in users]
    html_list = "<ul>{}</ul>".format("\n".join(html_nicknames))
    return HTML_TEMPLATE.format(title='Users', content=html_list)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
