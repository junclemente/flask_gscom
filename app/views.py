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

# Below is the list of White Papers to be added to the navigation bar.
# Enter the information below in the following format: ( title, filename ).
# They must also be entered in the order that you want them to appear in the
# navigation bar dropdown menu.
# whitepaper_list = [
#     ("AGC Design", "AGC Design.pdf"),
#     ("Broadband Wireless Modem", "Broadband wireless 4096-QAM Modem.pdf"),
#     ("DFE and Carrier Recovery", "DFE & Carrier Recovery.pdf"),
#     ("LDPC System Design", "LDPC System Design.pdf"),
#     ("Mapper", "Mapper.pdf"),
#     ("Project Budget", "Project Budget.pdf"),
#     ("Business Proposal", "Business Proposal.pdf"),
#     ("Business Development", "Business Development.pdf")]
