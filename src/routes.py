from flask import render_template, abort, redirect, url_for, request
from sqlalchemy.exc import DBAPIError, IntegrityError
from .models import Company, db
from . import app  # same as from src import app
from json import JSONDecodeError
import requests
import json
import os


# the @app is imported via 'from . import app'
@app.route('/') # default value is ['GET']
def home():
    return render_template('home.html')

@app.route('/search', methods=['GET'])
def search_form():
    return render_template('search.html')

@app.route('/search', methods=['POST'])
def search_results():
    # hit api with given stock symbol
    # store results in db - need to use a model
    # redirect to portfolio page

    # import pdb; pdb.set_trace()

    symbol = request.form.get('symbol')

    url = 'https://api.iextrading.com/1.0/stock/{}/company'.format(symbol)

    response = requests.get(url)
    data = json.loads(response.text)    

    # 'companyName' needs to match the database column for company
    # peter = User.query.filter_by(username='peter').first()
    # result = Company.query.filter_by(symbol='symbol').first()

    try:
        company = Company(name=data['companyName'], symbol=data['symbol'])
        db.session.add(company)
        db.session.commit()

        return redirect(url_for('.portfolio')) # redirect the portfolio page
    # except JSONDecodeError:
    except (DBAPIError, IntegrityError):
        abort(404)

    # except (DBAPIError, IntegrityError):
      # abort(400)
         
    # how do we check that what was committed is actually committed?
    # return response.text
    # return data['symbol']

    return render_template('search.html')

@app.route('/portfolio', methods=['GET'])
def portfolio():
  return render_template('portfolio.html')
