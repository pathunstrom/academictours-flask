from app import app
from flask import render_template, url_for

@app.route('/')
def home():
    return render_template("index.html",
                           layout="index",
                           referral=get_referral())


@app.route('/regions')
def regions():
    return render_template("regions.html",
                           title="Our Regions",
                           layout="region",
                           referral=get_referral())


@app.route('/region/<location>')
def region(location):
    return render_template("region.html",
                           title="{} Destinations".format(location),
                           layout=location.lower(),
                           referral=get_referral(),
                           destinations=get_destinations(location))


@app.route('/destination/<location>')
def destination_page(location):
    return "This is the {} destination page.".format(location)


@app.route('/tour/<tour>')
def tour_page(tour):
    return "This is the {} tour page.".format(tour)


@app.route('/contact/', methods=["POST"])
def handle_contact_form():
    return "This is not yet functioning."


def get_referral():
    referral = "This is a referral from an existing customer."
    customer = "John Doe"
    return referral, customer


def get_destinations(location):
    location = location.encode('utf-8')
    if location.lower() == "mediterranean":
        return [{'name': "Malta", "copy": "The jewel of the Mediterranean.",
                 'featured': True},
                {'name': "Sicily", "copy": "Sicilian sales copy.",
                 'featured': False},
                {'name': "Italy", "copy": "Italian sales copy.",
                 'featured': False},
                {'name': "Sardinia", "copy": "Sardinian sales copy.",
                 'featured': False},
                {'name': "Tunisia", "copy": "Tunisian sales copy.",
                 'featured': False}]
    elif location.lower() == "asia":
        return [{'name': "Bhutan", "copy": "Bhutan sales copy.",
                 'featured': False},
                {'name': "Nepal", "copy": "Nepal sales copy.",
                 'featured': False}]