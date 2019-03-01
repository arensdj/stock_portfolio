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
    return render_template('home.html')
    # return render_template('home.html')

# @app.route('/search')
# def home():
#     return 'home'

@app.route('/search', methods=['GET'])
def search_form():
    return render_template('stocks/search.html')

@app.route('/search', methods=['POST'])
def search_results():
    # hit api with given stock symbol
    # store results in db - need to use a model
    # redirect to portfolio page
    symbol = request.form.get('symbol')

    # url = 'https://api.iextrading.com/1.0/stock/aapl/company'
    url = 'https://api.iextrading.com/1.0/stock/{}/company'.format(symbol)

    response = requests.get(url)

    # instatiate a company
    data = json.loads(response.text)
    company = Company(name=data['companyName'], symbol=data['symbol'])
    # 'companyName' needs to match the database column for company

    db.session.add(company)
    db.session.commit()

    # how to we check that what was committed is actually committed?

    # return company.name + ' ' + company.symbol
    return redirect(url_for('.portfolio')) # redirect the portfolio page

    # return response.text
    # return data['symbol']

@app.route('/portfolio')
def portfolio():
  # print(Company.query.all())

  # return str(Company.query.all())

  return render_template('stocks/stocks.html')
