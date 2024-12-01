import json
import pytest
from app import app
from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.json
    tasks.append(task)
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if task_id < len(tasks):
        tasks.pop(task_id)
        return '', 204
    return jsonify({'error': 'Task not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_get_tasks(client):
    response = client.get('/tasks')
    assert response.status_code == 200
    assert response.json == []


def test_add_task(client):
    task = {'title': 'Test Task'}
    response = client.post('/tasks', data=json.dumps(task), content_type='application/json')
    assert response.status_code == 201
    assert response.json == task


def test_delete_task(client):
    task = {'title': 'Test Task'}
    client.post('/tasks', data=json.dumps(task), content_type='application/json')

    response = client.delete('/tasks/0')
    assert response.status_code == 204

    response = client.get('/tasks')
    assert response.json == []
