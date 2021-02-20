#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from forms import *
import os

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
#db = SQLAlchemy(app)

# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''
#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/')
def home():
    return render_template('pages/home.html')

@app.route('/choose')
def choose():
    return render_template('pages/choose.html')

@app.route('/form_school')
def form_school():
    return render_template('pages/form_school.html')

@app.route('/form_projects')
def form_projects():
    return render_template('pages/form_projects.html')

@app.route('/generel_individ')
def generel_individ():
    return render_template('pages/generel_individ.html')

@app.route('/generel_klass')
def generel_klass():
    return render_template('pages/generel_klass.html')

@app.route('/submit_school_individ')
def submit_school_individ():
    return render_template('pages/submit_school_individ.html')

@app.route('/submit_school_klass')
def submit_school_klass():
    return render_template('pages/submit_school_klass.html')

@app.route('/submit_school_project')
def submit_school_project():
    return render_template('pages/submit_school_project.html')

@app.route('/projects')
def projects():
    return render_template('pages/projects.html')

@app.route('/question1')
def question1():
    return render_template('pages/question1.html')

@app.route('/question2')
def question2():
    return render_template('pages/question2.html')

@app.route('/question3')
def question3():
    return render_template('pages/question3.html')

@app.route('/lekplats')
def lekplats():
    return render_template('pages/lekplats.html')

@app.route('/allman')
def allman():
    return render_template('pages/allman.html')

@app.route('/confirmation')
def confirmation():
    return render_template('pages/confirmation.html')

# Error handlers.
@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True #Fixes caching stuff
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
