from flask import Flask, render_template, redirect

app = Flask(__name__)


app.secret_key = '8bf9547569cd5a638931a8640cf9f86237931e92'

# databaseName = 'example6.db'
# itemsTable = 'items'
# debtorsTable = 'debtors'
# creditorsTable = 'creditors'
# usersTable = 'app_users'


def showWebPage(page, vars):
    return render_template(page, vars=vars)


@app.route('/')
@app.route('/home')
def hello_world():
    print __name__
    return showWebPage('index.html', vars={"home":"selected"})

@app.route('/donor')
def donar():
    return showWebPage('donor.html',vars={"donar":"selected"})


@app.route('/patient')
def patient():
    return showWebPage('patient.html',vars={"patient":"selected"})


@app.route('/contact')
def contact():
    return showWebPage('contact.html',vars={"contact":"selected"})

@app.route('/about')
def about():
    return showWebPage('about.html',vars={"about":"selected"})

@app.route('/faq')
def faq():
    return showWebPage('faq.html',vars={"faq":"selected"})

@app.errorhandler(404)
def page_not_found(e):
    return showWebPage('404.html', {'error': "The page you requested was not found!"})


if __name__ == "__main__":
    app.run(debug=True, port=10003, use_evalex=False)
    # app.run(debug=True,host='192.168.43.53',port=5007,use_evalex=False)
