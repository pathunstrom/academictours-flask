from app import app
import config
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from flask import render_template
from flask import request
import model
from operator import itemgetter
from random import choice
import smtplib


@app.route('/')
def home():
    return render_template("contact.html",
                           parent="index.html",
                           layout="index",
                           featured_tour=get_tours(featured=True)[0],
                           pledge=get_copy("pledge"),
                           about=get_copy("about"),
                           referral=get_referral())


@app.route('/regions/')
def regions_page():
    return render_template("contact.html",
                           parent="regions.html",
                           title="Our Regions",
                           layout="region",
                           regions=get_regions(),
                           selected_tours=get_copy("selected tours"),
                           custom_tours=get_copy("custom tours"),
                           referral=get_referral())


@app.route('/region/<location>/')
def region_page(location):
    region = get_regions(location)
    region["destinations"] = get_destinations(region=region["name"])
    return render_template("region.html",
                           title="{} Destinations".format(location),
                           layout=location.lower(),
                           referral=get_referral(),
                           region=region)


@app.route('/destination/<location>/')
def destination_page(location):
    destination = get_destinations(name=location)[0]
    destination["tours"] = get_tours(destination=destination["name"])
    return render_template("destination.html",
                           title="{}".format(location),
                           layout="destination",
                           referral=get_referral(),
                           destination=destination)


@app.route('/tour/<tour>/')
def tour_page(tour):
    tour = get_tours(name=tour.encode('utf-8'))[0]
    tour['itinerary'] = get_itinerary(tour["name"])
    tour['prices'] = get_prices(tour["name"])
    return render_template("contact.html",
                           parent="tour.html",
                           layout="tour",
                           tour=tour,
                           referral=get_referral())


@app.route('/contact/', methods=["POST"])
def handle_contact_form():
    print request.form
    from_address = config.server_email
    to_address = config.contact_email
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = "A new client for Academic Tours"
    body = """
           Mr. Boden,

           {name} just contacted you via your website contact form.

           You can reach them at {email} or {phone}.

           They said their dream vacation was:

           {vacation}
           """.format(name=request.form["name"],
                      email=request.form["email"],
                      phone=request.form["phone"],
                      vacation=request.form["destination"])
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(config.smtp_username, config.smtp_password)
    text = msg.as_string()
    server.sendmail(from_address, to_address, text)
    return render_template("thankyou.html",
                           referral=get_referral(),
                           layout="thankyou",
                           name=request.form["name"])


@app.route('/login/', methods=["GET", "POST"])
def login_page():
    return render_template("null.html",
                           referral=get_referral())


@app.route('/admin/')
def admin_page():
    return render_template("null.html",
                           referral=get_referral())


def get_copy(name):
    value = None
    for index in model.copy:
        if index['name'] == name:
            value = index

    return value


def get_destinations(name=None, region=None):
    value = []

    if region:
        location = region.encode('utf-8')
        for destination in model.destinations:
            if destination["region"].lower() == location.lower():
                value.append(destination)
        return value

    if name:
        location = name.encode('utf-8')
        for destination in model.destinations:
            if destination["name"].lower() == location.lower():
                value.append(destination)

    return value


def get_itinerary(tour):
    value = []
    for day in model.days:
        if day["tour"].lower() == tour.lower():
            day["landmarks"] = get_landmarks(tour, day["day"])
            value.append(day)

    return value


def get_landmarks(tour, day):
    value = []

    for relation in model.day_landmark:
        if relation["tour"] == tour and relation["day"] == day:
            for landmark in model.landmarks:
                if landmark["name"] == relation["landmark"]:
                    value.append(landmark)
                    break

    return value


def get_prices(tour):
    value = []

    for price in model.prices:
        if price["tour"].lower() == tour.lower():
            price["name"] = model.month[price["month"]]
            value.append(price)

    value.sort(key=itemgetter('month'))
    return value


def get_referral():
    value = choice(model.referrals)
    referral = value["referral"]
    customer = value["name"]
    return referral, customer


def get_regions(location=None):
    if location:
        for region in model.regions:
            if region["name"].lower() == location.encode('utf-8').lower():
                return region
    else:
        return model.regions


def get_tours(destination=None, featured=False, name=None):
    value = []
    if destination:
        for tour in model.tours:
            if tour["destination"].lower() == destination.lower():
                value.append(tour)
    elif featured:
        for tour in model.tours:
            if tour["featured"]:
                value.append(tour)
                break
    elif name:
        for tour in model.tours:
            if tour["name"].lower() == name.lower():
                value.append(tour)
                break
    else:
        raise IndexError

    return value