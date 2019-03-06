from flask import render_template, abort, redirect, url_for, flash, request, session
from sqlalchemy.exc import DBAPIError, IntegrityError
from .forms import CompanyForm, CompanyAddForm
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

@app.route('/search', methods=['GET', 'POST'])
def company_search():
    form = CompanyForm()

    if form.validate_on_submit():
        try:
            symbol = form.data['symbol']        
            url = 'https://api.iextrading.com/1.0/stock/{}/company'.format(symbol)
            # import pdb; pdb.set_trace()
            response = requests.get(url)
            data = json.loads(response.text)    
            session['context'] = data
            #session['symbol'] = symbol

            # return redirect(url_for('.portfolio'))
            return redirect(url_for('.preview_company'))
        except:
            flash('Something went wrong with your search.  Try again.')

    return render_template('search.html', form=form)

@app.route('/preview', methods=['GET', 'POST'])
def preview_company():
    """
    """
    form_context = {
        'name': session['context']['companyName'],
        'symbol' : session['context']['symbol']
    }
    form = CompanyAddForm(**form_context)

    if form.validate_on_submit():
        try:
            company = Company(name=form.data['name'], symbol=form.data['symbol'])
            db.session.add(company)
            db.session.commit()
        except IntegrityError:
            flash(form.data['name'] + ' This company exists in the Portfolio.')
            return redirect(url_for('.preview_company'))
        except DBAPIError as e:
            flash('Something went wrong with your search.')
            return redirect(url_for('.preview_company'))
        # except (DBAPIError, IntegrityError, JSONDecodeError):
        #     flash('Something went wrong with your search.')
        #     return render_template(url_for('.preview_company'))

        return redirect(url_for('.portfolio'))

    return render_template(
        'preview.html',
        form=form,
        symbol=form_context['symbol'],
        name=session['context']['companyName'],
    )

@app.route('/portfolio', methods=['GET'])
def portfolio():
    companies = Company.query.all()
    return render_template('company.html', companies=companies)