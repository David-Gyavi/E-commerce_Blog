# **E-Commerce-Blog**

![different_screen](media)

## **Goal for this project**

Have of you ever gone to a store full of computers and all computer accessories, reaching there when you even don't know what you want to take. Being asked lots of quetions but is 
more of beter to make it easire for people to access each and every stuff they would like to get or to buy while sitted at home on there computers or other gadgets to access what ever they want.
This case they ask you which type of part or computer you would like to take, which specifications would you like yet you know nothing.

The E-Commerce-Site will help and make your life more esier. How By just sitting down and start searching for each and everything and even knowing which kind is good and there prices as well.

Therefore in case you dont buy online it will be easy for you to know which kind of machine you like and what ever they ask you about you know exactly because you took time to search on web and 
find precisely what you wanted to do. So here you will be able to register and also signin so that all the items you bye are easily followed and you also get a bonus of creating an account.

Thanks for visiting my project.

<a></a>

## Table of contents 
* [UX](#ux)
    * [User Goals](#user-goals)
    * [User Stories](#user-stories)
    * [Site Owners Goals](#site-owners-goals)
    * [User Requirements and Expectations](#user-requirements-and-expectations)
        * [Requirements](#requirements)
        * [Expectations](#expectations)
    * [Design Choices](#design-choices)
        * [Fonts](#fonts)
        * [Colors](#colors)
        * [Structure](#structure)
* [Wireframes and Flowcharts](#wireframes-and-flowcharts)
    * [Wireframes](#wireframes)
    * [Flowcharts](#flowcharts)
    * [Database Structure](#database-structure)
* [Features](#features)
    * [Existing Features](#existing-features)
    * [Features to be implemented](#features-to-be-implemented)
* [Technologies used](#technologies-used)
    * [Languages](#languages)
    * [Libraries and Frameworks](#libraries-and-frameworks)
    * [Tools](#tools)
* [Testing](#testing)
* [Deployment](#deployment)
    * [Local Deployment](#local-deployment)
    * [Heroku Deployment](#heroku-deployment)
* [Credits](#credits)

--- 

<a name="ux"></a>

## **UX**

<a></a>

### **User Goals**

* The website has to work well on all kind of devices like mobile phones, tables and desktops.
* I want to have a clear dashboard where I can see all the different logs I have created. 
* The log should appear with the most recent one on top to be relevant. 
* I would like to have the option to add multiple Items.
* The website has to be easy to use and easy to update information
* Visually appealing website

[Back to Top](#table-of-contents)

<a></a>

### **User Stories**

* As a user, I would like to be able to register for the website so I can have my personal environment.
* As a user, I want to login after I created an account and see my previous inserted information.
* As a user, I would like to have a personal profile for my items. 
* As a user, I would like to track activity, food and weight. 
* As a user, I want to be able to add as many logs as I want, even multiple per day.
* As a user, I would like to have a dashboard where I can have a good overview. 
* As a user, I want to be able to search on date to get specific data. 
* As a user, I want to be able to add special notes to the log whenever relevant. 
* As a user, I want to be able to add another product bought.
* As a user, I want to be able to edit the product profile.
* As a user, I want to have the possibility to edit a log when I made a mistake or want to add/delete some info. 
* As a user, I want to have the possibiltiy to delete a log as well when no longer relevant. 
* As a user, I want the website to be easy to use. 
* As a user, I want the process to add / edit / delete product to be easy

<a></a>

### **Site owners Goals**
* To have an appealing website that a user to track and their products, etc.
* To have a great functionality so the user feels like this website helps them in their day-to-day life. 
* To make the website as personal as possible by giving the user the possibility to add information about their product in the profile.


[Back to Top](#table-of-contents)

<a></a>

### **User Requirements and Expectations**

<a></a>

#### Requirements

* Easy to navigate by using the few buttons
* Appealing dashboard with a functional overview
* Easy way to add a log to the dashboard
* Easy way to add another product to the profile
* Ability to edit and delete existing logs

<a></a>

#### Expectations

* When you have multiple products, it should be easy to navigate between them
* To have a dashboard where all the necessary information is visible
* It should be easy to add another log 
* Personalised profile with information about the product and an image
* To be able to filter on the logs in order to get specific information

[Back to Top](#table-of-contents)

<a></a>

### **Design Choices**

I have used [Coolors](https://coolors.co/ "Coolors.co") to come up with a color scheme that matches the atmosphere of a Ecommerce site.
For this website I have deciced to keep design simple, meaning I opted for a white background color with some Orange white for the Home.
I have added some color (black) for the buttons, navigation bar is left eith a white background design more visually appealing to the user. 
The reason for this is that for this project, the functionality is much more important and as there are a lot of functionalities I don't want to distract the user with overwhelming colors. 

<a></a>

#### Colors

Like I mentioned before, But all the colors I have used mostlty have followed that of the Ado-Botique project colors that fit well with the feeling of a Ecommerce site.
Below I will explain more why I choose the various colors and for what I will be using them.

![Color Palette](wireframes/color-palette.png)

* #ffffff: I have decided to keep the background of the overall website white in order give the clean look. I will also use this color as text color for the nav bar and buttons.
* #D9D9D9: This color I will use as a background color for whole dashboard. 
* #F5F5F5: This color I will use as a background color for the logs on the dashboard in order to have a small contract versus #D9D9D9 dashboard color.
* #284B63: This will be the color that I will use for my navigation bar and buttons in order to give a bit of color to the website. This color will also be used as the overall text color.

I have used a contrast checker in order to make sure that the contrast is sufficient.
This way my content will be easily readable. 

<a></a>

#### Fonts
In order to find appropriate fonts for my website, I have visited [Google Fonts](https://fonts.google.com "Google Fonts") to explore the various options.
For the titles and subtitles, I have used the font [Play](https://fonts.google.com/specimen/Roboto "Roboto") 
and for the main text I have used [Cormorant Garamond](https://fonts.google.com/specimen/Roboto "Roboto"). 

<a></a>

#### Structure

I have chosen to use [Materialize](https://materializecss.com/) to create an overall structure for my website. 
Materialize provides various elements of CSS and Javascript which is very helpful to keep a good structure on your page. 
The reason why I choose Materiaize is mainly due to the various features they offer like a datepicker, floating action button etc. 

[Back to Top](#table-of-contents)

--- 
<a></a>

<a></a>

### **Existing Features**

* Registration functionality
* Sign-In and Out functionality
* Add multiple products per user 
* CRUD Functions:
    * Create: possibility to add various products and logs
    * Read: dashboard where you can view the product profile(which was selected) and its logs
    * Update: possibility to update the product profile and logs
    * Delete: possibility to delete the product profiles and logs
* Search logs by log date

<a></a>

### **Features to be implemented**

* The user can also insert image url or download it from from his/her computer and also to upload the Image to the cloudaccounts.
* Have a more extensive user profile with, profile image, preferences and email to which you can send updates, newsletters etc.
* Have a 'forget password' functionality.
* Include a confirm password to make sure the user has chosen the password he/she wanted. 
* Possibility for the user to be able to add (and remove) products they would like to specificely track for their products like medication etc. 
* Add pagination so the list of logs will be display with a max of 20 logs per page.
* When the user has added their first log, I would like to remember the chosen metrics for any futher logs so they don't have to update this every time they add a log.
* This would be done through profile preferences or store the data in a cookie. 



[Back to Top](#table-of-contents)

<a></a>

## **Technologies used**

<a></a>

### **Languages**

* [HTML](https://en.wikipedia.org/wiki/HTML)
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://www.python.org/)

<a></a>


### **Libraries and Frameworks**

* [Font Awesome](https://fontawesome.com/)
* [Materialize](https://materializecss.com/)
* [Google Fonts](https://fonts.google.com/)
* [jQuery](https://jquery.com/)

### **Tools**
* [Git](https://git-scm.com/)
* [GitPod](https://www.gitpod.io/)
* [Heroku](https://www.heroku.com/)
* [W3C HTML Validation Service](https://validator.w3.org/)
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)

### **Frame Work**
[Django](https://www.djangoproject.com/)

[Back to Top](#table-of-contents)

<a></a>

## **Testing**

### **Registration**

#### User story: As a user, I would like to be able to register for the website so I can have my personal environment

* **Plan**  
I want to create a page where the user can register for the personal account to which only the user has access.
My first plan was to redirect the user to the  form right away to add the first product but I realised it might confuse the user. 
Therefore after registration, the user will be taken to a "Home page" where the only call-to-action will be to add their first product.
This way the user can make 'the decision' to add a item profile themselves and I don't make that choice for them.

* **Implementation**  
I created a form where the user can choose a username and a password. 
I have used the pattern attribute to only allow certain characters for the username and password. 
Correct feedback will be displayed whenever the user doesn't meet the pattern critera. 
Before creating the new account, I will check in the database if the username already exists. 
If so, correct feedback will be displayed to the user so he can choose another username. 
Password will be stored with the help of the password generate hash so it is stored safely.
After the registration was succesfull, the user will be redirected to the blank dashboard to add their first dog.
In case the user wrongfully clicked on register instead of sign-in, a link to the sign-in page is provided so the user doesn't have to go back. 
I have also implemented a 'Go back to the homepage' link so the user doesn't have to use the back button of the browser in case he/she wants to go back to the homepage.
I created the shopping bag where user can store all his items he want.
I have used a variable (register) to make the difference between the register and sign-in form.
When register is equal to True, I added the span which explains the requested format.
By implementing this, I have managed to merge the register and sign-in form into 1 form which simplifies my code. 
In the bag where the user stores his products, I made it easier for the user to delete and update his products.


* **Test**  
I have tried to create an account with an already existing username. Correct feedback is displayed.
Whenever I didn't meet the pattern criteria, the correct feedback was displayed, explaining which charachters etc are allowed. 
User acccount is created whenever all criteria was met and user is being redirect to blank dashboard.

I noticed that the feedback provided to the user when their input didn't match the required format was not being displayed on all devices. 
After some research I have decided to add the required pattern right above the input fields so the user will always know which format to use.

After receiving some feedback from friends and family who have tested the website, I have decided to make the feedback message stand out more. 
It took the user a while to notice the feedback when the username already exists. I have changed the text color to red so it really stands out. 

* **Result**  
Registration form is working as planned and user information is stored safely in the mongodb Users collection.
I had a problem adding products to the project, in that I got alot of errors in 403 but by the help of tutors I managed to solve it.
Feedback provided stands out nicely to inform the user. 
Redirection to blank dashboard works as well as planned so the user can choose to add its dog right away. 
'Back to homepage' link works as well and takes the user back to the homepage
Tested the registration on various browers and devices and the form is responsive and userfriendly. 
Having the pattern as a fixed element on the page, improved the user experience. 
Instead of filling in the fields without knowing the pattern, receiving the feedback and then filling in the fields again, the user can now insert right away the fields with the correct pattern. 

* **Verdict**
The test has passed all the criteria and works like planned.

### **Sign In**

#### User story: As a user, I want to login after I created an account and see my previous inserted information.

* **Plan**  
My plan is to create a login form where the user can fill in the username and password.
After signing in, the user will be redirected to the dashboard where the user can see the previously inserted information.
In case the user doesn't have any product added to the profile, the user will be redirected to the blank dashboard where a product profile can be added.

* **Implementation**  
I created a form where the user can fill in its username and password which will be verified with the information stored in the database. 
I created a form checkout where a user after feeling in information then the user can check out and is confirmed.
When the wrong information is being filled in, the correct feedback will be provided to the user. 
In case the user wrongfully clicked on sign-in instead of register, a link to the register page is provided so the user doesn't have to go back. 
I have also implemented a 'Button SHOP NOW' where it redirect you to the products page of different kind.

* **Test**  
Signing in with the correct username and password works as planned and the correct dashboard of that user will be displayed. 
Before it was bringing in error but late going through the code with the tutor it was put to right.
When the user fills in the wrong username and/or password, the correct message is being displayed on the screen. 
Also here the feedback message didn't stand out well enough so I have changed the color to red. 
Redirecting to register page and 'back to homepage' link works as well. 

* **Result**  
Sign-in form is working as planned and the input is being verified correctly with the stored information of the database.
Redirection to the correct dashboard works as well as planned so the user can add aproduct to the bag and as well is given a choice of deleting and updating.
Tested the sign-in form on various browers and devices and the form is responsive and userfriendly. 
Feedback provided to the user stands out nicely. 

* **Verdict**    
The test has passed all the criteria and works like planned.

