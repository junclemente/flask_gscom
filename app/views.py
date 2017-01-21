from app import app
from flask import render_template



@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/business')
def business():
    return render_template('business.html')


@app.route('/products')
def products():
    return render_template('products.html')


@app.route('/whitepaper/<whitepaper>')
def whitepaper(whitepaper):
    return render_template('whitepaper.html', whitepaper=whitepaper)


@app.route('/contact_us')
def contact():
    return render_template('contact.html')
