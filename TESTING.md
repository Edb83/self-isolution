<span id="top"></span>

Back to [README](README.md)

## Index

- <a href="#user-stories">User stories - how are they met?</a>
- <a href="#testing-manual">Manual</a>
- <a href="#testing-auto">Automated</a>
- <a href="#testing-responsive">Responsiveness</a>
- <a href="#testing-resolved">Resolved issues</a>
- <a href="#testing-unresolved">Unresolved issues</a>

---

<span id="user-stories"></span>

## User stories - how are they met?

### Overarching user expectations

**Consistency**

The site has been designed to be as consistent as possible, no matter the content:
- The Navbar and Footer remain the same across all pages, including Error pages.
- Headings and icons (form fields and add/edit/delete buttons) are standardised across all pages.
- Cards are a uniform shape and size per page and will never spill into a subsequent row.
- Cards represent a 'zoomed out' view of multiple selection items (Activities/Search Bar page and Categories pages), whereas views of single items (View Activity, input forms) are 'zoomed in' without a card to suggest a boundary.
- Where necessary, text is truncated to preserve the grid layout.

**Easy navigation**

The likely options a user might need at a given moment have been carefully considered to ensure a smooth browsing experience:
- The Navbar displays the active parent page the user is on, for example on desktop when on the Add Activity page, 'Profile' is the active navbar link. On mobile the actual page will be active. 
- Headings are descriptive of the content displayed even when a search or filter is applied.
- When a search finds no results, the user is encouraged to add their own content with a link to Add Activty.
- The title of each page updates in the browser window to indicate where the user is.
- Any view or action can be reached within four taps/clicks, e.g. from the Home page to confirming deletion of an activity: Profile > View > Delete > Confirm.
- The Footer contains top-level menu options, excluding Add Activity.

**Intuitive design**

- In the Navbar the Self Isolution logo takes users to the focal part of the site, the Activities page.
- Familiar icons have been used across the site for commonly expected actions e.g. add, edit, delete, search, back.
- Toasts pop-ups discretely alert the user when they perform meaningful actions i.e. logins and content changes.
- Activity and Category cards offer different functionality and are therefore styled and structured slightly differently to indicate this difference. Activity cards are blue with the image linking to the View Activity page whereas Category cards are green with the image expanding the card to reveal some more information about the category.
- As a user might expect, modals appear to confirm content deletion.

**Responsiveness**

- Pages adapt to a variety of screen sizes thanks to the Materialize grid template and extensive testing in Chrome Dev Tools.
- Where readability is compromised, page structure is modified to give more space to the elements (e.g. giving username its own row on the View Activity page).
- As large number of images are used, features such as image resizing, pagination and the `loading="lazy"` attribute keep the data footprint in check.

**Security**

- Passwords are hashed using Werkzeug Security.

**Appealing visuals**

- The card-based design allows for focus on the images uploaded by users.
- Simple, bold colours and use of consistent spacing bring clarity to the content.

### As a first-time visitor I want...

**To immediately understand what the purpose of the site is and what it can provide**

- The landing page has an image which is emotive of feeling unease at home, setting the theme suggested by the title of 'Self Isolution'.
- The heading beneath immediately indicates the purpose of the site: Are you trapped at home with your kids? If so then this site is for you.
- The blurb describes the COVID-19 situation, which should resonate with the site's intended audience of struggling parents.
- Below that are summaries of the two interactions you can have with the site: browsing activities and sharing your own, each with a link to exploring those interactions.
- Completing the 'tour' of the site are three examples of the most recently added content, as they appear on the Activities page, again with a link to follow.

**To see all content without having to register**

- There are no barriers to viewing any Activity or Category.
- Registering gives you the ability to add, edit and delete your content but nothing more.

**To be able to search for keywords**

- The Activities page has a clear Search area, which uses an index to check across activity name, summary, details and equipment required.

**To be able to filter activities by category**

- The Categories page has a prominant 'VIEW' button within each category's card, which when tapped/clicked will filter activities by that category.
- Activities can be filtered by target age or the activity author by tapping/clicking on the associated links either from the Activities page (except for author) or View Activity page.

**To be able to register easily without needing to input lots of information**

- The Register page asks only for username and password, nothing else.
- There is a visual indication that the username and password are of an acceptable length, along with clear requirements for the expected input.

### As a returning user I want...

