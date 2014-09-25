import json
from settings import API_KEY
from nuapiclient import NorthwesternAPIClient

# Initialize an API client with your key
client = NorthwesternAPIClient(API_KEY)

# First, list all of the terms
terms = client.terms()

# The terms come sorted from most recent to least recent
latest_term = terms[0]

# Get the first class in the first subject for the most recent term
subjects = client.subjects(term=latest_term['id'])
latest_subject = subjects[0]
courses = client.courses(term=latest_term['id'],
                         subject=latest_subject['symbol'])

# Print it out
print 'Here\'s the first class in %s for %s:' %\
            (latest_subject['name'], latest_term['name'])
print json.dumps(courses[0], indent=4)
