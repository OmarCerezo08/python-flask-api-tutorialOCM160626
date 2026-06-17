from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de datos en memoria (Lista global)
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

# 1. Endpoint para OBTENER todas las tareas
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200

# 2. Endpoint para AGREGAR una nueva tarea
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    
    if not request_body:
        return jsonify({"error": "Body cannot be empty"}), 400
        
    todos.append(request_body)
    return jsonify(todos), 200

# 3. Endpoint para ELIMINAR una tarea por su posición
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    # Validamos si la posición existe en la lista
    if position >= len(todos) or position < 0:
        return jsonify({"error": "Position out of range"}), 404
        
    todos.pop(position)
    return jsonify(todos), 200

# Siempre al final del archivo para arrancar el servidor
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)

