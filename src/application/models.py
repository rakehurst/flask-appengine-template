"""
models.py

App Engine datastore models

"""


from google.appengine.ext import ndb

class Fishery(ndb.Model):
    """Fishery Model"""
    name = ndb.StringProperty(required=True)
    description = ndb.TextProperty(required=True)
    nearest_town = ndb.StringProperty(required=True)
    nearest_county = ndb.StringProperty(required=True)
    address = ndb.StringProperty(required=True)
    telephone = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    website = ndb.StringProperty(required=True)
    water_type = ndb.StringProperty(required=True)
    fishery_type = ndb.StringProperty(required=True)
    stocked = ndb.StringProperty(required=True)
    permit_available = ndb.StringProperty(required=True)
    permit_contact = ndb.StringProperty(required=True)
    fascilities = ndb.StringProperty(required=True)
    species = ndb.StringProperty(required=True)
    longitute = ndb.StringProperty(required=True)
    latitude = ndb.StringProperty(required=True)
    created = ndb.DateTimeProperty(auto_now_add=True)


class ExampleModel(ndb.Model):
    """Example Model"""
    example_name = ndb.StringProperty(required=True)
    example_description = ndb.TextProperty(required=True)
    added_by = ndb.UserProperty()
    timestamp = ndb.DateTimeProperty(auto_now_add=True)
