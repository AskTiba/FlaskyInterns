# Import necessary dependencies:
from flask import Flask, jsonify, request

# Create an instance of the Flask application:
app = Flask(__name__)

# Create the in-memory data storage:
interns = {}

# Design the intern data structure:
class Intern:
    def __init__(self, name, email, start_date, end_date):
        self.name = name
        self.email = email
        self.start_date = start_date
        self.end_date = end_date

# Create an endpoint for registering new interns:
@app.route('/interns', methods=['POST'])
def register_intern():
    data = request.get_json()
    name = data['name']
    email = data['email']
    start_date = data['start_date']
    end_date = data['end_date']

    intern = Intern(name, email, start_date, end_date)
    interns[email] = intern

    return jsonify({'message': 'Intern registered successfully'})

# Implement an endpoint for retrieving all interns:
@app.route('/interns', methods=['GET'])
def get_all_interns():
    return jsonify({'interns': [intern.__dict__ for intern in interns.values()]})

# Develop an endpoint for editing interns:
@app.route('/interns/<email>', methods=['PUT', 'PATCH'])
def edit_intern(email):
    data = request.get_json()
    intern = interns.get(email)
    if intern:
        intern.name = data.get('name', intern.name)
        intern.start_date = data.get('start_date', intern.start_date)
        intern.end_date = data.get('end_date', intern.end_date)
        # You can update other fields similarly

        return jsonify({'message': 'Intern details updated successfully'})
    return jsonify({'message': 'Intern not found'})

# Implement an endpoint for deleting interns:
@app.route('/interns/<email>', methods=['DELETE'])
def delete_intern(email):
    if email in interns:
        del interns[email]
        return jsonify({'message': 'Intern deleted successfully.'})
    return jsonify({'message': 'Intern not found.'}), 404

# Define the route for searching interns:
@app.route('/search', methods=['GET'])
def search_interns():
    search_query = request.args.get('query')
    filtered_interns = [intern for intern in interns.values() if search_query in intern.name or search_query in intern.email]
    return jsonify({'interns': [intern.__dict__ for intern in filtered_interns]})

# Implement the route for sorting interns:
@app.route('/sort', methods=['GET'])
def sort_interns():
    sort_by = request.args.get('sort_by')
    if sort_by in ['name', 'email', 'start_date', 'end_date']:
        sorted_interns = sorted(interns.values(), key=lambda intern: getattr(intern, sort_by))
        return jsonify({'interns': [intern.__dict__ for intern in sorted_interns]})
    return jsonify({'message': 'Invalid sorting parameter.'}), 400

# Run the Flask application:
if __name__ == '__main__':
    app.run()
