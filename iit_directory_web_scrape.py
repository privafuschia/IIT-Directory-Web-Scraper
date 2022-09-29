import requests
from bs4 import BeautifulSoup

file = open('directories.txt', 'a')

for i in range(13):
    ## add number at end of link for page number
    URL = "https://www.iit.edu/directory?organization_type=All&title=&title_1=&page=" + str(i)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("article")

    for result in results:
        unit_type = result.find("li").text
        file.write(unit_type)

        unit_name = result.find("h3").text
        file.write(", " + unit_name)

        unit_email = result.find("span", class_="person-email")
        if unit_email:
            unit_email = unit_email.next.text
            file.write(", " + unit_email + "\n\n")
        else:
            file.write("\n\n")

        # unit_location = result.find("span", class_="profile-item__contact__item location")
        # if unit_location:
        #     unit_location = unit_location.next.next.text
        #     file.write("\n" + unit_location[1])

file.close()