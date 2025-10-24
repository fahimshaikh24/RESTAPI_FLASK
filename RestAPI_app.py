#RESTAPI APP USING FLASK
#AUTHOR: FAHIM SHAIKH

from flask import Flask, request, jsonify

app = Flask(__name__)

#Predefined User in memory
users = {
    1: {"name": "Fahim", "email": "fahim@example.com"}
}

# GET Method to view all the users in memory
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# POST Method to add new user in to the memory
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = len(users) + 1
    users[user_id] = data
    return jsonify({"message": "User added!", "user": users[user_id]})

# PUT Method to update a existing user in memory
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id in users:
        data = request.get_json()
        users[user_id].update(data)
        return jsonify({"message": "User updated!", "user": users[user_id]})
    return jsonify({"error": "User not found"}), 404

# DELETE Method to delete the user from memory
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted!"})
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
