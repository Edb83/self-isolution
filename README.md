# Self Isolution

![alt text](amiresponsive.png "Responsive sample")

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
- <a href="#deployment">Deployment</a>
- <a href="#credits">Credits</a>

---

<span id="context"></span>

## Context

The COVID-19 pandemic has had a dramatic effect on everyone's lives, not least those of working parents who can no longer rely on childcare or school due to the restrictions put in place.
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

- Consistent
- Easy to navigate
- Intuitive
- Responsive
- Secure
- Visually appealing

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

Wireframes created at the start of the project for **mobile**, **tablet** and **desktop** can be accessed [here](wireframes/), as well as the planned **site map** and **data schema**.

There were some noteworthy deviations from the plan. These were:

1. The Search bar was given greater prominance within Activities page rather than being housed in the Navbar.
2. Prep time was not included as a MongoDB key in the Activities collection to simplify the volume of user input required.
3. Ages were hardcoded instead of residing in a separate MongoDB collection and having their own area on the site.
4. Likes were not included due to time constraints, meaning 'Popular activities' was replaced by 'Recent activities' on the Home page.
5. The Categories dropdown was moved to a separate Categories page to declutter the Navbar.
6. The Ages dropdown was removed, but users can still filter by age by clicking on an existing activity's target age.
7. The Users' collection keys were simplified to just username and password as they would provide no functionality.
8. The Activities card content was revised following testing.
9. The View Activity page layout was revised due to awkward styling presentation, but functionality was mostly unchanged.

<span id="ux-design"></span>

### Design choices

The decision to use Materialize meant customisation was somewhat limited, but this was an acceptable compromise given the site's purpose of displaying user content clearly. Judicious use of the framework's cards gives the site a solid and consistent feel which promotes the user content. 

#### Colours

