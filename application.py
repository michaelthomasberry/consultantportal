# ___________CONSULTANT PORTAL_________
# Application allows users to:
# Feature 1: create projects, 
# Feature 2: View list of projects generated
# Feature 3: Request project support for specific projects

from cs50 import SQL
from flask import Flask, redirect, render_template, request

app = Flask(__name__)
db = SQL("sqlite:///projects.db")


@app.route("/")
def index():
    return render_template("index.html")
    
#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––    
# VIEW PROJECTS

@app.route("/view_projects")
def view_projects():
    #...select all the project data from database table 'projects'...
    rows = db.execute("SELECT * FROM projects")
    #... bring up webpage showing list of projects
    return render_template("viewmyprojects.html", rows = rows)
#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# REGISTER NEW PROJECT

@app.route("/register", methods=["GET","POST"])
def register():
    # bring up the webpage that shows the form.
    if request.method == "GET":
        return render_template("register.html")
    # assign each form data field to a varable. linking with register.html
    
    else:
        project_name = request.form.get("project_name")
        project_type = request.form.get("project_type")
        sector = request.form.get("sector")
        building_type = request.form.get("building_type")
        check_box = request.form.get("check_box")

        # insert the variable into the database
        db.execute("INSERT INTO projects (project_name, project_type, sector, building_type, check_box) VALUES (:project_name,:project_type,:sector,:building_type,:check_box)", project_name=project_name, project_type=project_type, sector=sector,building_type=building_type,check_box=check_box )
        return redirect("/view_projects")

#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––-––


    ## to change the port in flask you have to type: export FLASK_APP=application.py
