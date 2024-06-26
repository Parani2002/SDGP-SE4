import string
import requests
from tqdm import tqdm
import csv
from bs4 import BeautifulSoup, SoupStrainer

# Request HTML content from the webpage
html = requests.get('https://www.nibm.lk/courses/mba/')
s = BeautifulSoup(html.content, 'html.parser')

# Extract course links from different campuses
try:
    results00 = s.find('div', id='campuscolombo-campus')
    campuscolombo = results00.find_all('a')
except:
    pass

try:
    results01 = s.find('div', id='campusrajagiriya-campus')
    campusrajagiriya = results01.find_all('a')
except:
    pass

try:
    results02 = s.find('div', id='campuskandy-campus')
    campuskandy = results02.find_all('a')
except:
    pass

try:
    results04 = s.find('div', id='campusnic-kirulapone')
    campusnic = results04.find_all('a')
except:
    pass

try:
    results05 = s.find('div', id='campuskandy-innovation-center')
    campuskandyInnovation = results05.find_all('a')
except:
    pass


# Initialize arrays to store course links
degreeLinkArray = []

# Extract course links and append to degreeLinkArray
try:
    
    for link in campuscolombo:
        if link.has_attr('href'):
            degreeLinkArray.append(link['href'])
except:
    pass

try:
    for link in campusrajagiriya:
        if link.has_attr('href'):
            degreeLinkArray.append(link['href'])
except:
    pass

try:
    for link in campuskandy:
        if link.has_attr('href'):
            degreeLinkArray.append(link['href'])
except:
    pass

try:
    for link in campusnic:
        if link.has_attr('href'):
            degreeLinkArray.append(link['href'])
except:
    pass

try:
    for link in campuskandyInnovation:
        if link.has_attr('href'):
            degreeLinkArray.append(link['href'])

except:
    pass

# Print degreeLinkArray and its length for verification
print(degreeLinkArray)

print(len(degreeLinkArray))

# Open a CSV file to store course information
with open('Masters.csv', 'w', newline='') as file:
    for x in range(0, len(degreeLinkArray)):
        html = requests.get(degreeLinkArray[x])
        s = BeautifulSoup(html.content, 'html.parser')

        try:
            # Extract course information
            results0 = s.find('div', class_='short-info-box fullwidth')
            duration = results0.find_all('span')

            results1 = s.find('div', class_='programme-title-name')
            degreeName = results1.find_all('h1')

            results2 = s.find('div', class_='programme-intro fullwidth')
            description = results2.find_all('p')
            
            try:
                # Print course information
                print(x)
                print(degreeName[0].text)
                print(duration[0].text)
                print(duration[1].text)
                print(duration[3].text)
                print(degreeLinkArray[x])

                # Prepare course information for CSV writing
                if duration[1].text == 'Business Analytics Centre' or duration[1].text =='Productivity and Quality Centre':
                    
                    display = [degreeName[0].text, duration[0].text, duration[2].text, duration[3].text, duration[4].text,duration[5].text,
                               degreeLinkArray[x]]
                else:
                    display = [degreeName[0].text, duration[0].text, duration[1].text, duration[2].text, duration[3].text,duration[4].text,
                               degreeLinkArray[x]]
                    
            except:
                # Handling exceptions where some fields might be missing
                display = [degreeName[0].text, duration[0].text,None, duration[1].text, duration[2].text,duration[3].text,
                           degreeLinkArray[x]]
                
                    
            # Write course information to CSV file
            writer = csv.writer(file)
            writer.writerows([display])


        except:
            pass




