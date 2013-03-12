myProject
=========

Script to fetch data from http://vimoe.com and to store it in the database. And a front-end is also there to check the functionality.

I have user 3rd party API's like Dajax/Dajaxice, BeautifulSoup etc.

Steps to make this project working-
1. Create a virtual env
2. Install django
3. pip install dajaxice
4. pip install dajax
5. pip install beautifulsoup4
6. Download this project
7. cd myProject-master
8. DO some changes in settings.py
9. Change the path of views.py and crawlwer.py in myProject-master/myProject/Premiere
10. Python manage.py syncdb
11. python manage.py runserver

You are Done!

You have to run the crawler crawler.py from command prompt. This will run the crawler and start fetching data(ids) to file.

url /index will save the Vimeo User data from file that crawler.py has created to MySQL database. 

url /home will take you to the front-end.

