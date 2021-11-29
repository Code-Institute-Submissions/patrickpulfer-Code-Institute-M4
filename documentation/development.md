# Testing Documentation for [World Forums Project](https://github.com/patrickpulfer/Code-Institute-M4)

<br>

## Django in-build code testing

~~~bash
python3 manage.py test forum
~~~

## Bug Testing (Site functionalities)

### Browser & Device Compatibility

- Main App has been tested with:
  - Chrome on Android
  - Safari on iOS
  - Microsoft Edge for Linux, Chrome & Firefox on Desktop
- Admin Page
  - Chrome on Android
  - Safari on iOS
  - Microsoft Edge for Linux, Chrome & Firefox on Desktop


### HTML Code Validation

HTML files within the following folders have been tested against https://validator.w3.org/nu/:
- /templates/
- /forum/templates/forum
- /profiles/templates/profiles

Result:
- Validator showed no errors for the HTML files used in this project.


### CSS Code Validation
The file /static/css/main.css has been validated with https://jigsaw.w3.org/css-validator/ and resulted in no error.


### JavaScript Code Validation


### Test 2 - End User Flow

1. Navigate to App URL (https://django-test-world-forums.herokuapp.com/ for example)
2. Test navigation by clicking profile picture, then "Profile" or "Sign Out"
3. Test navigation of menu bar by shrinking the screen
4. Test navigation by clicking on a Forum


### Test 3 - Registration & Authentication
1. Navigate to App URL (https://django-test-world-forums.herokuapp.com/ for example)
2. Ensure you are not logged in
3. Click on "Sign Up" button which should appear in the top right corner 
4. Register an account and observe if you receive an email with confirmation link
5. Click on the link provided in the email and login


## Feedback from End User

### Aggie,

- _"Without any explanation from Patrick, it was very easy to register an account, login and create my first test discussion!"_

