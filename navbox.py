import mwclient
import pandas as pd

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

def add_nauvo_navbox(excel_file):

    try:
        df = pd.read_excel(excel_file, engine='openpyxl')
        print("Excel read.")
    except:
        print("Something went wrong. Check the path of the file.")

    for index, row in df.iterrows():
        cur = row["artikel"]
        
        article_text = read(cur)
        text = article_text.replace("[[Luokka:", "{{Nauvo}}\n[[Luokka:", 1)
        print(text)
        print()
        print("************************************************************")
        print()

add_nauvo_navbox("input.xlsx")