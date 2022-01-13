#Project setup

##Installation
1. Open terminal inside the repository
2. Execute docker setup via `docker-compose build` then `docker-compose up`

##API
* Access API on host `GET: 0.0.0.0:8000/api`
* Get specific data via ID `GET: 0.0.0.0:8000/api/{id}`


* Update specific data via ID 
* `{'school_name': 'New name'}`
* `PUT: 0.0.0.0:8000/api/{id}`


* Search DBN via `GET: 0.0.0.0:8000/api?q={DBN}`