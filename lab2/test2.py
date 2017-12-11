from urllib.request import urlopen
from bs4 import BeautifulSoup

website = urlopen("http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn")
html_content = website.read().decode("utf8")
website.close()


soup = BeautifulSoup(html_content, "html.parser")
table_news = soup.find("table", id = "tableContent")

tr_list = table_news.find_all("tr")

data_list = []
for tr in tr_list:
    td_list = tr.find_all('td')
    data = {}

    for index, td in enumerate(td_list):

        content = td.string
        if content != None:
            if index == 0:
                data["title"] = content.strip()
            elif index == 1:
                data["quy 1"] = content
            elif index == 2:
                data["quy 2"] = content
            else:
                data["quy 3"] = content


    if data != {}:
        data_list.append(data)
print(*data_list,sep = " ")
