from bs4 import BeautifulSoup
with open('leetcode2.html','r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content,'lxml')
    # print(soup.prettify())
    tags = soup.findAll(href=True)
    for tag in tags:
        temp = tag.get('href')
        if temp[1]=='p':
            print(temp)
    # print('\n\n')
