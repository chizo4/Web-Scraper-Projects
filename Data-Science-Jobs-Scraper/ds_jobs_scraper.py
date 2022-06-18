'''
Scrape latest Data Science job offers in London using Indeed API.

Note: If using, remember to specify your browser's User-Agent (line 27).

Author: Filip J. Cierkosz

Date: 01/2022
'''


from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime


# Array to store all the job items.
joblist = []


def get_data():
    '''
    Gets the data from the website.
    '''
    # Get the request from the specified website.
    headers = {'User-Agent':''} # <-- Specify your browser's User-Agent here!
    url = 'https://uk.indeed.com/jobs?q=data%20scientist%20%C2%A360%2C000&l=London%2C%20Greater%20London&vjk=8e4ebf6f8f6568f8'
    req = requests.get(url, headers)

    # Create the soup object specifying the HTML parser, then return it.
    soup = BeautifulSoup(req.content, 'html.parser')
    return soup


def refine_data(soup):
    '''
    Transforms the soup object, and extract the desired contents.
    '''
    # Find all the elements with the specified HTML tag and class name.
    divs = soup.find_all('div', class_='slider_item')

    # Iterate through all divs. For each offer, select: title, company, 
    # place, salary.
    for item in divs:
        title = item.find('h2').text.replace('new', '')
        company = item.find('span', class_='companyName').text
        place = item.find('div', class_='companyLocation').text[0:6]

        # Salary is not always published and so verify if it exists before
        # further refinement.
        try:
            salary = item.find('div', class_='salary-snippet').text
        except:
            salary = 'UNKNOWN'

        # Create a dictionary to store each data item, then append it in
        # the joblist array.
        job = {
            'title': title,
            'company': company,
            'place': place,
            'salary': salary
        }
        joblist.append(job)

    return joblist


def clear_file(fn):
    '''
    Optional usage. Clears the CSV datafile.
    '''
    f = open(fn, 'w+')
    f.close()
    print(f'The file {fn} has been cleared out.')


def main(fn):
    '''
    Invokes all functions and store the data in an appropriate file.
    '''
    # Clear the CSV file (optional).
    #clear_file(fn)

    # Get data from the website, then refine it.
    s = get_data()
    refine_data(s)

    # Create a pandas data frame and store the data in a CSV file.
    df = pd.DataFrame(joblist)
    df.to_csv(fn)

    # Create the datetime object of the current date and time.
    now = datetime.datetime.now()

    print(f'''
---------------
The datafile has been successfully updated!
Date of last update: {now.strftime('%d/%m/%Y %H:%M:%S')}.
---------------
''')


# Test harness.
if (__name__=='__main__'): 
    main('jobs.csv')
