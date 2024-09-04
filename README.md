# Django Recipe Application

## Goal
Learn to use Django and build an application to store and edit recipes. In connection with CareerFoundry Python for Web Developers course, This is my final project in the Full-Stack Web Developer program. 

## Main Functions
The main focus of this app is to view the recipe database I have created. The functions I built are a mix of GuerySet, Pandas, matpoltlib, and striaght python. The functions I am most proud of are as follows:

- SearchView()
  - This function is the backbone of the search page and allows you to search for a recipe and have the 'name' and 'ingredients' returned as well as a data visualization of how much time it takes to make the recipe in comparison to the other recipes in the database. 
  - This takes advantage of matplotlib, pandas, and QuesrySet functionality.
  - located: src | recipes | views.py

- get_chart()
  - This function feeds the chart data to the SearchView() function. This took me the most time to build because I needed to study up on matplotlib and how to build a function to get what I needed out of it.
  - Uses matplotlib and base64 functionality
  - located: src | recipes | utils.py

## Installation
TBA

