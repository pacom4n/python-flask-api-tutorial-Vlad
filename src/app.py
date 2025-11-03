from flask import Flask, jsonify, request 

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "Walk the dog", "done": True },
    { "label": "Finish the Flask project", "done": False }
]


@app.route('/todos', methods=['GET'])
def get_todos():
    """Devuelve la lista completa de tareas en formato JSON."""
    return jsonify(todos)


@app.route('/todos', methods=['POST'])
def add_new_todo():
    """Recibe una nueva tarea JSON, la añade a la lista y devuelve la lista actualizada."""
    try:
        request_body = request.get_json(force=True)
    except Exception:
        return jsonify({"msg": "Request body must be valid JSON"}), 400
    
    if isinstance(request_body, dict):
        todos.append(request_body)
    else:
        return jsonify({"msg": "Request body must be a single todo item (dictionary)"}), 400
    
    return jsonify(todos)


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    """Elimina la tarea en la posición especificada y devuelve la lista actualizada."""
    print("This is the position to delete:", position)
    
    try:
        del todos[position] 
    except IndexError:
        return jsonify({
            "msg": f"Error: Position {position} is out of bounds. The list only has {len(todos)} elements."
        }), 400
        
    return jsonify(todos)


@app.route('/myroute', methods=['GET'])
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)