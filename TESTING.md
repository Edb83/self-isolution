<span id="top"></span>

[README](README.md)

## TESTING Index

- <a href="#user-stories">User stories</a>
- <a href="#testing-auto">Automated</a>
- <a href="#testing-manual">Manual</a>
- <a href="#testing-responsive">Responsiveness</a>
- <a href="#testing-resolved">Resolved issues</a>
- <a href="#testing-unresolved">Unresolved issues</a>

---

<span id="user-stories"></span>

### User stories

TBC

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
