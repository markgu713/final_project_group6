import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
#from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, func, inspect
import sqlite3

app = Flask(__name__)

#################################################
# Database Setup
#################################################

# app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL', '') or "sqlite:///data/cacao_bean.sqlite"
# db = SQLAlchemy(app)

# # reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(db.engine, reflect=True)

conn = sqlite3.connect("data/cacao_bean.sqlite")

cur = conn.cursor()
cur.execute("SELECT * FROM cacao_clean_withbean")
cacao_table = cur.fetchall()
# print(cacao_table)
# Save references to each table
# tableList = Base.classes.keys()
# print(tableList)
# cacao_table = Base.classes.cacao_clean_withbean

# print(cacao_table)

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/manufacturing")
def manufacturingMain():
    return render_template("manufacturing.html")

@app.route("/marketplace")
def marketplace():
    return render_template("marketplace.html")

@app.route("/rawData")
def rawData():
    return render_template("data.html")

@app.route("/map")
def map():
    return render_template("map.html")

@app.route("/bean")
def bean():
    return render_template("bean.html")

@app.route("/data")
def data():
    cacao_data = jsonify(cacao_table)
    return cacao_data

@app.route("/manufacturing/<location>")
def manufacturing(location):
    """Return the MetaData for a given location."""
    # results = cur.execute(f"SELECT * FROM cacao_clean_withbean WHERE company_location='{location}'").fetchall()
    # Create a dictionary entry for each row of metadata information
    cacao_data = jsonify(cacao_table)
    return cacao_data

# def manufacturing(location):
#     """Return `otu_ids`, `otu_labels`,and `sample_values`."""
#     stmt = db.session.query(Samples).statement
#     df = pd.read_sql_query(stmt, db.session.bind)

#     # Filter the data based on the sample number and
#     # only keep rows with values above 1
#     cacao_data = df.loc[df[sample] > 1, ["company_location", "rating", "company", location]]
#     cacao_data.sort_values(by=location, inplace=True, ascending=False)
#     # Format the data to send as json
#     data = {
#         "company_location": cacao_data.company_location.values.tolist(),
#         "rating": cacao_data.rating.values.tolist(),
#         "company": cacao_data.rating.values.tolist(),
#     }
#     return jsonify(data)

# @app.route("/bean")
# def sourcing():
#     """Return the MetaData for a given sample."""
#     sel = [
#         cacao_table.specific_bean_origin,
#         cacao_table.bean_origin_country,
#         cacao_table.rating,
#         cacao_table.bean_type,
#     ]
#     results = db.session.query(
#         *sel).filter(cacao_table.company_location == location).all()

#     # Create a dictionary entry for each row of metadata information
#     cacao_data = {}
#     for result in results:
#         cacao_data["company_location"] = result[0]
#         cacao_data["rating"] = result[1]
#     print(cacao_data)
#     return jsonify(cacao_data)

if __name__ == "__main__":
    app.run()
