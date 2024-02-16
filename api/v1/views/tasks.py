#!/usr/bin/python3
"""Object that handles all default RestFul API actions for Tasks."""

from models.task import Task
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/tasks', methods=['GET'], strict_slashes=False)
@swag_from('documentation/tasks_api_docs.yml')
def get_tasks():
    """Retrieves the list of all Task objects."""
    all_tasks = storage.all(Task).values()
    list_tasks = []
    for task in all_tasks:
        list_tasks.append(task.to_dict())
    return jsonify(list_tasks)


@app_views.route('/tasks/<task_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/tasks_api_docs.yml', methods=['get'])
def get_task(task_id):
    """Retrieves a specific task."""
    task = storage.get(Task, task_id)
    if not task:
        abort(404)

    return jsonify(task.to_dict())

@app_views.route('/tasks', methods=['POST'], strict_slashes=False)
@swag_from('documentation/tasks_api_docs.yml', methods=['POST'])
def post_task():
    """Create a new task."""
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'task_name' not in request.get_json():
        abort(400, description="Missing task name")
    if 'task_description' not in request.get_json():
        abort(400, description="Missing task description")

    data = request.get_json()
    instance = Task(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/tasks/<task_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/tasks_api_docs.yml', methods=['PUT'])
def put_task(task_id):
    """Update a task"""
    task = storage.get(Task, task_id)

    if not task:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(task, key, value)
    storage.save()
    return make_response(jsonify(task.to_dict()), 200)


@app_views.route('/tasks/<task_id>', methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/tasks_api_docs.yml', methods=['DELETE'])
def delete_task(task_id):
    """Delete a Task Object from the database."""
    task = storage.get(Task, task_id)

    if not task:
        abort(404)

    storage.delete(task)
    storage.save()
    return make_response(jsonify({}), 200)
