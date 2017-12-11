from gmail import GMail,Message
from random import choice

file_names = ["1.html", "2.html", "3.html"]
file_name = choice(file_names)

reasons = ["ebola", "aids", "sap chet"]
reason = choice(reasons)

template_file = open("1.html", "r", encoding="utf8")
html_content = template_file.read()
template_file.close()

html_content = html_content.replace("{{reason}}", reason)


gmail = GMail("lamptit3110@gmail.com","lanaya1996")



msg = Message('Test Message',to = "lamptit96@gmail.com", html =html_content )






gmail.send(msg)
