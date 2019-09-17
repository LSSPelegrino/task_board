# Task board
### A simple task board, made using Flask 

## Setup
Prerequisites:
* Python 3.7

Clone the repository using:  
```bash
$ git clone https://github.com/LSSPelegrino/task_board.git
```
Navigate to the created folder and create a virtual environment. I recommend [virtualenvwrapper](https://medium.com/the-andela-way/configuring-python-environment-with-virtualenvwrapper-8745c2895745).


With a virtual enviroment activated, install the requirements running the following command at the project's root:
```bash
(venv) $ pip install -r requirements.txt 
```
After the installation is complete, run:
```bash 
(venv) $ flask run
```
The development server should be running on [localhost](127.0.0.1:5000).

The database runs on SQLite and the repository ships with an example database.

## API
The current version does not have a front end, but it's possible to test the API requests. 

The following actions are allowed:


Action  | HTTP Verb |URL Path                      | Description
:------:|:---------:|------------------------------|---
Read    |```GET```  |```/api/tasks/?page=1&per_page=10```|URL to read tasks in a paginated manner
Create  |```POST``` |```/api/task```               |URL to add a task
Update  |```PUT```  |```/api/task/{task_id}```     |URL to edit a task
Read    |```GET```  |```/api/task/{task_id}```     |URL to read a specific task
Update  |```PUT```  |```/api/task/{task_id}/done```|URL to toggle task as done

Date and time must be passed as [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations). Example: 1989-09-18T08:00-04:00. 

All date and times returned are UTC.

If you'd like to try the API, I recommend using [HTTPie](https://httpie.org/doc#installation). 

The following examples are based on HTTPie's syntax:

```bash
$ http GET "http://localhost:5000/api/tasks?page=2&per_page=2"
```

```bash
HTTP/1.0 200 OK
Content-Length: 660
Content-Type: application/json
Date: Mon, 16 Sep 2019 23:51:00 GMT
Server: Werkzeug/0.15.6 Python/3.7.4

{
    "_meta": {
        "page": 2,
        "per_page": 2,
        "total_items": 5,
        "total_pages": 3
    },
    "items": [
        {
            "completed_at": "2019-09-15T04:16:42.595Z",
            "deadline": "1982-01-01T00:00:00.000Z",
            "description": "You have to let that raga drop",
            "done": true,
            "task_id": 3,
            "title": "Rock the casbah"
        },
        {
            "completed_at": null,
            "deadline": "2005-02-02T00:00:00.000Z",
            "description": "All that I can do",
            "done": false,
            "task_id": 4,
            "title": "Be yourself"
        }
    ]
}
```
```bash
$ http POST http://localhost:5000/api/tasks "title=Get up, stand up" "description=Don't give up the fight" "deadline=1973-01-01T00:00:00.000-05:00"
```
```bash
HTTP/1.0 201 CREATED
Content-Length: 181
Content-Type: application/json
Date: Mon, 16 Sep 2019 23:57:19 GMT
Location: http://localhost:5000/api/tasks/6
Server: Werkzeug/0.15.6 Python/3.7.4

{
    "completed_at": null,
    "deadline": "1973-01-01T05:00:00.000Z",
    "description": "Don't give up the fight",
    "done": false,
    "task_id": 6,
    "title": "Get up, stand up"
}

```

```bash
$ http PUT http://localhost:5000/api/tasks/6 "deadline=1981-05-11T00:00:00.000-05:00"
```
```bash
HTTP/1.0 200 OK
Content-Length: 182
Content-Type: application/json
Date: Tue, 17 Sep 2019 00:44:15 GMT
Server: Werkzeug/0.15.6 Python/3.7.4

{
    "completed_at": null,
    "deadline": "1981-05-11T05:00:00.000Z",
    "description": "Don't give up the fight",
    "done": false,
    "task_id": 6,
    "title": "Get up, stand up"
}

```

```bash
$ http GET http://localhost:5000/api/tasks/1
```
```bash
HTTP/1.0 200 OK
Content-Length: 179
Content-Type: application/json
Date: Tue, 17 Sep 2019 00:47:24 GMT
Server: Werkzeug/0.15.6 Python/3.7.4

{
    "completed_at": "2019-09-15T04:16:42.593Z",
    "deadline": "2015-04-15T10:41:00.000Z",
    "description": "Just do it",
    "done": true,
    "task_id": 1,
    "title": "Do it"
}
```

```bash
$ http PUT http://localhost:5000/api/tasks/1/toggle_done
```
```bash
HTTP/1.0 200 OK
Content-Length: 158
Content-Type: application/json
Date: Tue, 17 Sep 2019 00:50:43 GMT
Server: Werkzeug/0.15.6 Python/3.7.4

{
    "completed_at": null,
    "deadline": "2015-04-15T10:41:00.000Z",
    "description": "Just do it",
    "done": false,
    "task_id": 1,
    "title": "Do it"
}

```

## Built with
* [Flask](https://palletsprojects.com/p/flask/)

## To do list

* Build a simple front end
* Add unit tests
* Implement API authenticators 
* Migrate to a better database software, possibly PostgreSQL

## Acknowledgements
* Heavily based on Miguel Grinberg's [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) 