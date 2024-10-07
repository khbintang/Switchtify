# Assignment 6: JavaScript and Asynchronous JavaScript

## Implementation Steps

- [x] Modify the previously created assignment 5 to use AJAX.

Step-by-step:
1. Reviewed the existing code from assignment 5.
2. Identified areas where synchronous operations could be replaced with asynchronous ones, particularly in product loading and creation.
3. Planned the necessary changes to implement AJAX for GET and POST requests for product management.

- [x] AJAX GET
   - [x] Modify the item data cards code to support AJAX GET.
   - [x] Implement task retrieval using AJAX GET.

Step-by-step:
1. Created a new JavaScript function `refreshProducts()` to fetch product data using AJAX GET.
2. Modified the `main.html` template to remove the server-side rendering of product cards.
3. Implemented a function to dynamically create and populate product cards with the data received from the AJAX GET request.
4. Called this function when the page loads and after any changes to the product list.
5. Updated the `get_product_json` view in `views.py` to return only the products belonging to the logged-in user.

- [x] AJAX POST
   - [x] Create a button that opens a modal with a form to add an item.
   - [x] Create a new view function to add a new item to the database.
   - [x] Create a `/create-ajax/` path that points to the new view function you created.
   - [x] Connect the form you created in the modal to the `/create-ajax/` path.
   - [x] Implement asynchronous refresh on the main page to display the latest item list without reloading the entire main page.

Step-by-step:
1. Added a "Add New Product" button to the `main.html` template.
2. Created a modal dialog with a form for adding new products using Tailwind CSS classes for styling.
3. Implemented a new view function `create_product_ajax` in `views.py` to handle the AJAX POST request.
4. Added a new URL pattern in `urls.py` for the `/create-product-ajax/` path.
5. Wrote JavaScript to handle form submission via AJAX POST using jQuery.
6. Updated the product list dynamically after successful form submission by calling `refreshProducts()`.

- [x] Execute the `collectstatic` command.

Step-by-step:
1. Opened a terminal.
2. Navigated to the Switchtify project directory.
3. Ran the command: `python manage.py collectstatic`
4. Confirmed that static files were collected successfully.

- [x] Answer the following questions in the README.md file in the root folder (please modify the README.md you have created; add subheadings for each assignment).
  Explain the benefits of using JavaScript in developing web applications!
  Explain why we need to use await when we call fetch()! What would happen if we don't use await?
  Why do we need to use the csrf_exempt decorator on the view used for AJAX POST?
  On this week's tutorial, the user input sanitization is done in the back-end as well. Why can't the sanitization be done just in the front-end?
  Explain how you implemented the checklist above step-by-step (not just following the tutorial)!

- [x] Perform add-commit-push to GitHub.


## Answers to Questions

1. Explain the benefits of using JavaScript in developing web applications!

JavaScript enhances web applications by enabling client-side interactivity, cross-platform compatibility, and access to a rich ecosystem of frameworks. It allows for full-stack development with Node.js, supports event-driven programming, and has wide browser support. JavaScript improves performance by offloading processing to the client-side, resulting in faster, more responsive, and scalable web applications.

2. Explain why we need to use await when we call fetch()! What would happen if we don't use await?

Using await with fetch() is crucial for handling asynchronous operations in JavaScript. It allows the code to pause execution until the Promise returned by fetch() is resolved, making the code more readable and easier to follow. Without await, fetch() immediately returns a Promise object instead of the actual data, potentially leading to errors if you try to use the result immediately. It also complicates error handling, as errors may go unnoticed if the code continues executing without waiting for the Promise to resolve.

3. Why do we need to use the csrf_exempt decorator on the view used for AJAX POST?

The csrf_exempt decorator is used on views for AJAX POST requests to bypass Django's built-in Cross-Site Request Forgery (CSRF) protection. AJAX requests often don't include the CSRF token by default, causing Django to reject them as unsafe. While csrf_exempt provides a quick solution, it should be used cautiously as it can introduce security vulnerabilities. A safer alternative is to manually include the CSRF token in the AJAX request header.

4. On this week's tutorial, the user input sanitization is done in the back-end as well. Why can't the sanitization be done just in the front-end?

Back-end sanitization is essential because front-end security can be easily bypassed by malicious users. The server is the last line of defense against attacks like SQL injection, XSS, and command injection. Back-end sanitization ensures data integrity and consistency across different clients, protects sensitive server resources, and handles untrusted external data sources. While front-end sanitization improves user experience, it cannot replace the crucial security role of back-end sanitization in safeguarding the entire system.

5. Explain how you implemented the checklist above step-by-step (not just following the tutorial)!

Step-by-step implementation details are already included in the "Implementation Steps" section above.]

