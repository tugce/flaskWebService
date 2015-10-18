from flask import Flask, jsonify, abort

app = Flask(__name__)

tasks = [{'id': 1, 'title': 'Do this', 'description': 'you need to do it', 'done': False},{'id': 2, 'title': 'todo 2', 'description': 'this is number 2 on your todo list', 'done': False}]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if(len(task) == 0):
        abort(404)
    return jsonify({'task': task[0]})
if __name__ == '__main__':
    app.run(debug=True)
