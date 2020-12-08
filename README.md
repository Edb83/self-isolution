# Bug: Materialize select dropdown does not function correctly on iOS. Either dropdown does not appear or selects the wrong item when clicked
Solution: Stopping propagation on touchend event (https://stackoverflow.com/a/52851046)

# Bug: iOS select caret visible when using the Materialize fix above
Solution: adding `-webkit-appeance: none` to select elements (https://stackoverflow.com/questions/7638677/how-can-i-remove-the-gloss-on-a-select-element-in-safari-on-mac)


# Todo:

Add 'unassigned category' for activities on deletion of category
Change Ages into hard-coded options rather than mongo collection

Update requirements.txt