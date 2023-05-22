#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    employee_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    # Fetch employee data
    response = requests.get(employee_url)
    if response.status_code != 200:
        print(f"Failed to retrieve employee data. Error: {response.status_code}")
        return

    employee_data = response.json()
    employee_name = employee_data['name']

    # Fetch TODO list for the employee
    response = requests.get(todos_url)
    if response.status_code != 200:
        print(f"Failed to retrieve TODO list data. Error: {response.status_code}")
        return

    todos_data = response.json()

    # Calculate progress
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task['completed']]
    num_completed_tasks = len(completed_tasks)

    # Display progress
    print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t{task['title']}")

# Usage example
employee_id = 1  # Replace with the desired employee ID
get_employee_todo_progress(employee_id)

