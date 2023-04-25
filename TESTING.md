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

### NAVIGATION
| Element     | Expectation        | Test Result  |
| ------------- | ------------- |---------------|
| Navbar links | Link to the correct pages | Pass | 
| Footer  | Social links open in a new tab | Pass |           

### HOMEPAGE 
| Element     | Expectation        | Test Result  |
| ------------- | ------------- |---------------|
| Page  | Not visible when user logs in/signs up  | Pass |
| 'Browse all" button | Links to the browse recipes page| Pass | 
| 'Sign up' button  | Links to the Sign Up page | Pass |
| Carousel for small screens  | Shows the latest 4 added recipes, slides automatically and controls work | Pass |

### BROWSE RECIPES
| Element     | Expectation        | Test Result  |
| ------------- | ------------- |---------------|
| Search bar  | Returns the recipes containing the inputted ingredient in the title or ingredients list. Empty result if there's no match.  | Pass |
| Category filter | Returns the recipes that belong in the selected category| Pass | 
| Recipe cards  | Shows average rating | Pass |
| Recipe cards  | On click, they link to the related recipe details page | Pass |

### LOGIN PAGE
| Element     | Expectation        | Test Result  |
| ------------- | ------------- |---------------|
| Form  | Invalid input data is handled  | Pass |
| Form | Valid input data logs the user in| Pass | 
| 'Remember me' checkbox  | When selected, the user is not logged out after inactivity | Pass |
| 'Log me in' button  | Based on valid or invalid form data, on click it either logs the user in or asks for valid data insertion | Pass |

### SIGNUP PAGE
| Element     | Expectation        | Test Result  |
| ------------- | ------------- |---------------|
| Form  | Invalid input data is handled  | Pass |
| Form | Valid input data logs the user in| Pass | 
| 'Remember me' checkbox  | When selected, the user is not logged out after inactivity | Pass |
| 'Sign up' button  | Based on valid or invalid form data, on click it either registers the user or asks for valid data insertion | Pass |

### LOGOUT PAGE
| Element     | Expectation        | Test Result  |
| ------------- | ------------- |---------------|
| Confirm logout button  | On click, the user is logged out and notifies user about it  | Pass |

### COOKBOOK
| Element     | Expectation        | Test Result  |
| ------------- | ------------- |---------------|
| Search bar  | Returns the recipes containing the inputted ingredient in the title or ingredients list. Empty result if there's no match.  | Pass |
| Category filter | Returns the recipes that belong in the selected category| Pass |
| Recipe cards  | On click, they link to the related recipe details page | Pass |


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

- - -
## 6) LIGHTHOUSE REPORTS

All of myKTCN app pages have been tested for Performance, Accessibility, Best Practices and SEO using [Lighthouse Chrome Developer Tool](https://developer.chrome.com/docs/lighthouse/overview/).

Results are reported in the table below and we can notice that the scores are not ideal, particularly regarding Performance.
I improved the scores by optimizing, resizing and converting the images uploaded to Cloudinary to the webp format, but I couldn't better them further: the main factor for them is load time, and since the site loads on Heroku, gets the images from Cloudinary (users also may upload images in formats that are not web friendly/sized properly) and gets the database information from ElephantSQL, there really isn't much that can be done to improve the scores further.

| Page     | Performance (D-M)  | Accessibility (D-M)   | Best Practices (D-M)  | SEO (D-M)  | Desktop results |Mobile results |
| ------------- | -------------|--------------|--------------|--------------|--------------|--------------|
| __homepage__ |  82-62  |   92-92  |  100-100   | 90-92   | <details><summary>click</summary> ![home-desktop](docs/TESTING-images/lighthouse-reports/lighthouse-homepage-loggedout-desktop.png) </details>|<details><summary>click</summary> ![home-mobile](docs/TESTING-images/lighthouse-reports/lighthouse-homepage-loggedout-mobile.png) </details> |
| __browse_recipes__ - logged out user |  53-49  |   89-88  |  100-100   | 90-89   | <details><summary>click</summary> ![browse-logout-desktop](docs/TESTING-images/lighthouse-reports/lighthouse-browserecipes-loggedout-desktop.png) </details>|<details><summary>click</summary> ![browse-logout-mobile](docs/TESTING-images/lighthouse-reports/lighthouse-browserecipes-loggedout-mobile.png) </details> |
| __browse_recipes__ - logged in user |  52-49  |   89-88  |  100-100   | 90-89   | <details><summary>click</summary> ![browse-login-desktop](docs/TESTING-images/lighthouse-reports/lighthouse-browserecipes-loggein-desktop.png) </details>|<details><summary>click</summary> ![browse-login-mobile](docs/TESTING-images/lighthouse-reports/lighthouse-browserecipes-loggein-mobile.png) </details> |
| __cookbook__ |  75-65  |   89-88  |  100-100   | 90-89   | <details><summary>click</summary> ![cookbook-desktop](docs/TESTING-images/lighthouse-reports/lighthouse-cookbook-desktop.png) </details>|<details><summary>click</summary> ![cookbook-mobile](docs/TESTING-images/lighthouse-reports/lighthouse-cookbook-mobile.png) </details> |
| __drafts__ |  71-64  |   95-94  |  92-92   | 90-92   | <details><summary>click</summary> ![drafts-desktop](docs/TESTING-images/lighthouse-reports/lighthouse-drafts-desktop.png) </details>|<details><summary>click</summary> ![drafts-mobile](docs/TESTING-images/lighthouse-reports/lighthouse-drafts-mobile.png) </details> |
| __recipe_create__ |  98-73  |   94-92  |  100-100   | 90-92   | <details><summary>click</summary> ![addrecipe-desktop](docs/TESTING-images/lighthouse-reports/lighthouse-addrecipe-desktop.png) </details>|<details><summary>click</summary> ![addrecipe-mobile](docs/TESTING-images/lighthouse-reports/lighthouse-addrecipe-mobile.png) </details> |
| __recipe_edit__ |  97-69  |   94-92  |  100-100   | 90-92   | <details><summary>click</summary> ![editrecipe-desktop](docs/TESTING-images/lighthouse-reports/lighthouse-editrecipe-desktop.png) </details>|<details><summary>click</summary> ![ editrecipe-mobile](docs/TESTING-images/lighthouse-reports/lighthouse-editrecipe-mobile.png) </details> |
| __recipe_delete__ |  85-75  |   95-94  |  100-100   | 90-92   | <details><summary>click</summary> ![deleterecipe-desktop](docs/TESTING-images/lighthouse-reports/lighthouse-deleterecipe-desktop.png) </details>|<details><summary>click</summary> ![deleterecipe-mobile](docs/TESTING-images/lighthouse-reports/lighthouse-deleterecipe-mobile.png) </details> |
| __login__ |  97-67  |   95-95  |  100-100   | 90-92   | <details><summary>click</summary> ![login-desktop](docs/TESTING-images/lighthouse-reports/lighthouse-login-desktop.png) </details>|<details><summary>click</summary> ![login-mobile](docs/TESTING-images/lighthouse-reports/lighthouse-login-mobile.png) </details> |
| __signup__ |  93-84  |   95-95  |  100-100   | 90-92   | <details><summary>click</summary> ![signup-desktop](docs/TESTING-images/lighthouse-reports/lighthouse-signup-desktop.png) </details>|<details><summary>click</summary> ![signup-mobile](docs/TESTING-images/lighthouse-reports/lighthouse-signup-mobile.png) </details> |







