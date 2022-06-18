'''
Get the time of your GitHub membership using GitHub API.

Written by: Filip J. Cierkosz

Date: 02/2022
'''

import json
from urllib.request import urlopen
from datetime import datetime

# Get the number of days of being a GitHub member.
def get_membership_time(usr):
    url = 'https://api.github.com/users/'+usr
    response = urlopen(url)
    obj = json.load(response)
    # Get the date of starting a GitHub account, convert it into 
    # a datetime object, then return the membership period by
    # subtracting accStartDate from currDate.
    acc_start_date = datetime.fromisoformat(obj['created_at'][:-1])
    curr_date = datetime.today()
    member_time = curr_date-acc_start_date
    return f'You have been a GitHub member for {member_time.days} days.'

# Sample.
usr = '' # <-- Specify your username here!
print(get_membership_time(usr))
