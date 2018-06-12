from flask import Flask, jsonify, render_template, request
from classes.manager import Manager
from classes.project import Project

import json
from pathlib import Path
app = Flask(__name__)

manager = Manager(load=True)

@app.route('/', methods=['GET'])
def index():
	'''
	Get projects template
	'''
	return render_template('template.html')

@app.route('/projects/get', methods=['GET', 'POST'])
def get():
	'''
	Get all projects.
	'''
	if 'name' in request.args:
		data = manager.get_projects(request.form['name'])
	else:
		data = manager.get_projects()
	return jsonify({'error': False, 'data': data})

@app.route('/projects/put', methods=['POST'])
def put():
	'''
	Create a new project.
	-> name
	-> repo_link
	-> port
	'''
	result = manager.add_project(Project(request.form['name'], request.form['repo_link'], request.form['port']))
	return jsonify({'error': result}) # Project successfully added

@app.route('/projects/put', methods=['POST'])
def post():
	'''
	Modify a project.
	-> name
	-> repo_link
	-> port
	'''
	for project in projects:
		if project.get_name() == request.form['name']:
			project.set_name(request.form['name'])
			project.set_repo_link(request.form['repo_link'])
			project.set_port(request.form['port'])
			return jsonify({'error': False}) # Project found and edited.
	return jsonify({'error': True}) # Project not found.

@app.route('/projects/delete', methods=['POST'])
def delete():
	'''
	Delete a project.
	-> name
	'''
	length = len(projects)
	for x in range(0, length):
		if projects[x].get_name() == request.form['name']:
			projects.remove(x)
			return jsonify({'error': False}) # Project found and deleted.
	return jsonify({'error': True}) # Project not found.

@app.route('/hook', methods=['POST'])
def hook():
	print(request.args)

if __name__ == '__main__':
	app.run(debug=True)
