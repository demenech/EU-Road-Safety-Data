# EU-Road-Safety-Data
This is my solution for the Data Wrangling Challenge for Datopian. <br>
My task was to create a script which would export the data from the 'European Union Road Safety Facts and Figures' table in [this Wikipedia article](https://en.wikipedia.org/wiki/Road_safety_in_Europe) to a CSV file. <br>
As a bonus, I have created [this spreadsheet](https://docs.google.com/spreadsheets/d/1UVr9ZxVYsvoBv68kA2QY_b77CwTDXsxAXf1i4JSYZf0/edit?usp=sharing) to display an insight on how GDP per capita and Vehicle ownership are related to Road Safety Deaths in the EU.

## What's contained in this repository
The repository has a script which generates a CSV file for the EU Road Safety Data and the resulting generated CSV file, aswell as the requirements.txt with the script's dependencies and the datapackage.json for the Tabular Data Package.

## Dependencies
- Python 3.7
- Requests Package
- BeautifulSoup Package

## How to run the script
Make sure you have Python 3.7 and Pip installed. The repository has a requirements.txt file, so the script's dependencies can be installed through:
1. Clone the repository
2. Navigate to the folder
3. Run: *pip install -r requirements.txt*

More on this process can be found in [this link](https://note.nkmk.me/en/python-pip-install-requirements/).
