from urllib.request import urlopen
from bs4 import BeautifulSoup

#1 Dowload
website = urlopen("http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn")
html_content = website.read().decode("utf8")
website.close()

#2 Tìm thẻ table
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find('table',id = 'tableContent')
tr_list = table.find_all('tr')

#Code bằng cơm
# list_id = ['01', '02', '10', '11', '20',
#             '21', '22', '23', '24', '25', '26',
#             '30', '31', '32', '40','50', '51','52',
#             '60','61','62','70','80','81']

# for ids in list_id:
#     tr_list = table.find("tr", id = ids)
#     for td in tr_list:
#         content = td.string
#         if content == None:
#             continue
#         print(content)


for tr in tr_list:
    td_list = tr.find_all('td')

    print(td_list)
    for td in td_list:
        content = td.string
        if content == None:
           continue
        print(content)
        print("- "*20)
    
