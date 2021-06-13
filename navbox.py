import mwclient
import pandas as pd
import re

username = "Cqsi" # sätt användarnament för botten här
password = open("foo.txt", "r").read() # Mitt lösenord är i denna fil och därför finns inte filen på Github

lang = "fi" # fi/sv/en etc

site = mwclient.Site(lang + ".wikipedia.org")
site.login(username, password) 
    
def read(article):
    page = site.pages[article]

    if page.exists:
        return page.text()
    else:
        return "Wikipedia page doesn't exist"

def add_navbox(excel_file, navbox):

    try:
        df = pd.read_excel(excel_file, engine='openpyxl')
        print("Excel read.")
    except:
        print("Something went wrong. Check the path of the file.")

    for index, row in df.iterrows():
        cur = row["artikel"]
        
        text = read(cur)
        print(text)

#add_navbox("input.xlsx", "{{Nauvo}}")