**To log in and out easily**

- Links for logging in and out are clearly displayed in the Navbar and Footer, depending on whether the user is logged in or not.

**To be able to add new activities easily**

- A pulsing "+" button to add a new activity once logged in can be found on the Home, Activities and Profile pages.
- Text links inviting users to add an activity can be found on the Home and Profile pages.
- There are also links in the Navbar (under Profile) and Footer.
- The Add Activity page clearly shows what details can be provided and, in the case of activity equipment, the format which should be used. There are dropdowns for set options (category and target age) and a character counter to indicate the expected length of inputs.
- Adding an image URL or list of equipment is not required, which can sometimes be frustrating if just wanting to get content up.

**To be able to edit or delete activities I have added**

- Users can access the Edit Activity page for activites they have created by tapping/clicking on the floating action button within the activity's card on the Activities page, and also using the edit button in the View Activity or Profile pages.
- Users can delete their activites by tapping/clicking the delete button on the View Activity or Profile pages.
- As deleting an activity is a less common action (and to prevent accidental taps/clicks), this option is not present on the Activities page.
- On tapping/clicking to delete an activity, a modal pops up to confirm they wish to delete.

**To upload my own images rather than inputting a URL**

- When adding or editing an activity from the respective page, users can upload an image (max size 8mb) from their device or leave blank to use the associated category's image.

**To be able to see all the activities I have added in one place**

- The Profile page displays all activities added by a user, in a smaller card size for ease of viewing.
- Only the title, date added and buttons for editing or deleting are displayed.

**To be able to 'favourite' activities created by other users**

- Owing to time constraints this feature has not yet been implemented.

### As the site owner I want...

**To be able to edit or remove content created by users**

- The admin (user with username of "admin") has the same view of the site as other users so as to more easily determine which activities they have added personally. However, from the View Activity page they have the same options as the activity's owner to tap/click a button to edit or delete the activity.

**To be able to add, edit or remove categories**

- The admin has the ability to add a new category either by tapping/clicking the pulsing "+" button on the Categories page, or via the additional Navbar or Footer option.
- The admin can edit or delete a category in much the same was as a user would edit an activity, by tapping/clicking on the respective button within the category's card on the Categories page.
- The Add and Edit Category pages are consistent with the Add and Edit Activity pages.
- From the Edit Category page the admin can change the summary and image of the category, but not it's name so as to prevent awkward impacts on the associated activities.
- On choosing to delete a category, a modal pops up to confirm the action.
- If deleting a category, associated activities are moved to the "Unassigned" category rather than being deleted.

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="testing-manual"></span>

## Manual testing

The following tests have been carried out without issue:

**Navigation bar**

Mobile:
- Navbar is fixed to the top of the viewport when scrolling down.
- Tapping/clicking the Self Isolution logo takes users to the Activities page.
- All available menu options appear in the Sidenav when the hamburger icon is tapped/clicked.
- The correct menu options appear depending on the user's session status:
  - **Not logged in**: Home, Activities, Categories, Register, Log In
  - **Logged in**: Home, Activities, Categories, Profile, Add Activity, Log Out
  - **Logged in as "admin"**: as above plus Add Category
- The active page is indicated.
- Tapping/clicking each link takes the user to the relevant page, or logs the user out.

On screen widths greater than 991px:
- The hambuger icon is replaced by available menu options .
- Restricted user options (View, Add Activity, Add Category) are moved to a dropdown menu under Profile. The dropdown menu links all work as expected.
- Hover effects appear when moused-over.

**Footer**

- The footer appears at the bottom of the screen, even when all content is removed.
- The menu options all open the correct page, or log the user out.
- Each social media link opens the relevant external page in a new window.

**Home page**

- Links to Activities and Register direct to the correct pages.
- FAB for Add Activity only appears if user is logged in.
- Latest Activities shows the three most recently added activities.
- Cards function as expected (see Cards, above).

**Register page**

- The 'Log In' link takes the user to the Log In page.
- Entering a username or password not matching the form validation highlights the issue to the user, and indicates "Looks good!" if validated.
- Submitting a username (upper or lowercase) which has already been registered reloads the page and displays a Toast indicating username already taken.
- When the 'Register' button is tapped/clicked with valid details, the user is redirected to their Profile page and a Toast indicates they have successfully registered.
- On registering, the new user's username and password are added to the Users collection on the database.

