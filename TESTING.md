<span id="top"></span>

[README](README.md)

## Index

- <a href="#user-stories">User stories</a>
- <a href="#testing-manual">Manual</a>
- <a href="#testing-auto">Automated</a>
- <a href="#testing-responsive">Responsiveness</a>
- <a href="#testing-resolved">Resolved issues</a>
- <a href="#testing-unresolved">Unresolved issues</a>

---

<span id="user-stories"></span>

## User stories

### Overarching user expectations

**Consistent**
The site has been designed to be as consistent as possible, no matter the content:
- The Navbar and Footer remain the same across all pages, including Error pages.
- Headings and icons (form fields; add, edit, delete buttons) are standardised across all pages.
- Cards are a uniform shape and size per page and will never spill into a subsequent row.
- Cards represent a 'zoomed out' view of multiple selection items (Activities/Search Bar page and Categories pages), whereas views of single items (View Activity, input forms) are 'zoomed in' without a card to suggest a boundary.
- Where necessary, text is truncated to preserve the grid layout.

**Easy to navigate**
The likely options a user might need at a given moment have been carefully considered to ensure a smooth browsing experience:
- The Navbar displays the active parent page the user is on, for example on desktop when on the Add Activity page, 'Profile' is the active navbar link. On mobile the actual page will be active. 
- Headings are descriptive of the content displayed even when a search or filter is applied.
- When a search finds no results, the user is encouraged to add their own content with a link to Add Activty.
- The title of each page updates in the browser window to indicate where the user is.
- Any view or action can be reached within four clicks, e.g. from the Home page to confirming deletion of an activity: Profile > View > Delete > Confirm.
- The Footer contains top-level menu options, excluding Add Activity


**Intuitive**
- Activity and Category cards offer different functionality and are therefore styled and structured slightly differently to indicate this difference. Activity cards are blue with the image linking to the View Activity page whereas Category cards are green with the image expanding the card to reveal some more information about the category.

**Responsive**
- 

**Secure**
- 

**Visually appealing**
- The card-based design allows for focus on the images uploaded by users


### As a first-time visitor I want

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
- The Activities page has a large Search area.
**To be able to filter activities by category**
- The Categories page has a prominant 'VIEW' button within each category's card, which when clicked will filter activities by that category.
- Activities can be filtered by target age or the activity author by clicking on the associated links either from the Activities page (except for author) or View Activity page.
**To be able to register easily without needing to input lots of information**
- The registration form asks only for username and password, nothing else.
- There is a visual indication that the username and password are of an acceptible length, along with clear requirements for the expected input.

### As a returning user I want

**To log in and out easily**
- Links for logging in and out are clearly displayed in the Navbar and Footer, depending on whether the user is logged in or not.
**To be able to add new activities easily**
- A pulsing "+" button to add a new activity once logged in can be found on the Home, Activities and Profile pages.
- Text links inviting users to add an activity can be found on the Home and Profile pages.
- There are also links in the Navbar (under Profile) and Footer.
- The Add Activity page clearly shows what details can be provided and, in the case of activity equipment, the format which should be used. There are dropdowns for set options (category and target age) and a character counter to indicate the expected length of inputs.
- Adding an image URL or list of equipment is not required, which can sometimes be frustrating if just wanting to get content up.
**To be able to edit or delete activities I have added**
- Users can access the Edit Activity page for activites they have created by clicking on the floating action button within the activity's card on the Activities page, and also using the edit button in the View Activity or Profile pages.
- Users can delete their activites by clicking the delete button on the View Activity or Profile pages.
- As deleting an activity is a less common action (and to prevent accidental clicks), this option is not present on the Activities page.
- On clicking to delete an activity, a modal pops up to confirm they wish to delete.
**To upload my own images rather than inputting a URL**
- When adding or editing an activity from the respective page, users can upload an image (max size 8mb) from their device or leave blank to use the associated category's image
**To be able to see all the activities I have added in one place**
- The Profile page displays all activities added by a user, in a smaller card size for ease of viewing.
- Only the title, date added and buttons for editing or deleting are displayed.
**To be able to 'favourite' activities created by other users**
- Owing to time constraints this feature has not yet been implemented.

### As the site owner I want:

**To be able to edit or remove content created by users**
- The admin (user with username of "admin") has the same view of the site as other users so as to more easily determine which activities they have added personally. However, from the View Activity page they have the same options as the activity's owner to click a button to edit or delete the activity. 
**To be able to add, edit or remove categories**
- The admin has the ability to add a new category either by clicking the pulsing "+" button on the Categories page, or via the additional Navbar or Footer option.
- The admin can edit or delete a category in much the same was as a user would edit an activity, by clicking on the respective button within the category's card on the Categories page.
- The Add and Edit Category pages are consistent with the Add and Edit Activity pages.
- From the Edit Category page the admin can change the summary and image of the category, but not it's name so as to prevent awkward impacts on the associated activities.
- On choosing to delete a category, a modal pops up to confirm the action.
- If deleting a category, associated activities are moved to the "Unassigned" category rather than being deleted.

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>


<span id="testing-manual"></span>

## Manual testing

**Summary**:

TBC... :

**1. TBC**

- TBC

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="testing-auto"></span>

## Automated testing

[Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) - audit summary for both desktop and mobile:

- Performance: **X - X%**
- Accessibility: **X - X%**
- Best Practices: **X - X%**
- SEO: **X - X%**

[W3C - HTML](https://validator.w3.org/) - ? errors, ? warnings - **PASS**

[W3C - CSS](https://jigsaw.w3.org/css-validator/) - ? errors, ? warnings - **PASS**

Details TBC

- Use of...

[CSS Lint](http://csslint.net/) - 0 errors, 46 warnings - **PASS**

- Disallow @import
- Requires compatible vendor prefixes (these were added by css auto-prefixer)
- Unknown properties (again relating to styling added by css auto-prefixer)
- Disallow !important (which is necessary to override Materialize styling)
- Disallow IDs in selectors (these relate to elements and styles which are not going to be reused)
- Disallow overqualified elements (in these instances the qualifications are necessary to override both Materialize and piggyback on the output of Flask Paginate)


[Unicorn revealer - overflow](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln/related) - no evidence of overflow - **PASS**

[JS Hint](https://jshint.com/) - 0 errors, 0 warnings - **PASS**

- Adding 'function form' of `use strict` removed all warnings.

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>


## Responsiveness

TBC

<span id="testing-responsive"></span>

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

## Issues and resolutions

<span id="testing-resolved"></span>

### Resolved

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
- Solution: save format of `raw_image` to pass into `new_image` so that it can be accessed by ImageOps. [Source]((https://stackoverflow.com/questions/29374072/why-does-resizing-image-in-pillow-python-remove-image-format))

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

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="testing-unresolved"></span>

### Unresolved

?

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>