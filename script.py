import webbrowser
import csv
with open('./links.csv') as file:
    links = csv.reader(file)
    for row in links:
        webbrowser.open_new_tab(row[0])
