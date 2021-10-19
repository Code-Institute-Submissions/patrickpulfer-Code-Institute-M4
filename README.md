Milestone 3 submission for [Code Insitute](https://codeinstitute.net)

---

<br><br>
<img src="https://img.shields.io/github/last-commit/patrickpulfer/Code-Institute-M4?style=for-the-badge">
<img src="https://img.shields.io/github/repo-size/patrickpulfer/Code-Institute-M4?style=for-the-badge">
<img src="https://img.shields.io/github/languages/count/patrickpulfer/Code-Institute-M4?style=for-the-badge">

# World Forums, let's share together!
<br>

## Project Description
- World Forums is an one-stop all inclusive forum to share ideas and socialize. It is designed to have modern features and a distinctive look.
- This project is my submission to the Milestone 3 project at Code Institute Full-Stack Software Development Diploma. For more information about the submission and project requirements, please visit [Development Documentation](./documentation/development.md).

<br>

## Main URLs are (example with host):
- https://django-test-world-forums.herokuapp.com/ (Main application)
- https://django-test-world-forums.herokuapp.com/admin/ (Admin Portal)

<br>

## Features
Written in python with django framework, the application is designed to bring a feature-rich forum for the end user. Features include:
- Free to use model forum with modern looks
- Stripe payment system to get access to premium-only member forums
- Rich-text discussion creation to impress your friends
- Customizable user profile, where you can express yourself with bio and your own avatar
- Ability to view other user's profile and their discussions
- Admin portal for admins to manage users, payment details, forums, etc.
- Amazong AWS file storage for static and media files
<br>

### Preview:

<br>

### Potential future Feature Roadmap

- Progressive Web App with offline mode
- Ability for users to create custom forums
  <br><br>

## Technologies Used

This application has been built by using the following technologies:

- <a href="https://www.djangoproject.com/"><img height="30" src="https://cdn.svgporn.com/logos/django.svg"></a>
    - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.

- <a href="https://stripe.com/en-ie/payments"><img height="30" src="https://cdn.svgporn.com/logos/stripe.svg"></a>
    - A complete payments platform, engineered for growth

- <a href="https://www.python.org/"><img height="30" src="https://cdn.svgporn.com/logos/python.svg"></a>
    - Python is a programming language that lets you work quickly and integrate systems more effectively.

- <a href="https://www.djangoproject.com/"><img height="30" src="https://cdn.svgporn.com/logos/html-5.svg"></a>
    - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
- [HTML 5](https://www.w3.org/TR/2008/WD-html5-20080122/) / [CSS](https://www.w3.org/Style/CSS/Overview.en.html) / [JavaScript](https://262.ecma-international.org/10.0/index.html)
- [JQuery](https://jquery.com)
  - Simplified DOM manipulation.
- [Font Awesome](https://fontawesome.com/)
  - Iconic SVG, font, and CSS framework.
- [Bootstrap](https://getbootstrap.com/)
  - Front-end framework for web development.
- [Material Design for Bootstrap](https://mdbootstrap.com/)
  - The most popular UI KIT for building responsive, mobile-first websites and apps - free for personal & commercial use
- Python Packages:
    - [Gunicorn](https://pypi.org/project/gunicorn/), [Pillow](https://pypi.org/project/Pillow/), [psycopg2](https://pypi.org/project/psycopg2/), [boto3](https://pypi.org/project/boto3/), [s3transfer](https://pypi.org/project/s3transfer/), [django-allauth](https://github.com/pennersr/django-allauth), [ckeditor](https://ckeditor.com/) - see [requirements.txt](https://github.com/patrickpulfer/Code-Institute-M4/blob/main/requirements.txt) for full list!

<br>

## Development

For development process, please [click here](./documentation/development.md).
<br><br>

## Deployment

### Demo
- Application can be found at https://django-test-world-forums.herokuapp.com/.

<br>

### Requirements

- A host capable to run python3 applications and PIP3, with internet access
  - Example: https://www.heroku.com/


### Steps for dependencies

- Stripe
  1. Create a Stripe account and in your dashboard, navigate to Products, then click on [+ Add Product](https://dashboard.stripe.com/test/products/create)
  2. Create your Product with the desired price and not down the following details: ```ID``` & ```Price ID```
  3. In your dashboard, click on "Developers" and select "Webhooks" from the left menu.
  4. Here, click on "+ Add endpoint" and enter your app's ```Endpoint URL``` and a short description
  5. Once created, select that endpoint and click on ```Reveal``` of your Signing Secret section. Note this ID as you will require it later

- Amazon AWS
  1. Create an Amazon AWS account and login into it
  2. Create an S3 bucket by following [these steps.](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
  3. Follow [this guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/HostingWebsiteOnS3Setup.html) to configure your AWS S3 bucket for static website hosting
  4. In your CORS settings, add the following:
    ~~~
    [
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
    ]
    ~~~
  5. Before following [this guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/walkthrough1.html) to create an IAM user, give control access over the bucket, make sure you download the CSV file with your secret IDs during the user creation!

### Steps for Application Server
- Heroku
  1. [Review official documentation for steps](https://devcenter.heroku.com/articles/getting-started-with-python)
  2. Create a Postgres database and note the URL you will need for your environment variables
  2. Add the necessary environment variables to Heroku
     1. Go to Heroku Settings Tab
     2. Click Reveal Config Vars and populate with the following values:

|Key | Value |
|:---|:---|
|SECRET_KEY | (New Django Secret Key generated at https://djecrety.ir/) |
|HEROKU_HOSTNAME | (From Heroku, this is your app URL) |
|DATABASE_URL| (From Heroku, the URL for your database) |
|USE_AWS | True |
|AWS_ACCESS_KEY_ID | (From AWS, this is in your downloaded CSV file) |
|AWS_ACCESS_SECRET_KEY_ID | (From AWS, this is in your downloaded CSV file) |
|STRIPE_ENDPOINT_SECRET | From Stripe, these can be found by following [this guide](https://support.stripe.com/questions/locate-api-keys-in-the-dashboard) |
|STRIPE_PUBLIC_KEY | From Stripe, these can be found by following [this guide](https://support.stripe.com/questions/locate-api-keys-in-the-dashboard)  |
|STRIPE_SECRET_KEY | From Stripe, these can be found by following [this guide](https://support.stripe.com/questions/locate-api-keys-in-the-dashboard)  |
|STRIPE_WH_SECRET | (From Stripe, this is the Webhook Secret you've noted earlier) |
|EMAIL_HOST_USER | (From Google, a GMail account you would like to use to send emails from) |
|EMAIL_HOST_PASS | (App Password for the same Gmail account by following [this guide.](https://support.google.com/accounts/answer/185833)) |

### Application

  4. Post deployment setup requires you to download and execute [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).
  5. In your Heroku CLI, run the following commands:
  ~~~bash
  heroku run python3 manage.py migrate
  ~~~
  6. Then create a super user with the following command and not the username and password:
  ~~~bash
  heroku run python manage.py createsuperuser
  ~~~
  7. Run the app in Heroku and navigate to the admin pannel, usually found by appending ```/admin/``` to your URL
  8. Next to "Products", click on "Add".
  9. Add a name for your premium forum access and enter your "Stripe Product ID" you've noted earlier.
  10. On the same page under Prices, click "Add another Price" and add the Price ID you've created earlier + the actual price (example 10€ would be ```1000```)
  11. All steps are done for deployment.

#### Alternative deployment (Directly to Linux Server)
  1. You may deploy the repo locally. The follow instructions below are for a Linux machine
  2. Create a folder where you want the App to reside and navigate to it in your command line
  3. Clone the App from GitHub:
  ```bash
  git init
  git clone https://github.com/patrickpulfer/code_insitute_m4.git .
  ```
  4. Create an environment variable file called .env and add the variables advised above.
  5. Install dependencies with PIP3:
  ```bash
  pip3 install -r requirements.txt
  ```
  6. Run the initial setup for the database:
  ```bash
  python3 manage.py migrate
  ```
  7. Run the App
  ```bash
  python3 manage.py runserver
  ```
  Note: If you plan to deploy as an actual production server on Linux, you may want to look into [WSGI](https://wsgi.readthedocs.io/en/latest/what.html), [Gunicorn](https://gunicorn.org/) and a proper web server like NGINX.
  <br>