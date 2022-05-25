from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)
excel_file = pd.read_excel('plant.xlsx')

data = [
    ("01.07.2021", 51, 100),
    ("02.07.2021", 22, 80),
    ("03.07.2021", 70, 80),
    ("04.07.2021", 54, 80),
    ("05.07.2021", 48, 80),
    ("06.07.2021", 41, 60),
    ("07.07.2021", 74, 60),
    ("08.07.2021", 76, 60),
    ("09.07.2021", 78, 60),
    ("10.07.2021", 80, 60),
    ("11.07.2021", 82, 60),
    ("12.07.2021", 73, 60),
    ("13.07.2021", 51, 60),
    ("14.07.2021", 42, 40),
    ("15.07.2021", 76, 40),
    ("16.07.2021", 52, 40),
    ("17.07.2021", 66, 100),
    ("18.07.2021", 96, 100),
    ("19.07.2021", 98, 100),
    ("20.07.2021", 73, 100),
    ("21.07.2021", 67, 100),
]


@app.route('/')
def html_table():
    return render_template('index.html',  tables=[excel_file.to_html(classes='data', justify='center')])


@app.route('/chart')
def html_chart():
    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    data_water = [row[2] for row in data]
    return render_template('chart.html', labels=labels, values=values, data_water=data_water)