# Todo:

# Features:

## DONE Change Ages into hard-coded options rather than mongo collection
## DONE Add delete confirmation for activity and category
## DONE Add image upload
## DONE Fix image upload edit
 - Add image delete from S3 Bucket ??
## DONE Fix activity_lists not updating correctly - names need to be unique or use ObjectID
## DONE Add file_update for categories
## DONE Add handling of files > 1mb... see werkzeug 413 error handler - only in production version?
## DONE Add resizing of user image uploads and handling of portrait images rotating on resize
## DONE Add search functionality for categories.html
## DONE Add filter by user
## DONE Add category stats (number of and list of 3)
- Add search functionality for age and category show as chips
## DONE Combine user/admin options under Profile
## DONE Add toasts
- Add edit user ??
- Add delete user ??
- Add likes/favourites (as list in mongodb?) ??
- Add 'unassigned category' for activities on deletion of category

# Content:

## DONE Flesh out view_activity
- Flesh out home
## DONE Revise category card content
## DONE Flesh out profile
- Flesh out footer

# Structure:

- Merge add category and delete user into 'manage'/admin area
- Fix routing/error handling - permissions for page access?

# Styling:

## DONE Add password/field requirements
## DONE Fix image handling within cards
## DONE Check duplicate equipment chips

# Project:

## DONE Update requirements.txt




# Bugs:

## Bug: Materialize select dropdown does not function correctly on iOS. Either dropdown does not appear or selects the wrong item when clicked
- Solution: Stopping propagation on touchend event (https://stackoverflow.com/a/52851046)

## Bug: iOS select caret visible when using the Materialize fix above
- Solution: adding `-webkit-appeance: none` to select elements (https://stackoverflow.com/questions/7638677/how-can-i-remove-the-gloss-on-a-select-element-in-safari-on-mac)

## Bug: portrait images rotating on resize
- Solution: caused by PIL not reading image EXIF metadata. Fixed by importing ImageOps and using ImageOps.exif_transpose(image) (https://www.mmbyte.com/article/46440.html)

# Issues:

## Issue: images uploaded to AWS not updating on edit
- Solution: missing enctype="multipart/form-data"

## Issue: images not uploading on deployed site
- Solution: add AWS secret keys to cvars on heroku

## Issue: unable to use PIL.ImageOps on image files once opened
- Solution: save format of raw_image to pass into new_image so that it can be accessed by ImageOps (https://stackoverflow.com/questions/29374072/why-does-resizing-image-in-pillow-python-remove-image-format)

## Issue: pymongo.errors.InvalidOperation: cannot set options after executing query
- Solution: to various issues(!) - using list()

## Issue: session-only pages e.g. add activity are accessible even if not logged in by entering url
- Solution: 


# RESOURCES:

- Handling file uploads with Flask: (https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask)
- Boto S3: (https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#id224)
- Uploading to AWS S3 using boto: (https://www.zabana.me/notes/flask-tutorial-upload-files-amazon-s3)
- Resizing images prior to S3 upload: (https://stackoverflow.com/a/56241877)
- Pillow: (https://pillow.readthedocs.io/en/stable/index.html)
- Image processing with Pillow: (https://dzone.com/articles/image-processing-in-python-with-pillow)

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

TBC

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>
<span id="ux"></span>

## UX

<span id="ux-overview"></span>

### Overview

TBC

<span id="ux-stories"></span>

### User stories

#### As a first-time user I want:

- To...

#### As a returning user I want:

- To...

<span id="ux-wireframes"></span>

### Wireframes

Wireframes for **mobile** and **desktop** can be accessed [here](wireframes/).

There were some noteworthy deviations from the plan. These were:

1. TBC

<span id="ux-design"></span>

### Design choices

#### Colours

TBC

##### Core

TBC

- ![#ffffff](https://via.placeholder.com/15/ffffff/000000?text=+) #ffffff (White)


#### Fonts

[Orbitron](https://fonts.google.com/specimen/Orbitron#about)

TBC

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="features"></span>

## Features

<span id="features-current"></span>

### Current

**1. TBC**

- TBC


<span id="features-future"></span>

### Future

**TBC**

- TBC



<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="technologies"></span>

## Technologies Used

### Languages

- HTML
- CSS
- Javascript
  - [jQuery](https://jquery.com/) - 

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

<span id="testing-unresolved"></span>

#### Unresolved

- **TBC**

TBC


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

- [Title](#)


#### Code used/modified from other sources

- [Title](#)


### Content

- All text outssde of user-generated content is original

### Acknowledgements

- Jonathan Munz (Code Institute Mentor) - for his reassurance, support and invaluable suggestions

### Disclaimer

This site was developed for educational purposes.

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>