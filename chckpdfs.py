#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 22:23:36 2022

@author: edombek
"""

import os

with open('index.html') as file:
    for i, line in enumerate(file.readlines()):
        if "href=" in line and "?file=https://raw.githubusercontent.com/rf-slf-4x1/site_materials/main/" in line and ".pdf" in line:
            file = line.split("?file=https://raw.githubusercontent.com/rf-slf-4x1/site_materials/main/")[1].split('"')[0]
            if not os.path.isfile('../site_materials/' + file):
                print(f'"{file}"')