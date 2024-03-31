# School Management Platform

A platform for managing students, classrooms, subjects and attendances in a school.
Made with web2py and TypeScript.

## Installation
1. Execute the following command to run the project with Docker:
```bash
  docker-compose up --build -d
```
2. Access the application at [http://localhost:8000/](http://localhost:8000/)

## Usage
- On the initial page, you will see a list of cards corresponding to the actions available for each entity (students, classrooms, subjects and attendances).
- These actions are also available in the navigation bar.
- For each entity (except attendances), you can create, read, update and delete records.
- For attendances, you can only create and read records. The attendances correspond to the presence of students in a classroom on a given subject.
