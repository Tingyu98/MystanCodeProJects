"""
File: webcrawler.py
Name: Ting_Yu
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male number: 10895302
Female number: 7942376
---------------------------
2000s
Male number: 12976700
Female number: 9208284
---------------------------
1990s
Male number: 14145953
Female number: 10644323
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #
        tags = soup.find_all(("table", {"class": "t-stripe"}))
        male_num = 0
        female_num = 0
        for tag in tags:
            lst = tag.tbody.text.split("\n")
            lst.pop(0)
            for i in range(400):
                if i % 2 == 1:
                    lst_ = lst[i].split()
                    male_number = int(lst_[1].replace(",", ""))
                    male_num += male_number
                    female_number = int(lst_[3].replace(",", ""))
                    female_num += female_number
            print(f"Male Number: {male_num}")
            print(f"Female Number: {female_num}")


if __name__ == '__main__':
    main()
