from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)





























"""
##################################### TO BE MOVED LATER ############################

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store (replace with a database in a real-world scenario)
people_data = {'name'}





@app.route('/create_person', methods=['POST', 'GET'])
def create_person():
    if request.method == 'POST':
        data = request.get_json()

        name = data.get('name')
        password = data.get('password')
        initial_amount = data.get('initial_amount', 0)

        if name is None or password is None:
            return jsonify({'error': 'Name and password are required'}), 400

        if name in people_data:
            return jsonify({'error': 'Person with that name already exists'}), 400

        people_data[name] = {'name': name, 'password': password, 'amount': initial_amount}

        return jsonify({'message': 'Person created successfully'}), 201

@app.route('/add_money/<name>', methods=['PATCH'])
def add_money(name):
    data = request.get_json()
    password = data.get('password')
    amount = data.get('amount')

    if name not in people_data:
        return jsonify({'error': 'Person not found'}), 404

    if password != people_data[name]['password']:
        return jsonify({'error': 'Access denied. Incorrect password'}), 403

    if amount is None or not isinstance(amount, (int, float)):
        return jsonify({'error': 'Invalid amount'}), 400

    people_data[name]['amount'] += amount

    return jsonify({'message': 'Money added successfully'}), 200

@app.route('/subtract_money/<name>', methods=['PATCH'])
def subtract_money(name):
    data = request.get_json()
    password = data.get('password')
    amount = data.get('amount')

    if name not in people_data:
        return jsonify({'error': 'Person not found'}), 404

    if password != people_data[name]['password']:
        return jsonify({'error': 'Access denied. Incorrect password'}), 403

    if amount is None or not isinstance(amount, (int, float)):
        return jsonify({'error': 'Invalid amount'}), 400

    if people_data[name]['amount'] < amount:
        return jsonify({'error': 'Insufficient funds'}), 400

    people_data[name]['amount'] -= amount

    return jsonify({'message': 'Money subtracted successfully'}), 200

@app.route('/get_person/<name>', methods=['GET'])
def get_person(name):
    data = request.get_json()
    password = data.get('password')

    if name not in people_data:
        return jsonify({'error': 'Person not found'}), 404

    if password != people_data[name]['password']:
        return jsonify({'error': 'Access denied. Incorrect password'}), 403

    return jsonify(people_data[name])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


"""