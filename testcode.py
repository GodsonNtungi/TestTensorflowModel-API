import io
import os
import time

os
import base64
from PIL import Image
import requests

with open("obama.jpg", "rb") as img_file:
    stra= base64.b64encode(img_file.read())
    stra11=stra.decode('utf8')

    headers = {
        'accept': 'application/json',}
for i in range(1000):
    g=int(input("Enter 1 for get test , 2 for titanic post, 3 for picture post "))
    n=int(input("Number of pictures in a list: "))
    z=int(input("URL in use \n 0: local host \n 1:heroku host :  "))
    url_list=['http://127.0.0.1:3000/','https://titanicmodelapi89.herokuapp.com/']

    if g==1:
        with requests.get(url_list[z]) as res0:
            print(res0.text)
    elif g ==2:
        with requests.post(url_list[z]+'/titanicModel',headers=headers,json={'body':[[3,2,3,2,1]]}) as res1:
            print(res1.text)

    elif g == 3:
        picture_list=[]
        for i in range(n):
            picture_list.append(stra11)
        start = time.time()
        try:
            with requests.post(url_list[z]+'/imageprediction',json={'body':picture_list}) as res2:
                print(res2.text)
        except NameError:
            print("There was a problem")

        end = time.time()
        print(end-start)