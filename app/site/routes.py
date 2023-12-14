from flask import Blueprint, render_template

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
def profile():
    return render_template('profile.html')

@site.route('/women_cloths')
def women_cloths():
    return render_template('women_cloths.html')

@site.route('/men_cloths')
def men_cloths():
    return render_template('men_cloths.html')