[Coolers](https://coolors.co/) was used to find an appropriate colour scheme for the site, however the decision was made to default to Materialize's stock colours wherever possible, and to simply use the hex values of the framework's named colours in any required custom CSS styling.

**Core**

Two bold shades of Materialize's indigo were used for the core elements of the site, namely the Navbar, Footer and section headings. The aim was to have a neutral colour, not overly warm, to maintain a contrast with the white text and background.

- ![#3949ab](https://via.placeholder.com/15/3949ab/000000?text=+) #3949ab (indigo darken-1)
- ![#1a237e](https://via.placeholder.com/15/1a237e/000000?text=+) #1a237e (indigo darken-4)

**Cards**

To give the activity and category cards some weight, lighter shades of indigo and green were used. The aim was to distinguish the two types of cards so that users can tell at a glance which page they are on and what the cards are representing. To provide a touch of variety, the chips containing required equipment on the View Activity page have a lighter shade of blue.

- ![#e8eaf6](https://via.placeholder.com/15/e8eaf6/000000?text=+) #e8eaf6 (indigo lighten-5)

- ![#f1f8e9](https://via.placeholder.com/15/f1f8e9/000000?text=+) #e8eaf6 (light-green lighten-5)

- ![#0077ff](https://via.placeholder.com/15/0077ff/000000?text=+) #0077ff ("Dodger Blue")

**Buttons**

It was important for the buttons to have have consistent colours with intuitive suggestions about their functions. A slightly lighter shade of indigo was used for buttons which could be classed as part of the outer 'shell' of the site, responsible for navigating the site and matching the Navbar and Footer's colour. These are  Search, 'Back to Activities', active pagination page, 'View' (category's activities) and 'Cancel' (a deletion). One exception was made for the hover effect of activity filters (i.e. target age, category and activity author), to provide some variety.

A 'green means go' approach was taken for buttons which suggest the user will be making changes to their content (i.e. Edit and 'Submit'). Negative user actions (i.e Delete and Cancel search) are naturally red.

Orange was used as an accent colour for the pulsing FAB 'Add Activity' and 'Add Category' and also for Toast alert messages.

- ![#26a69a](https://via.placeholder.com/15/26a69a/000000?text=+) #26a69a (teal lighten-1)

- ![#3f51b5](https://via.placeholder.com/15/3f51b5/000000?text=+) #3f51b5 (indigo)

- ![#f44336](https://via.placeholder.com/15/f44336/000000?text=+) #f44336 (red)

- ![#ff6d00](https://via.placeholder.com/15/ff6d00/000000?text=+) #f44336 (orange accent-4)

**Transition and transformation**

To add to the physicality of the cards, the Materialize `hoverable` (all) and `waves-effect` (categories) classes were used. To give the Footer a touch of interactivity, a subtle scale effect has been applied on clickable links.

#### Fonts

[Bubblegum Sans](https://fonts.google.com/specimen/Bubblegum+Sans#about)

A cursive font which gives a sense of childlike playfulness, in keeping with the site's theme of creativity and fun. This font is used sparingly for the Self Isolution logo, sub-headings and hard titles. 

[Montserrat](https://fonts.google.com/specimen/Montserrat#about)

Monserrat is the ever steady foil to more playful fonts like Bubblegum Sans, used here for all other content to provide a soft clarity.

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="database-model"></span>

### Database model

MongoDB's non-relational database structure makes sense for this type of site as there are only a few relationships between the various collections. Nevertheless, the ability to relate certain collections to one another was used to preserve key relationships which could have been lost due to users making changes to their content (e.g. activity_name).

#### Activities collection

|**Key**|**Type**|**Notes**|
|:-----|:-----|:-----|
|_id|ObjectId||
|activity_name|string|The user's chosen title of the activity.|
|category_name|string|To avoid potential muddling of activity categories the decision was made to prevent category names being changed by the admin, which meant using a string rather than ObjectID was preferable.|
|target_age|string|Options such as 'Under 2' and '6+' meant using int was not appropriate here.|
|activity_summary|string|Brief summary used to flesh out cards on Activities page.|
|activity_details|string|The main content of the View Activity page.|
|image_file|string|This is a link to a user image uploaded to Amazon AWS. If left blank the relevant category.image_file will be used, but this field will be left unaltered.|
|created_by|string|Set on activity creation. As users cannot change username, simpler to store as a string.|
|date_added|string|Set on activity creation. Activities are sorted by _id therefore simplest to store as a string.|
|activity_equipment|string|Rather than storing as an array, it was simpler to request users enter each item on new line and manipulate in Python.|

#### Categories collection

|**Key**|**Type**|**Notes**|
|:-----|:-----|:-----|
|_id|ObjectId||
|category_name|string|The admin's chosen title of the category. Cannot be changed.|
|category_summary|string|Brief summary to add some meat to the Categories cards.|
|image_file|string|This is a link to an image uploaded to Amazon AWS by the admin.|
|activity_list|Array|Given the possibility of users changing the name of their activity, the decision was made to store activity ObjectIDs in array.|


#### Users collection

|**Key**|**Type**|**Notes**|
|:-----|:-----|:-----|
|_id|ObjectId||
|username|string|Chosen by user on account creation. Cannot be changed.|
|password|string|Chosen by user on account creation and hashed using Werkzeug Security.|

#### Ages collection

Initially it was anticipated that the admin might need the ability to change the target age ranges, but as the site progressed this no longer seemed necessary and this collection was abandoned and replaced by a hardcoded selection.

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="features"></span>

## Features

<span id="features-current"></span>

### Current

**1. Material design**

MaterializeCSS features:
- [Cards](https://materializecss.com/cards.html)
- [Forms](https://materializecss.com/text-inputs.html)
- [Menu dropdown](https://materializecss.com/dropdown.html)
- [Modals](https://materializecss.com/modals.html)
- [Sidenav](https://materializecss.com/sidenav.html)
- [Toasts](https://materializecss.com/toasts.html)

**2. Secure passwords**

When registering for the site, the user's password is hashed so that it is not revealed to the database owner.

**3. CRUD functionality**

Visitors can:
- View all activities
- View all categories.

Users can:
- Add their own activities
- Edit their own activities 
- Delete their own activities.

The admin can:
- Add their own activities
- Edit any users' activities
- Delete any users' activities
- Add a category
- Edit a category
- Delete a category.

**4. Image uploads**

Rather than having to find a URL for an image, users can upload their own files. This encourages them to provide their own content, but if they skip this step then a default image is displayed from the relevant category.

**5. Image resizing**

Prior to uploading an image, a user's file is resized so that it does not adversely affect site load times, and also gives some control over its dimensions.

**6. User profile**

Users can view all activities they have created in one place and easily edit or delete them.

**7. Admin rights**

The admin has the additional ability to:
- Edit or delete any activity on the site from its View Activity page
- Add categories
- Edit a category summary or image (but they cannot edit the name of a category to preserve relationship integrity)
- Delete categories from the Categories page, with measures for preserving relational integrity for activities no longer associated with a category.

**8. Confirm delete**

When the user or admin clicks to delete an activity or category, a modal pops up to confirm they wish to do so to prevent accidental deletion.

**9. Category reassignment on deletion**

When the admin chooses to delete a category which has associated activities, these activities are moved to the 'Unassigined' category and are still visible on the site. 

**10. Search**

All users can search for keywords appearing in:
- Activity title
- Activity summary
- Activity description
- Activity required equipment

Activities can be filtered by category from the Categories page and also by target age or activity author by clicking on the associated tag from the Activities, View Activity or Profile pages.

**11. Pagination**

The Activities page (and any search or filters applied) will limit the number of activities visible to 9 in order to reduce the number of images loaded and keep the focus on the content. As individual users are unlikely to be adding much more than 9 activities, it makes sense not to paginate the Profile page to avoid spilling onto a second page in this rare instance.

**12. Access protection**

Routes to restricted functions such as add, edit and delete (for both session user and admin) are protected so that they cannot be accessed by brute force via the URL.

**13. 404 and 500 error handling**

Pages for 404 and 500 errors keep the user on the site when something goes wrong, allowing them to return to the content with minimal disruption.


<span id="features-future"></span>

### Future

- Ability to favourite activities
- Ability to add comments to activities to encourage user interaction
- Contact the admin option
- A deeper profile (number of kids, interests etc.)
- Edit profile option
- Delete account option
- Ability to view other profiles
- Superuser implementation, rather than a single admin
- Admin area (page to view all site content in one place and edit as required including deleting users)
- Option to delete images from S3 Bucket through the site
- Speedier hosting of S3 Bucket images to improve performance

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="technologies"></span>

## Technologies Used

### Languages

- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python](https://www.python.org/)
  - [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)

### Frameworks

- [Flask](https://palletsprojects.com/p/flask/)
- [jQuery](https://jquery.com/)
- [Materialize](https://materializecss.com/)

### Extensions and kits

- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [Flask Paginate](https://pythonhosted.org/Flask-paginate/)
- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [Werkzeug](https://palletsprojects.com/p/werkzeug/)

### Project management

- [Amazon AWS](https://aws.amazon.com/) (S3)
- [Balsamiq](https://balsamiq.com/wireframes/)
- [GitHub](https://github.com/)
- [GitPod](https://gitpod.io/)
- [Heroku](https://www.heroku.com/about)
- [MongoDB](https://www.mongodb.com/)

### Tools

- [Am I Responsive?](http://ami.responsivedesign.is/)
- [Autoprefixer](https://autoprefixer.github.io/)
- [Coolers.co](https://coolors.co/1a237e-79b791-ee6055-214e34-f1edee)
- [Favicon.io](https://favicon.io//)
- [Font Awesome](https://fontawesome.com/)
- [Google Fonts](https://fonts.google.com/)


<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="deployment"></span>

## Deployment

The master branch of this repository is the most current version and has been used for the deployed version of the site.

### Prerequisites

[Python 3](https://www.python.org/downloads/) - core code

[PIP](https://pypi.org/project/pip/) - package installation

[Git](https://git-scm.com/) - version control

[MongoDB](https://www.mongodb.com/)

- MongoDB is the database used by the app to store content uploaded by its users.
- The following collections should be created:
  - activities
  - categories
  - users
- A document in categories should be created with the following fields:

|**Key**|**Value**|**Type**|
|:-----|:-----|:-----|
|category_name|Unassigned|String|
|category_summary||String|
|image_file||String|
|activity_list||Array|

[Amazon AWS S3 Bucket](https://aws.amazon.com/)

- An Amazon S3 Bucket is used to host the images uploaded to the app by its users.

***Values for the env.py environment variables and Heroku Cvars used in the sections below will be unique to each MongoDB and S3 Bucket created. Please refer to their respective documentation for further details.***


### How to clone Self Isolution

To clone this project from its [GitHub repository](https://github.com/Edb83/self-isolution):

1. From the repository, click **Code**
2. In the **Clone >> HTTPS** section, copy the clone URL for the repository
3. In your local IDE open Git Bash
4. Change the current working directory to the location where you want the cloned directory to be made
5. Type `git clone`, and then paste the URL you copied in Step 2

```console
git clone https://github.com/Edb83/self-isolution.git
```

6. Press Enter. Your local clone will be created
7. Create a file called env.py to hold your app's environment variables, which should contain the following:

```console
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "<app secret key>")
os.environ.setdefault("MONGO_URI", "mongodb+srv://<username>:<password>@<cluster_name>-ofgqg.mongodb.net/<database_name>?retryWrites=true&w=majority")
os.environ.setdefault("MONGO_DBNAME", "<database name>")

os.environ.setdefault("S3_BUCKET", "<S3 bucket name>")
os.environ.setdefault("S3_KEY", "<S3 key>")
os.environ.setdefault("S3_SECRET_ACCESS_KEY", "<S3 secret key>")
os.environ.setdefault("S3_LOCATION", "https://<S3 bucket name>.s3.<S3 bucket region>.amazonaws.com/")
```
8. **Make sure that env.py is listed in your .gitignore file to prevent your environment variables being pushed publicly**


### How to deploy to Heroku

To deploy the app to Heroku from its [GitHub repository](https://github.com/Edb83/self-isolution), the following steps were taken:

1. From the GitPod terminal, create **requirements.txt** and **Procfile** using these commands:

```console
pip3 freeze --local > requirements.txt
echo web: python app.py > Procfile
```

2. **Push** these files to GitHub
3. **Log In** to [Heroku](https://id.heroku.com/login)
4. Select **Create new app** from the dropdown in the Heroku dashboard
5. Choose a unique name ('self-isolution') for the app and the location nearest to you
6. Go to the **Deploy** tab and under **Deployment method** choose GitHub
7. In **Connect to GitHub** enter your GitHub repository details and once found, click **Connect**
8. Go to the **Settings** tab and under **Config Vars** choose **Reveal Config Vars**
9. Enter the following keys and values, which must match those in the env.py file created earlier:

|**Key**|**Value**|
|:-----|:-----|
|IP|`0.0.0.0`|
|PORT|`5000`|
|SECRET_KEY|`<app secret key>`|
|MONGO_URI|mongodb+srv://`<username>`:<password>@`<cluster_name>`-ofgqg.mongodb.net/`<database_name>`?retryWrites=true&w=majority|
|MONGO_DBNAME|`<database name>`|
|S3_BUCKET|`<S3 bucket name>`|
|S3_KEY|`<S3 key>`|
|S3_SECRET_ACCESS_KEY|`<S3 secret key>`|
|S3_LOCATION|https://`<S3 bucket name>`.s3.`<S3 bucket region>`.amazonaws.com/|

10. Go back to the **Deploy** tab and under **Automatic deploys** choose **Enable Automatic Deploys**
11. Under **Manual deploy**, select **master** and click **Deploy Branch**
12. Once the app has finished building, click **Open app** from the header row of the dashboard

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="testing"></span>

## Testing

Full details of testing can be found [here](TESTING.md).

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="credits"></span>

## Credits

### Tutorials

- Code Institute Task Manager Project ([Tim Nelson](https://github.com/TravelTimN))
- [Boto S3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#id224)
- [Handling file uploads with Flask](https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask)
- [Flask Paginate](https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9)
- [Pillow](https://pillow.readthedocs.io/en/stable/index.html)
- [Uploading to AWS S3 using boto](https://www.zabana.me/notes/flask-tutorial-upload-files-amazon-s3)

### Student projects

- [SWAP your clothes](https://github.com/LigaMoon/swap-clothes-app)
- [Wean Cuisine](https://github.com/Lucyjpjones/wean-cuisine)

### Code modified from other sources

- [Resizing images prior to S3 upload](https://stackoverflow.com/a/56241877)
- [Image processing with Pillow](https://dzone.com/articles/image-processing-in-python-with-pillow)
- [Checking duplicate key value pairs](https://stackoverflow.com/a/3897516)

### Content

- All text outside of user-generated content is original
- [Favicon](https://favicon.io/emoji-favicons/house)
- Images from [Pixabay](https://pixabay.com/)

### Acknowledgements

- Jonathan Munz (Code Institute Mentor) - for his reassurance, support and invaluable suggestions
- Tim Nelson (Code Institute Tutor) - for his patience in helping me to solve an issue with updating a MongoDB array
- All of the Code Institute tutors who helped me to solve some of the snagging issues towards the end of the project

### Disclaimer

This site was developed for educational purposes.

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>