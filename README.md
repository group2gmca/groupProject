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

## Architecture

Diagrams etc

## Diagrams:

Entity Relationship Diagram

![erd2](https://github.com/group2gmca/groupProject/blob/master/documentation/ERD.jpg)
## Initial plan:

WHAT WE THOUGHT WE SHOULD DO

## Solution:

WHAT WE DID RELATED TO ARCHITECTURE

### Deployment

How we are going to deploy the app azure gcp docker swarm etc etc

CI PIPELINE

Pipeline diagram with our technologies used here

### Testing

For testing pytest add what we can

### Technologies used:

Visual studio code – Source code

Version control system – Git

Project tracking – Trello

Testing – Pytest

CI server – Jenkins

VM SQL – GCP

ADD MORE TECHNOLOGIES HERE

## Front end design:

SHOW A FEW SHOTS OF OUR APP WORKING HOME PAGE PRIZE PAGE

Build shell Jenkins

## Improvements:

IMPROVEMENTS OR THINGS WE COULD OF DONE BETTER
