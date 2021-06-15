import mwclient

username = "Cqsi" # sätt användarnament för botten här
password = open("password.txt", "r").read() # Mitt lösenord är i denna fil och därför finns inte filen på Github

lang = "sv" # fi/sv/en etc

site = mwclient.Site(lang + ".wikipedia.org")
site.login(username, password)

def bulk_change(word, change):

    # load Wikipedia page
    page = site.pages["Kirjais"]

    if page.exists:
        article_text = page.text()

        text = article_text.replace(word, change)
        print(text)

    else:
        print("Wikipedia page doesn't exist")

    # make the output clearer
    print()
    print("************************************************************")
    print()

        
bulk_change("Nagu", "Pargas")