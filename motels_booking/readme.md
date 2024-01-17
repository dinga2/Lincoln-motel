1. Technical selection
Use Python+django+MySQL as the main development tool.
Python has concise syntax, high development efficiency, and rich open-source frameworks and libraries that can help us quickly build web applications.
Django is a free web application framework for Python, with rich features and easy scalability. The documents are complete and easy to understand.
The page uses Django template + bootstrap + jQuery.
The Django template is similar to the jinja2 template used by Flask before and is the default template system for Django, which can quickly and conveniently develop web pages.
Bootstrap+jquery is a common front-end library used to beautify pages and achieve dynamic effects
Architecture Overview
Using the Django standard MTV pattern, the application is divided into three layers of Model: responsible for the relationship mapping (ORM) between business objects and databases, which is equivalent to the Model in the MVC pattern. Template: Responsible for displaying pages to users (HTML), similar to views in MVC. View: Responsible for business logic and calling Model and Template when appropriate. Equivalent to Controller in MVC.
Database design
Function implementation
User: Hotel inquiry, view hotel details, inquire about quotes, book rooms, view reservations, cancel reservations, and pay for reservations.
Administrator: Add, delete, and modify hotels. Adding, deleting, and modifying room types. Pricing strategy adjustments include price increases in certain regions and weekend discounts.
Customer service: View user reservations and cancel them.
test
Black box testing
The black box observes data output through data input and checks whether the internal functions of the software are normal. When testing, input data into the software and wait for data output. If the data output is consistent with the expected data, it indicates that the software has passed the test. Suppose there is a discrepancy between the data and the expected data, even if the discrepancy is small. In that case, it indicates an internal problem in the software program that needs to be resolved as soon as possible.
You can add some unit testing to this, and you can also write some unit testing