**Log In page**

- The 'Register' link takes the user to the Register page.
- Entering a username or password not matching the form validation highlights the issue to the user.
- Entering either an incorrect username or password displays a Toast indicating "Incorrect Username and/or Password".
- When the 'Log In' button is tapped/clicked with valid details, the user is redirected to their Profile page and a Toast including their username indicates they have successfully logged in.


**Activities page**

Search functionality:

- After entering a term in the search field and either tapping/clicking the search icon or pressing Enter, the correct results are displayed from the indexed fields (activity_name, activity_summary, activity_details and activity_equipment).
- Tapping/clicking the cancel icon reloads the page with no query applied.
- The section heading updates to reflect the search term used.
- Pagination works when a search has been applied.
- If no results are found, a message to the effect appears. If logged in, a working link to Add Activity is displayed, otherwise working links to Register or Log In are displayed.

Cards:

- All activities in the collection are displayed, each with the correct title, image, summary, category and target age.
- Activities are displayed with the most recent at the top (by sorting the activity_id).
- If the user is logged in and the author of an activity, the Edit Activity FAB is displayed within the card, which takes the user to the correct Edit Activity page.
- For activities where the user has not uploaded an image, the correct image is displayed from the associated category.
- Tapping/clicking on an activity's image takes the user to the correct View Activity page.
- Tapping/clicking on an activity's category or target age correctly filters the activities displayed, updating the section heading to indicate the filter applied.
- Summaries which are longer than the card's width are truncated and do not cause the card to spill into the following row.
- The hover effect is applied when a card is moused over.

Pagination:

- The number of visible activities is limited to 9 per page.
- Only if pagination is necessary (over 9 activities), will links appear beneath the activities with corresponding page numbers.

**Add Activity page**

- If user has been logged out and tries to add an activity (or tries to open url with brute force using /add_activity) they are redirected to Log In page with Toast alert.
- The 'Choose category' and 'Choose age' input fields are populated with the documents from the Categories collection on MongoDB and the ages from the AGES list in app.py, respectively. Changes to these lists are reflected in the dropdowns.
- Input field validation and character counters function as expected, indicating issues with input and correctly displaying chars remaining.
- Image upload
  - On tapping/clicking the 'Upload Image' input field, the user is given the option to choose an image to upload.
  - On submitting the Add Activity form, the image is uploaded to the Amazon S3 Bucket and a unique URL is generated.
  - If the user choses not to upload an image, the image_file key has an empty string value (the relevant category image will be used instead).
- Image resizing
  - Before the image is upload to the S3 Bucket, it is resized so that its longest side is a maximum of 500px, as evident when viewing the image from other pages through Chrome Dev Tools.
  - The image is also orientated using its EXIF metadata so that it does not rotate when saved. When uploading portrait images without using the `resize_image` function, they will usually be flipped horizontally.
- The 'Cancel' button takes user back to the Activities page.
- The 'Submit' button:
  - Adds the activity to the Activities collection.
  - Adds the activity_id to the category's activity_list key.
  - Redirects to the user to the Activities page, showing the new activity at the top of the activities grid.
  - Displays a Toast confirming activity has been successfully added.
- If activity name chosen already exists in database (upper or lowercase):
  - Redirects to Add Activity page.
  - Displays a Toast alerting that name already exists.

**Edit Activity page**

The same tests as for Add Activity were carried out, with the following additional tests:
- If user has been logged out and tries to edit an activity (or tries to open url with brute force using /edit_activity/activity_id) they are redirected to Log In page with Toast alert.
- If user is logged in and tries to edit another user's activity by brute force, they are redirected to View Activity page with Toast message alerting "This Activity belongs to someone else!"
- The admin can edit any activity.
- The input fields are prepopulated with the activity's existing values where available.
- If an activity is in the "Unassigned" category (due to the category being deleted by the admin), this option is only available to the admin in the dropdown.
- If no new image is uploaded, the previously uploaded image URL is preserved.
- The 'Update' button:
  - Changes the activity's values in the Activities collection.
  - If a new category is chosen, adds the activity_id to the new category's activity_list key and removes it from the old one.
  - Redirects to the user to the View Activity page.
  - Displays a Toast confirming activity has been successfully added.
- If activity name chosen already exists in database (upper or lowercase):
  - Redirects to the relevant Edit Activity page.
  - Displays a Toast alerting that name already exists.

