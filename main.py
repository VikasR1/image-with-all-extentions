import requests
from bs4 import BeautifulSoup
import shutil   # library to import files from urls

url = input("enter your url")
response= requests.get(url)

filename = "temp.html"
soup = BeautifulSoup(response.text, "html.parser")

formatted_text = soup.prettify()

try:
    with open(filename, "w+") as f:
        f.write(formatted_text)
except Exception as e:
    print(e)

list_imgs = soup.find_all('img')
no_of_imgs = len(list_imgs)
# count the anchor tag
list_as = soup.find_all('a')
no_of_as = len(list_as)

print("number of img tags",no_of_imgs )
print("number of anchor tags", no_of_as)

# naming the images from 1 to ...
j=1
for imgTag in list_imgs:
    try:
        imgLink = imgTag.get('src')
        # print(imgLink)
        # checking image extention
        ext = imgLink[imgLink.rindex('.'): ]
        # selecting all extentions
        if ext.startswith(".png"):
            ext=".png"
        elif ext.startswith(".jpeg"):
            ext=".jpeg"
        elif ext.startswith(".jpg"):
            ext=".jpg"
        elif ext.startswith(".svg"):
            ext=".svg" 
        fileNameImg=str(j)+ext
        # requesting the image link
        imgresp = requests.get(imgLink, stream=True)
        # opening the file, in (mode or double quotation) "wb" for writing binary file
        with open(fileNameImg, "wb") as file:
            shutil.copyfileobj(imgresp.row,file)
    except Exception as e:
        print(e)
    j=j+1