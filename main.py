from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome('./chromedriver')

context_summary = []
title = []
votes = []
answers = []
views = []
tag = []
user = []
time = []
link = []
id1 = []

def sc():

    context  = driver.find_elements(By.XPATH, '//div[@class="s-post-summary    js-post-summary"]')
    for x in context:
        id1.append(x.get_attribute('data-post-id'))
        title.append(x.find_element(By.XPATH, '*//h3[@class = "s-post-summary--content-title"]').text)
        context_summary.append(x.find_element(By.XPATH, '*//div[@class = "s-post-summary--content-excerpt"]').text)
        v = x.find_elements(By.XPATH, '*//span[@class = "s-post-summary--stats-item-number"]')
        tagg = x.find_elements(By.XPATH, '*//li[@class = "d-inline mr4 js-post-tag-list-item"]')
        user__ = x.find_elements(By.XPATH, '*//a[@class = "flex--item"]')
        user.append(user__[0].text)
        tag.append([xxx.text for xxx in tagg])
        temp = [vv.text for vv in v]
        votes.append(temp[0])
        answers.append(temp[1])
        views.append(temp[2])
        s = (x.find_elements(By.XPATH, "*//time[@class = 's-user-card--time']/..//span[@title]"))
        time.append(s[1].get_attribute("title"))
        links = x.find_element(By.XPATH, "*//h3[@class='s-post-summary--content-title']/a").get_attribute('href')
        link.append(links)
        

page = 1
while page != 200:
    if page == 1:
        driver.get(f"https://stackoverflow.com/questions?tab=newest&page={page}&pagesize=50")
        sc()
        page += 1
    else:
        driver.get(f"https://stackoverflow.com/questions?tab=newest&page={page}&pagesize=50")
        sc()
        page += 1

data = pd.DataFrame({
    'id': id1,
    'User': user,
    'title': title,
    'body': context_summary,
    'tag' : tag,
    'Vote' : votes,
    'Answer': answers,
    'Views':  views,
    'Timestamp': time,
    'Links': link
        })


data.to_csv('file1.csv')