**View Activity page**

- The 'Back to Activities' button at the top of the page redirects to the Activities page.
- The correct full-size image is displayed above the activity title, the dimensions of which are revealed in Chrome Dev Tools (see Image Resizing under Add Activity page above).
- If the user is the creator of the activity or the admin, icons to delete or edit the activity are visible either side of the activity title, otherwise the row contains nothing but the title.
- The edit button takes the user to the relevant Edit Activity page.
- The delete button brings up a confirmation modal:
  - Tapping/clicking the modal's 'Cancel' button closes the modal.
  - Tapping/clicking the 'Delete' button removes the activity from the collection and redirects the user to their Profile page along with a Toast confirming deletion (including the activity name).
- The corrrect target age, category and activity author are displayed, and when tapped/clicked will filter activities as expected.
- The activity's equipment items are displayed in separate chips (providing they have been entered on separate lines).
- If no activity_equipment has been entered, a message is visible reporting "You won't need any specialized tools for this one!"

**Categories page**

- All categories from the categories collection are displayed in cards.
- Tapping/clicking a category image expands the card to reveal the category summary and a maximum list of three associated activities.
- If there are no associated activities, it displays the message "We are still waiting for this one to be filled up!"
- The 'View' button displays the number of associated activities for each category and if tapped/clicked takes user to a view of activities filtered by that category.
- If there are no associated activities, the 'View' button is greyed-out.
- The Add Category FAB and edit/delete icons display only if logged in as admin, but tapping/clicking them takes the admin to the correct page or brings up the confirm delete modal.
- The button for the admin to delete the "Unassigned" category is not available.

**Add/Edit Category page**

The same tests as for Add/Edit Activity were carried out, with the following additional tests:
- The page is only accessible if logged in as admin
- If the admin has been logged out and tries to add a category they are redirected to the Log In page with Toast alert.
- If a user is logged in and tries to add a category by brute force, they are redirected to the Categories page with Toast message alerting "That's an Admin's job!"
- The option to edit the category name is not available.
- Form validation requires the admin to upload a category image (as this is used for activities without an uploaded image).

**Profile page**

- Add Activity FAB links to the Add Activity page.
- All activities created by user display uniformly in cards.
- Activity name, image and creation date all display correctly.
- Tapping/clicking on card image takes user to correct View Activity page.
- The edit button links to Edit Activity page.
- The delete button brings up confirmation modal.
- If no activities have been added by the user, a message is displayed calling them to add some.

**Delete function / modal button**

Activities:
- If user has been logged out and tries to delete an activity (or tries to open url with brute force using /delete_activity/activity_id) they are redirected to Log In page with Toast alert.
- If user is logged in and tries to delete another user's activity by brute force, they are redirected to View Activity page with Toast message alerting "This Activity belongs to someone else!"
- The admin can delete any activity.
- The button targets the correct activity for deletion, and the activity name appears in the modal.
- Removes the activity from the activities collection.
- Removes the activity's ObjectId from the associated category's activity_list.

Categories:
- If admin is logged out and tries to delete a category (or tries to open url with brute force using /delete_category/category_id) they are redirected to Log In page with Toast alert.
- If user is logged in and tries to delete a category by brute force, they are redirected to the Categories page with Toast message alerting "That's an Admin's job!"
- The admin can delete any category.
- The button targets the correct category for deletion, and the category name appears in the modal along with the activities which will be left without an associated category.
- Changes the category_name value to "Unassigned" in any associated activities.
- Removes the category from the categories collection.

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="testing-auto"></span>

## Automated testing

[Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) - Lighthouse audit summary for both desktop and mobile:

**Home page**

- Performance: **88 - 95%**
- Accessibility: **97%**
- Best Practices: **100%**
- SEO: **100%**

**Register / Log In pages**

- Performance: **91 - 99%**
- Accessibility: **97%**
- Best Practices: **100%**
- SEO: **100%**

**Activities page**

- Performance: **79 - 97%**
- Accessibility: **100%**
- Best Practices: **100%**
- SEO: **90%**

**Categories page**

- Performance: **82 - 99%**
- Accessibility: **97%**
- Best Practices: **100%**
- SEO: **100%**

**Add / Edit pages**

- Performance: **90 - 99%**
- Accessibility: **88%**
- Best Practices: **100%**
- SEO: **98 - 100%**

