# Get the time of your GitHub membership using GitHub API.
# Written by: Filip J. Cierkosz
# Date: 02/2022

import json
from urllib.request import urlopen
from datetime import datetime

# Get the number of days of being a GitHub member.
def getMembershipTime(usr):
    # Specify and access the URL.
    url = 'https://api.github.com/users/'+usr
    response = urlopen(url)
    # Load JSON object.
    obj = json.load(response)
    # Get the date of starting a GitHub account, convert it into 
    # a datetime object, then return the membership period by
    # subtracting accStartDate from currDate.
    accStartDate = datetime.fromisoformat(obj['created_at'][:-1])
    currDate = datetime.today()
    memberTime = currDate-accStartDate
    return f'You have been a GitHub member for {memberTime.days} days.'

# Test harness.
usr = '' # <-- Specify your username here!
print(getMembershipTime(usr))
