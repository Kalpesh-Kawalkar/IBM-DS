!mamba install bs4==4.10.0 -y
!pip install lxml==4.6.4
!mamba install html5lib==1.1 -y
# !pip install requests==2.26.0

# HTML File
'''
%%html
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>
<h3><b id='boldest'>Lebron James</b></h3>
<p> Salary: $ 92,000,000 </p>
<h3> Stephen Curry</h3>
<p> Salary: $85,000, 000 </p>
<h3> Kevin Durant </h3>
<p> Salary: $73,200, 000</p>
</body>
</html>
'''
# html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

# BeautifulSoup Object
soup = BeautifulSoup(html, "html.parser")

# Displays the content in html variable
print(soup.prettify())

tag_object=soup.title
print("tag object:",tag_object)

print("tag object type:",type(tag_object))

# Accessing tab objects
tag_object=soup.h3
tag_object

# Children, Parents and Siblings
tag_child =tag_object.b
tag_child

parent_tag=tag_child.parent
parent_tag

tag_object
tag_object.parent

sibling_1=tag_object.next_sibling
sibling_1

sibling_2=sibling_1.next_sibling
sibling_2

sibling_3=sibling_2.next_sibling
sibling_3

tag_child['id']
tag_child.attrs
tag_child.get('id')

tag_string=tag_child.string
tag_string
type(tag_string)

unicode_string = str(tag_string)
unicode_string

