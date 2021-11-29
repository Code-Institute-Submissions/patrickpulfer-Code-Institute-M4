# Testing Documentation for [World Forums Project](https://github.com/patrickpulfer/Code-Institute-M4)

<br>
<img src="./media/logo.png" width="50%">  
<br>
<br>

# Testing User Stories as defined in our [UX Strategy Section](https://github.com/patrickpulfer/Code-Institute-M4#strategy--user-stories).

## As the owner, I want to...

### Offer a place where I can publicly share interesting stories/news/ideas
1. Navigate to a Forum (ex. Gaming)
2. Click on "+ CREATE A NEW POST" button displayed under the description of the forum
3. Enter a Discussion Title as this field is required. Other fields can be left in blank
4. Click "Submit" button

### Allow other users to participate with their ideas or share their opinion and feedback on my stories
1. Navigate to a Forum where a Discussion Post exists (ex. Gaming)
2. Click on "View Discussion" of one of the listed discussions
3. Scroll to the bottom and in the white empty field below "Your comment", add a comment and click the button "REPLY" at the end of the page

### Allow users to register on my site to actively participate in our discussions but keep read-only open to unregistered users
a.
  1. On the top navigation bar, click on your avatar
  2. Select "Sign Out" and confirm by clicking "Sign Out"
  3. Enter a where a Discussion Post exists (ex. Gaming)
  4. Observe that Discussions are publicly accessible without being logged in

b.
  1. On the top navigation bar, click on "Sign Up"
  2. Fill out the presented form but make sure the submitted email address is valid and unique
  3. Click on "SIGN UP" once finished
  4. In your email, you should find a new email from World Forums asking to confirm your email by clicking on a link. Perform this step.
  5. Once clicked, you should now be back into the Login Page. Login with your newly created account and observe the ability for users to create an account

### Be able to create forums so that discussions can be organized within them
1. Navigate to the Admin Page" by adding "/admin/" at the end of the URL (ex. https://django-test-world-forums.herokuapp.com/admin/)
2. Enter your admin account credential and click "Log In"
3. Search for the "FORUM" section and click on "Forums"
4. On the right side of the page, click on the grey button called "ADD FORUM +"
5. Create a Forum name (ex. sports, preferential lower-case without spaces)
6. Create a Topic (ex. Sports)
7. Add a Description
8. Click "SAVE" and observe the newly created Forum in the homepage

### Offer a free service but also be able to monetize for exclusive member only content
1. Looking at the tests performed earlier, we can conclude this service is for free
2. Ensure you are on the homepage and logged into your account
3. On the top navigation bar, click on your Avatar and select "Profile"
4. On the left side of your profile, click on "Go PREMIUM"
5. Observe the Product Description and the pricing. Click on "CHECKOUT"
6. Observe the Stripe Checkout Page containing the Product Description and requesting payment details
7. To test the payment system without actual monetary transaction, use the card number "4242 4242 4242 4242"
8. Fill the rest of the payment details and click "Pay"
9. Observe that you have been re-directed back to the app
10. Navigate back to your profile and observe a "Concierge" badge being displayed on the left side of your profile


## As an End User or site consumer, I want to:

