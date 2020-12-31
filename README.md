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




# RESOURCES:

- Handling file uploads with Flask: (https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask)
- Boto S3: (https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#id224)
- Uploading to AWS S3 using boto: (https://www.zabana.me/notes/flask-tutorial-upload-files-amazon-s3)
- Resizing images prior to S3 upload: (https://stackoverflow.com/a/56241877)
- Pillow: (https://pillow.readthedocs.io/en/stable/index.html)
- Image processing with Pillow: (https://dzone.com/articles/image-processing-in-python-with-pillow)