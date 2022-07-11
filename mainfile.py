import pyshorteners

shortner = pyshorteners.Shortener()
link = input("Enter the link: ")

shorted_link =shortner.tinyurl.short(link)
print(shorted_link)