### View topics as a guest
1. Navigate to the homepage (ex. https://django-test-world-forums.herokuapp.com/)
3. Enter a where a Discussion Post exists (ex. Gaming)
4. Enter a Discussion Post by clicking the respective "VIEW DISCUSSION" button
4. Observe that Discussions are publicly accessible as a guest

### Register for my own account
1. On the top navigation bar, click on "Sign Up"
2. Fill out the presented form but make sure the submitted email address is valid and unique
3. Click on "SIGN UP" once finished
4. In your email, you should find a new email from World Forums asking to confirm your email by clicking on a link. Perform this step.
5. Once clicked, you should now be back into the Login Page
6. Login with your newly created account details
7. Observe the username on the right side of the top navigation bar

### Customize my profile with a bio and profile picture 
1. On the right side of the top navigation bar, click on your Avatar or Username
2. Select "Profile"
3. Find the "Edit" button on the top of your Profile and click on it
4. In your "Avatar section, click on "Choose File to select an image from your computer (square picture is desired) then click "OK"
5. In your "Your Details" section, fill out your First Name, Last Name, Location
6. Click on the calendar symbol below "Your Date of Birth" and select a date
7. Fill out your Biography in your "About You" section
8. Click on the green button called "SAVE CHANGES"
9. Observe your profile being updated with the new details you've just provided

### Create my own discussions
1. Navigate to a Forum (ex. Gaming)
2. Click on "+ CREATE A NEW POST" button displayed under the description of the forum
3. Enter a Discussion Title as this field is required. Other fields can be left in blank
4. Click "Submit" button
5. Observe your new Discussion Post available in the Forum

### Edit my own discussions that I've created
1. Click on "VIEW DISCUSSION" of the same Discussion Post you've created earlier
2. Find the green "EDIT DISCUSSION" button and click on it (found below the details)
3. Click on "Choose File" and select a new Picture for your Discussion Post
4. Click on "SAVE CHANGES" and observe your Discussion Post being updated with the new picture

### Add comments to mine and other discussions
1. On the same Discussion Post, scroll to the bottom of the page
2. Under "Your comment" label, you should find the white text box, select it
3. Enter any comment you want and then click on "REPLY" button at the end of the page
4. Observe your comment being created

### Have an exclusive forum section for premium only
1. By following the previous tests, you should be a Premium Member already
2. Navigate to the homepage (ex. https://django-test-world-forums.herokuapp.com/)
3. Observe the Premium Logo "Concierge" and the Premium Forums right below (Note: Member Forums are the free ones)

<br>

# Functionality Testing

## Code Validation
### HTML Code Validation
I have tested the HTML files found in the following against https://validator.w3.org/nu/ with positive results:
- /templates/
- /forum/templates/forum
- /profiles/templates/profiles

### CSS Code Validation
The file /static/css/main.css has also been positively validated with https://jigsaw.w3.org/css-validator/ and resulted in no error.

### JavaScript Code Validation
I've parsed my main.js file against https://jshint.com/ and noticed that Stripe's Code is failing. This is something outside of my control to fix.

## Django in-build code testing
I have created a limited Django Unit Testing to specifically test the forum app since some models have chain dependencies. To run these tests, use the following code:
~~~bash
python3 manage.py test forum
~~~

## Browser & Device Compatibility
| Device | App | Result |
| --- | --- | --- |
|Android|Google Chrome|✅| 
|iPhone|Safari|✅|
|iPad|Google Chrome|✅|
|PC|Google Chrome on Linux|✅|
|PC|Google Chrome|✅|
|PC|Microsoft Edge|✅|
|Chromebook|Google Chrome|✅| 

## Further Testing

### Top Navigation Bar
| Mobile | PC |
| --- | --- |
|✅ Logged in, Name & Username should appear behind a "Hamburger Menu"|✅ Logged in, Name & Username should appear on the right side| 
|✅ Logged in, clicking on Name & Username should present "Profile" & "Sign Out" menu options|✅ Same as on Mobile| 
|✅ Logged in, clicking on "Profile" navigates to the Profile Page |✅ Same as on Mobile |
|✅ Logged in, clicking on "Sign Out" navigates to the Sign Out confirmation Page |✅ Same as on Mobile |
|✅ Logged out, "Log In" & "Sign Up" should appear behind a "Hamburger Menu"|✅ Logged out, "Log In" & "Sign Up" should appear on the right side| 
|✅ Logged out, clicking on "Log In" navigates to the Login Page |✅ Same as on Mobile |
|✅ Logged out, clicking on "Sign Up" navigates to the Registration Page |✅ Same as on Mobile |
|✅ Clicking on the Logo or "World Forums" should navigate to the Home Page (Forum Overview) |✅ Same as on Mobile |

### Login Page
| Mobile | PC |
| --- | --- |
|✅ Javascript should add the class "form-control" to both "Username" & "Password" form |✅ Same as on Mobile|
|✅ "Username" & "Password" fields should be the same size |✅ Same as on Mobile |
|✅ "SIGN IN" button should appear before "FORGOT PASSWORD?" |✅ "SIGN IN" button should appear on the same line as "FORGOT PASSWORD?" |

### Registration Page
| Mobile | PC |
| --- | --- |
|✅ Logo should correctly scale |✅ Same as on Mobile |
|✅ Javascript should add the class "form-control" to all input fields |✅ Same as on Mobile|
|✅ All form input fields should have the same width |✅ Same as on Mobile |
|✅ "SIGN UP >" button should expand to page width  |✅ Same as on Mobile |
|✅ "SIGN UP >" button should not proceed if form is empty |✅ Same as on Mobile |

### Home Page (Forum Overview)
| Mobile | PC |
| --- | --- |
|✅ Logo should correctly scale |✅ Same as on Mobile |
|✅ Concierge Forums should be displayed first |✅ Same as on Mobile |
|✅ Forums should all be stacked vertically and expand full width |✅ Only two Forums should be displayed per line |
|✅ Clicking on a Forum should navigate to the actual forum |✅ Same as on Mobile |

### Discussion View
| Mobile | PC |
| --- | --- |
|❌ A long URL created in CKEditor may cause horizontal scrollbar to appear. |✅ There should be no horizontal scroll bar |
|✅ Discussion Post images should scale appropriately to not cause overflow |✅ Same as on Mobile |
|✅ Clicking on the name of Discussion Post creator should navigate to his/her profile |✅ Same as on Mobile |
|✅ Clicking on "VIEW DISCUSSION" button should navigate to the respective Discussion View |✅ Same as on Mobile |
|✅ Clicking on "CREATE A NEW POST" should navigate to the Discussion Creation page |✅ Same as on Mobile |

### Discussion New
| Mobile | PC |
| --- | --- |
|✅ "Discussion Title" input field should be properly scaled |✅ Same as on Mobile |
|✅ "Add a picture" selector field should be properly scaled |✅ Same as on Mobile |
|❌ "CKEditor input field may overflow and cause a horizontal scrollbar  |✅ CKEditor should be properly scaled |
|✅ "SUBMIT" button should appear on top of "CANCEL" button |✅ "SUBMIT" &  "CANCEL" should appear on the same line|
|✅ Clicking on "CANCEL" should navigate back to the respective Forum |✅ Same as on Mobile |
|✅ Clicking on "SUBMIT" should not submit the post if no Title has been input |✅ Same as on Mobile |
|✅ Clicking on "SUBMIT" should create a Discussion Post |✅ Same as on Mobile |

### Discussion Edit
| Mobile | PC |
| --- | --- |
|✅ Discussion Post images should scale appropriately to not cause overflow |✅ Same as on Mobile |
|❌ "CKEditor input field may overflow and cause a horizontal scrollbar  |✅ CKEditor should be properly scaled |
|✅ Control buttons should have the following vertical order "SAVE CHANGES", "CANCEL", "DELETE" |✅ Control buttons should all be on the same line |
|✅ "DELETE" button should present a "Are you sure?" modal |✅ Same as on Mobile |
|✅ "Cancel" button in "Are you sure?" modal should navigate to Discussion View Page |✅ Same as on Mobile |
|❌  "Are you sure?" bootstrap modal is not properly scaled |✅ "Are you sure?" bootstrap modal should be properly scaled |
|✅ "CANCEL" button should navigate to Discussion View Page |✅ Same as on Mobile |
|✅ "SAVE CHANGES" button should submit the changes and navigate to Discussion View Page|✅ Same as on Mobile |

### Profile View
| Mobile | PC |
| --- | --- |
|✅ Sections should appear by the following order: Details, Bio, Premium, Profile Edit, Discussion List |✅ Details, Bio, Premium sections should appear on the left side while Edit and Discussion Lists on the right |
|✅ "EDIT" button should only appear if you are viewing own Profile |✅ Same as on Mobile |
|✅ "EDIT" button should navigate to the Profile Edit Page |✅ Same as on Mobile |
|✅ Clicking the forum badge icon should navigate to respective forum |✅ Same as on Mobile |
|✅ Clicking on "VIEW DISCUSSION" button should navigate to respective Discussion Post |✅ Same as on Mobile |
|✅ Clicking on "Go Premium" button should navigate to the Product Overview Page |✅ Same as on Mobile |
|✅ Images should be properly scaled and not overflow |✅ Same as on Mobile |


### Profile Edit
| Mobile | PC |
| --- | --- |
|✅ Sections should appear in the following order: Avatar, Status, Details, Bio |✅ Sections should appear as a grid of 4 boxes |
|✅ "SAVE CHANGES" should appear before "CHANGE PASSWORD"  |✅ "SAVE CHANGES" and "CHANGE PASSWORD" should appear on the same line |
|✅ Clicking on "SAVE CHANGES" should submit the changes |✅ Same as on Mobile |
|✅ Clicking on "CHANGE PASSWORD" should navigate to the Password Change Page |✅ Same as on Mobile |

### Logout Page
| Mobile | PC |
| --- | --- |
|✅ Should be appropriately scaled |✅ Same as on Mobile |
|✅ Clicking on "SIGN OUT" button should end user's session |✅ Same as on Mobile |

### Change Password Page
| Mobile | PC |
| --- | --- |
|✅ Clicking on "Change Password" button with missing fields should not proceed |✅ Same as on Mobile |
|✅ Clicking on "Forgot Password?" link should navigate to the Forgot Password page |✅ Same as on Mobile |
|✅ Javascript should add the class "form-control" to all input fields |✅ Same as on Mobile|