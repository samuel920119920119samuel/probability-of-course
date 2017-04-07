import requests
from bs4 import BeautifulSoup

class_id = input('請輸入課程流水號：')
print (class_id)



class_url = 'https://course.ncu.edu.tw/Course/main/support/courseDetail.html?crs=' + str(class_id)

res = requests.get(class_url)
soup = BeautifulSoup(res.text)

total = 0
for item in soup.select('.even'):
    "print (item.select('td')[8].string)"
    if item.select('td')[7].string == "1" and item.select('td')[8].string == "The course is to be assigned.":
        total = total + 1
print (total)

for item in soup.select('.odd'):
    "print (item.select('td')[7].string)"
    if item.select('td')[7].string == "1" and item.select('td')[8].string == "The course is to be assigned.":
        total = total + 1
print (total)

"""
user_order = input('請輸入志願序：')
print (user_order)

while order <= user_order
    department==other_department && grade == other_grade
"""        
