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


   # loop through pages folders
   for page_d in os.listdir(_SRC_d):
      # avoid master folder
      if page_d == "master":
         continue

      print('page : '+page_d)

      page_d_path = os.path.join(_SRC_d,page_d)
      index_f_path = os.path.join(page_d_path, 'index.html')

      if not os.path.isfile(index_f_path):
         print("Index path is not a file, can't generate html : "+index_f_path)
         continue

      page_f = open(index_f_path, "r")
      page_html = page_f.read()
      page_dom = BeautifulSoup(page_html, 'html.parser')

      content = page_dom.find('div', {"class":"paper"})
      template_dom.find('div', {"id":"couve3"}).insert_before(content)


   # create main html file from filled template html dom
   build_html_f = os.path.join(_BUILD_d,'index.html')
   with open(build_html_f, 'w') as fp:
      fp.write(template_dom.prettify())


if __name__ == "__main__":
   main()
