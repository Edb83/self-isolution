# Bug: Materialize select dropdown does not function correctly on iOS. Either dropdown does not appear or selects the wrong item when clicked
Solution: Stopping propagation on touchend event (https://stackoverflow.com/a/52851046)

# Bug: iOS select caret visible when using the Materialize fix above
Solution: adding `-webkit-appeance: none` to select elements (https://stackoverflow.com/questions/7638677/how-can-i-remove-the-gloss-on-a-select-element-in-safari-on-mac)


## Bug: images uploaded to AWS not updating on edit
Solution: missing enctype="multipart/form-data"

# Bug: images not uploading on deployed site
Solution: add AWS secret keys to cvars on heroku

# Todo:

Features: 
## DONE Change Ages into hard-coded options rather than mongo collection
## DONE Add delete confirmation for activity and category
## DONE Add image upload
## Fix image upload edit
## DONE Fix activity_lists not updating correctly - names need to be unique or use ObjectID
## DONE Add file_update for categories
- Add handling of files > 1mb... see werzeug 413 error handler - only in production version?
## DONE Add search functionality
  - inc. category, age, equipment chips
- Fix views for admin and session user
- Add toasts
- Add delete user ??
- Add likes/favourites (as list in mongodb?) ??
- Add category stats ??
- Add 'unassigned category' for activities on deletion of category


Content: 
## DONE Flesh out view_activity
- Flesh out home
- Revise category card content
- Flesh out profile
- Flesh out footer

Structure:
- Merge add category and delete user into 'manage'/admin area

Styling:
## DONE Add password/field requirements
- Fix image handling within cards
- Check duplicate equipment chips

Project:
## DONE Update requirements.txt