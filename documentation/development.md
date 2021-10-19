## Project Requirements for Code Institute Full-Stack Software Development Diploma

## Full Stack Frameworks with Django Milestone Project
- Build a full-stack site based around business logic used to control a centrally-owned dataset.
- Set up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service.
- Setup a e-commerce functionality by using Stripe payments
  <br>

## My approach

- I have taken inspiration from a real-life website called [Reddit](https://www.reddit.com/) where users can share ideas and discuss these ideas in a "forum"-style manner.

- In this document, I will attempt to explain the process I went through in thinking, planning and developing this project by utilizing industry-standard methodologies.

<br>

# UX Design

<br>
For this project, I've adopted the methodology of the five planes of UX, which consist of:

- Strategy
- Scope
- Structure
- Skeleton
- Surface Design

> “The Elements of User Experience” book written by Jesse James Garrett, one of the founders of Adaptive Path, a user experience consultancy based in San Francisco.

<br>

## Strategy

### User Stories & Requirements

- Owner, Administrator:
    1. I want to offer a place where I can publicly share interesting stories/news/ideas
    2. I want other users to participate with ideas or share their opinion on my stories
    3. I want to offer a free service but also be able to monetize for exclusive member only content
    4. I want to customize my profile to include a short "Who am I" and ideally a profile picture

- End Users, site consumers:
    1. I want to share my ideas/opinions and have other users like me participate in the conversation
    2. I want to read other user's ideas and be able to participate in their conversation
    3. I want to at least read other user's ideas without having to login
    4. I want to have an exclusive club access, even if have to pay for it!
    5. I want to clutter or distraction, an intuitive forum that works on my PC, tablet and Phone

<br>

### Scope of this Project (based on owner and end user requirement/stories)

- To create an application that is accessible on mobile, tablet, laptops and desktops and is easy to navigate
- To create a website with uncluttered, logical and intuitive navigation which is easy to follow
- To store, manipulate, edit and delete (CRUD) data in a secure database, in this case Postgres
- To create a monetization strategy for exclusive member access
- To create an app (website) written with Django framework, ready to be deployed to Heroku

<br/>

### Structure

- Forum Page (Mobile first approach)
  - Top:
    - A navigation bar with Title and a "hamburger" menu if accessed by small screen devices. This menu will allow the user to visit their profile and login/logout
  - Central:
    - Forums are displayed as large boxes for intuitive navigation
    - "Concierge" Premium Forums are displayed first if user is part of the club
  - Bottom:
    Simple footer displaying Copyright and Credit of the app creator

- Discussion List Page (Mobile first approach)
  - Top:
    - A navigation bar with Title and a "hamburger" menu if accessed by small screen devices. This menu will allow the user to visit their profile and login/logout
  - Central:
    - Discussion Name and Description at the top, including a "Create new Post" button for logged users
    - List of all Discussion posts below, including the Title, the discussion body, link to it's creator and button to "view" the discussion
  - Footer:
    - Footer will display the Copyright and the credits for the app creator

- Discussion View Page (Mobile first approach)
  - Top:
    - A navigation bar with Title and a "hamburger" menu if accessed by small screen devices. This menu will allow the user to visit their profile and login/logout
  - Central:
    - Discussion picture on top, followed by the Title and the actual discussion post
    - At the end of the post, additional details like link to post creator, link to it's belonging forum and date of the post will be shown
    - If the logged user is also the creator, he may edit the post via button that appears at the end
  - Footer:
    - Footer will display the Copyright and the credits for the app creator

<br/>

### Skeleton

To be adhered to the structure outlined above, the following wireframes were drafted:

- End User Welcome Screen  
  <img src="./media/wireframe_mobile1.png" width="30%">

- End User Questions Card Screen  
  <img src="./media/wireframe_mobile2.png" width="70%">

- Admin Panel Screen  
  <img src="./media/wireframe_admin1.png" width="70%">

Note:

- Design has been implemented to draw the end user to the middle of the screen

<br/>

### Surface Design

To emphasize the origin of the project and the company behind it, the decision was made to include the colour scheme that would best match the colours in the existing logo:

- <img src="https://yourcoach.ie/resources/img/logos/logo_2020.png" width="5%">

Colour pallet:

- Main Colour (buttons & titles): <span style="color:#F3F0F1;background-color:#990011FF;"> #990011FF</span>
- Main background:<span style="color:black;background-color:#FCF6F5FF;">#FCF6F5FF</span>


<br>

### Database Design

| <img src="./pictures/db_admin.png"> | <img src="./pictures/db_questions.png"> | <img src="./pictures/db_settings.png"> |
| ----------------------------------- | --------------------------------------- | -------------------------------------- |

<br>

## Testing

<br>

## Debug Logging

The application has been designed with debugging in mind. In your main application folder, you will find a file called `logs.log` which will contain similar information as below:

```
2021-05-12 21:13:12,267 INFO     Main application has been initialized!
2021-05-12 21:13:12,364 INFO     MongoDB Connected successfully!
2021-05-12 21:13:12,743 INFO     MongoDB Server version: 4.4.6
2021-05-12 21:13:12,759 INFO     MongoDB Text Search index has already been created... skipping.
2021-05-12 21:13:12,781 INFO     Database 'TheInterviewMasterDeck' detected in MongoDB!
2021-05-12 21:13:12,785 INFO      * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
2021-05-12 21:18:24,160 INFO     127.0.0.1 - - [12/May/2021 21:18:24] "[37mGET / HTTP/1.1[0m" 200 -
2021-05-12 21:18:26,403 INFO     127.0.0.1 - - [12/May/2021 21:18:26] "[37mGET /start HTTP/1.1[0m" 200 -
2021-05-12 21:18:35,912 INFO     127.0.0.1 - - [12/May/2021 21:18:35] "[37mGET /admin HTTP/1.1[0m" 200 -
2021-05-12 21:18:35,930 INFO     127.0.0.1 - - [12/May/2021 21:18:35] "[36mGET /static/admin_main.css HTTP/1.1[0m" 304 -
2021-05-12 21:18:36,009 INFO     127.0.0.1 - - [12/May/2021 21:18:36] "[37mGET /static/images/wallpaper.jpg HTTP/1.1[0m" 200 -
2021-05-12 21:18:56,733 INFO     Admin Login attempt successful
2021-05-12 21:18:56,753 INFO     127.0.0.1 - - [12/May/2021 21:18:56] "[37mPOST /admin HTTP/1.1[0m" 200 -
2021-05-12 21:18:58,616 INFO     127.0.0.1 - - [12/May/2021 21:18:58] "[37mGET /admin_cards HTTP/1.1[0m" 200 -
2021-05-12 21:19:01,974 INFO     127.0.0.1 - - [12/May/2021 21:19:01] "[37mGET /admin_card_update/11 HTTP/1.1[0m" 200 -
2021-05-12 21:19:05,471 INFO     Questions Card has been deleted successfully
2021-05-12 21:19:05,472 INFO     127.0.0.1 - - [12/May/2021 21:19:05] "[32mGET /admin_card_delete/609855be0f54ae446426e983 HTTP/1.1[0m" 302 -
2021-05-12 21:19:05,518 INFO     127.0.0.1 - - [12/May/2021 21:19:05] "[37mGET /admin_cards HTTP/1.1[0m" 200 -
```

## Bug Testing (Site functionalities)

### Test 1 - Browser & Device Compatibility

- Main App has been tested with:
  - Chrome on Android
  - Safari on iOS
  - Microsoft Edge for Linux, Chrome & Firefox on Desktop
- Admin Page
  - Chrome on Android
  - Safari on iOS
  - Microsoft Edge for Linux, Chrome & Firefox on Desktop

### Test 3 - Errors at parsing HTML & CSS

- Website has been tested at https://validator.w3.org/nu/ & https://jigsaw.w3.org/css-validator/ and showing no errors related to the app
- https://jigsaw.w3.org/css-validator/ shows CSS errors specifically for external dependencies, which I can't resolve on my own

### Test 4 - End User Flow

1. Navigate to App URL (http://the-interview-master-deck.herokuapp.com/ for example)
2. Test swipe left:  
   <img src="./pictures/test_user1.png" width="20%">
3. Click on Start:  
   <img src="./pictures/test_user2.png" width="20%">
4. Swipe a few cards to the left and observe Cards being sorted randomly
5. Click on "Search" button:  
   <img src="./pictures/test_user3.png" width="20%">
6. Enter a keyword in the text box, in this case "leaving" and click "Search:"  
   <img src="./pictures/test_user4.png" width="20%">
7. Observe all cards being displayed with the selected word "leaving":  
   <img src="./pictures/test_user5.png" width="20%">

### Test 5 - Admin Login Flow

1. Navigate to the Admin Portal (http://the-interview-master-deck.herokuapp.com/admin as example)
2. Enter your admin credentials created earlier during setup (Admin:SuperSecret123! for the demo) and click Login:  
   <img src="./pictures/test_login1.png" width="50%">
3. Observe login being successfully and Python Flash displaying the following message:  
   <img src="./pictures/test_login2.png" width="20%">

### Test 6 - Admin Question Cards Creation and Deletion Flow

1. You should be logged into the Admin Portal
2. Click on "Cards" in your top navigation bar
3. On the right side of the screen, we will enter a test interview question as shown below:  
   <img src="./pictures/test2.png" width="80%">
4. After entering a test interview question, tick the box "Visible?" and then click "Add New Card"
5. Observe the Python Flash message about the card creation and the new Interview Question Card appearing at the bottom of the list as shown below:
   <img src="./pictures/test3.png" width="50%">
6. Now on your mobile phone, navigate to the end user page (http://the-interview-master-deck.herokuapp.com/start), swipe through a few Interview Question Cards and observe if the new question does appear as shown below:  
   <img src="./pictures/test4.png" width="20%">
7. Back in your Admin Portal, click on "Update" button on the newly created Interview Question Card. You should now see a new page as shown below:
   <img src="./pictures/test5.png" width="70%">
8. On this screen, click on "Delete Card". You should see a confirmation asking if you really want to delete the Interview Question Card. Click "OK":  
   <img src="./pictures/test6.png" width="30%">
9. Once confirming, you should be re-directed to the Cards Management Page. Observe the deleted card missing and Python Flash message informing on the action as shown below:  
   <img src="./pictures/test7.png" width="40%">

Note: If you have access to `logs.log`, you can to see the workflow being reflected in the debug logging"
<br>

### Additional testing

To test the update Interview Question Card functionality, you may click on "Update" of an Interview Question Card, change the text and click "Update". Once back at your Card Management page, you should see the particular question being altered.

<br>

## Feedback from Stakeholders

### Aggie, yourcoach.ie

- _"I am very happy with the result! I am ready to recommend, and use this app as a supporting tool for my coaching practices. The Admin Portal is very easy to navigate through so no training required for me!"_

### End User 1

- _"Simple, does what I would want and no adds"_

### End User 2

- _"This is perfect! An app I'm not afraid to use because it does not distract me. Linking/Bookmark specific questions is a plus!!!"_
