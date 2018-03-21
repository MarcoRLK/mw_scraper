import pandas as pd
import numpy as np
from scraping_test import Scraper

scraper = Scraper()
dates = pd.date_range('2018-01-01', periods=70, freq='M')
course_names = []
course_credits = []
scraper.mw_scrapper(course_names, course_credits)

print (len(course_names))

# df = pd.DataFrame(np.random.randn(70,4), columns=['Data*', 'B', 'C', 'D'])
df = pd.DataFrame( course_credits, columns=['Creditos'], index=course_names )

print(df)
