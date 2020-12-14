# Bug: Materialize select dropdown does not function correctly on iOS. Either dropdown does not appear or selects the wrong item when clicked
Solution: Stopping propagation on touchend event (https://stackoverflow.com/a/52851046)

# Bug: iOS select caret visible when using the Materialize fix above
Solution: adding `-webkit-appeance: none` to select elements (https://stackoverflow.com/questions/7638677/how-can-i-remove-the-gloss-on-a-select-element-in-safari-on-mac)


# Todo:

Features: 
## DONE Change Ages into hard-coded options rather than mongo collection
## DONE Add delete confirmation for activity and category
- Add search functionality
  - inc. category, age, equipment chips
## DONE Add image upload
- Fix image upload edit
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
- Fix image handling within cards
- Add password/field requirements
- Check duplicate equipment chips

Project:
- Update requirements.txt