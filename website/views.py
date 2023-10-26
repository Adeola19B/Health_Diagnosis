from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route("/")
def home():
    return render_template(r'base.html')

@views.route("/kidney_form")
def kidney_form():
    return render_template(r'kidney.html')



@views.route("/liver_form")
def liver_form():
    return render_template(r'liver.html')


@views.route("/stroke_form")
def stroke_form():
    return render_template(r'stroke.html')


@views.route("/diabete_form")
def diabete_form():
    return render_template(r'diabete.html')
