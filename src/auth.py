# from



@app.route(‘/register’)
def register():
  form = AuthForm( )    #<— this instantiates an AuthForm constructor
  return render_template( ‘/auth/register.html’, form=form)  

  return ‘I am register’


@app.route(‘/login’)
def login():
  form = AuthForm( )
  return render_template( ‘/auth/login.html’, form=form)  

  return ‘I am login’

def login_required(view_function):   # the 'view_function' comes from the routes.py

    @functools.wrap(view)
    def wrapped_view(**kwargs):
        if g.user is None:   # there is not a user, then abort message and redirect
            abort(404)
            # retrn redirect(url_for('.login'))

        return view(**kwargs)

    return wrapped_view

@app.before_request   # before any request, does the following stuff
def load_logged_in_user():  
    """
    """
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)

