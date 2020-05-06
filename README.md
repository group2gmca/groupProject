# Prize Generator application

## Group Project Due 7th May 2020 at QA Academy Devops.

## Index

Assignment Brief and Initial Solution

Risk Assessments

Architecture

ERD Diagram & Trello (Kanban Agile Methodologies)

Initial Plan

Implemented Solution

Deployment

Testing

Front-End & Build Design

Improvements

## Assignment Brief

To create a micro-service orientated architecture for an application that composes of at least 4 services that work together incorporating core methodologies and technologies covered in our core modules during our time at the academy.

## Solution

Our group solution is to create a Prize Generator application that allows the user to be assigned a username/account number when they visit the application, this username/account number can then be thrown into a prize generator to see if they have won a prize.

The prize generator will consist of 4 services running together. The first service will be the main API and be running the core application. This application will display a username/account no and will allow the user to navigate around via html pages.

The second service will be generating half of the username/account number, this service will generate a random object of a three or four character string that will be both uppercase and lowercase and will pass this back onto service 1.

The third service will be generating the second half of the username\account number which will be a selection of randomly generated numbers. This object will then be sent to back to service 1.

The fourth and final service will allow us to create 2 versions of the application, one version when it is feeling generous with the prize output and another where it is feeling less generous.

The output from service 2 and 3 will be concatenated to form one username/ account number. The backend will complete the logic to determine a prize and then this will be stored into a database along with a prize.

## Risk Assessment
Initial Risk Assessment
![Risk](https://github.com/group2gmca/groupProject/blob/master/documentation/risk1.png)

Risk Asessment 2
![Risk](https://github.com/group2gmca/groupProject/blob/master/documentation/risk2.png)

## Architecture
Initial Architecture Plan 
![Arch](https://github.com/group2gmca/groupProject/blob/master/documentation/arch.png)

Architecture V2
![Arch2](https://github.com/group2gmca/groupProject/blob/master/documentation/updated%20architecture.png)

## Diagrams:

Entity Relationship Diagram
![erd2](https://github.com/group2gmca/groupProject/blob/master/documentation/ERD.jpg)

Trello Kanban Agile Methodology
[Link to Trello](https://trello.com/b/3rFrn4n5/sfia2-project "Trello-Board")

## Initial plan:

The initial plan was to create our code in python using visual studio and use git as our version control system to be able to push to git as a team we were going to use the feature branch model to work together seamlessly. 
We planned on using Jenkins as our CI server which would autonomously push any changes made in our code linked to git using webhooks 
We also planned on using docker containers to run each of our micro services and link them together using docker swarm on master and worker nodes.  
For testing we planned on using pytest to test the code and database. For the database section of the project we are going to use mysql/pymysql as it is commonly used and understood, other options available to us are to use CosmosDB.  
For hosting our application we have two options Azure or GCP, also to spin up our application we have the ability to use Terraform and Kubernetes


## Solution:

Following a revised look at the architecture (architecture V2 image) to create an app that satisfied the MVP first, we created a swarm of 1 manager and 2 worker VM's. The master created our 4 service application using a docker-compose file situated at the route. We then implemented crontab, which ran a script every 3 minutes checking if there had been new builds of our images in the docker registry. Our images would only be rebuilt if the source code on the master branch had been changed with a pull request. We used docker hub's functionality to create builds and configured this in our organisations build settings.
Using all these together meant that each time there was a merge to the master branch, docker hub automated a build, our master vm searched for new images, updated images, replicated it across workers and because we had a load balancer- we had 0 downtime.

### Deployment

DockerHub
![docker](https://github.com/group2gmca/groupProject/blob/master/documentation/docker%20hub.png)

CI PIPELINE
![CI](https://github.com/group2gmca/groupProject/blob/master/documentation/cpipe.png)
This is our CI Pipeline

### Testing

For the Testing we conducted tests on the code and database using Pytest. Here are some of our Coverage Reports
![coverage1](https://github.com/group2gmca/groupProject/blob/master/documentation/cov1.png)
![coverage2](https://github.com/group2gmca/groupProjectblob/master/documentation/cov2.png)

### Technologies Used:

- Source code - Visual Studio Application
- Languages - HTML CSS(BOOTSTRAP) PYTHON
- Version Control - GIT
- Project Tracking - Trello(Kanban System)
- CI Server - Docker/Cron
- Build Tool - Docker/Stack
- VM - GCP
- Database - Mysql container in Docker


## Front end design:

Below are some screenshots of our Interface:

Main Page of our Interface

![home](https://github.com/group2gmca/groupProject/blob/master/documentation/home.jpg)

Prize Page showing No Prize Won 

![nowin](https://github.com/group2gmca/groupProject/blob/master/documentation/nowin.jpg)

Prize Page Showing Small Prize Won

![smallprize](https://github.com/group2gmca/groupProject/blob/master/documentation/smallprize.jpg)

Screenshots of some of our builds in Docker-Stack-Crontab

## Improvements:

IMPROVEMENTS OR THINGS WE COULD OF DONE BETTER
