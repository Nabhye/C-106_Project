import plotly.express as px
import csv

with open('cups of coffee vs hours of sleep.csv') as file_csv:
    df = csv.DictReader(file_csv)
    fig = px.scatter(df, x="Coffee in ml", y="sleep in hours")
    fig.show()
