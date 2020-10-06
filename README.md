<h1 align="center">Robbie's <strong>GYM</strong> Website</h1> 

[View the live project here.](https://robbiesgym.herokuapp.com/)

​	This website a milestone project for Code Institute.  The project's purpose is to create a website that allows users or  	an admin to store and manipulate data records.

​	It is a website for a fictional gym.

​	The project allowing a user or an admin  to create, read, update, and delete (full CRUD functionality) data. 

<h2 align="center"><img src="https://robbiesgym.s3.eu-west-2.amazonaws.com/media/allresp.png"></h2>



[TOC]



## User Experience (UX)

### User stories

- #### First Time Visitor Goals

  1. As a First Time Visitor, I want to easily understand the main purpose of the site and learn more about the gym.
  2. As a First Time Visitor, I want to be able to easily navigate throughout the site to find content.
  3. As a First Time Visitor, I want to be able to easily find the location of the gym.
  5. As a First Time Visitor, I want to see what kind of exercises, facilities are there.
  6. As a First Time Visitor, I want to find information about products, and trainers and membership options.
  7.  As a First Time Visitor, I want to locate their social media links to see their followings on social media to determine how trusted and known they are.

- #### Returning Visitor Goals

  1. As a Returning Visitor, I want to find information about classes and class timetables.
    2. As a Returning Visitor, I want to find information about products and trainers and membership options.
    3. As a Returning Visitor, I want to find a way to get in touch with the GYM.
    4. As  a Returning Visitor, I want to find community links.

- #### Frequent User Goals

  1. As a Frequent User, I want to be able to safely log in.
    2. As a Frequent User, I want to check to see if there are any newly added classes in the timetable
    3. As a Frequent User, I want to check to see if there are any new products, trainers or membership options.
    4. As a Frequent User, I want to see my notes about my progress and modify or delete them.
    5. As a Frequent User, I want to see my previous purchases.
    6. As a Frequent User, I want to be able to purchase products or membership.

- #### Admin User Goals

  1. As an Admin User, I want to be able to safely log in.
    2. As an Admin User, I want to be able to add, edit ,and delete products.
    3. As an Admin User,  I want to be able to add, edit ,and delete trainers.
    4. As an Admin User, I want to be able to add, edit ,and delete users if needed.
    5. As an Admin User, I want to see user's previous purchases.

### Design
-   #### Colour Scheme
    -   The main colours used are black,orange, and white.
    -   The black gives a bit of a serious look to the website, white makes it crispy and orange makes it fresh and lively.
    -   Orange lines, underlines, and highlights are used to break the seriousness of the darkness of the black. 
    
-   #### Typography
    -   Nunito-Sans, sans-serif font used mostly on the website with Sans Serif as the fall-back font in the case for any reason the font isn't being imported into the site correctly. Nunito Sans is given a professional look to the website.
    
-   #### Imagery
    - Large images used to be striking and to catch the user's attention. Carousels added to give the impression of movement of the pages.
    
      

*   ### Wireframes

    -   PC wireframes - mock-up [View](https://github.com/robibrutoczki/lastmilestone/tree/lastmilestone/Documentation/PCwireframes)
-   Tablet wireframes - mock-up [View](https://github.com/robibrutoczki/lastmilestone/tree/lastmilestone/Documentation/TABLETwireframes)
    -   Mobile wireframes - mock-up [View](https://github.com/robibrutoczki/lastmilestone/tree/lastmilestone/Documentation/MOBILEwireframes)


## Features

-   Responsive on all device sizes
-   Interactive elements
-   Authentication with Django-[Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
-   Secure payment with [Stripe](https://stripe.com)
-   Membership options on PLAN page.
-   PRODUCT page - supplements, clothes, and drinks
-   Search by categories, sorting by, and word search on PRODUCT page.
-   SCHEDULE page with timetable and notes(full CRUD functionality).
-   CONTACTS page Email sending function and google map.

## Technologies Used

### Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5) for HTML pages and snippets

- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) to make some changes on bootstrap's CSS

- [JavaScript](https://www.javascript.com)

- [Python 3](https://www.python.org/download/releases/3.0/) for the applications

  

### Frameworks, Libraries & Programs Used

Bootstrap 4:

- Bootstrap was used to assist with the responsiveness and styling of the website.

[Google Fonts:](https://fonts.google.com/)

- Google fonts were used to import the 'Nunito-Sans' font into the base.css file which is used on all pages throughout the project.

[Font Awesome:](https://fontawesome.com/)

- Font Awesome was used on all pages throughout the website to add icons.

[jQuery:](https://jquery.com/)

- jQuery came with Bootstrap to make the navbar responsive but was also used for the "underline" function in the navbar. It is a document ready function using 

  ```
  .addClass('active')
  ```

  and the URL of the loading page.

[Git](https://git-scm.com/)

- Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub.

[GitHub:](https://github.com/)

- GitHub is used to store the project's code after being pushed from Git.

[PhotoScape X:](http://x.photoscape.org/)

- PhotoScape X was used to create the image for README.md, resizing images, and editing photos for the website.

[Justinmind:](https://www.justinmind.com/)

- Justinmind was used to create the [wireframes](https://github.com/) during the design process.

[EmailJS](https://www.emailjs.com/): 

- ​	EmailJS was used to send emails from Contact page.

[Stripe](https://stripe.com): 

- ​	STRIPE was used to make test card payments.

  

[AWS S3](https://s3.console.aws.amazon.com/s3): 

- ​	S3 was used to store static and media files.

  

  

## Testing

The W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) for CSS checking
-   [Nu HTML checker](https://validator.w3.org/) for HTML checking

Validation results

- [CSS](https://github.com/robibrutoczki/lastmilestone/tree/lastmilestone/Documentation/CSSvalid)
- [HTML](https://github.com/robibrutoczki/lastmilestone/tree/lastmilestone/Documentation/HTMLvalid)



### Testing User Stories from User Experience (UX) Section

- #### First Time Visitor Goals

  **As a First Time Visitor,** I want to easily understand the main purpose of the site and learn more about the gym.

  1. Upon entering the site, users are automatically greeted with a clean and easily readable navigation bar to go to the page of their choice. Underneath there is a Carousel with Text and a "Sign Up" Call to action button.
  2. The carousel images giving a dynamic feels to the website.
  3. The user has options, click the buttons to sign up to Robbie's GYM or scroll down to learn more about the GYM.

  **As a First Time Visitor,** I want to be able to easily be able to navigate throughout the site to find content.

  1.  At the top of each page, there is a clean navigation bar, each link describes what the page they will end up at clearly. The actual page's name gets a highlight and an underline helps to identify the page for the user.
  2. On every pages, there is a redirection call to action to ensure the user always has somewhere to go and doesn't feel trapped as they get to the bottom of the page. There are modals with information too.
  3. On the Contact page, there is a form to send a message to the site admin. Also, there is a google map with opening times and a dot to show the location of our GYM.

  **As a First Time Visitor,** I want to see what kind of exercises, facilities are there.

  1. Once the new visitor on the About Us page they will notice what kind of exercises, facilities we offer.
  2. The user can also scroll to the bottom of this page to read about our trainers.

  **As a First Time Visitor,** I want to find information about products, and trainers and membership options.

  1. On the navbar About us, Plans and Products pages shows this information to user. 

  **As a First Time Visitor,** I want to locate their social media links to see their followings on social media to determine how trusted and known they are.

  1. The footer of the bottom of every page shows our social media links. (They aren't valid Robbie's GYM links, but they take the user to the relevant social media platform.)

  

- #### Returning Visitor Goals

  1. As a **Returning Visitor**, I want to find information about classes and class timetables.

      1. These are under the schedule page.
      2. There are options to show the classes, all of them or individual classes.
      3. Under the timetable, the user can find some information about some of our classes.

  2. As a **Returning Visitor**, I want to find the best way to get in contact with Robbie's GYM with any questions I may have.

      1. The navigation bar highlights the "Contact" page.
      2. Here they can fill out the form on the page to send a message to us or use our contact information to reach us. Alternatively, they can message the GYM on social media.

  3. As  a **Returning Visitor**, I want to find social media links.
      1. The footer contains links to the social media Facebook, Twitter, LinkedIn, Instagram, and Youtube.
      
      2. Whichever link they click, it will be open up in a new tab to ensure the user can easily get back to the website.
      
         

-   #### Frequent User Goals

    As a **Frequent User**, I want to be able to safely log in.

    1. The user would get a "Verify Your E-mail Address" message to make sure the user is valid.

       (we used Django-allauth for registration and login/off functions.)

    As a **Frequent User**, I want to check to see if there are any newly added classes in the timetable

    1. The user would already be comfortable with the website layout and can easily click the right link in the navigation.
    
    As a **Frequent User**, I want to check to see if there are any new products, trainers or membership options.
    
    1. The user would already be comfortable with the website layout and can easily click the right link in the navigation.
    
    As a **Frequent User**, I want to see my notes about my progress and modify or delete them.
    
    1. A logged-in user can add notes to the Schedule page(for example: a note about exercises etc), can be seen by the user only. It can be edited or deleted. Timestamp automatically added at creation or modification.
    
    As a **Frequent User**, I want to see my previous purchases.
    
    1. A logged-in user can see prior purchases by clicking on My Account and on my profile to see user info and past purchases.
    
    As a **Frequent User**, I want to be able to purchase products or membership.
    
    1. A logged-in user can purchase products from the Product page and Membership from the Plans page by clicking on the membership's buy button.
    
       
    
- #### Admin Goals

  1. As an **Admin User,** I want to be able to safely log in.

     1. Django-Allauth gives all the functions for safe authentication.
     2. There are options on the admin panel  Authentication and Authorization to give staff status to users.
     
2. As an **Admin User,** I want to be able to add, edit and delete products.
  
     1. Admin has a full CRUD functionality for the product. Go to my account then choose Product Management .
     
        Then on Add Product admin can add product, after adding a product, a Product details page comes up where Admin can edit or delete the product.
     
     2. Admin can choose a product from the Product page, click on the picture or edit button to go the Edit Product page. If Admin wants to delete product, click on the delete button under the product's picture.
     
  3. As an **Admin User,**  I want to to be able to add, edit, and delete trainers.
  
     1. Admin has a full CRUD functionality for trainers. Go to my account then choose Trainer Management .
       
        Then on Add Trainer Admin can add trainer, after adding a trainer, a Trainer details page comes up where Admin can edit or delete trainer.
       
     2. Admin can choose a trainer from the About us page, click on the picture or edit button to go the Edit Trainer page. If Admin wants to delete a trainer, click on the trainer's picture then on the Trainer page click on the delete button next to the trainer's picture.
       
        4. As an **Admin User,** I want to be able to add, edit, and delete users if needed.
       
       1. Admin has to go to the admin panel (https://robbiesgym.herokuapp.com/admin/auth/user/) ,after log in, Admin able to delete users.
            
            
        5. As an **Admin User,** I want to see users previous purchases.
         
       1. Admin have to go to the admin panel (https://robbiesgym.herokuapp.com/admin/checkout/order/), after log in, Admin able to see user's orders.


### 

### Further Testing

-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge, and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX .
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.
-   We tested every page on [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) for CSS and [Nu HTML checker](https://validator.w3.org/) for HTML . All test came out valid and without errors. The results are here: [CSS](https://github.com/robibrutoczki/lastmilestone/tree/lastmilestone/Documentation/CSSvalid) and [HTML](https://github.com/robibrutoczki/lastmilestone/blob/lastmilestone/Documentation/CSSvalid/Checkout.png) .

Tested Authentication and Note  [pdf](https://github.com/robibrutoczki/lastmilestone/blob/lastmilestone/Documentation/Signinpictures/Signinprocess.pdf)

### Known Bugs

- ```
  /workspace/.pip-modules/lib/python3.8/site-packages/django_currentuser/db/models/fields.py:54: UserWarning: You passed an argument to CurrentUserField that will be ignored. Avoid args and following kwargs: default, null, to.
    warnings.warn(self.warning)
  ```

  This message comes up when running

  ```
  python manage.py runserver
  ```

  in GitPod. This bug makes no effect on the website.

  

-   When popup "toast" messages closed, sometimes a white dot left in the top,right corner of the screen.  

## Deployment

**HEROKU **

### Deployment on Heroku 

Used GitHub Repository to deploy our project on Heroku..

1. Log in to Heroku

2. Go to Deploy on the menu, choose GitHub on the Deployment method.

3. Type in the repository, where our product is.

4. Click  connect

5. Scroll down to Automatic deploys, and enable automatic deploys.

   From now if we push anything to this git repo, it will be automatically deployed on Heroku.

6. Now go to settings, scroll down to Config Vars and press Reveal Config Vars.

   Type in  all the keys and values. Make sure there aren't any typos.

   ```
   USE_AWS                                                           True
   ```

   ```
   SECRET_KEY                                                         ffffffffffffff
   ```

   

7. Go to Resources menu and on the add-ons, type Heroku Postgres.

8. Then attach to are project. Go back to Config Vars and add the keys:

   ```
   DATABASE_URL                                                         postgres://.....
   ```

   

9.  Add all the necessary KEYs and VALUEs.

10. Then there is two ways to deploy your project :

    - In Heroku go back to Deploy,scroll down to Manual deploy, and press Deploy Branch or

    - In GitPod push something (README.md etc) to GitHub

    Go to Activity in Heroku's menu, in the Activity Feed you can see your project uploading/installing.

     

    

11. **Note**

    - Sometimes you need to use Heroku's console, click on More, that is on the top right corner.

      Choose run console, it is a console but with limited functionality, compared to GitPod's terminal.

      I had to use it to my project to sync the database.

    - If you leave a trailing white space after the value of the key, the key might not work.   

    

    

    

### AWS S3

1. Log in to Amazons [AWS](https://aws.amazon.com)

2. Open My Account and click on AWS Management Console

3. Click services on top left corner,then S3 in Storage

4. Go to Create bucket,Add a name and a region (choose the closest to your location).

5. Unblock all public access(We want to share are images and static files with Heroku).

6. Create bucket.

7. Click on your bucket and click CORS Configuration

   ```
   <?xml version="1.0" encoding="UTF-8"?>
   <CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <CORSRule>
       <AllowedOrigin>*</AllowedOrigin>
       <AllowedMethod>GET</AllowedMethod>
       <MaxAgeSeconds>3000</MaxAgeSeconds>
       <AllowedHeader>Authorization</AllowedHeader>
   </CORSRule>
   </CORSConfiguration>
   ```

   then save it.

8. Go to Bucket Policy, click policy generator (left,bottom of the page)

   ###### Step 1: Select Policy Type: S3 Bucket policy

   ###### Step 2: Add Statement(s):

   - Principal: * (all)

   - Actions :GetObject

   - ###### **Amazon Resource Name (ARN)**: get it from previous page (Bucket policy editor ARN: arn:aws:s3::YOURBACKETNAME

   - Generate policy and copy code and save it.

     ```
     {
         "Version": "2012-10-17",
         "Id": "Policy1601113536224",
         "Statement": [
             {
                 "Sid": "Stmt1601113530003",
                 "Effect": "Allow",
                 "Principal": "*",
                 "Action": "s3:GetObject",
                 "Resource": "arn:aws:s3:::YOURBACKETNAME/*"
             }
         ]
     }
     ```

     This means your bucket open to GetObject requests

9. Go to Properties and click on Static website hosting, add index.html and error.html and save

   with this our bucket is ready.

10. Go to services and find IAM **Identity and Access Management (IAM)**.

11. Go to groups and create one (ie:manage-mysite), then go to Policies to create a policy, click on create policy.

12. Click on the JSON tab and you can see the import policy. Click on it then choose S3 AmazonS3FullAccess policy then add the arn. We using a list here. First is the bucket, second is adds another rule for all files.

    Review policy, give a name, and decryption to it then create policy.

    ```
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "s3:*",
                "Resource": [
                    "arn:aws:s3:::yoursite",
                    "arn:aws:s3:::yoursite/*"
                ]
            }
        ]
    }
    ```

    

13. Go back to Groups and Attach Policy. Choose your policy. Tick the box and attach the policy by pressing the button on the right bottom of the page.

14. Go to Users, add a user. Add a user name and **Programmatic access** then next permissions. Add the user to the group.

15. Click until the end to create the user.

16. Download .csv file (containing user keys) These keys need for Django app and Heroku's Config Var. 

17. Then we have to install boto3 and Django-storages for Django. Add storages to installed apps.

    Need a setup to let Django know which bucket we communicate with.

    ```
    if 'USE_AWS' in os.environ:
       
        # Bucket Config
        AWS_STORAGE_BUCKET_NAME = 'robbiesgym'
        AWS_S3_REGION_NAME = 'eu-west-2'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    ```

    

18. Go to Heroku and add these keys to Congig Vars and USE_AWS set to True.

19. Create a custum_storages.py file for settings for media and static.

    ```
    class StaticStorage(S3Boto3Storage):
        location = settings.STATICFILES_LOCATION
    
    
    class MediaStorage(S3Boto3Storage):
        location = settings.MEDIAFILES_LOCATION
        
    ```

    After that :

    ```
    # Static and media files
        STATICFILES_STORAGE = 'custom_storages.StaticStorage'
        STATICFILES_LOCATION = 'static'
        DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
        MEDIAFILES_LOCATION = 'media'
    ```

    Overdrive:

    ```
    # Override static and media URLs in production
        STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
        MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
    ```

    

20. Heroku will run python manage.py collectstatic to collect all static files.

21. Now we just have to push changes to GitHub and it will deploy our project to Heroku.



### STRIPE

1. Log in to [STRIPE](https://aws.amazon.com)

2. We have to use stripe elements to accept payments. We add this to base.html

   ```
   <script src="https://js.stripe.com/v3/"></script>
   ```

3. Go to Checkout and add :

   ```
   {% block postloadjs %}
       {{ block.super }}
       {{ stripe_public_key|json_script:"id_stripe_public_key" }}
       {{ client_secret|json_script:"id_client_secret" }}
       <script src="{% static 'checkout/js/stripe_elements.js' %}"></script>
   {% endblock %}
   ```

   

4. Go to Stripe Home and get the Publishable key and the secret key  and add to Herokus's Config Vars:

   ```
   STRIPE_PUBLIC_KEY                                                pk_testnjksfohijsfp
   STRIPE_SECRET_KEY                                                sk_test_51Gughsae  
   ```

   

5. Go to Developers / Webhooks tab to add endpoint.

   Type the endpoints URL then a description . Choose receive all events then click Add endpoint.

6. Click on Signing secret to reveal the webhook's secret key. 

   ```
   STRIPE_WH_SECRET                                                  whsec_wEmrSCpeNzUZwK7Vmu5l90rVyR
   ```

   

## Credits

### Code

-   Images mainly came from [Pexels](https://www.pexels.com/)

-   [Bootstrap4](https://getbootstrap.com/docs/4.4/getting-started/introduction/): Bootstrap Library used throughout the project mainly to make the site responsive using the Bootstrap Grid System.

-   Used code from the lessons with Code Institute.

### Content

-   All content was written by the developer.


### Acknowledgements

-   My Mentor for continuous helpful feedback.

-   Tutor support at Code Institute for their support.