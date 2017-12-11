from urllib.request import urlopen
from bs4 import BeautifulSoup

#download website
website = urlopen("http://dantri.com.vn")
html_content = website.read().decode("utf8")

website.close()

#2: creat BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")
# print(soup.prettify())

ul_news = soup.find("ul", "ul1 ulnew")
# print(ul_news.prettify())
li_new_list = ul_news.find_all("li")

for li in li_new_list:
    a_link = li.h4.a
    title = a_link["title"]
    content = a_link.string

    print(content)
    print("_" * 20)
