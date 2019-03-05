# stock_portfolio

<!-- # how to setup, install, and run your application -->
# Flask application boilerplate for Stock Portfolio App
# 1. Clone repo
# 2. Ensure that .env file contains the below configs
#    i. Add any additional details for values, such as username and password for DATABASE_URL
# 3. Create Virtualenv & Activate
#    i. Ensure that you have a tool for loading env vars (dotenv, pipenv, etc)
# 4. Create a Database in PostgreSQL called weather
# 5. 'Upgrade' migrations to DB
#    i. flask db upgrade
#    ii. If migrations/ directory is not present first run:
#       a. flask db init
#       b. flask db migrate -m 'initial migration'
#       c. THEN...
#       d.flask db upgrade
# 5. Start the server: flask run

# FLASK_APP=src/wsgi.py
# FLASK_ENV=development
# DATABASE_URL=postgres://localhost:5432/companies
# SECRET_KEY=5a9143ae-c439-4ea1-8228-5d67da63d1e4