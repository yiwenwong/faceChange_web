# coding=UTF-8
import os

import requests
import json
import simplejson
import base64
import tkinter


def face(ff1, ff2):
    def find_face(img_url):
        url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
        data = {"api_key": 'w1dCuSyxycpc9W88J1ZTN6nHYLG1CkoU',
                "api_secret": '0vnq6zJb8VDR6p1Mc0gKssGnS4VD2xzM',
                "img_url": img_url,
                "return_landmark": 1
        }
        files = {"image_file": open(img_url, 'rb')}
        answer = requests.post(url, data=data, files=files)
        req_con = answer.content.decode("utf-8")
        req_dict = json.JSONDecoder().decode(req_con)
        req_json = simplejson.dumps(req_dict)
        req_json2 = simplejson.loads(req_json)
        faces = req_json2['faces']
        list0 = faces[0]
        rectangle = list0['face_rectangle']
        return rectangle

    def merge_face(img1_url, img2_url, img_afterurl, number):
        fa1 = find_face(str(img1_url))
        fa2 = find_face(str(img2_url))
        rec1 = str(str(fa1['top'])+','+str(fa1['left'])+','+str(fa1['width'])+','+str(fa1['height']))
        rec2 = str(str(fa2['top'])+','+str(fa2['left'])+','+str(fa2['width'])+','+str(fa2['height']))
        merge_url = 'https://api-cn.faceplusplus.com/imagepp/v1/mergeface'
        f1 = open(img1_url, 'rb')
        f1_b64 = base64.b64encode(f1.read())
        f1.close()
        f2 = open(img2_url, 'rb')
        f2_b64 = base64.b64encode(f2.read())
        f2.close()
        data={"api_key": 'w1dCuSyxycpc9W88J1ZTN6nHYLG1CkoU',
              "api_secret": '0vnq6zJb8VDR6p1Mc0gKssGnS4VD2xzM',
              "template_base64": f1_b64,
              "template_rectangle": rec1,
              "merge_base64": f2_b64,
              "merge_rectangle": rec2,
              "merge_rate": number
        }
        answer = requests.post(merge_url, data=data)
        req_con = answer.content.decode("utf-8")
        req_dict = json.JSONDecoder().decode(req_con)
        result = req_dict['result']
        afterimg = base64.b64decode(result)
        file = open(str(img_afterurl), 'wb')
        file.write(afterimg)
        file.close()

    basedir = "/Users/yiwenwong/Desktop/python_face/"
    fu1 =basedir+ff1
    fu2 =basedir+ff2
    fu3 =basedir+"afterface.jpg"
    merge_face(fu1, fu2, fu3, 100)