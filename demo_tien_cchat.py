#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 23:00:38 2022

@author: trungle
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

soup = BeautifulSoup()

# Pagination setup

i = 1

# Generate list

my_data = []

# Retrieve website 

for i in range(1,12):
    
    url = f"https://cchatclothes.vn/san-pham-pc357299.html?page={i}"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "lxml")
    
    div_container = soup.find('div', id="product-lists")

    product_pane = div_container.findAll('div', {'class': "col-lg-25"})

# Scrap data from product pane
    for product in product_pane:
        
        product_name = product.find('div', class_ ='product-detail').a['title']
        product_image = product.find('div', class_ ='product-image').img['data-src']
        product_price = product.find('span', class_ ='single-price tp_product_price').text
        
        my_data.append(
            {"product_name": product_name,
             "product_image": product_image,
             "product_price": product_price})
    

# Output table

table_cchat = pd.DataFrame(my_data)

table_cchat.to_csv("table_cchat.csv")

