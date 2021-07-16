# Milestone Project 3

## Contents
* [Purpose](#Purpose)
* [UX](#UX)
* [Technologies](#Technologies)
* [Testing](#Testing)
* [Supported Browsers And Devices](#Supported-Browsers-And-Devices)
* [Deployment](#Deployment)
* [Credits](#Credits)
<br>

## Purpose

The purpose of this project is to showcase everything I have learned within the Python and Backend Development modules of the Code Institute Full Stack Development course. A full list of technologies used can be found in the technologies section of this document.
<br>
<br>
The purpose of the website is to allow users to browse and comment on cryptocurrencies as well as create their own watchlist. 
<br>
<br>
Disclaimer: This website is for educational purposes only, this is not financial advice.
<br>
Please see below for the link to the website.

https://coinhold-ms3.herokuapp.com/
<br>
<br>

## UX

### User Stories
As an anonymous user I want to:

1. Browse cryptocurrencies.
1. Search for cryptocurrencies I am interested in.
1. See comments on cryptocurrencies from other people.
<br>

As a registered user I want to:

1. Add cryptocurrencies to my own watchlist.
1. Remove cryptocurrencies from my watchlist.
1. Comment on cryptocurrencies.
1. Edit comments I have submitted.
1. Delete comments I have submitted.

### Design

#### Colour Scheme
Off White - Background colour, this is because it contrasts well with white and black.
<br>
White -  Background colour of cryptocurrency content and log in/register forms, this is because it contrasts well with off white.
<br>
Black - Navigation bar and body text, this is because it contrasts well with snow.
<br>
Gold - Navigation bar and buttons, this is because it contrasts well with black.
<br>
#### Typography
Oswald - This font will be used throughout the whole webpage, this is because it looks clean, professional and is easy to read.
<br>
#### Wireframes
To see the wireframes for all pages on both desktop and mobile view please click the below link.
<br>
[Wireframes](wireframes/wireframes.pdf)
<br>
#### Data Structure
This site uses MongoDB. Its database contains the following collections:
<br>
![alt text](https://github.com/sanjaysanghera/Milestone-Project-3/blob/master/static/images/data-structure.JPG)
<br>
#### Final Pages
* Home - Displays a list of cryptocurrencies. This list can be filtered with the search bar. Registered users can add cryptocurrencies to their watchlist.
* Watchlist - Displays a list of cryptocurrencies that a registered user has added to their watchlist.
* Crypto - Display information about the selected crypto. Registered users can submit, edit and delete comments to this page. Non-registered users can view comments.
* Log In - Registered users can log in on this page.
* Register - New users can register to the website on this page.

## Technologies

* **HTML** - This has been used to structure the project.
* **CSS** - This has been used to style the project.
* **Java Script** - This has been used to add complex features to the project.
* **Bootstrap** - This has been used to create the navigation bar and contact form.
* **Font Awesome** - This has been used to import Oswald font and social media icons.
* **GitHub** - This has been used to store and deploy the code for the project.
* **GitPod** - This has been used to create the code for the project.
* **Google Chrome Developer Tools** - This has been used to inspect the web pages and debug any issues.
* **Balsamiq Wireframes** - This has been used to create the wireframes for the project.
<br>


## Testing

### Code Validation

* HTML file has been validated using the W3C HTML Validation Service website.
* CSS file has been validated using the W3C CSS Validation Service website.
* JS files have been validated using the JSHint website.
* Python files have been validated using the PEP8 website.
<br>

### User Story Testing

### Additional Testing

* If a logged in user tries to access the log in page they will be redirected to the home page. "You are already logged in!" message appears.
* If a logged in user tries to access the register page they will be redirected to the home page. "You are already registered!" message appears.
* If a user who is not logged in tries to add a crypto to a watchlist, "Please log in or register to add to watchlist" message appears.
* A comment can only be deleted/edited by the user who created the comment.
* If a user tries to register with a username or password that does not match the requirements, "Please match the format requested" meesage appears.
* If a user tries to register without filling in both the username and password fields, "Please fill in this field" message appears.
* If a user tried to submit a blank comment, "Please fill in this field" message appears.
* If a user tries to register with a username that has already been taken, "You are already registered!" message appears.
* If a users login attempt is unsuccessfull, "Incorrect Username and/or Password" message appears.
* If a new user registers they will be redirected to the home page, "Welcome, username" message appears.
* If a user logs in they will be redirected to the home page, "Welcome, username" message appears.
* If a user submits a comment, "Thank you for commenting" message appears.
* If a user deletes a comment, "Your comment has been deleted" message appears.
* If a user edits a comment, "Your comment has been edited" message appears.
<br>

## Supported Browsers And Devices

Below is all the browsers and devices the website has been tested on.
<br>
<br>
**Google Chrome (Right clicked the page and selected Inspect then Toggle Device Toolbar)**
<br>
**Microsoft Edge (Right clicked the page and selected Inspect then Toggle Device Emulation)**
* Moto G4
* Galaxy S5
* Pixel 2
* Pixel 2 XL
* iPhone 5/SE
* iPhone 6/7/8
* iPhone 6/7/8 Plus
* iPhone X
* iPad
* iPad Pro
* Surface Duo
* Galaxy Fold
<br>

**Firefox (Right clicked the page and selected Inspect Element then Responsive Design Mode)**
* Galaxy S9/S9+
* iPad
* iPhone 6/7/8
* iPhone 6/7/8 Plus
* iPhone X/XS
* Kindle Fire HDX
<br>

## Deployment

This project was created using GitHub/GitPod and deployed using Heroku.

### Cloning

In order to clone this project:

1. Log in to GitHub and find the GitHub Repository.
2. Click the "code" button and copy the HTTPS link
3. Open Git terminal and type "git clone" followed by the link and hit "enter".

### Database Setup

In order to set up a database in MongoDB:

1. Login to MongoDB
2. Create a cluster as well as a database.
3. Create three collections within your database following this [data structure](#data-structure)

### Heroku Deployment

1. Add an env.py file to your workspace containing the following variables:
  - os.environ["PORT"] = "5000"
  - os.environ["IP"] = "0.0.0.0"
  - os.environ["SECRET_KEY"] = "YOUR_SECRET_KEY"
  - os.environ["MONGO_URI"] = "YOUR_MONGODB_URI"
  - os.environ["MONGO_DBNAME"]= "DATABASE_NAME"
2. Create an application:
  - Log in to Heroku
  - Click on the "New" button and "Create new app"
3. Connect to GitHub
  - Click on the "Deploy" tab and "Connect to GitHub"
  - Enter the name of your GitHub repository and click "Connect"
  - Go to the "Settings" tab and create config vars based on variables created in env.py previously
  - Once all your GitHub files are pushed, navigate back to the "Deploy" tab, select "Enable automatic deploys" and deploy the branch to Heroku


## Credits

### Content
The text content for the Crypto about section was taken from:
<br>
https://www.coinbase.com/



  
