import string
import requests
from tqdm import tqdm
import csv
from bs4 import BeautifulSoup, SoupStrainer


# Send a GET request to the specified URL
html = requests.get('https://www.nibm.lk/courses/degree/')

# Parse the HTML content using BeautifulSoup
s = BeautifulSoup(html.content, 'html.parser')

# Try to find and extract links for the 'campuscolombo-campus'
try:
    results00 = s.find('div', id='campuscolombo-campus')
    campuscolombo = results00.find_all('a')
except:
    pass
# Try to find and extract links for the 'campusrajagiriya-campus'
try:
    results01 = s.find('div', id='campusrajagiriya-campus')
    campusrajagiriya = results01.find_all('a')
except:
    pass
# Try to find and extract links for the 'campuskandy-campus'
try:
    results02 = s.find('div', id='campuskandy-campus')
    campuskandy = results02.find_all('a')
except:
    pass
# Try to find and extract links for the 'campusnic-kirulapone'
try:
    results04 = s.find('div', id='campusnic-kirulapone')
    campusnic = results04.find_all('a')
except:
    pass
# Try to find and extract links for the 'campuskandy-innovation-center'
try:
    results05 = s.find('div', id='campuskandy-innovation-center')
    campuskandyInnovation = results05.find_all('a')
except:
    pass



degreeLinkArray = []

# Try to extract href attributes from links and append to degreeLinkArray
try:
    
    for link in campuscolombo:
        if link.has_attr('href'):
            degreeLinkArray.append(link['href'])

    for link in campusrajagiriya:
        if link.has_attr('href'):
            degreeLinkArray.append(link['href'])

    for link in campuskandy:
        if link.has_attr('href'):
            degreeLinkArray.append(link['href'])

    for link in campusnic:
        if link.has_attr('href'):
            degreeLinkArray.append(link['href'])

    for link in campuskandyInnovation:
        if link.has_attr('href'):
            degreeLinkArray.append(link['href'])

except:
    pass

print(degreeLinkArray)

print(len(degreeLinkArray))
# Open a CSV file for writing
with open('degree.csv', 'w', newline='') as file:
    for x in range(0, len(degreeLinkArray)):

        # Send a GET request to the current degree link
        html = requests.get(degreeLinkArray[x])
        s = BeautifulSoup(html.content, 'html.parser')

        try:

            # Try to find and extract information from the current degree page
            results0 = s.find('div', class_='short-info-box fullwidth')
            duration = results0.find_all('span')

            results1 = s.find('div', class_='programme-title-name')
            degreeName = results1.find_all('h1')

            results2 = s.find('div', class_='programme-intro fullwidth')
            description = results2.find_all('p')

            print(x)
            print(degreeName[0].text)
            print(duration[0].text)
            print(duration[1].text)
            print(duration[3].text)
            print(degreeLinkArray[x])

            if duration[1].text == 'Business Analytics Centre' or duration[1].text =='Productivity and Quality Centre':

                display = [degreeName[0].text, duration[0].text, duration[2].text, duration[3].text, duration[4].text,duration[5].text,
                           degreeLinkArray[x]]
            else:
                display = [degreeName[0].text, duration[0].text, duration[1].text, duration[2].text, duration[3].text,duration[4].text,
                           degreeLinkArray[x]]
                

            # Write the extracted information to the CSV file
            writer = csv.writer(file)
            writer.writerows([display])


        except:
            pass




