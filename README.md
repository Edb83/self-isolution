# Self Isolution

![alt text](# "Responsive sample")

**[Live demo](https://self-isolution.herokuapp.com/)**

---

<span id="top"></span>

## Index

- <a href="#context">Context</a>
- <a href="#ux">UX</a>
  - <a href="#ux-overview">Overview</a>
  - <a href="#ux-stories">User stories</a>
  - <a href="#ux-wireframes">Wireframes</a>
  - <a href="#ux-design">Design</a>
- <a href="#database-model">Database model</a>
- <a href="#features">Features</a>
  - <a href="#features-current">Current</a>
  - <a href="#features-future">Future</a>
- <a href="#technologies">Technologies Used</a>
- <a href="#testing">Testing</a>
  - <a href="#testing-auto">Automated</a>
  - <a href="#testing-manual">Manual</a>
  - <a href="#testing-responsive">Responsiveness</a>
  - <a href="#testing-resolved">Resolved issues</a>
  - <a href="#testing-unresolved">Unresolved issues</a>
- <a href="#deployment">Deployment</a>
- <a href="#credits">Credits</a>

---

<span id="context"></span>

## Context

The COVID-19 pandemic has had a dramatic effect on everyone's lives, not least those of working parents who can no longer rely on childcare due to the restrictions put in place.
When a case occurs in your child's bubble and they are forced to self-isolate at home, you can expect to spend your days fitting work in around your children's homeschooling
and other needs. Without the option of leaving the house you'll be climbing the walls in no time, feeling guilty that you've left them to watch Peppa Pig for 4 hours straight, again.
You need to break the cycle and find some inspiration without having to create elaborate plans which will likely be greeted with a slow clap and roll of the eyes, leaving you
ever more frustrated with them, yourself and the situation at large. You need a Self Isolution.

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>
<span id="ux"></span>

## UX

<span id="ux-overview"></span>

### Overview

Self Isolution is a site aimed at parents of young children who have been put into self-isolation. Users are looking for ideas for simple activities to entertain, educate and somehow enrich the lives of their offspring, without leaving the comfort of their own homes. All content is available without registering, but once logged in users can add their
own activity ideas and share the collective burden of raising this misfortunate generation. All design decisions have been made with the following goals in mind:
- Accessibility
- Ease of use
- Responsiveness
- Simplicity

<span id="ux-stories"></span>

### User stories

#### Overarching user expectations

- Visually appealing
- Easy to navigate
- Intuitive icon/button functionality
- Secured passwords

#### As a first-time visitor I want

- To immediately understand what the purpose of the site is and what it can provide
- To see all content without having to register
- To be able to search for keywords
- To be able to filter activities by category
- To be able to register easily without needing to input lots of information

#### As a returning user I want

- To log in and out easily
- To be able to add new activities easily
- To be able to edit or delete activities I have added
- To upload my own images rather than inputting a URL
- To be able to see all the activities I have added in one place
- To be able to 'favourite' activities created by other users

#### As the site owner I want:

- To be able to edit or remove content created by users
- To be able to add, edit or remove categories

<span id="ux-wireframes"></span>

### Wireframes

Wireframes for **mobile** and **desktop** can be accessed [here](wireframes/).

There were some noteworthy deviations from the plan. These were:

1. Search bar given greater prominance within Activities page rather than being housed in navbar
2. Prep time not included as a MongoDB key
3. Ages hardcoded instead of residing in separate MongoDB collection
4. Likes not included, meaning 'Popular activities' was replaced by 'Recent activities' on the home page
5. Categories dropdown moved to separate Categories page
6. Ages dropdown removed, but users can still filter by age by clicking on existing activity's target age
7. Users' collection keys simplified to just username and password
8. Activities card content revised based on testing
9. Activity page layout revised due to awkward styling presentation, but functionality mostly unchanged

<span id="ux-design"></span>

### Design choices

The decision to use Materialize means customisation is somewhat limited, but this is an acceptible compromise given the site's purpose of displaying user content clearly. Judicious use of the framework's cards gives the site a solid and consistent feel which promotes the user content. 

#### Colours

TBC

##### Core

TBC

- ![#ffffff](https://via.placeholder.com/15/ffffff/000000?text=+) #ffffff (White)


#### Fonts

[Bubblegum Sans](https://fonts.google.com/specimen/Bubblegum+Sans#about)

TBC

[Montserrat](https://fonts.google.com/specimen/Montserrat#about)

TBC

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>


<span id="database-model"></span>

### Database model

MongoDB's non-relational/document-based database structure makes sense for this type of site as there are only a few relationships between the various collections. Nevertheless, the ability to relate certain collections to one another was used to preserve key relationships which could have been lost due to users making changes to their content.

#### Activities collection

**Key**|**Type**|**Notes**
:-----:|:-----:|:-----:
_id|ObjectId|
activity_name|string|The user's chosen title of the activity.
category_name|string|To avoid potential muddling of activity categories the decision was made to prevent category names being changed by the admin, which meant using a string rather than ObjectID was preferable.
target_age|string|Options such as 'Under 2' and '6+' meant using int was not appropriate here.
activity_summary|string|Brief summary used to flesh out cards on Activities page.
activity_details|string|The main content of the View Activity page.
image_file|string|This is a link to a user image uploaded to Amazon AWS. If left blank the relevant category.image_file will be used, but this field will be left unaltered.
created_by|string|Set on activity creation. As users cannot change username, simpler to store as a string.
date_added|string|Set on activity creation. Activities are sorted by _id therefore simplest to store as a string.
activity_equipment|string|Rather than storing as an array, it was simpler to request users enter each item on new line and manipulate in Python.

#### Categories collection

**Key**|**Type**|**Notes**
:-----:|:-----:|:-----:
_id|ObjectId|
category_name|string|The admin's chosen title of the category. Cannot be changed.
category_summary|string|Brief summary to add some meat to the Categories cards.
image_file|string|This is a link to an image uploaded to Amazon AWS by the admin.
activity_list|Array|Given the possibility of users changing the name of their activity, the decision was made to store activity ObjectIDs in array.


#### Users collection

**Key**|**Type**
:-----:|:-----:
_id|ObjectId|
username|string|Chosen by user on account creation. Cannot be changed.
password|string|Chosen by user on account creation and hashed using Werkzeug Security.

#### Ages collection

Initially it was anticipated that the admin might need the ability to change the target age ranges, but as the site progressed this no longer seemed necessary and this collection was abandoned and replaced by a hardcoded selection.

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="features"></span>

## Features

<span id="features-current"></span>

### Current

**?. Material design**

MaterializeCSS features:
- Cards
- Chips
- Forms
- Input character counter
- Menu dropdown
- Modals
- Side navigation bar
- Toasts

**?. Online database**

MongoDB

**?. Secure user login**

Werkzeug hashed passwords

**?. User profile**

A user can view all activities they have created in one place and easily edit or delete them

**?. CRUD functionality**

All visitors can
- view all activities
- view all categories

User can
- add own activities
- edit own activities 
- delete own activities

Admin can
- add own activities
- edit any activity
- delete any activity
- add category
- edit category
- delete category

**?. Search**

**?. Filter**

All visitors can filter activities by
- category
- target age
- author

**?. Image uploads**

Amazon AWS using S3 Bucket

**?. Image resizing**

Pillow

**?. Admin rights**

The admin 

**?. Defensive programming**
- user session check for accessing restricted content (add, edit, delete activity; add, edit, delete category, PROFILE?)
- moving activities to "Unassigned" category if associated category deleted by admin
- delete confirmation for activities and categories
- 404 and 500 error handling
- utilising `ObjectId` wherever sensible, to prevent reference to a key which a user could change (e.g. `category.activity_list`)


<span id="features-future"></span>

### Future

**TBC**

- Edit user
- Delete user
- Favourite activities
- Superuser rather than single admin
- Admin area (page to view all site content in one place and edit as required inc delete user)
- Contact admin
- Pagination
- Deeper profile (number of kids, interests)
- Ability to view other profiles
- Add comments to activities
- Image delete from S3 Bucket
- Speedier hosting of S3 Bucket images

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="technologies"></span>

## Technologies Used

### Languages

- HTML
- CSS
- Javascript
  - [jQuery](https://jquery.com/)
- Python
  - [Flask Paginate](https://pythonhosted.org/Flask-paginate/)

### Project management

- [Balsamiq](https://balsamiq.com/wireframes/) - Wireframe creation tool
- [GitHub](https://github.com/) - Version control and deployment
- [GitPod](https://gitpod.io/) - IDE used to code the game

### Style and theme

- [Autoprefixer](https://autoprefixer.github.io/) - a PostCSS plugin which parses CSS and adds vendor prefixes
- [Favicon.io](https://favicon.io//) - to generate the app's favicons for a variety of devices
- [Google Fonts](https://fonts.google.com/) - TBC
- [Materialize](https://materializecss.com/) - TBC

### Online resources

- [Am I Responsive?](http://ami.responsivedesign.is/) - to produce the README showcase image

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="testing"></span>

## Testing

<span id="testing-auto"></span>

### Automated testing

[Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) - audit summary for both desktop and mobile:

- Performance: **X - X%**
- Accessibility: **X - X%**
- Best Practices: **X - X%**
- SEO: **X - X%**

[W3C - HTML](https://validator.w3.org/) - ? errors, ? warnings - **PASS**

[W3C - CSS](https://jigsaw.w3.org/css-validator/) - ? errors, ? warnings - **PASS**

Details TBC

- Use of...

[CSS Lint](http://csslint.net/) - X errors, X warnings - **PASS**

Details TBC

- Use of...


[Unicorn revealer - overflow](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln/related) - no evidence of overflow - **PASS**

[JS Hint](https://jshint.com/) - X errors, X warnings - **PASS**

Details TBC

- Use of...

<span id="testing-manual"></span>

### Manual testing

**Summary**:

TBC... :

**1. TBC**

- TBC

<span id="testing-responsive"></span>

### Responsiveness

TBC

#### Browsers

Tested on:

- Chrome
- Edge
- Firefox
- Safari (iOS)

#### Screen sizes

Tested with Chrome DevTools using profiles for:

- Moto G4
- Galaxy S5
- Pixel 2
- Pixel 2 XL
- iPhone 5 SE
- iPhone 6/7/8
- iPhone 6/7/8 Plus
- iPhone X
- iPad
- iPad Pro

... and also using the responsive profiles of:

- Mobile S (320px)
- Mobile M (375px)
- Mobile L (425px)
- Tablet (768px)
- Laptop (1024px)
- Laptop L (1440px)

Real world testing on:

- iPhone 6S
- iPhone SE
- iPhone 11 Pro
- Asus ZenBook
- Dell XPS 7590

### Issues and resolutions

<span id="testing-resolved"></span>

#### Resolved

**TBC**

- TBC

**Materialize select dropdown does not function correctly on iOS. Either dropdown does not appear or selects the wrong item when clicked**
- Solution: Stopping propagation on `touchend` event (https://stackoverflow.com/a/52851046)

**iOS select caret visible when using the Materialize fix above**
- Solution: adding `-webkit-appeance: none` to select elements (https://stackoverflow.com/questions/7638677/how-can-i-remove-the-gloss-on-a-select-element-in-safari-on-mac)

**Portrait images rotating on resize**
- Solution: caused by PIL not reading image EXIF metadata. Fixed by importing ImageOps and using `ImageOps.exif_transpose(image)` (https://www.mmbyte.com/article/46440.html)

**Images uploaded to AWS not updating on edit**
- Solution: missing `enctype="multipart/form-data"`

**Images not uploading on deployed site**
- Solution: add AWS secret keys to cvars on heroku

**Unable to use PIL.ImageOps on image files once opened**
- Solution: save format of `raw_imag`e to pass into `new_image` so that it can be accessed by ImageOps (https://stackoverflow.com/questions/29374072/why-does-resizing-image-in-pillow-python-remove-image-format)

**pymongo.errors.InvalidOperation: cannot set options after executing query**
- Solution: to various issues(!) - using `list()`

**Session-only pages and functions are accessible even if not logged in 'brute-forcing' url**
- Affects: `add_activity`, `edit_activity`, `delete_activity`, `add_category`, `edit_category`, `delete_category`
- Solution: add conditional `if "user" in session` around functions with redirect to appropriate page if not found

**On category deletion and subsequent reallocation of child activities to "Unassigned" category, only first item reallocated in MongoDB**
- Solution: create a list of dependent activities and use `$addToSet` and `$each` options to add to the `unassigned_category` rather than `$push` inside a `for` loop:
`mongo.db.categories.find_one_and_update(unassigned_category, {"$addToSet": {"activity_list": {"$each": activities}}})`

**Paginate linting error**
`Possible unbalanced tuple unpacking with sequence defined at line 233 of flask_paginate: left side has 3 label(s), right side has 2 value(s)pylint(unbalanced-tuple-unpacking)`
- Resolution: running `app.py` through Flake8 does not reveal this to be an error

<span id="testing-unresolved"></span>

#### Unresolved

?


## Deployment

There is just one branch of this project (master) and the deployed version of this site is the most current version in the repository.

### How to deploy

TBC

### How to run locally

TBC


<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="credits"></span>

## Credits

#### Tutorials and inspiration

- [Code Institute Task Manager Project](#)
- [Boto S3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#id224)
- [Pillow](https://pillow.readthedocs.io/en/stable/index.html)


#### Code used/modified from other sources

- [Handling file uploads with Flask](https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask)
- [Uploading to AWS S3 using boto](https://www.zabana.me/notes/flask-tutorial-upload-files-amazon-s3)
- [Resizing images prior to S3 upload](https://stackoverflow.com/a/56241877)
- [Image processing with Pillow](https://dzone.com/articles/image-processing-in-python-with-pillow)
- [Checking duplicate key value pairs](https://stackoverflow.com/a/3897516)


### Content

- All text outside of user-generated content is original
- [Favicon](https://favicon.io/emoji-favicons/house)

### Acknowledgements

- Jonathan Munz (Code Institute Mentor) - for his reassurance, support and invaluable suggestions
- Tim (Code Institute Tutor) - for his patience and help solving pushing a list to a MongoDB array
- Michael (Code Institute Tutor) - for walking through a merge conflict resolution
- ? (Code Institute Tutor) - for help spotting a key missing `enctype="multipart/form-data"` on a template

### Disclaimer

This site was developed for educational purposes.

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>