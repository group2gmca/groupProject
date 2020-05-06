# Prize Generator application

## Group Project Due 7th May 2020 at QA Academy Devops.

Index

Links to different sections here.

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
![Arch](https://github.com/group2gmca/groupProject/blob/master/documentation/arch.png)

Architecture V2
![Arch2](https://github.com/group2gmca/groupProject/blob/master/documentation/updated%20architecture.png)

## Diagrams:

Entity Relationship Diagram

![erd2](https://github.com/group2gmca/groupProject/blob/master/documentation/ERD.jpg)
## Initial plan:

The initial plan was to create our code in python using visual studio and use git as our version control system to be able to push to git as a team we were going to use the feature branch model to work together seamlessly. 
We planned on using Jenkins as our CI server which would autonomously push any changes made in our code linked to git using webhooks 
We also planned on using docker containers to run each of our micro services and link them together using docker swarm. 
ADD MORE ABOUT DOCKER TECH WE HAVE USED
for testing we planned on using pytest to test the code 
ADD MORE ON TESTING
testing environments?
for the database section of the project we are going to use mysql/pymysql as it is commonly used and understood, other options available to us are to use CosmosDB.
for hosting our application we have two options Azure or GCP
also to spin up our application we have the ability to use Terraform and Kubernetes

WHAT WE THOUGHT WE SHOULD DO

## Solution:

WHAT WE DID RELATED TO ARCHITECTURE

### Deployment

How we are going to deploy the app azure gcp docker swarm etc etc
DockerHub
![docker](https://github.com/group2gmca/groupProject/blob/master/documentation/docker%20hub.png)

CI PIPELINE
![CI](https://github.com/group2gmca/groupProject/blob/master/documentation/cpipe.png)
This is our CI Pipeline

### Testing

For the Testing we conducted tests on the code and database using Pytest. Here are some of our Coverage Reports
![coverage1](https://github.com/group2gmca/groupProject/blob/master/documentation/cov1.png)
![coverage2](https://github.com/group2gmca/groupProjectblob/master/documentation/cov2.png)

### Technologies used:

Visual studio code – Source code

Version control system – Git

Project tracking – Trello

Testing – Pytest

CI server – Docker/CRON

Docker / Docker Swarm 

VM SQL – GCP

Database - Mysql

Source code - Python/html/css/Bootstrap

ADD MORE TECHNOLOGIES HERE

## Front end design:

Main Page of our Interface

![home](https://github.com/group2gmca/groupProject/blob/master/documentation/home.jpg)

Prize Page showing No Prize Won 

![nowin](https://github.com/group2gmca/groupProject/blob/master/documentation/nowin.jpg)

Prize Page Showing Small Prize Won

![smallprize](https://github.com/group2gmca/groupProject/blob/master/documentation/smallprize.jpg)

SHOW A FEW SHOTS OF OUR APP WORKING HOME PAGE PRIZE PAGE

Build shell Jenkins

## Improvements:

IMPROVEMENTS OR THINGS WE COULD OF DONE BETTER
