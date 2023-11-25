
# Train and Pedal. Bicimad & Bicipark Explorer

# Data Project Bicimad or Bicipark 
## _Train and Pedal. Bicimad or Bicipark Explorer_


Welcome to the world of sustainable mobility. We will analyze two urban initiatives: Bicimad and Biciparkd. Our goal is to facilitate communications between sports centers and bike parks and to understand how these bicycle transportation options contribute to the sustainability of our city and improve the quality of life of its inhabitants.

Both proposals offer innovative solutions to encourage the use of bicycles as a means of transportation in urban environments.

## 🙋 Name
Bicimad & Bicipark Explorer

## 👶 Status

## 🏃 One-liner
Explore the world of urban cycling with Bicimad & Bicipark Explorer a project to analyze and visualize data from two prominent bike-sharing initiatives.

## 💻 Technology stack
- Python3
- Json
- Pandas as pd
- Requests
- Numpy as np
- Fuzz and process from fuzzywuzzy
- Argparse


## 💥 Core technical concepts and inspiration
The objective of Bicimad & Bicipark Explorer is to provide a complete overview of bicycle parking near our sports facilities, allowing users to compare and contrast the availability of Bicimad and Bicipark. The project is inspired by the growing importance of sustainable urban mobility and the need for instant information on this data.

We use geolocation techniques to provide accurate results based on the user's location. This allows us to identify and visualize the nearest sports facilities and bike stations in real time.

We implement fuzzy matching algorithms to improve search capabilities. These algorithms allow us to find approximate matches between text strings, making it easier to identify locations even when there are typos or differences in naming.

## 🔧 Configuration
Requirements
- Python3 
- Json
- Pandas as pd
- Requests
- Numpy as np
- Fuzz and process from fuzzywuzzy
- Argparse 

Prerequisites
- Python:
Bicimad & Bicipark Explorer is built using Python. Make sure you have Python installed on your system. You can download it from python.org.
- Pandas:
Bicimad & Bicipark Explorer relies on the Pandas library for data manipulation. Install it using the command:
```sh
pip install pandas
```
- FuzzyWuzzy:
FuzzyWuzzy is used for fuzzy string matching. Install it using the command:
```sh
pip install fuzzywuzzy
```
Installation Instructions:

- Clone the Repository:
Clone this repository to your local machine using the following command:
```sh
git clone [repository_url]
```
- Navigate to the Project Directory:
Change your working directory to the project folder:
``` sh
cd [project_folder]
```
- Install Dependencies:
Install the project dependencies by running the following command:
```sh
pip install -r requirements.txt
```
- Run the Application:
Execute the main script to run the Bicimad & Bicipark Explorer:
```sh
python script.py -a [application] -l [ocation]
```
## 🙈 Usage
Parameters
- Application: Choose between Bicimad or Bicipark.
- Location (optional): Specify a location to filter results using fuzzy matching.

Examples

Explore Bicimad:

```sh
python script.py -a BICIMAD
```
Explore Bicipark and filter by location "Parque":

```sh
python script.py -a BICIPARK -l "Parque"
```

## 📁 Folder Structure

└── __h_datamadpt0923_project_m1__

    ├── _wip_ 
    ├── modules
    ├── __pycache__
    │   └──  funciones.py
    |   └──  geo_calculations.py
    |   └── prog.py
    ├── notebooks
    │   ├── ipynb_checkpoints
    │   └── bicimad.ipynb 
    |   └── dev_notebook_ipynb
    ├── .gitignore
    ├── LICENSE
    ├── main.py
    ├── README
    ├── __trash__
    ├──  data
        ├── bicimad_data.csv
        ├── bicimad_stations.csv
        ├── bicipark_data.csv
        └── bicipark_stations.csv

## 💩 ToDo
Implement fuzzy matching for better location filtering.

Handle additional user input. 

## ℹ️ Further Info

Credits: 
- Open Data sources for Bicimad and Bicipark.

- Open data sources for sports centers 












 


 

