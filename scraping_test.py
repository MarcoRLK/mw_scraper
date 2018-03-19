from bs4 import BeautifulSoup as soup
from urllib2 import urlopen as uReq

#grabbing the page
uClient = uReq("https://matriculaweb.unb.br/graduacao/fluxo.aspx?cod=6360")
page_html = uClient.read()
uClient.close()

#html parser
page_soup = soup(page_html, 'html.parser')

courses_tables = page_soup.findAll('div', {'class', 'table-responsive'})
courses_tables.pop(0)

for semester in courses_tables:
    print('--------')
    semester_courses = semester.findAll('tr')
    semester_courses.pop(0)
    semester_courses.pop(0)

    for course in semester_courses:
        course_attributes = course.findAll('td')
        #getting only the text from couse 'a tag'
        course_name = course_attributes[4].find('a').contents[0]
        
        course_credits = course_attributes[5].contents[0]

        print (course_name + ' ' + course_credits)
