import requests
from bs4 import BeautifulSoup

html_text = requests.get("https://www.jobindex.dk/jobsoegning/it/systemudvikling?q=Computer").content
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('h4')
cities = soup.find_all('span', class_='jix_robotjob--area')
field_stars = soup.find_all('div', class_="my-4 d-flex justify-content-between flex-column-reverse flex-md-row align-items-sm-end")
stars = [field.find('a', class_='jix-toolbar__rating-score') for field in field_stars]
ratings = [rating.find('a', class_='jix-toolbar__rating-count') for rating in field_stars]
paragraphs = soup.find_all('p')

for job, city, star, rate, paragraph in zip(jobs, cities, stars, ratings, paragraphs):
    job_text = job.text.strip()
    city_text = city.text.strip()
    star_text = star.text.strip() if star else ""
    rating_text = rate.text.strip() if rate else ""

    if job_text:
        print(job_text)
    if city_text:
        print(city_text)
    if star_text:
        print(star_text)
    if rating_text:
        print(rating_text)

    print()
