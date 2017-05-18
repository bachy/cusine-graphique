#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Author: Bachir Soussi Chiadmi <bach>
# @Date:   18-05-2017
# @Email:  bachir@esadhar.net
# @Last modified by:   bach
# @Last modified time: 21-04-2017
# @License: GPL-V3


import sys, os, shutil
import markdown
# import mistune
from bs4 import BeautifulSoup
import pypandoc
import json
import re

_SRC_d = 'pages'
_BUILD_d = "build"
# CUR_PATH = os.path.dirname(os.path.abspath(__file__))

print("Building book")

def main():
   # clean build directory
   if os.path.isdir(_BUILD_d):
      shutil.rmtree(_BUILD_d, ignore_errors=True)
   os.mkdir(_BUILD_d)

   parse_pages()

def parse_pages():
   print("Parse book")

   # get template html
   template_f = open("templates/index.tpl.html", "r")
   template_html = template_f.read()
   template_dom = BeautifulSoup(template_html, 'html.parser')

   scss = "// compiled css\n\n"

   # loop through pages folders
   for page_d in os.listdir(_SRC_d):
      # avoid master folder
      if page_d == "master":
         continue

      print('page : '+page_d)

      page_id = page_d.replace(' ', '-')

      page_d_path = os.path.join(_SRC_d,page_d)
      index_f_path = os.path.join(page_d_path, 'index.html')
      if not os.path.isfile(index_f_path):
         print("Index path is not a file, can't generate html : "+index_f_path)
         continue

      styles_f_path = os.path.join(page_d_path, 'styles.css')
      if not os.path.isfile(styles_f_path):
         print("Styles path is not a file, can't generate css : "+styles_f_path)
         continue


      page_f = open(index_f_path, "r")
      page_html = page_f.read()
      page_dom = BeautifulSoup(page_html, 'html.parser')

      styles_f = open(styles_f_path, "r")
      styles = styles_f.read()

      scss += "."+page_id+"{\n"
      scss += "\t"+styles
      scss += "}\n\n"

      for div in page_dom.find_all('div', {"class":"paper"}):
         print(div['class'])
         div['class'].append(page_id)

         for img in div.find_all('img'):
            # print(img['src'])
            src = '../pages/'+page_d+'/'+img['src']
            img['src'] = src
            
         template_dom.find('div', {"id":"couve3"}).insert_before(div)


   # create main html file from filled template html dom
   build_html_f = os.path.join(_BUILD_d,'index.html')
   with open(build_html_f, 'w') as fp:
      fp.write(template_dom.prettify())

   build_scss_f = os.path.join(_BUILD_d,'styles.scss')
   with open(build_scss_f, 'w') as fp:
      fp.write(scss)


if __name__ == "__main__":
   main()
