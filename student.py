import plotly.express as px
import csv

with open('Student Marks vs Days Present.csv')as file_csv:
    df = csv.DictReader(file_csv)
    fig = px.scatter(df, x="Marks In Percentage", y="Days Present")
    fig.show()