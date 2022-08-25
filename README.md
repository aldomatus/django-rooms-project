<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/aldomatus/django-rooms-project">
    <img src="https://i.imgur.com/CgA9TyV.png" alt="Header" >
  </a>
   <div align="center">
   <a href="https://www.facebook.com/aldo.matusmartinez" ><img src="https://github.com/edent/SuperTinyIcons/blob/master/images/svg/facebook.svg" title="Facebook" width="60"  margin="30px"/></a><a href="https://github.com/aldomatus/" ><img src="https://github.com/edent/SuperTinyIcons/blob/master/images/svg/github.svg" title="Github" width="60"/></a><a href="https://www.instagram.com/aldomatus1/" ><img src="https://github.com/edent/SuperTinyIcons/blob/master/images/svg/instagram.svg" title="Instagram" width="60"  /></a><a href="https://www.linkedin.com/in/aldomatus/" ><img src="https://github.com/edent/SuperTinyIcons/blob/master/images/svg/linkedin.svg" title="Linkedin" width="60"  /></a>

  </div>

  <h4 align="center"></h4>

  <p align="center">
    A REST api made with Django Rest Framework in which you can practice the methods: GET, POST, PUT and DELETE, of a tasks list application. This API will be connected to the postgres database.
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project is made with the intention of create a REST API to book rooms and events
* Add the list of requirements in a requirements.txt file
* Create a REST API with the methods: GET, POST, PUT and DELETE
* Test endpoints

### Built With

Major technologies
* [Django](https://www.djangoproject.com/)
* [Postgres](https://www.postgresql.org/)

### Frameworks and Libraries 

#### Django
Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

#### Django Rest Framework
Django REST framework is a powerful and flexible toolkit for building Web APIs.

### To check your rest api
#### Insomnia

With their streamlined API client, you can quickly and easily send REST, SOAP, GraphQL, and GRPC requests directly within Insomnia.
Link to visit insomnia website: - [Link](https://insomnia.rest/download)
<div align="center">
 <img src=https://seeklogo.com/images/I/insomnia-logo-A35E09EB19-seeklogo.com.png width="100" alt="Header" >
  </div>


#### Postman
Postman is a collaboration platform for API development. Postman's features simplify each step of building an API and streamline collaboration so you can create better APIs—faster.
Link to visit postman website: - [Link](https://www.postman.com/downloads/)
<div align="center">
 <img src=https://seeklogo.com/images/P/postman-logo-F43375A2EB-seeklogo.com.png width="100" alt="Header" >
</div>


<!-- GETTING STARTED -->
## Getting Started



### Prerequisites
For this project you need to have the postgres database installed. If you have not installed it yet, you can create a dockerfile to run your database, you can work with its graphical interface or from the console, both ways will serve you.
Let's create a database from the terminal:

1. Once postgres is installed we can open a terminal and type the following code to access postgres
```docker
   docker run --name events -p 5433:5432 -e POSTGRES_USER=postgresUser -e POSTGRES_PASSWORD=postgresPW -e POSTGRES_DB=events -d postgres
```

### .env file 🌍 (Example)
```
DATABASE_HOST=192.168.0.116
DATABASE_USER=postgresUser
DATABASE_PASSWORD=postgresPW
DATABASE_NAME=events
DATABASE_PORT=5433
```

<!-- EXPLAIN CODE -->
## Description of the REST API code


### Installation

1. Clone the repo
   ```
   git clone git@github.com:aldomatus/django-rooms-project.git
   ```
  
2. inside our dir we create a virtual environment to have our libraries together.
  
      3.1 To download the library that allows us to create virtual environments
      ```
      sudo apt-get install python3-venv
      ```

      3.2. Create the virtual environment
      ```
      python3 -m venv env_dir
      ```
    
      3.3. Activate the virtual environment we go to the created folder and inside the terminal we write:
      ```
      source env_dir/bin/activate
      ```
  
3. Once the virtual environment is activated, we return to the folder where the requirements.txt file is and to install our libraries we must type the following line. (if you are using python 3 you only must type python3)
     ```
     python -m pip install -r requirements.txt
     ```

4. we run the server with...
     ```
     python manage.py runserver
     ```

5. If all goes well, our application should already be executing the manage.py file with python using the postgres database, now we just have to check by entering the following link in our browser:

   ```
   http://localhost:8000/
   ```
6. You should have a response like this:
   ```
   {
      "message": "Welcome to my API"
   }
   ```


<!-- USAGE EXAMPLES -->
## Usage

Inside the repository there is a file called api.postman collection.json with which the tests can be done towards the endpoints

### Requirements:
1. The business can create a room with M capacity
      * POST
      * Send the json through the url: http://127.0.0.1:8000/rooms/create/
     ```json
        {
         "is_available": 1,
         "capacity_of_users": 10,
         "busy_places": 0
        }
     ```
   Response example:
      ```json
        Status: 201 Created
        {
         "capacity_of_users": 10,
         "busy_places": 0,
         "is_available": true
        }
     ```


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/aldomatus/django-rooms-project/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Aldo Matus - [Linkedin](https://www.linkedin.com/in/aldomatus/) [Facebook](https://www.facebook.com/aldo.matusmartinez/)

Project Link: [Repository](https://github.com/aldomatus/django-rooms-project)