**Profile page**

- Performance: **73 - 98%**
- Accessibility: **100%**
- Best Practices: **100%**
- SEO: **100%**

[W3C - HTML](https://validator.w3.org/) - 0 errors, 0 warnings - **PASS**

[W3C - CSS](https://jigsaw.w3.org/css-validator/) - 0 errors, 45 warnings - **PASS**

- Use of unknown vendor extensions

[CSS Lint](http://csslint.net/) - 0 errors, 51 warnings - **PASS**

- Disallow @import
- Requires compatible vendor prefixes
  - These were added by css auto-prefixer
- Unknown properties
  - Relating to styling added by css auto-prefixer
- Disallow !important
  - Used only where necessary to override Materialize styling
- Disallow IDs in selectors
  - Selecting via IDs has only been used for styles which will not be reused and the specificity was needed
- Disallow overqualified elements
  - In these instances the qualifications are necessary to both override Materialize and piggyback on the output of Flask Paginate

[Unicorn revealer - overflow](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln/related) - no evidence of overflow - **PASS**

[JS Hint](https://jshint.com/) - 0 errors, 0 warnings - **PASS**

- Adding 'function form' of `use strict` removed all warnings.

[PyCodeStyle](https://github.com/PyCQA/pycodestyle) - 0 warnings - **PASS**

- NB a simple tox.ini was created during the site's development to increase `max-line-length` to 120, but all code is now PEP8 compliant. 

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="testing-responsive"></span>

## Responsiveness

The site has been designed with a mobile-first philosophy and, supported by [Materialize](https://materializecss.com/), has been thoroughly tested at all stages of development using [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools).

In addition to Materialize's breakpoints, various media queries have been used to maximise the legibility of text and provide sufficient spacing for all content. These queries include optimised `margin`, `padding`, `text-align` and adjustments of `display` to accommodate changes in HTML structure. Particular attention has been paid to the appearance of cards and buttons on different devices.

Examples:

- on the View Activity page the 'Back' button has been aligned with the activity details below in keeping with Materialize's breakpoints.
- on the Categories page, the cards' appearance at the breakpoints from 2 to 3 columns was studied to make sure that even in a worst case scenario their content would not be put out of place. Revisions saw the card choice and position of each element tested, including when logged in as admin and the edit and delete buttons are visible.
- the Footer content was separated out on larger screen sizes to make better use of the space.
- the `flow-text` Materialize class has been used for any large text areas to ensure they are as legible as possible depending on device viewed with.


<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

### Browsers

Tested on:

- Chrome
- Edge
- Firefox
- Safari (iOS)

### Screen sizes

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


<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

## Issues and bugs

<span id="testing-resolved"></span>

### Resolved

**Materialize select dropdown does not function correctly on iOS**

A known bug with Materialize meaning either the dropdown does not appear or selects the wrong item when tapped/clicked.

- Solution: Stopping propagation on `touchend` event ([Source](https://stackoverflow.com/a/52851046))

**iOS select caret visible when using the Materialize fix above**

A subsequent issue resulting from the propogation fix above made for an untidy look.

- Solution: adding `-webkit-appeance: none` to select elements ([Source](https://stackoverflow.com/questions/7638677/how-can-i-remove-the-gloss-on-a-select-element-in-safari-on-mac))

**Portrait images rotating on resize**

This issue is caused by PIL not reading image EXIF metadata resulting in images being rotated when resized.

- Solution: importing ImageOps and using `ImageOps.exif_transpose(image)` ([Source](https://www.mmbyte.com/article/46440.html))

**Images uploaded to AWS not updating on edit**

After updating `add_activity` and form in add_activity.html, this change was missed in the edit_activity.html form.

- Solution: add missing `enctype="multipart/form-data"` attribute in form.

**Images not uploading on deployed site**

Images could be uploaded in the local app but not on the deployed site. 

- Solution: add AWS secret keys to cvars on Heroku, to match those in env.py.

**Unable to use PIL.ImageOps on image files once opened**

Pillow not able to process uploaded images due to a TypeError.

- Solution: save format of `raw_image` to pass into `new_image` so that it can be accessed by ImageOps. ([Source]((https://stackoverflow.com/questions/29374072/why-does-resizing-image-in-pillow-python-remove-image-format)))

**Values from collection fields not always appearing in templates**

Throughout development there were sudden instances where Jinja would only sometimes show data from the MongoDB collection. This happens due to the Cursor instance being expended so a copy is required to access more than once. 

- Solution: rather than using the Cursor object, convert to a list with `list(mongo.db.collection.find(...))`

**Users being able to brute-force access to restricted pages or functions via the URL**

Even if not logged in, anyone could go to "/add_activity" or "/add_category" and even edit or delete by using "/delete_category/category_id". Just because a link is not presented does not mean the routes cannot be accessed (especially risky when the code is available).

- Solution: add layered conditions to functions (`add_activity`, `edit_activity`, `delete_activity`, `add_category`, `edit_category`, `delete_category`) to get the correct path, e.g. `if "user" not in session` or `elif session["user"] != activity_owner and session["user"] != "admin"`. Then redirect to an appropriate page with flash/Toast message.
- This also presented a good opportunity to reduce the levels of nesting by using `if not` rather than `if` statements, to improve code readability.

**On category deletion and subsequent reallocation of child activities to "Unassigned" category, only first item reallocated in MongoDB**

Using `$push` inside a `for` loop only pushes the first instance of a list, which meant only one activity from a category which was deleted could be appended to the activity_list key in the "Unassigned" category.

- Solution: create a list of dependent activities and use `$addToSet` and `$each` options to add to `unassigned_category` rather than `$push` inside a `for` loop:
```
mongo.db.categories.find_one_and_update(unassigned_category, {"$addToSet": {"activity_list": {"$each": activities}}})
```

**Checking for existing activity or category names only applies to exact matches**

Unlike the check for `existing_user` which can apply `lower()` to the form request, it was not immediately obvious how to apply this to a Cursor object retreived from MongoDB and so `if any(d["activity_name"] == activity["activity_name"] for d in existing_activities)` was used to find any exact matches. As many many activities with the same name were added during testing, it was apparent that this would not find examples where the case alone was different.

- Solution: create a list of lowercase existing item names from the database and compare with the chosen activity/category name.

**When editing an activity without changing its name, alert that activity name already exists**

Following the fix above, this occured due to not completing the logical step of checking whether the activity name was being changed, always finding that the name already existed in the databse.

- Solution: add `if lowercase_name != activity["activity_name"].lower()` to the check.

**Pagination link not finding type of $search when search applied**

This error would occur when a search was applied showing a number of results in excess of the `PER_PAGE` pagination limit. The search form's "query" was not being passed through after the first page and had a type of `None`, which could be tested by forcing `query` to be a string and revealing empty subsequent pagination pages.

- Solution: removing `methods=["GET", "POST"]` from the search route, switching `query = request.form.get("query")` to `query = request.args.get("query")` in the search function, and changing `method="POST"` to `method="GET"` in the search form.

**Paginate linting error**

Raised by Gitpod:
```console
Possible unbalanced tuple unpacking with sequence defined at line 233 of flask_paginate: left side has 3 label(s), right side has 2 value(s)pylint(unbalanced-tuple-unpacking)
```

- Resolution: running `app.py` through Flake8 does not reveal this to be an error

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="testing-unresolved"></span>

**Lack of autocomplete attribute**

Warning reported by Chrome console:
```
[DOM] Input elements should have autocomplete attributes
```
- Resolution: added `autocomplete` to Register and Log In inputs.


### Unresolved

**Warnings reported by Chrome console**

```console
materialize.min.js:formatted:3756 [Violation] Added non-passive event listener to a scroll-blocking 'touchmove' event. Consider marking event handler as 'passive' to make the page more responsive. See https://www.chromestatus.com/feature/5745543795965952
```
- Despite efforts to mark the eventlisteners `{passive: true}`, this warning could not be resolved. 


```console
[Violation] Forced reflow while executing JavaScript took [x]ms
```
- Understanding how to resolve this issue was beyond the scope of this project.

**Problems reported by GitPod**

```console
Special characters must be escaped : [ > ].
```
- Despite attempts to escape the `>` character [as suggested by the Jinja documentation](https://jinja.palletsprojects.com/en/2.11.x/templates/#escaping), this warning persists in the console.

```console
Doctype must be declared first.
```
- This was understood to relate to GitPod failing to recognise the `!DOCTYPE html` in base.html being passed through to the other HTML templates.

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>