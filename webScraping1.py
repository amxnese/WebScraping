import re
from bs4 import BeautifulSoup

#the text method is still working but it is deprecated that's why it's better to use re
soup = BeautifulSoup("<title>The Dormouse's story</title>","lxml")
txt = soup.find_all(string="The Dormouse's story") #Remember that this retursn a list'

#'string' method searches for the exact text so you had to use re in this case
soup = BeautifulSoup("<option value='certificate'>Certificate</option>",'lxml')
txt1 = soup.find_all(string=re.compile("Cert"))

#checking the text that a specific tag contains
soup = BeautifulSoup("<title><b>Hello</b> There",'lxml')
txt2 = soup.text #output: Hello There

#searching for a specific attrs in a non specific tag,if the attr is 'class' its better to use 'class_='
name_soup = BeautifulSoup('<input name="email"/>', 'lxml')
txt3 = name_soup.find_all(attrs={"name":"email"})

#Searching a tag by its CSS class
#passing 'class_' a string
soup = BeautifulSoup("<a class='sister' href='http://example.com/lacie' </a>","lxml")
txt4 = soup.find_all(class_="sister")

#passing 'class_' a function
soup = BeautifulSoup("<a class='sister'' href='http://example.com/elsie'>Elsie</a>","lxml")
def has_six_characters(css_class):
    return css_class is not None and len(css_class) == 6
txt5 = soup.find_all(class_=has_six_characters)

#we can limit the result that 'find_all' returns by passing a value to the 'limit' param
html = "<section><p>this is one</p> <p>this is two</p></section>"
soup = BeautifulSoup(html,"lxml")
txt6 = soup.find_all("p",limit=1) #returns a list of one item

#'find' is exactly as if we called 'find_all' with limit=1
txt7 = (soup.find("p")) #returns a string

#there is a shortcut for both find_all and find methods as they are the most used methods
soup("p") # ==> soup.find_all("p")
soup.p # ==> soup.find("p")

#difference between find_parent and find_parents
from bs4 import BeautifulSoup

html = """
<div class="grandparent">
    <div class="parent">
        <p class="child">Hello, world!</p>
    </div>
    <div class="parent">
        <p class="child">Goodbye, world!</p>
    </div>
</div>
"""
soup = BeautifulSoup(html,'html.parser')
tag = soup.find('p', class_='child')
parent_div = tag.find_parent('div') # the direct parent of the 'child' ==> parent
grand_parent_div = tag.find_parents('div') # the absolute parent of 'child' ==> grandparent

#find_next and find_all_next
#find_next returns the first next specific tag of another specific tag
#find_all_next returns every specific tag that comes after another specific tag
html = """
<div class="one">
    <div class="two">
        <p>from div two</p>
    </div>
    <div class="three">
        <p>from div three</p>
    </div>
</div>
"""
soup = BeautifulSoup(html,'lxml')
one = soup.find("div",class_="one") #OUTPUt ==> <div class="one">...</div>
two = one.find_next("div") #OUTPUT ==> <div class="two">...</div>
three = one.find_all_next("div") #OUTPUt ==> <div class="two"></div><div class="three"></div>
# the same concept for find_previous and find_all_previous