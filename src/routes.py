from flask import render_template, abort, redirect, url_for, request
from sqlalchemy.exc import DBAPIError, IntegrityError
from .models import Company, db
from . import app  # same as from src import app
import requests
import json
import os


# the @app is imported via from . import app
@app.route('/') # default value is ['GET']
def home():
    """
    """
    return render_template('stocks/home.html')

@app.route('/search', methods=['GET'])
def search_form():
    return render_template('stocks/search.html')

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

    # instatiate a company
    company = Company(name=data['companyName'], symbol=data['symbol'])
    print(company)
    print(company.name, company.symbol)

    # 'companyName' needs to match the database column for company

    # peter = User.query.filter_by(username='peter').first()

    # result = Company.query.filter_by(symbol='symbol').first()
    # import pdb; pdb.set_trace()

    try:
      db.session.add(company)
      db.session.commit()
    except (DBAPIError, IntegrityError):
      abort(400)
         
    # if result:
      # print(Company.query.filter_by(symbol='symbol').first())
    # else:
      # import pdb; pdb.set_trace()

    # how do we check that what was committed is actually committed?
    # return response.text
    # return data['symbol']

    return redirect(url_for('.portfolio')) # redirect the portfolio page

@app.route('/portfolio')
def portfolio():
  # print(Company.query.all())
  # return str(Company.query.all())

  return render_template('stocks/stocks.html')
