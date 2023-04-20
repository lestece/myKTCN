# myKTCN app Testing

## TABLE OF CONTENTS

1) [Manual Testing](#1-manual-testing)
    - []()
    - []()
    - []()
    - []()
    - []()
    - []()
2) [Code Validation](#2-code-validation)
    - [W3C HTML Validation]()
    - [W3C (Jigsaw) CSS Validation]()
    - [JSHint JavaScript Validation]()
    - [CI Python Linter Python Validation]()
3) [Responsiveness testing](TESTING.md/#3-responsiveness-testing)
    - [Homepage responsiveness](TESTING.md/#homepage-responsiveness)
    - [Browse recipes responsiveness](TESTING.md/#homepage-modal-windows-responsiveness)
    - [Cookbook responsiveness](TESTING.md/#quiz-responsiveness)
    - [Recipe form responsiveness](TESTING.md/#signup-page-responsiveness)
    - [Drafts page responsiveness](TESTING.md/#quiz-result-responsiveness)
    - [User account responsiveness](TESTING.md/#dosha-modal-window-responsiveness)
4) [Browser compatibility](TESTING.md/#4-browser-compatibility)
5) [Bugs and fixes](TESTING.md/#5-bugs-and-fixes)
6) [Lighthouse reports](TESTING.md/#6-ligthouse-reports)
7) [User testing](TESTING.md/#7-user-testing)

[⬅ Back to the README.md file](README.md)

- - -
## 1) MANUAL TESTING

- - -

## 2) CODE VALIDATION
### W3C HTML VALIDATION

All html pages have been run through the [W3C HTML Validator](https://validator.w3.org/) and the below results were returned.

| HTML page     | Errors        | Warnings      | See results  |
| ------------- | ------------- |---------------|--------------|
| base.html     | None          | None          | <details><summary>base results</summary> ![base.html results](docs/TESTING-images/html-validation/base.html-validated.png) </details>|
| index.html    | None          | None          |<details><summary>index results</summary> ![index.html results](docs/TESTING-images/html-validation/index.html-validated.png) </details>|
| browse_recipes.html    | None          | None          |<details><summary>browse recipes results</summary> ![browse_recipes.html results](docs/TESTING-images/html-validation/browse-recipes.html-validated.png) </details>|
| cookbook.html    | None          | None          |<details><summary>cookbook results</summary> ![cookbook.html results](docs/TESTING-images/html-validation/cookbook.html-validated.png) </details>|
| recipe_create.html    | **Yes**         | None          |<details><summary>Add recipe results</summary> ![recipe_create.html results](docs/TESTING-images/html-validation/recipe_create.html-summernoteerrors.png) </details>|
| recipe_edit.html    | **Yes**         | None          |<details><summary>Edit recipe results</summary> ![recipe_edit.html results](docs/TESTING-images/html-validation/recipe-edit.html-summernoteerrors.png) </details>|
| recipe_confirm_delete.html    | None          | None          |<details><summary>Delete recipe results</summary> ![recipe_confirm_delete.html results](docs/TESTING-images/html-validation/recipe-confirm-delete.html-vaidated.png) </details>|
| recipe_details.html    | None          | None          |<details><summary>recipe details results</summary> ![recipe_details.html results](docs/TESTING-images/html-validation/recipe_details.html-validated.png) </details>|
| drafts.html    | None          | None          |<details><summary>drafts results</summary> ![drafts.html results](docs/TESTING-images/html-validation/drafts.html-validated.png) </details>|
| 404.html    | None          | None          |<details><summary>404 page results</summary> ![404.html results](docs/TESTING-images/html-validation/404.html-validated.png) </details>|
| login.html    | None          | None          |<details><summary>login results</summary> ![login.html results](docs/TESTING-images/html-validation/login.html-validated.png) </details>|
| logout.html    | None          | None          |<details><summary>logout results</summary> ![logout.html results](docs/TESTING-images/html-validation/logout.html-validated.png) </details>|
| signup.html    | None          | None          |<details><summary>signup results</summary> ![signup.html results](docs/TESTING-images/html-validation/signup.html-validated.png) </details>|

As indicated in the table, there are two pages that return validation errors: __recipe_create.html__ and __recipe_edit.html__. These errors come from the installed Summernote library, that runs on the ingredients and method input fields in the recipe form. These errors stay __unresolved/cannot be fixed__ since they come from an external source.
- - - 
### Jigsaw CSS VALIDATION

__No errors or warnings__ are returned when passing the styles.css through the [Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/).

![CSS Validation](docs/TESTING-images/css-validation/css-validated.png)

- - -
### JSHint JavaScript VALIDATION

All the sripts used in myKTCN have been run through the [JSHint Javascript Validator](https://jshint.com/) and they return __no errors__.

| Script     | Errors        | See results  |
| ------------- | -------------|--------------|
| carousel     | None          | <details><summary>carousel script results</summary> ![carousel script results](docs/TESTING-images/javascript-validation/jshint-carousel-validated.png) </details>|
| messages display     | None          | <details><summary>display messages script results</summary> ![display messages script results](docs/TESTING-images/javascript-validation/jshint-displaymessages-validated.png) </details>|
| rating system     | None          | <details><summary>rating system script results</summary> ![rating system script results](docs/TESTING-images/javascript-validation/jshint-ratingsystem-validated.png) </details>|
| select2     | None          | <details><summary>select2 script results</summary> ![select2 script results](docs/TESTING-images/javascript-validation/jshint-select2-validated.png) </details>|

- - -
### CI Python Linter Python VALIDATION

All the main Python files were run through the [CI Python Linter Validator](https://pep8ci.herokuapp.com/) with __no errors__ returned.

| Python file     | Errors        | See results  |
| ------------- | -------------|--------------|
| forms.py     | None          | <details><summary>forms.py results</summary> ![forms.py results](docs/TESTING-images/python-validation/forms.py-validated.png) </details>|
| models.py     | None          | <details><summary>models.py results</summary> ![models.py results](docs/TESTING-images/python-validation/models.py-validated.png) </details>|
| urls.py     | None          | <details><summary>urls.py results</summary> ![urls.py results](docs/TESTING-images/python-validation/urls.py-validated.png) </details>|
| views.py     | None          | <details><summary>views.py results</summary> ![views.py results](docs/TESTING-images/python-validation/views.py-validated.png) </details>|