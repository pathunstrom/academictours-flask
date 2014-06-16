from app import app
from flask import render_template
from model import tours, copy


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
def regions():
    return render_template("contact.html",
                           parent="regions.html",
                           title="Our Regions",
                           layout="region",
                           regions=get_regions(),
                           selected_tours=get_copy("selected tours"),
                           custom_tours=get_copy("custom tours"),
                           referral=get_referral())


@app.route('/region/<location>/')
def region(location):
    return render_template("region.html",
                           title="{} Destinations".format(location),
                           layout=location.lower(),
                           referral=get_referral(),
                           destinations=get_destinations(location))


@app.route('/destination/<location>/')
def destination_page(location):
    body = """<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
              Curabitur arcu tellus, condimentum at mauris porta, sodales
              placerat orci. Aenean lacinia aliquam ultricies. In ultricies
              bibendum nisl a rhoncus. Morbi tempus eros eu urna tincidunt
              dapibus. Nam tempor, nisl at sodales adipiscing, elit arcu
              vehicula arcu, et vulputate nunc lorem quis dolor. Ut porta
              auctor ultricies. Ut nec ante porttitor, aliquam est ut,
              placerat turpis. Sed posuere orci id dui varius, id rhoncus
              felis varius. Nam suscipit lorem eget ligula vulputate, sed
              interdum odio sagittis.</p>
              <p>Cras id magna vitae velit placerat scelerisque id id diam.
              Sed hendrerit faucibus nisl eu lobortis. Praesent accumsan
              pellentesque nunc a pellentesque. In hac habitasse platea
              dictumst. Morbi et viverra enim. Donec tempus orci et ipsum
              mattis, vitae posuere urna tempus. Nam iaculis rhoncus augue, in
              tincidunt nisl mattis vitae. Suspendisse pretium urna nec
              tristique mattis. Mauris mollis nisi at sem sodales, at tincidunt
              libero aliquet. Nullam vitae feugiat nibh.</p>
           """
    return render_template("destination.html",
                           title="{}".format(location),
                           body=body,
                           layout="destination",
                           referral=get_referral(),
                           tours=get_tours(location))


@app.route('/tour/<tour>/')
def tour_page(tour):
    return render_template("contact.html",
                           parent="tour.html",
                           layout="tour",
                           tour=get_tour(0),
                           referral=get_referral())


@app.route('/contact/', methods=["POST"])
def handle_contact_form():
    return "This is not yet functioning."


def get_copy(name):
    v = None
    for i in copy:
        if i['name'] == name:
            v = i

    return v


def get_referral():
    referral = "This is a referral from an existing customer."
    customer = "John Doe"
    return referral, customer


def get_regions():
    return [{"name": "test", "summary": "test summary"},
            {"name": "test", "summary": "test summary"}]


def get_tours(destination=None, featured=False):
    matching_tours = []
    if destination:
        for tour in tours:
            if tour["destination_id"] == destination:
                matching_tours.append(tour)
    elif featured:
        for tour in tours:
            if tour["featured"]:
                matching_tours.append(tour)
                break
    else:
        raise IndexError

    return matching_tours


# Unfinished or temporary functions for development
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


def get_destination():
    pass


def get_tour(tour_id):
    name = "Test Tour"
    copy = """
    <p>This section is for descriptions of the tour.</p>
    <p>Key highlights, sales copy, that sort of thing.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    Curabitur arcu tellus, condimentum at mauris porta, sodales placerat orci.
    Aenean lacinia aliquam ultricies. In ultricies bibendum nisl a rhoncus.
    Morbi tempus eros eu urna tincidunt dapibus. Nam tempor, nisl at sodales
    adipiscing, elit arcu vehicula arcu, et vulputate nunc lorem quis dolor.
    Ut porta auctor ultricies. Ut nec ante porttitor, aliquam est ut,
    placerat turpis. Sed posuere orci id dui varius, id rhoncus felis varius.
    Nam suscipit lorem eget ligula vulputate, sed interdum odio sagittis.</p>
    """
    return {"name": name, "copy": copy, "itinerary": get_itinerary(1)}


def get_itinerary(key):
    return [{"number": 1, "summary": "Day one summary",
             "landmarks": get_landmarks(0)},
            {"number": 2, "summary": "Day two summary",
             "landmarks": get_landmarks(0)}]


def get_landmarks(key):
    return [{"name": "Landmark", "copy": "Landmark copy"} for x in range(2)]