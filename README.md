<img src="https://img.shields.io/github/license/GabrielSantos198/LEMBRAR-ME_BACK-END?color=blue&style=for-the-badge" alt=""> <img src="https://img.shields.io/github/repo-size/GabrielSantos198/LEMBRAR-ME_BACK-END?style=for-the-badge" alt=""> <img src="https://img.shields.io/github/languages/count/GabrielSantos198/LEMBRAR-ME_BACK-END?style=for-the-badge" alt=""> <img src="https://img.shields.io/github/issues/GabrielSantos198/LEMBRAR-ME_BACK-END?color=blue&style=for-the-badge" alt=""> <img src="https://img.shields.io/github/issues-pr/GabrielSantos198/LEMBRAR-ME_BACK-END?color=blue&style=for-the-badge" alt=""> <img src="https://img.shields.io/github/stars/GabrielSantos198/LEMBRAR-ME_BACK-END?color=blue&style=for-the-badge" alt="">

<p align="center">
<img src="https://gabrielsantos198.github.io/LEMBRAR-ME_FRONT-END/imgs/computer.jpg" width=300px alt="">
</p>

<h1 align="center"> ⭐ LEMBRAR-ME API </h1>

<p align="center">
  ⭐ This is the README file for the LEMBRAR-ME API. It provides information about the API, how to use it, and how to contribute to the project.
</p>

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#table-of-contents)

<p align="center">
  <a href="#introduction"> 🧩 Introduction </a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#endpoints"> 🚀 Endpoints</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#dependencies"> 🧪 Dependencies</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#contribute">💡 Contribute</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#credits"> 🏆 Credits </a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</p>
<br/>

<a id="introduction"></a>
## 🧩 Introduction

***⭐ This project consists of a To-Do List API, which has been given the identifying name LEMBRAR-ME, that allows users to efficiently and organizedly manage their tasks. The API was developed using modern and scalable technologies such as Python, Django and Postgresql, and follows good development practices to ensure code quality and security. With the LEMBRAR-ME API, users will be able to create, update, and delete tasks. Additionally, the API has an excellent search feature so that users can easily find the tasks they want to perform. The objective of this project is to provide an effective solution for task management and can be easily integrated with other applications.***
<br/>
<br/>


<a id="endpoints"></a>
## 🚀 Endpoints
  > URL: https://lembrar-me-api.up.railway.app >>> All results were successfully achieved. In general, these are the results of each request.

⭐ Method | ⭐ Endpoint | ⭐ Explanation
|---|---|---|
GET | /annotations/ | Get all annotations
GET | /annotations/search/?q={query} | Search annotation
GET | /annotations/{id}/ | Get 1 annotation
POST | /api/token/ | Obtain access token
POST | /api/token/refresh/ | Update access token
POST | /api/register/ | Register user
POST | /subscribe/ | Subscribe 
POST | /contact/ | Get in touch
POST | /create/annotation/ | Create annotation
PUT | /api/update/password/ | Change user password
PUT | /annotations/update/{id}/ | Update annotation
DELETE | /api/delete/account/ | Delete user account
DELETE | /delete/annotation/{id}/ | Delete annotation
<br/> 

<a id="dependencies"></a>
## 🧪 Dependencies
> Requirements to rotate the code.
- Docker
- docker-compose
- git

<h4>Step-1</h4> <code>git clone link https://github.com/GabrielSantos198/LEMBRAR-ME_BACK-END/</code>

<h4>Step-2</h4> Change the values of environment variables in the docker-compose.yml.<br/><br/>

Key | Value
|---|---|
DEBUG | True/False
SECRET_KEY | Application secret key
EMAIL_HOST_USER | Your Gmail
EMAIL_HOST_PASSWORD | Gmail app password
CLOUD_NAME | Your name in Cloudinary
API_KEY | Your API key on Cloudinary
API_SECRET | Your API secret on Cloudinary
<br />

<h4>Step-3</h4> After placing the values of the environment variables, just run the command: <code>docker-compose up</code> and the application will be available on port 8000.<br/>
<br/>

OBS: It is also possible to run the application without docker, just clone the repository, create an .env file in the root of the project with the necessary keys and values and install the project dependencies in requirements.txt, however the use of docker is encouraged, for a construction with no chance of failure.

<a id="contribute"></a>
## 💡 How to contribute
If you would like to contribute to this project, please follow the steps below:

1- Create a fork of this repository by clicking the "Fork" button in the top right corner of the page.

2- Clone your fork to your local machine:
`git clone https://github.com/your_username/repository_name.git`

3- Create a branch for your changes:
`git checkout -b my_feature_branch`

4- Make desired changes to the code and add your files using the `git add .` command.

5- Ensure your code passes all tests.

6- Commit your changes with a clear message of what was done:
`git commit -m "Added new feature"`

7- Push to the branch you created on your fork:
`git push origin my_feature_branch`

8- Open a pull request to this repository by clicking the "New Pull Request" button on your fork's repository page.

9- Wait for the project reviewer to evaluate your code.

Thank you for your contribution!




<br/> 

## License
***This project is licensed under the MIT. See the LICENSE file for more information.***
<br/>
<br/>
<br/>
<a id="credits"></a>
## 🏆 Credits

  ### ***⭐ For every project we have to give credits to the creators so nothing better than finishing with a golden key with the creators / creator of the project***.

<br /> 

<div > 

| [<img src="https://avatars.githubusercontent.com/u/69887726?v=4" width=300><br><sub> Gabriel Santana </sub>](https://www.linkedin.com/in/gabrielsantana444) | ***Hello 😃 If you made it this far, I believe you liked my project, in which case we have something in common, so how about we talk a little? My call on linkedin*** 😁 |
|---|---|

