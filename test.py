import mwclient
import pandas as pd

username = "PFredrikaBot" # sätt användarnament för botten här
password = open("password.txt", "r").read() # Mitt lösenord är i denna fil och därför finns inte filen på Github

lang = "fi" # fi/sv/en etc

site = mwclient.Site(lang + ".wikipedia.org")
site.login(username, password) 

edit_summary = "Added {{Nauvo}} navbox"

page = site.pages["Iso-Nauvo"]

if page.exists:
    article_text = page.text()

    if "{{Nauvo}}" not in article_text:

        text = article_text.replace("[[Luokka:", "{{Nauvo}}\n\n[[Luokka:", 1)
        print(text)
        
        # DO NOT RUN THE LINE BELOW IF YOU DON'T WANT TO EDIT THE ARTICLE
        page.edit(text, edit_summary)
    else:
        print("{{Nauvo}} already in page")

else:
    print("Wikipedia page doesn't exist")