from flask import render_template, session, request, redirect, url_for, flash
from . import home

# Database
import database as db

# Line data
labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

values = [
    967.67, 1190.89, 1079.75, 1349.19,
    2328.91, 2504.28, 2873.83, 4764.87,
    4349.29, 6458.30, 9907, 16297
]

months = ["Unknown",
          "January",
          "Febuary",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"]

# Pages

@home.route('/')
def homepage():
  return render_template('page/index.html')

## statistics
@home.route('/statistics')
def stats():
  servers = db.get_all_servers()
  x = []
  for server in servers:
    e = server.id,server.name,server.usage['daily'],server.usage['monthly']
    x.append(e)
  return render_template('page/info.html',servers=x)

## statistics
@home.route('/stats/<id>')
def statss(id):
  server = db.server(id)
  colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]
  print(db.get_from_config('month',id))
  values = []
  max = 0
  labels = db.get_from_config('month',id)
  for label in labels:
    if max < int(db.get_from_config('month',id)[label]):
      max = int(db.get_from_config('month',id)[label])
    values.append(db.get_from_config('month',id)[label])
  new_labels = []
  for label in labels:
    new_labels.append(months[int(label)])
  return render_template('page/server_info.html',server=server, max=max, labels=new_labels, values=values)
