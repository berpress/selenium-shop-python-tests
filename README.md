# selenium-shop-python-tests
[![Build Status](https://app.travis-ci.com/berpress/selenium-shop-python-tests.svg?branch=main)](https://app.travis-ci.com/berpress/selenium-shop-python-tests)

**Selenium ui python tests.**

![](images/images.png)

This is a tutorial project (https://berpress.github.io/react-shop) that shows how to implement ui tests in Python. The test application simulates the operation of a product shop. You can register users, add an item and pay for it.

**Tests use**: Python/Selenium 4/Pytest/Faker/Page Object pattern


**See API**, that use shop application:

git: https://github.com/berpress/flask-restful-api

url: https://stores-tests-api.herokuapp.com

swagger: https://app.swaggerhub.com/apis/berpress/flask-rest-api/1.0.0

description: https://berpress.github.io/flask-restful-api/ (🇬🇧, 🇷🇺)

**How to start**

Use python 3.8 +
Create and activate virtual environments

```
python3 -m venv env
source env/bin/activate
```

Run in terminal

```
pip install -r requirements.txt
```

or install poetry https://python-poetry.org/, then

```
poetry install
```
and start all tests

```
pytest
```

**Attention**:

Before using the test store, you need to prepare the data. When you first visit the site, there will be a corresponding button
