from bs4 import BeautifulSoup as soup
from urllib2 import urlopen as uReq


class Scraper:
    #grabbing the page
    def page_grabber(self):
        uClient = uReq("https://matriculaweb.unb.br/graduacao/fluxo.aspx?cod=6360")
        page_html = uClient.read()
        uClient.close()
        return page_html

    #html parser
    def html_parser(self, page_html):
        page_soup = soup(page_html, 'html.parser')
        return page_soup

    def get_courses_tables(self, page_soup):
        courses_tables = page_soup.findAll('div', {'class', 'table-responsive'})
        courses_tables.pop(0)
        return courses_tables


    def get_courses_datas(self, courses_tables):
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

    def mw_scrapper(self):
        page_html = self.page_grabber()
        page_soup = self.html_parser(page_html)
        courses_tables = self.get_courses_tables(page_soup)
        self.get_courses_datas(courses_tables)
