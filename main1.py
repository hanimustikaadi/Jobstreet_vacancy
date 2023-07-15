import requests
import json
from bs4 import BeautifulSoup

import os
import pandas as pd

# scraper = cloudscraper.create_scraper()
# url = 'https://www.indeed.com/q-odoo-remote-jobs.html?vjk=6a129b83abd8da73'
# s = requests.session()
# r = scraper(url)
# res = s.get(url)
# print(res.status_code)
# sp = BeautifulSoup(r.text,'html.parser')
# print(sp.title.text)





def input_url():
    url = input("Masukan url  :")
    return url


def get_total_page(url):
    url1 = f'{url}'
    res = requests.get(url1)
    soup = BeautifulSoup(res.text, 'html.parser')

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    with open('temp/res.html', 'w+') as outfile:
        outfile.write(res.text)
        outfile.close()

    total_pages = []
    # scraping step
    soup = BeautifulSoup(res.text, 'html.parser')
    tes = soup.find_all('option')
    for tes1 in tes:
        total_pages.append(tes1.text)

    total = max(total_pages)
    print('jumlah halaman: ' , total)


def get_all_items(url):
    url1 = f'{url}'
    res = requests.get(url1)
    soup = BeautifulSoup(res.text, 'html.parser')


    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    with open('temp/res.html', 'w+') as outfile:
        outfile.write(res.text)
        outfile.close()

    soup = BeautifulSoup(res.text, 'html.parser')
    content=soup.find_all('div','z1s6m00 _1hbhsw65a _1hbhsw6ga _1hbhsw6n _1hbhsw60 _1hbhsw662')

    jobs_list = [] #membuat tipe list
    i =1
    for item in content:
        title = item.find('h1', 'z1s6m00 _1hbhsw64y y44q7i0 y44q7i3 y44q7i21 y44q7ii')


        company = item.find('span', 'z1s6m00 bev08l1 _1hbhsw64y _1hbhsw60 _1hbhsw6r')

        dict = {
            'no': i,
            'title': title.text,
            'company': company.text
            #'link': link1



        }

        i=i+1
        jobs_list.append(dict) #membuat tipe list


    #membuat json file, json = list
    try:
        os.mkdir('json_result')
    except FileExistsError:
        pass

    with open('json_result/job_list.json', 'w+') as json_data:
        json.dump(jobs_list, json_data)
    print('jaon created')

    #create csv
    df = pd.DataFrame(jobs_list)
    df.to_csv('indeed_data.csv', index=False)
    df.to_csv('indeed_data.xlsx',index=False)

    #data created
    print('data created succes')

if __name__ == '__main__':
    url = input_url()
    get_all_items(url)
    get_total_page(url)






