import requests
import csv
from bs4 import BeautifulSoup

html = requests.get('https://www.sliit.lk/computing/programmes/')
s = BeautifulSoup(html.content, 'html.parser')

results00 = s.find('div', class_='row gutter-xs')
degree = results00.find_all('a')

degreeLinkArray=[]
degreeCurtinLinkArray=[]

for link in degree[2:len(degree)-7]:
    if link.has_attr('href'):
        if link.text.endswith("– Curtin University"):
            degreeCurtinLinkArray.append(link['href'])
            print("curtin")
        else:
            degreeLinkArray.append(link['href'])
            print("normal")

with open('Sliit_Computing.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Program", "Category", "Location", "Type", "Duration", "Schedule", "University", "Link"])

    for degree_link in degreeLinkArray:
        html = requests.get(degree_link)
        s = BeautifulSoup(html.content, 'html.parser')

        degreeName = s.find('h3', class_='tbk__title').get_text(strip=True)
        degreeSubtitle = s.find('h3', class_='tbk__subtitle').get_text(strip=True)
        degreeNameText = f"{degreeName} {degreeSubtitle}"

        details = s.find_all('span', class_='znListItems-text')
        duration = next((d.get_text(strip=True).replace('Duration: ', '') for d in details if 'Duration' in d.get_text()), '')
        location = next((d.get_text(strip=True).replace('Location: ', '') for d in details if 'Location' in d.get_text()), '')

        writer.writerow([degreeNameText, "Computing", location, "Degree", duration, "Full Time", "Normal", degree_link])

    for curtin_link in degreeCurtinLinkArray:
        html = requests.get(curtin_link)
        s = BeautifulSoup(html.content, 'html.parser')        

        paragraphs = s.find_all('p')
        if len(paragraphs) >= 6:
            program_name = paragraphs[0].get_text(strip=True)
            location = paragraphs[5].get_text(strip=True)
            duration = paragraphs[4].get_text(strip=True)
            description = paragraphs[1].get_text(strip=True)

            writer.writerow([program_name, "Computing", location, "Degree", duration, description, "Curtin University", curtin_link])
