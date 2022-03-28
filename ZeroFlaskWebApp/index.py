from flask import Flask, render_template, request, jsonify, redirect, url_for, Response
from uszipcode import SearchEngine
import json

app = Flask(__name__)

'''
This is the api that acts as a landing page, and displays a for to the user to enter the name and zipcode
'''
@app.route("/create_phrase", methods=['GET', 'POST'])
def landing_page():
    return render_template('index.html')


'''
This method converts the name into Pig Latin
'''
def convert_to_latin(input_str):
    names = input_str.split()
    final_name = ""
    for name in names:
        final_name = final_name + (name[1:] + name[0] + "ay").capitalize() + " "
    return final_name.strip()


'''This method is responsible to create a response dictionary containing the latin converted name, county and 
population. This dictionary is then converted into a response json '''
def build_response(name, zipcode):
    response_dict = {}
    latin_name = convert_to_latin(name)

    search = SearchEngine()
    population = search.by_zipcode(zipcode).population
    county = search.by_zipcode(zipcode).county

    response_dict['latin_name'] = latin_name
    response_dict['county'] = county
    response_dict['population'] = str(population)
    return response_dict


'''
On form submit, this fetch api is called which uses uszipcodes api to fetch county and population.
'''
@app.route("/fetch", methods=['POST'])
def fetch_data():
    print(request)
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    name = request.json.get('name', None)
    zipcode = request.json.get('zipcode', None)

    if not name:
        return jsonify({"msg": "Missing name parameter"}), 400
    if not zipcode:
        return jsonify({"msg": "Missing zipcode parameter"}), 400

    response_dict = build_response(name, zipcode)

    print(json.dumps(response_dict))

    return response_dict
