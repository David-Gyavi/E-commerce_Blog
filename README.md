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


### **Profile Product**

#### User story: As a user, I would like to have a personal profile for my product. 

* **Plan**  
The user should be able to created a profile for the product in which it can fill in various information. 
Possible input fields should be the name of the product, description and an image of the product. 
A summary of the dog profile will be displayed on the dashboard overview. 

* **Implementation**  
I have created a form with the various input fields where the user can fill in the information. 
I have only made the product_name field required as for the other fields, the user might not want to fill in this information. Some user might not know the date of birth etc so he/she might not want to fill this in. 
For the image, I worked with an url that has to be filled in. The product image can be easily uploaded by user from its device and/or cloud.
The user can also use the AWS web tier to make changes like uploading media file to the project and many more. 
The user is given a chance to make choice of which item he would buy as wel as the user would be able checkout for the products he has bought. 

* **Test**  
I have tested the add product, signin, signout form various times to make sure they work properly.
The input is stored correctly in the product collections.  
Shop now button works as planned and takes the user to the page after resolving some issues. See [Bugs](#bugs)
In order to display the correct product for the user, I have addded the _id of the user as a hidden inputfield for the add product which is stored in the database.

When testing this on mobile devices (iPhoneSE and iPhone8), I noticed that the datepicker was not working how it should.
After conducting various reseach, I have come up with solution which you can find under [Bugs](#bugs).
 
After various testing, I came to the conclusion that it didn't make sense that the user could able to add product profiles with the same name.
When the user adds a product, I now first check if the user already has a product profile with that name and the correct feedback is being shown to the user. 
Implementing this, brought another issue along with the cancel update in case the user has more than 1 product already added to its profile. 
When the user now wants to create another profile with the same name, receives feedback that the profile already exists and then clicks 'cancel', 
the user will be taken to the profile for which he/she wanted to create a profile. 

* **Result**  
Adding a profile for the product works as planned and looks good across various browsers and devices.  
Upon submitting the form, the input is stored correctly in the database. 

* **Verdict**  
The test has passed all the criteria and works like planned.

### **Dashboard**

#### User story: As a user, I would like to have a dashboard where I can have a good overview. 

* **Plan**  
I would like to create a dashboard where the user can see the profile of the products on the navbar. 
On small devices the profile will be displayed on top of the page with the logs of the products below. 
Whenever the user has multiple products, I want that the user is able to select the profile that should be displayed on the dashboard. 
This will be displayed above the product profile on small devices and on top of the dashboard for large screen. 
The dashboard should be very clear and intuitive to use.   

When the user doesn't have any product yet added to its user account, a blank dashboard will be displayed with a very clear call-to-action to add the first product. 
On the place where normally the logs would show, I will the following text: "After you added your products, come here to start tracking!"

* **Implementation**  
My dashboard exists out of several of  main parts, the search box, my Account and the bag plus the nav links display. 

    *Product profile*  
    Here it shows all the submitted information about the product, including the button shop now which gives a personal feeling to the user. 
    When the user hasn't filled in the url, it shows 'Click here to add an image' which takes the user to the products page. 
    Left on top it has a a logo "ECOMMERCE SITE" where the user can click and goes back to the home page. 
    Below the profile it shows an edit button and a delete button. 
    When the user doesn't have a dog added yet, it will display an empty profile with a call-to-action to add a dog profile.

    *Logs display*   
    The logs that will be displayed are from the products profile selected. 
    When no product profile is added yet, here it will show that as soon as they added a dog, they can come here to start tracking.
    When a product profile is added but no logs are submitted yet, it shows 'Click here or on the add button right below to add your first log" which takes you to the logs page. 
    From the moment the user has at least submitted 1 log, another button will appear above the logs with the following text: Click here to search logs by date'. 
    This will take the user to the search logs page where a search can be performed and updated. 
    For medium devices and up I have included a floating action button which is displayed right below on the screen. 
    Even if the user is in the middle of the screen, the button will be displayed, giving the user the possibility the add a log without having to scroll up to the top. 
    The floating action button will be hidden on small screens and a normal button will appear on below the search button. 
    I have implemented this because the floating action button was appearing on top of the product profile which might have confused the user with the add another product button. 

    Whenever the user has more than 1 product in its bag, a select element will appear above the top right corner of the dashboard saying: "Selected successfully". 
    Here the names of all the product that the user has will be displayed. 
    When the user clicks on the name, the form will be submitted (without submit button, by using javascript) and the profile and logs of that product will be displayed on the dashboard. 

* **Test**  
The correct dashboard is being displayed depending on if the user has already added a product profile.
When the dashboard is being displayed after registring and adding the first product profle, the correct profile is being displayed under product profile. 
Under logs the text to add first log is being displayed correctly.  
From the moment the user adds a first log, the log is being displayed nicely on the screen with nice focus on the date to make the dashboard more appealing. 
The text to add first log disappears and the button to search logs by date appears nicely above the log. 
When multiple logs have been added, the logs are ordered by log date with the most recent one first.  
On small devices the floating action button disappears and a normal button appears right below the search button. 

When the user has added more than 1 product, the select box appears above the dashboard, allowing the user to select the profile that should be displayed on the dashboard. 

During testing I noticed that the order of logs was not correct. In manage.py I sorted the logs by with the most recent first. 
This was not going correctly as I had set a different format for the date, with the month written in full. 
The logs were being sorted incorrectly because of this. See [Bugs](#bugs) for the solution to this problem.

I also had a problem of error server 500 which was comming from the base.html template about the add_profile and it was supposed to be profile bt I was helped by the tutor
and the credit goes to them I could not fix it however it looks easy.

* **Result**  
The dashboard looks as planned across various browers and devices. 
All the functionalities work as planned and the correct information is being displayed on the screen. 
Hiding the floating action button on small devices works well and improves the user experience. 
After resolving the issue with the date format, the logs are being sorted correctly. 

* **Verdict**  
The test has passed all the criteria and works like planned.

### **Search Logs**

#### User story: As a user, I want to be able to search on date to get specific data. 

* **Plan**  
After a while the user will have a lot of logs which will make it more complicated to find a certain log. 
I want the user to be able to filter on the logs depending on the log date to make it easier find a certain log. 
In the future I would also like to add pagination to the logs so it doesn't look like an endless list of logs. See [Features to be implemented](#features-to-be-implemented)
Currently I don't have the required skills or knowledge for this so I will only implement the search function.
But this will be for the feature implemented As the log_date is a required field for adding a log, the user will be able to search for all the logs. 

* **Implementation**  
As of the moment the user has added at least 1 log for the products profile, a button will appear on top where the user can click to go to the search logs page.   
If there was no log found with that logs date, the following message will appear: 
"There are no logs for this date". 
After this, the user can either search on another date or return to the dashboard. 

The user also has the option to edit or delete a log after searching it. After they edited or deleted the log, the user will be taken back to the dashboard of the relevant product. 

* **Test**  
When I implemented the above strategy, I noticed that the logs of other products where showing as well with the same products. 
In my function I have included the product_id in order to only display the logs of that date of the relevant products. 
When no logs are found, the correct message is being displayed on the screen. 
The shop now button to take the user to the product page works as planned and the dashboard of the products for which you were performing the search is being loaded. 

When you click a day, it is clear you still have to click search in order to see the results.
See [Features to be implemented](#features-to-be-implemented) for further explanation. 

* **Result**  
The search logs page works as planned across various browsers and devices. 
Search function works as planned and return the correct logs or feedback message depending on the user input. 
Button to take the user back to the relevant dashboard functions as planned. 

* **Verdict**  
The test has passed all the criteria and works like planned.

### **Multiple product profiles**

#### User story: As a user, I want to be able to add another product.

* **Plan**  
As some users might have multiple product, it is a good user experience that they can have all their dogs under 1 account instead having to create multiple user accounts. 
On the dashboard under product profile, a button will be dislayed left on top where the user can click to add another product. 
This will take the user to the add dog page, same page as where the user was redirected to after registering.
A cancel button will be displayed in case the user doesn't want to proceed with adding another product.

* **Implementation**  
The form is the same one as when the user created a first product profile.
The main difficulty of having multiple product per user, was the display on the dashboard. 
In the end I have decided to add a select box above the profile whenever the user has more than 1 product added to the profile. 
In the select box I added a default option with the text: Select the product profile you want to see. 
The option that the user can choose will depend on the amount of dogs added to the profile, the names of the dogs will be displayed as the value. 

    In order to accomplish the above, I have decidede to add the product_id to the dashboard url. 
    Whenever the user clicks on the product name in the select box, the form will automatically submit (with the help of javascript) and load the dog profile and logs of the selected product. 
    Implementing the above solution meant as well that I had to rewrite a big part of my other functions. 
    This to make sure that everytime there was a redirect to the dashboard, the correct dog_id had to be included. 

    When the user signs in, the dashboard that will be displayed will be the first one that was loaded in the product collection of the database. 

* **Test**  
After I had implemented the above solution, I had to test all the other functionalities as well to make sure the correct dog profile was being displayed on the dashboard. 
Whenever the user has more than 1 product, the select box is being displayed with the product names that the user has created. 
Upon clicking the product name for which the user would like to see the dashboard, the form is submitted and the correct info is being displayed. 
When the user removes the previously last product (and has only 1 product remaining), the select box disappears and profile of the remaining product is displayed. 
I made sure that whenever a new log was added, edited or deleted, the dashboard of the relevant product kept on being displayed on the screen. 

When testing on other devices (iPhone SE and iPhone8 in this case), we noticed that the select box was not working properly. 
This is was the same issue as I had for the datepicker. See solution under [Bugs](#bugs)

* **Result**  
Having multiple product on the profile was a big challenge which has taken a lot of time and testing. 
The functionality is now working as planned across various devices and browsers. 
The select box appears nicely like planned above the dashboard.

* **Verdict**  
The test has passed all the criteria and works like planned.

### **Edit log and product profile**

#### User story: As a user, I want to be able to edit the product profile / As a user, I want to have the possibility to edit a log when I made a mistake or want to add some info. 

* **Plan**  
The user has to be able to edit an existing log and dog profile when a mistake was made or when the user wants to add certain information. 
Here it is important that the information that the user inserted before remains intact and will be displayed on the page in order to have a good user experience. 
Every log and dog profile will have an edit button which will take the user to the editlog or editprofile screen. 

* **Implementation**  
For this functionality I used the same product-form / log-form.  
I have used a variable (add) to make the difference between adding and editing a product/log. 
When add is not equal to True, I added a value attribute with the previous filled in information. 
By implementing this, I have managed to merge the add and edit form into 1 form which simplifies my code. 
The value of the input fields will already be filled in with the information that the user has inserted before. 
When the user submits the form, all the fields will be updated in the relevant collection in the database. 
In order to make this function work, I had to include the product_id for the edit product profile and the log_id for the edit log profile. 
This way I made sure that the correct profile or log was updated. 

* **Test**  
I have tested the edit functionality various times to make sure the data was being updated correctly. 
After the submission of the form, the user is being redirected to the dashboard of the product for which the changes were made. 
Cancel button also takes the user back to the dashboard in case the user doesn't want to proceed with the changes.

I noticed when testing that when the user would edit a product profile and change the product name to an already existing dog profile name, the user would still have 2 product profiles with the same name. 
Also here I now first check to see if the product name already exists in the database for this user and if so, feedback is provided to the user and the form is not being processed. 
The user can either choose a different name or cancel to go back to the dashboard. I still ran in quite some difficulties when implementing this. You can find more information in [Bugs](#bugs).




