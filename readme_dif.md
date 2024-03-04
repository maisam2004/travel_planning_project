
# Travel App

![YourTravelApp Logo](travel_planning/static/images/background/travel_app7u.jpg)

<img src="./travel_planning/static/images/wireframes/tree_screen_image.jpg" style="width: 100%; height: 70%;">

Explore the holiday deals through TravelApp, your ultimate travel companion.

Visit the live site: [TravelApp.com](https://travelapp.com/)

Embark on a virtual journey, discover new destinations, and plan your next adventure!

## Contents

- [Frontend](#frontend)
- [User Experience](#user-experience-ux)

  - [User Stories](#user-stories)
- [Design](#design)

  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Imagery](#imagery)
  - [Wireframes](#wireframes)
  - [Features](#features)
    - [Destination Discovery](#destination-discovery)
    - [Future Enhancements](#future-enhancements)
  - [Accessibility](#accessibility)
  - [homepage](#homepage)#homepage
  - [explore page](#explore-page-crud-explore)
  - [about page](#about)
  - [User account](#account)
  - [contact](#contact)
  - [signup / login](#login)
- [Technologies Used](#technologies-used)

  - [Languages Used](#languages-used)
  - [Frameworks, Libraries &amp; Programs Used](#frameworks-libraries--programs-used)
- [Deployment &amp; Local Development](#deployment--local-development)

  - [Deployment](#deployment)
  - [Local Development](#local-development)
    - [How to Fork](#how-to-fork)
    - [How to Clone](#how-to-clone)
- [Testing](#testing)

  - [Automated Testing](#automated-testing)
    - [W3C Validator](#w3c-validator)
    - [JavaScript Validator](#javascript-validator)
    - [Lighthouse](#lighthouse)
  - [Manual Testing](#manual-testing)
    - [Testing User Stories](#testing-user-stories)
    - [Full Testing](#full-testing)
- [Credits](#credits)

  - [Code Used](#code-used)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgments](#acknowledgments)

## Frontend


![YourTravelApp Banner](travel_planning/static/images/background/travel_app7u.jpg)

## User Experience (UX)

### User Stories

#### First Time Visitor Goals

- I want to explore new travel destinations and get inspired for my next trip.
- I want a user-friendly interface that allows me to navigate through the site effortlessly.
- I want to find comprehensive travel guides and information about different holiday packages.

#### Returning Visitor Goals

- I want to interact with an interactive map to plan my itinerary effectively.

#### Frequent Visitor Goals

- I want to contribute by sharing my travel experience and tips.
- I want to connect with other travel enthusiasts .

---

## Design

### Colour Scheme

"The color scheme is thoughtfully curated to capture the essence of adventure and wanderlust. While predominantly earthy tones are employed to evoke a sense of groundedness and connection to nature, the design also incorporates elements of glassmorphism. Background images are strategically utilized to infuse depth and dimension, creating a visually immersive experience that echoes the beauty of the natural world."

- Primary Color: `#643279` (Purple)
- Secondary Colour: `#ffffff` (Shiny White)
- Accent Colour: `#c06c84` (Dusty Rose)
- Background: `#f8b400` (Bright Yellow)

![YourTravelApp Color Scheme](travel_planning/static/images/background/different_color.png)

### Typography

The chosen fonts are both modern and easy to read, enhancing the overall user experience.by help from this [Fontpair](https://www.fontpair.co/) website guide.

- Page Title: [Roboto Slab ](https://fonts.google.com/specimen/Roboto?query=roboto)
- Body Text title: [amulya](https://www.fontshare.com/fonts/amulya)
- Body text : [Roboto](https://fonts.google.com/specimen/Roboto?query=roboto)
- Body text : [amulya](https://www.fontshare.com/fonts/amulya)
  ![Amulya exapmple Font Example](travel_planning/static/images/background/amulya.jpg)

### Imagery

Stunning images of landscapes and iconic landmarks are incorporated to transport users to different corners of the world. Each page features visually appealing photos to enhance the travel experience.

### Wireframes

Wireframes for mobile, desktop were created using microsoft paint.

--Hompage -- hompage desktop and mobile

- <img src="./travel_planning/static/images/wireframes/homepage1.jpg" style="width: 60%; height: 60%;">- <img src="./travel_planning/static/images/wireframes/homepage2.jpg" style="width: 60%; height: 60%;">-<img src="./travel_planning/static/images/wireframes/home_mobileview1.jpg" style="width: 30%; height: 50%;">-<img src="./travel_planning/static/images/wireframes/home_mobileview2.jpg" style="width: 30%; height: 50%;">

--Explored page  -- about share info of their holiday

- <img src="./travel_planning/static/images/wireframes/explored.jpg" style="width: 60%; height: 60%;">
- <img src="./travel_planning/static/images/wireframes/explored_mobileview.jpg" style="width: 30%; height: 50%;">

--About page  -- about compony view

<img src="./travel_planning/static/images/wireframes/about.jpg" style="width: 60%; height: 60%;">
<img src="./travel_planning/static/images/wireframes/about_mibleview.jpg" style="width: 30%; height: 50%;">

-- Account page -- user own info page

- <img src="./travel_planning/static/images/wireframes/account.jpg" style="width: 50%; height: 50%;"> - <img src="./travel_planning/static/images/wireframes/account_mobleview.jpg" style="width: 30%; height: 45%;">

-- contact  page -- company contact information

- <img src="./travel_planning/static/images/wireframes/account.jpg" style="width: 50%; height: 50%;"> - <img src="./travel_planning/static/images/wireframes/account_mobleview.jpg" style="width: 30%; height: 45%;">

--Login page  -- user login page

- <img src="./travel_planning/static/images/wireframes/login.jpg" style="width: 50%; height: 50%;"> <img src="./travel_planning/static/images/wireframes/login_mobleview.jpg" style="width: 30%; height: 50%;">

--Signup page  -- user sign up page

- <img src="./travel_planning/static/images/wireframes/signup.jpg" style="width: 60%; height: 50%;"> <img src="./travel_planning/static/images/wireframes/signup_mobileview.jpg" style="width: 30%; height: 60%;">

### Features

Explore the rich features of TravelApp, meticulously crafted to offer users an immersive and dynamic journey. Leveraging the power of Flask and a robust database system, every corner of the application pulsates with interactivity, ensuring seamless navigation and personalized experiences tailored to each user's preferences.

1. **Responsive Design:**

   - All pages are seamlessly responsive, ensuring a consistent and

 optimal viewing experience across all devices.

2. **Destination Discovery:**

   - Discover new travel destinations through curated cads and showing data in modal with interactive map .
3. **Travel Guides:**

   - Access comprehensive travel guides with useful tips, recommendations, and insights for various populare cities.
4. **User Profiles:**

   - Create a personalized user profile to share travel experiences, connect with other users, in explored page
5. **Interactive Maps:**

   - Plan your itinerary effectively with interactive maps showcasing points of interest, hotels, and attractions.

#### Future Enhancements

- Integration with booking platforms to facilitate hotel and tour reservations.
- User-generated content, including reviews, photos, and travel stories.
- Advanced search filters for tailored destination recommendations.
- Social media integration for seamless sharing and community engagement.

### Accessibility

TravelApp is committed to accessibility and strives to provide an inclusive experience for all users. The site is designed with accessibility features such as:

- Semantic HTML for screen readers and assistive technologies.
- High contrast color schemes for improved readability.
- Keyboard navigation support for users with mobility impairments.
- Alt text for images to ensure content comprehension for visually impaired users.

## Page Structure and Navigation

Each page in the application follows a consistent layout with a header and footer included in the base HTML file. Specific routes are responsible for generating the content for each page, ensuring a cohesive user experience throughout the application.

### Header and Footer Inclusion

The header and footer elements, containing navigation links and other essential components, are defined in the base HTML file. This ensures uniformity across all pages and simplifies navigation for users.

### Page-Specific Routing

Page-specific routes are configured to generate content for individual pages. These routes determine the data and layout to be displayed based on the requested page, ensuring that users are directed to the appropriate content.

By maintaining a standard structure and employing specific routing mechanisms, the application offers seamless navigation and consistent presentation across all pages.

### main pages

- <img src="./travel_planning/static/images/wireframes/full_homepage.jpeg" style="width: 65%; height: 20%;">- <img src="./travel_planning/static/images/wireframes/full_mobile_homepage.jpeg" style="width: 30%; height: 50%;">

### [Homepage ](#homepage)

The homepage of Travelapp offers a captivating introduction to the travel experience, blending aesthetics and functionality seamlessly.

- **Site Name and Logo:**

  - The site name and logo take center stage, creating a distinctive visual identity for TravelWander.com.
- **Navbar:**

  - An intuitive navigation bar ensures easy exploration, allowing users to effortlessly access different sections of the website.
- **Social Icons:**

  - Social icons are strategically placed, providing quick links to connect with TravelWander.com on various social media platforms.
- **Welcome Text:**

  - A warm welcome text invites users to embark on a virtual journey, setting the tone for an immersive travel experience.
- **Continents Slides:**

  - Three slides showcasing breathtaking images of different continents create a visually stunning backdrop, offering a glimpse into the diverse destinations awaiting exploration.
- **Company Information:**

  - Information about the company is elegantly presented, providing insights into TravelWander's mission and offerings.
- **Customer Reviews:**

  - Customer reviews add a personal touch, offering authentic perspectives and enhancing the credibility of the travel services.
- **Background :**

  - A dynamic background  runs throughout the homepage, adding a touch of dynamism and reinforcing the travel theme.
- **Modal for Deals:**

### Homepage Travel Deals Modal

The homepage of travelapp introduces users to enticing travel deals displayed as interactive cards. Upon clicking on a travel deal card, users can access a detailed modal window that provides comprehensive information about the selected deal. This modal enhances the user experience by offering a convenient way to explore key details and make informed decisions regarding their travel plans.

- <img src="./travel_planning/static/images/wireframes/modal_deals.jpeg" style="width: 30%; height: 50%;">
- **Modal Content:**

  - The modal window presents essential details such as the price of the travel package, destination, duration of the holiday, and any special offers or discounts available. By displaying this information prominently, users can quickly assess the value and suitability of the travel deal, facilitating efficient decision-making.
- **Interactive Map:**

  - In addition to textual information, the modal incorporates an interactive map feature that visualizes the destination of the travel package. By leveraging mapping technologies, users can gain insights into the geographical location, nearby attractions, and points of interest associated with the holiday destination, enhancing their understanding and appreciation of the travel offer.
- **Contact Information:**

  - To further assist users and address any inquiries or concerns, the modal includes contact details such as telephone numbers or email addresses for reaching out to travelapp's customer support team. This direct communication channel enables users to seek personalized assistance, receive expert guidance, and make informed decisions regarding their travel arrangements.

By integrating a feature-rich modal window into the homepage's travel deal cards, travelapp enhances user engagement and satisfaction, providing a seamless browsing experience that empowers users to explore, evaluate, and book their dream holidays with confidence and ease.

##### home Route Explanation

-**Page**: Home Page

-**Method**: POST, GET

-**Purpose**: Renders the home page and handles the submission of wished holidays.

-**Tech Used**: Flask, Flask SQLAlchemy, Flask-WTF, Bootstrap (for flash messages)

-**Functionality**:

- Queries all travel packages from the database.
- Initializes a form for submitting wished holidays (`WishedHolidayForm`).
- If the form is submitted (`POST` request) and passes validation:

  - Creates a new `WishedHoliday` object with the submitted data.
  - Adds the new `WishedHoliday` object to the database session.
  - Commits the changes to the database.
  - Flashes a success message to the user.
  - Redirects the user to the wished holiday page (`wished_holiday` route).
- If an exception occurs during database operations:

  - Logs the error message.
  - Flashes an error message to the user.
  - Renders the home page again with the form to handle the exception.

-**Template**: Renders the `home.html` template, passing the following data:

  -`travel_packages`: List of all travel packages queried from the database.

  -`form`: Instance of the `WishedHolidayForm` for submitting wished holidays.

---

<img src="./travel_planning/static/images/wireframes/full_explored.jpeg" style="width: 65%; height: 20%;">- <img src="./travel_planning/static/images/wireframes/full_mobile_explored.jpeg" style="width: 30%; height: 50%;">

## Explore Page (crud) {#explore}

- [explore page](#explore)

The "Explore" page of travelapp serves as a dynamic platform for users to share their latest holiday experiences, complete with captivating images and personal anecdotes. Utilizing Bootstrap's card feature, each submission is elegantly presented in a visually appealing format, enhancing readability and engagement.

- **User Submissions:**

  - Users can effortlessly post their recent holiday details, including destination highlights, activities, and memorable moments. Accompanied by stunning images, each submission offers a unique glimpse into diverse travel experiences, inspiring others to embark on their adventures.
- **Interactive Cards:**

  - Bootstrap cards facilitate seamless navigation and interaction, allowing users to explore submissions with ease. The inclusion of edit and delete buttons empowers users to modify their content, ensuring flexibility and control over their posted experiences.
- **Database Interaction:**

  - Behind the scenes, travelapp seamlessly interacts with the database to retrieve, display, and manage user submissions. Leveraging the power of Flask and SQLAlchemy, the platform delivers a seamless user experience, enabling smooth data handling and efficient content management.

Through a combination of intuitive design, interactive features, and robust database functionality, the "Explore" page invites users to share their travel tales, connect with fellow adventurers, and discover new destinations in an immersive and engaging manner.

##### Explore Route Explanation

* **Page** : Explore Page
* **Method** : POST, GET
* **Purpose** : Renders the explore page and handles the addition of new destinations.
* **Tech Used** : Flask, Flask SQLAlchemy, Flask-WTF, Bootstrap (for flash messages)
* **Functionality** :
* Initializes a form for adding destinations (`AddDestinationForm`).
* Checks if the user is authenticated:
  * If authenticated:
    * Handles form submission:
      * Saves the uploaded image and retrieves the file path.
      * Creates a new `Destination` object with the submitted data.
      * Adds the new `Destination` object to the database session.
      * Commits the changes to the database.
      * Flashes a success message to the user.
      * Redirects the user back to the explore page.
    * Retrieves all destinations ordered by name from the database.
  * If not authenticated:
    * Retrieves all destinations from the database.
* Renders the `explore.html` template, passing the following data:
  * `form`: Instance of the `AddDestinationForm` for adding destinations.
  * `all_destinations`: List of all destinations queried from the database.

This route handles the rendering of the explore page and allows authenticated users to add new destinations. It utilizes forms for data submission and interacts with the database to store and retrieve destination information.

---

<img src="./travel_planning/static/images/wireframes/full_about.jpeg" style="width: 65%; height: 20%;">- <img src="./travel_planning/static/images/wireframes/full_about_mobile.jpeg" style="width: 30%; height: 50%;">

#### About Page

- [about page](#about)

---

The "About" page of travelapp offers a glimpse into our vision, approach, and the process behind our platform's creation. Designed to be both informative and engaging, this page provides insights into what drives us and how we strive to deliver exceptional travel experiences.

- **Our Vision:**

A compelling image accompanies our vision statement, symbolizing our commitment to revolutionizing the way people explore the world. Through innovative technology and unparalleled service, we aspire to inspire wanderlust and facilitate memorable journeys for every traveler.

- **Our Approach:**

An illustrative image complements our approach, highlighting our dedication to personalization, convenience, and sustainability. We believe in tailoring travel experiences to individual preferences, simplifying the booking process, and promoting eco-conscious practices to protect our planet for future generations.

- **Our Process:**

Step-by-step visuals outline our process, from conceptualization to implementation, showcasing our meticulous attention to detail and user-centric design philosophy. By prioritizing user feedback, continuous improvement, and seamless integration of cutting-edge technologies, we ensure that every aspect of travelapp reflects our commitment to excellence.

#### about Route Explanation

- **Page**: About Us Page
- **Method**: POST, GET
- **Purpose**: Renders the about us page.
- **Tech Used**: Flask, Flask SQLAlchemy, Jinja (for templating)
- **Functionality**:
  - Renders the `about_us.html` template, which displays information about the website or organization.
- **Template**: Renders the `about_us.html` template, which typically includes information such as the purpose of the website, team members, mission statement, and contact information.

This route simply renders the about us page without any additional functionality. It serves as a static page to provide information about the website or organization to the users.

---

<img src="./travel_planning/static/images/wireframes/full_account.jpeg" style="width: 65%; height: 20%;">- <img src="./travel_planning/static/images/wireframes/full_mobile_account.jpeg" style="width: 30%; height: 50%;">

## Account Page

The "Account" page of travelapp offers users a personalized space to view and manage their profile information, including uploaded images and details of their last wished holiday. With a focus on user-centric design and functionality, this page provides a seamless experience for users to interact with their account settings and preferences.

- **Profile Information:**

  - Users can access and update their profile information, including username, email, and any additional details provided during registration. The user-friendly interface ensures easy navigation and efficient management of account details.
- **Upload Personal Image:**

  - A dedicated feature enables users to upload a personalized profile image, enhancing their presence and adding a touch of personalization to their account. Utilizing Flask's file upload functionality, users can effortlessly select and upload images directly from their device.
- **Last Wished Holiday:**

  - As part of the user experience enhancement, travelapp displays details of the user's last wished holiday on the "Account" page. Leveraging data stored in the WishedHoliday table, users can conveniently reference their desired holiday preferences, facilitating future travel planning and exploration.
- **Database Integration:**

  - Behind the scenes, travelapp seamlessly integrates with a database system to retrieve and display user information, uploaded images, and wished holiday details. Leveraging Flask-SQLAlchemy, the platform ensures secure data storage and efficient data retrieval, enhancing the overall user experience.

###### Through a combination of intuitive design, personalized features, and robust database functionality, the "Account" page empowers users to manage their profile, upload personalized content, and access essential information, fostering a seamless and engaging user experience.

##### Account Route Explanation

- **Page**: Account Page
- **Method**: GET, POST
- **Purpose**: Renders the user account page and allows users to manage their profile information and view wished holidays.
- **Tech Used**: Flask, Flask-Login, Flask SQLAlchemy, Flask-WTF, Bootstrap (for flash messages)
- **Functionality**:

  - Retrieves wished holidays associated with the current user from the database.
  - Retrieves the user's profile image if it exists.
  - Initializes a form (`UserImageForm`) for uploading or updating the user's profile image.
  - If the form is submitted (`POST` request) and passes validation:

    - Saves the uploaded image to the server.
    - Updates the user's profile image record in the database.
    - Flashes a success message to the user.
    - Redirects the user back to the account page to view the updated profile image.
  - Renders the account page with the user's profile information, profile image, and wished holidays.
- **Template**: Renders the `account.html` template, passing the following data:

  - `user`: Current user object.
  - `current_user_image1`: Path to the current user's profile image.
  - `user_image_form`: Instance of the `UserImageForm` for uploading or updating profile image.
  - `wishes`: List of wished holidays associated with the current user.

---

<img src="./travel_planning/static/images/wireframes/full_contact.jpeg" style="width: 65%; height: 20%;">- <img src="./travel_planning/static/images/wireframes/full_mobile_contact.jpeg" style="width: 30%; height: 50%;">

## Contact Page

- [User account](#account)
  - [contact](#contact)
  - [signup / login](#login)

The "Contact" page of travelapp serves as a centralized hub for users to access essential contact information and connect with the platform's administrators. With a focus on accessibility and user engagement, this page provides convenient access to support channels and location details.

- **Contact Information:**

  - Users can easily locate contact details, including email addresses and phone numbers, enabling seamless communication with travelapp's support team. The intuitive layout ensures quick access to essential information, facilitating efficient resolution of inquiries and support requests.
- **Interactive Map:**

  - An interactive map feature enhances the user experience by visually representing the geographical location of travelapp's headquarters or primary operating regions. Leveraging mapping APIs, users can explore the platform's physical presence and gain insights into its global reach and coverage.
- **Email Integration:**

  - To streamline communication and facilitate direct inquiries, travelapp offers users the option to send emails directly from the "Contact" page. By integrating email functionality, users can compose messages within the platform, minimizing friction and enhancing convenience.
- **User-friendly Interface:**

  - The "Contact" page features a user-friendly interface designed to promote ease of use and accessibility. Clear navigation elements and prominently displayed contact information ensure that users can quickly locate and utilize the available communication channels without any hassle.

Through its comprehensive approach to user support and engagement, the "Contact" page reinforces travelapp's commitment to customer satisfaction and service excellence. By providing users with accessible contact information, interactive map functionality, and seamless email integration, the platform empowers users to connect with ease and confidence, fostering a positive and enriching user experience.

##### Contact Us Route Explanation

- **Page**: Contact Us Page
- **Method**: GET
- **Purpose**: Renders the contact us page, allowing users to access the contact information and form.
- **Tech Used**: Flask, Jinja2, HTML, CSS
- **Functionality**:

  - Renders the `contact_us.html` template, providing users with the contact information and form.
- **Template**: Renders the `contact_us.html` template, which may include:

  - Contact details such as email addresses, phone numbers, or physical addresses.
  - A form for users to submit inquiries, feedback, or messages.
  - Any additional information or instructions related to contacting the website or business.

---

<img src="./travel_planning/static/images/wireframes/full_signup.jpeg" style="width: 65%; height: 20%;">- <img src="./travel_planning/static/images/wireframes/full_mobile_signup.jpeg" style="width: 30%; height: 50%;">

<img src="./travel_planning/static/images/wireframes/full_login.jpeg" style="width: 65%; height: 20%;">- <img src="./travel_planning/static/images/wireframes/full_mobile_login.jpeg" style="width: 30%; height: 50%;">

## Signup and Login Pages

The "Signup" and "Login" pages of travelapp serve as key entry points for users to access and interact with the platform's features securely. Designed with a focus on user authentication and account management, these pages provide a seamless and intuitive experience for new users registering for membership and existing members logging into their accounts.

- **Signup Page:**

  - The "Signup" page enables new users to create an account and become members of the travelapp community. With a user-friendly registration form, users can provide essential information, such as username, email address, and password, to establish their accounts securely. Stringent validation checks ensure data accuracy and integrity, enhancing the overall signup process and mitigating potential errors or discrepancies.
- **Login Page:**

  - The "Login" page offers registered users convenient access to their accounts, facilitating secure authentication and personalized interactions with travelapp's features. Utilizing industry-standard encryption protocols, such as HTTPS and secure password hashing, the login process ensures robust protection of user credentials and sensitive information. Through a streamlined login interface, users can enter their credentials confidently, knowing that their privacy and security are prioritized.
- **Database Integration:**

  - Both the "Signup" and "Login" pages seamlessly interact with travelapp's secure database infrastructure, storing and retrieving user account data in a protected environment. By leveraging database technologies and secure authentication mechanisms, the platform maintains data integrity and confidentiality, safeguarding user information against unauthorized access or manipulation.
- **Responsive Design:**

  - The "Signup" and "Login" pages feature responsive design elements, ensuring optimal display and functionality across various devices and screen sizes. Whether accessing the platform from a desktop computer, tablet, or smartphone, users can enjoy a consistent and accessible signup and login experience, enhancing usability and convenience.

Through its commitment to user privacy, security, and usability, travelapp's "Signup" and "Login" pages establish a strong foundation for user engagement and satisfaction. By prioritizing data protection, seamless integration, and responsive design, the platform empowers users to register, login, and access its features with confidence and ease.

##### Signup Route Explanation

- **Page**: Signup Page
- **Method**: GET, POST
- **Purpose**: Handles user signup form submission and creates a new user account.
- **Tech Used**: Flask, Flask-WTF, Flask SQLAlchemy, Flask-Login, Bootstrap (for flash messages)
- **Functionality**:

  - Initializes a form instance (`SignupForm`) for user signup.
  - If the form is submitted (`POST` request) and passes validation:

    - Retrieves username, email, and password from the form data.
    - Checks if the username or email is already taken in the database.
    - If not taken, creates a new user object and adds it to the database.
    - Flashes a success message to the user upon successful account creation.
    - Logs in the new user automatically.
    - Redirects the user to the home page.
  - Renders the signup page with the signup form.

##### Login Route Explanation

- **Page**: Login Page
- **Method**: GET, POST
- **Purpose**: Handles user login form submission and authenticates user credentials.
- **Tech Used**: Flask, Flask-WTF, Flask SQLAlchemy, Flask-Login, Bootstrap (for flash messages)
- **Functionality**:

  - If the request method is `POST`:

    - Retrieves username and password from the login form data.
    - Queries the database for a user with the provided username.
    - If a user is found and the password is correct:

      - Logs in the user.
      - Redirects the user to the home page.
    - If the username or password is invalid:

      - Flashes an error message to the user.
  - Renders the login page with the login form.

## Backend of application ( CRUD )

#### Introduction

Welcome to the backend of our Flask TravelApp project! In this section, we'll delve into the inner workings of our backend architecture, exploring its crucial role in managing server-side operations, processing data, and interacting with the database.

The backend serves as the backbone of our application, handling various tasks such as user authentication, data retrieval and manipulation, and business logic implementation. It plays a pivotal role in ensuring the smooth functioning of the application, providing the necessary infrastructure for delivering content to users and facilitating seamless interactions between the frontend and the database.

A well-designed backend is essential for maintaining the integrity and reliability of our application. It enables us to efficiently process user requests, handle complex business logic, and manage data persistence, ultimately contributing to a positive user experience.

In the following sections, we'll explore the technologies, database structure, and route explanations that comprise our backend architecture, offering insights into the underlying mechanisms that power our Flask TravelApp.but first lests see  file structure

<img src="./travel_planning/static/images/wireframes/file_structure.jpg" style="width: 40%; height: 20%;">

##### **File Structure**

**-Core application structure:**

* **run.py:** The main Flask application file that launches the server and routes requests to appropriate handlers.
* **routes.py:** Defines URL routing logic and logic for handling incoming requests. It renders templates, interacts with data models, and serves as the central entry point for application functionality.
* **models.py:** Defines data models that represent entities in your application. These models typically interact with a database using an ORM like SQLAlchemy.
* **forms.py:** Defines forms for user input validation. Forms help ensure data integrity and provide a structured way to collect user input. WTForms is a common library used for form creation.
* **templates/**: Contains HTML templates that define the application's user interface. Flask renders these templates with dynamic content populated from data models and forms.

**-Application configuration:**

* **__init__.py:** An empty file or file containing initialization code for the package. In some cases, it might import core modules to establish the package structure.
* **env.py:** Defines sensitive configuration settings like security keys, database URLs, and mail service details. This file should **never** be committed to version control (e.g., GitHub) due to the sensitive nature of its contents.
* **.gitignore:** A file that specifies files and directories to be excluded from version control. This helps prevent sensitive information (like `env.py`) and unnecessary files (like `venv`) from being committed to repository.

**-Deployment:**

* **Procfile:** (Optional) A file used by deployment platforms like Heroku to specify the commands to run your application in a production environment.
* **Requirements.txt:** A file that lists the Python packages required by your application. This file ensures that the same dependencies are installed on different environments, promoting consistency and reproducibility.

**Additional :**

* **static/**: This directory is included in your response, but it's a common location to store static assets like CSS, JavaScript, and image files that are directly accessible to the web browser.
* **dump.sql**: This SQL dump file is used to replicate your database on Heroku Postgres.
* **Maintain consistent formatting:** Use consistent indentation and spacing to improve readability.

### backend Technologies and Frameworks:

"**To ensure the proper functioning of this application, the following technologies must be imported within the routes.py file.**"

Here's an updated list of technologies and frameworks used in your Flask TravelApp project :

* Flask: A lightweight and flexible web framework for Python.
* Flask SQLAlchemy: A Flask extension that adds ORM support for SQLAlchemy, facilitating database interactions.
* Flask Login: A Flask extension for managing user authentication and session management.
* Flask Mail: A Flask extension for sending email messages.
* PostgreSQL: A powerful open-source relational database management system used for data storage in the application.
* Werkzeug: A utility library for WSGI (Web Server Gateway Interface) applications, used in Flask for file handling and other tasks.
* Jinja2: A templating engine for Python, used in Flask for generating dynamic HTML content.
* Psycopg2: A PostgreSQL adapter for Python, used for interacting with the PostgreSQL database.
* SQLAlchemy: A SQL toolkit and Object-Relational Mapping (ORM) library for Python, used in conjunction with Flask SQLAlchemy for database operations.
* SMTPlib: A Python library for sending email messages via the Simple Mail Transfer Protocol (SMTP).
* Heroku: A cloud platform that hosts your Flask application and provides tools for deployment, scaling, and monitoring.

### Database Structure:

This application utilizes a PostgreSQL database for storing data. The database schema was designed to efficiently manage application data such as users, destinations, and travel plans.

To define the database structure, models were created using a Python framework (e.g., SQLAlchemy). These models represent the data entities captured by the application forms, ensuring consistent data storage and retrieval.

***Travel_planning DB***

The provided images (db_pic1.jpg and db_pic2.jpg) illustrate the relationships between the database tables.

<img src="./travel_planning/static/images/wireframes/db_pic1.jpg" style="width: 80%; height: 20%;">

<img src="./travel_planning/static/images/wireframes/db_pic2.jpg" style="width: 80%; height: 20%;">

To ensure the proper creation of database tables, I meticulously examined the forms utilized on each page of the application. Understanding the data input requirements of these forms was crucial for designing the database schema effectively.

To translate these form structures into database tables, I created two essential files: models.py and forms.py. The models.py file defined the database models corresponding to each form, specifying the fields and their data types. On the other hand, the forms.py file encapsulated the form structures themselves, facilitating data validation and user input handling.

This systematic approach ensured that the database tables accurately represented the data captured by the application forms, establishing a robust foundation for seamless data management and retrieval.

##### | homepage - backend |

    -route (/)

```
@app.route('/', methods=['GET', 'POST'])
def home():
    # Your code for rendering the home page
```

Here's the table specifically for the home route,

| Route (URL Pattern) | HTTP Method | Description                              | Page Interaction                                      | Database Table(s) | Related models.py Classes | Related forms.py Classes |
| ------------------- | ----------- | ---------------------------------------- | ----------------------------------------------------- | ----------------- | ------------------------- | ------------------------ |
| `/` (Home)        | GET         | Displays the homepage                    | - Show "Travel Packages" section                      | `TravelPackage` | `TravelPackage`         | -                        |
| `/` (Home)        | POST        | Handles "Wished Holiday" form submission | - Process and store user's wished holiday preferences | `WishedHoliday` | `WishedHoliday`         | `WishedHolidayForm`    |

I've implemented a feature to display enticing deals to users. These deals are sourced from a dedicated table in the database called TravelPackage.

```
def home():
  
    travel_packages 			=    TravelPackage.query.all()
```

To achieve this, I created a database model named TravelPackage to represent each deal. This model is closely integrated with a form specifically designed for adding new deals, which is accessible through an admin-only page called ***add_travel_package.***

The add_travel_package page, although not visible to regular users, serves as a management interface for administrators to insert new deals into the TravelPackage table.

* modal part deals use these data as well

-route('/add_travel_package', methods=['GET', 'POST'])

| Route (URL Pattern)     | HTTP Method | Description                                  | Page Interaction                               | Database Table(s)                         | Related models.py Classes                 | Related forms.py Classes |
| ----------------------- | ----------- | -------------------------------------------- | ---------------------------------------------- | ----------------------------------------- | ----------------------------------------- | ------------------------ |
| `/add_travel_package` | GET         | Displays the "Add Travel Package" form       | - Renders the form to add a new travel package | None                                      | None                                      | `AddTravelPackageForm` |
| `/add_travel_package` | POST        | Handles "Add Travel Package" form submission | - Processes and stores new travel package data | `TravelPackage`, `TravelPackageImage` | `TravelPackage`, `TravelPackageImage` | `AddTravelPackageForm` |

**Explanation:**

* The table shows both GET and POST methods for the home route (`/`).
* The GET request:
  * Retrieves all `TravelPackage` objects from the database using `TravelPackage.query.all()`.
  * Renders the "home.html" template, passing the retrieved travel packages and an empty `WishedHolidayForm` to the template context.
* The POST request:
  * Validates the submitted `WishedHolidayForm` data.
  * Creates a new `WishedHoliday` object with data from the form, including user ID retrieved from `current_user` (ensure it's correct).
  * Adds the `WishedHoliday` object to the database session using `db.session.add(wished_holiday)`.
  * Commits the changes to the database using `db.session.commit()`.
  * Handles potential exceptions (e.g., database errors) using a `try-except` block:
    * On success, flashes a success message and redirects to the `wished_holiday` route (assuming it exists).
    * On error, logs the error, flashes an error message, and re-renders the `home.html` template with the form.

| Explore  - backend |
| ------------------ |

users be able to see where other user went for holiday and see a picture of and while any use who post this data could edit or delete this info ,and these two buttons was disable for other user . and routes used for this page , was

```
# Route for exploring destinations
@app.route('/explore', methods=['GET', 'POST'])
def explore():
    # Your code for exploring destinations


# Route for editing a destination
@app.route('/explore/edit/<int:destination_id>', methods=['GET', 'POST'])
def edit_destination(destination_id):
    # Your code for editing a destination

# Route for deleting a destination
@app.route('/explore/delete/<int:destination_id>', methods=['POST'])
def delete_destination(destination_id):
    # Your code for deleting a destination

```

| Route (URL Pattern)                      | HTTP Method           | Description                                         | Page Interaction                                                          | Database Table(s) | Related models.py Classes | Related forms.py Classes                               |
| ---------------------------------------- | --------------------- | --------------------------------------------------- | ------------------------------------------------------------------------- | ----------------- | ------------------------- | ------------------------------------------------------ |
| `/explore` (GET)                       | GET                   | Displays the "Explore" page                         | - Shows all destinations                                                  | `Destination`   | `Destination`           | `AddDestinationForm` (optional, for logged-in users) |
| `/explore` (GET)                       | GET (logged-in user)  | Displays the "Explore" page with additional actions | - Shows all destinations                                                  | `Destination`   | `Destination`           | `AddDestinationForm`                                 |
| `/explore` (POST)                      | POST (logged-in user) | Handles "Add Destination" form submission           | - Adds a new destination for the logged-in user, including image upload   | `Destination`   | `Destination`           | `AddDestinationForm`                                 |
|                                          |                       |                                                     | - Saves the uploaded image and associates it with the new destination     |                   |                           |                                                        |
| `/explore/delete/<int:destination_id>` | POST                  | Handles "Delete Destination" action                 | - Deletes a specific destination (if user is authorized)                  | `Destination`   | `Destination`           | None                                                   |
| `/explore/edit/<int:destination_id>`   | GET                   | Displays the "Edit Destination" form                | - Renders the form to edit a specific destination (if user is authorized) | `Destination`   | `Destination`           | `EditDestinationForm`                                |
| `/explore/edit/<int:destination_id>`   | POST                  | Handles "Edit Destination" form submission          | - Updates the edited destination (if user is authorized)                  | `Destination`   | `Destination`           | `EditDestinationForm`                                |

**Explanation:**

* The table shows the different scenarios based on user authentication and HTTP methods.
* Logged-in users have additional functionalities like adding destinations.
* The GET request for non-logged-in users:
  * Displays the "Explore" page with all destinations (`all_destinations = Destination.query.all()`).
  * Optionally includes the `AddDestinationForm` (depending on your implementation).
* The GET request for logged-in users:
  * Displays the "Explore" page with all destinations (`all_destinations = Destination.query.order_by(Destination.name).all()`).
  * Includes the `AddDestinationForm` for adding new destinations.
* The POST request for logged-in users:
  * Validates the submitted `AddDestinationForm` data.
  * Saves the uploaded image using `save_destination_image(form.image.data)` and stores the path in `image_path`.
  * Creates a new `Destination` object with form data and the saved image path.
  * Adds the new destination to the database and commits the changes.
  * Flashes a success message, redirects to the `explore` page.

---

##### | Signup - backend |

| ---------------- |

user by entering required data in form  would be able join this web and route related to deal with entered data was :

```
@app.route('/signup', methods=['GET', 'POST'])
def signup():
```

    Table for`/signup` Route

| Route (URL Pattern) | HTTP Method | Description                    | Page Interaction                                                                          | Database Table(s) | Related models.py Classes | Related forms.py Classes |
| ------------------- | ----------- | ------------------------------ | ----------------------------------------------------------------------------------------- | ----------------- | ------------------------- | ------------------------ |
| `/signup`(GET)    | GET         | Displays the signup form       | - Renders the form for user registration                                                  | `User`          | `User`                  | `SignupForm`           |
| `/signup`(POST)   | POST        | Handles signup form submission | - Processes and stores user registration data                                             | `User`          | `User`                  | `SignupForm`           |
|                     |             |                                | -**Stores passwords securely using hashing (implemented in `User.set_password`)** |                   |                           |                          |

**Explanation:**

* The table shows both GET and POST methods for the signup route.
* The GET request:
  * Renders the `signup.html` template with an empty `SignupForm` for users to enter their information.
* The POST request:
  * Validates the submitted form data using `form.validate_on_submit()`.
  * Extracts username, email, and password from the form.
  * Checks for existing usernames or emails in the `User` table using a query:
    * `existing_user = User.query.filter((User.username == username) | (User.email == email)).first()`.
  * If an existing user is found, flashes an error message.
  * If no existing user is found:
    * Creates a new `User` object with the provided information.
    * Sets the user's password securely using `new_user.set_password(password)`.
    * Adds the new user to the database session using `db.session.add(new_user)`.
    * Commits the changes to the database using `db.session.commit()`.
    * Flashes a success message and logs in the new user using `login_user(new_user)`.
    * Redirects the user to the home page (`url_for('home')`).

---

##### | Login -backend |

| -------------- |

user by entering required data in form  would be able to enter to his accoutn and routes related to deal with entered data was :

```
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
  
```

Table for Routes:

| Route (URL Pattern)                      | HTTP Method     | Description                   | Page Interaction                                           | Database Table(s)   | Related models.py Classes | Related forms.py Classes        |
| ---------------------------------------- | --------------- | ----------------------------- | ---------------------------------------------------------- | ------------------- | ------------------------- | ------------------------------- |
| **`@login_manager.user_loader`** | N/A (Decorator) | Defines user loader function  | - N/A                                                      | `User`            | `User`                  | N/A                             |
| `/login`(GET)                          | GET             | Displays the login form       | - Renders the form for entering username and password      | `User`(potential) | `User`                  | N/A (potentially `LoginForm`) |
| `/login`(POST)                         | POST            | Handles login form submission | - Processes login credentials, validates against user data | `User`            | `User`                  | N/A (potentially `LoginForm`) |

juse explain login_manager :

**`@login_manager.user_loader`:**

This decorator defines a function named `load_user` that acts as the user loader for Flask-Login. Its purpose is to retrieve a user object based on the provided user ID.

**Explanation:**

* The `@login_manager.user_loader` decorator associates the `load_user` function with the Flask-Login instance.
* The function takes a `user_id` argument representing the unique identifier of the user.
* It uses the `User.query.get(int(user_id))` expression to retrieve the user object from the database based on the provided ID (converted to an integer).
* This function is crucial for Flask-Login to manage user sessions and identify logged-in users.

> These routes demonstrate essential user authentication functionalities. The `load_user` function establishes a mechanism for Flask-Login to retrieve users, while the `/login` route handles login requests, validates credentials, and manages user sessions

---

##### | reset password -backend |

| ----------------------- |

```
@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
```

**Table for `/reset_password_request` Route:**

| Route (URL Pattern)               | HTTP Method | Description                                      | Page Interaction                                             | Database Table(s)   | Related models.py Classes | Related forms.py Classes     |
| --------------------------------- | ----------- | ------------------------------------------------ | ------------------------------------------------------------ | ------------------- | ------------------------- | ---------------------------- |
| `/reset_password_request`(GET)  | GET         | Displays the "Reset Password Request" form       | - Renders the form for entering email address                | `User`(potential) | `User`                  | `ResetPasswordRequestForm` |
| `/reset_password_request`(POST) | POST        | Handles "Reset Password Request" form submission | - Processes email address, sends password reset instructions | `User`            | `User`                  | `ResetPasswordRequestForm` |

**Explanation:**

* The table shows both GET and POST methods for the route.
* The GET request renders the "Reset Password Request" form for users to enter their email address.
* The POST request:
  * Validates the form data.
  * Checks if the email exists in the `User` table (using `User.query.filter_by(email=form.email.data).first()`)
  * If the email exists:
    * Generates a secure token for password resetting.
    * Saves the token in the user's `reset_password_token` attribute.
    * Creates an email message with HTML content (including a reset link) and sends it to the user's email address using Flask-Mail.
    * Flashes a success message if the email is sent successfully.
  * If the email doesn't exist, flashes an error message.
* The route redirects back to the login page (`url_for('login')`) in all cases.

**Additional Note:**

* ###### Remember to configure Flask-Mail with your email server settings.

###### for reset_password page

```
@app.route('/reset_password_token/<token>', methods=['GET', 'POST'])
def reset_password_token(token):
```

Table for `/reset_password_token/<token>` Route:

| Route (URL Pattern)                     | HTTP Method | Description                              | Page Interaction                               | Database Table(s)   | Related models.py Classes | Related forms.py Classes |
| --------------------------------------- | ----------- | ---------------------------------------- | ---------------------------------------------- | ------------------- | ------------------------- | ------------------------ |
| `/reset_password_token/<token>`(GET)  | GET         | Displays the "Reset Password" form       | - Renders the form for entering a new password | `User`(potential) | `User`                  | `ResetPasswordForm`    |
| `/reset_password_token/<token>`(POST) | POST        | Handles "Reset Password" form submission | - Processes and updates the user's password    | `User`(potential) | `User`                  | `ResetPasswordForm`    |

**Explanation:**

* The table shows both GET and POST methods for the route.
* The `<token>` in the URL pattern represents a unique token associated with the password reset request.
* The GET request:
  * Retrieves the user object (potentially using the token) - Note: The example code uses `User.query.get(1)` which is not recommended for production due to bypassing token validation.
  * Renders the "Reset Password" form for entering the new password.
* The POST request:
  * Validates the form data.
  * Updates the user's password using `user.set_password(form.password.data)`, ensuring secure hashing (replace `bcrypt` with your chosen method).
  * Saves the changes to the database using `db.session.commit()`.
  * Flashes a success message and redirects to the login page.

**Important Notes:**

* The provided code snippet uses `User.query.get(1)` to retrieve the user, which is not secure and bypasses token validation. In a production environment, you should use the token to retrieve the associated user object and ensure it's valid before allowing password reset.

> This table and explanation provide a general overview of the route's functionality. Remember to adjust the details and implement proper security measures based on your specific implementation and user authentication requirements.

---

| account -backend |
| ---------------- |

###### to show wished holiday form which was filled and sumbited on homepage form

```
@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
  

    # Retrieve wished holidays associated with the current user
    wishes = WishedHoliday.query.filter_by(user_id=current_user.id).all()
```

| Route (URL Pattern) | HTTP Method | Description                                                   | Page Interaction                                                    | Database Table(s)        | Related models.py Classes | Related forms.py Classes |
| ------------------- | ----------- | ------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------ | ------------------------- | ------------------------ |
| /account            | GET, POST   | Renders the user account page and handles user image uploads. | Displays user account details and allows uploading a profile image. | WishedHoliday, UserImage | WishedHoliday, UserImage  | UserImageForm            |

Explanation:

- The table outlines the functionality of the /account route, which allows users to view and manage their account details.
- Both GET and POST methods are used for this route.
- The GET request:
  - Retrieves wished holidays associated with the current user from the WishedHoliday table using a query.
  - Retrieves the user's profile image path from the UserImage table if it exists.
  - Creates an instance of the UserImageForm for uploading a new profile image.
  - Renders the account.html template, passing the current user object, profile image path, user image form, and wished holidays data to the template.
- The POST request:
  - Validates the submitted form data using user_image_form.validate_on_submit().
  - Saves the uploaded image file to the static/images folder.
  - Updates the user's profile image path in the UserImage table or creates a new record if it doesn't exist.
  - Commits the changes to the database.
  - Flashes a success message and redirects the user back to the account page.
- The table provides clarity on the interaction between the backend logic, database operations, and user interface for the /account route.

---

### Code Snippets of other routes :

    there was another***routes***  which not interact with databse : **about** and **contact**

```
# Route for the about us page
@app.route('/about', methods=['GET', 'POST'])
def about():
    # Your code for rendering the about us page

# Route for the contact us page
@app.route('/contact_us')
def contact_us():
    # Your code for rendering the contact us page

```

---

### Database Interaction:

To facilitate interaction with the database, the application utilizes classes defined in `models.py` and forms defined in `forms.py`. These files play a crucial role in defining the structure of the database tables and handling user input, respectively.

* **`models.py`** : Defines the database models using SQLAlchemy ORM. Each class represents a table in the database, and the attributes within the class correspond to the table columns. These models define the structure of the database and provide methods for querying and manipulating data.
* **`forms.py`** : Contains form classes using Flask-WTF for user input validation and processing. These forms define the fields and validators necessary for capturing user data. They ensure that data entered by users adheres to specific rules and constraints before interacting with the database.

Together, these files establish a robust system for managing data within the application, ensuring proper storage, retrieval, and validation of information entered by users. They form the backbone of the application's backend functionality, enabling seamless communication with the underlying database.

##### -code sniped of models.py and forms.py

#### User Model:

```python
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    # Define relationships
    destinations = db.relationship('Destination', backref='user', lazy=True)
```

#### Destination Model:

```python
class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    likes = db.Column(db.Integer, default=0)
    image = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
```

#### TravelPackage Model:

```python
class TravelPackage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    location = db.Column(db.String(150))
    hotel = db.Column(db.String(100))
    hotel_description = db.Column(db.Text)
    duration = db.Column(db.String(100))
    package_price = db.Column(db.Float)
    latitude = db.Column(db.String(50), nullable=False)
    longitude = db.Column(db.String(50), nullable=False)
```

#### WishedHoliday Model:

```python
class WishedHoliday(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    holiday_type = db.Column(db.String(50), nullable=False)
    travel_duration = db.Column(db.Integer, nullable=False)
    price_range = db.Column(db.String(100), nullable=False)
    travel_time = db.Column(db.String(100), nullable=False)
    departure_location = db.Column(db.String(100), nullable=False)
    additional_info = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
```

### Form Snippets:

#### SignupForm:

```python
class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
```

#### UserImageForm:

```python
class UserImageForm(FlaskForm):
    image = FileField('Profile Image', validators=[DataRequired(), FileAllowed(['jpg', 'png', 'jpeg'])])
```

#### AddTravelPackageForm:

```python
class AddTravelPackageForm(FlaskForm):
    name = StringField('Travel Package Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    hotel = StringField('Hotel')
    hotel_description = TextAreaField('Hotel Description')
    duration = StringField('Duration')
    package_price = FloatField('Package Price')
    latitude = StringField('Latitude', validators=[DataRequired()])
    longitude = StringField('Longitude', validators=[DataRequired()])
    image1 = FileField('Image 1')
    image2 = FileField('Image 2')
    image3 = FileField('Image 3')
    submit = SubmitField('Add Travel Package')
```

#### WishedHolidayForm:

```python
class WishedHolidayForm(FlaskForm):
    holiday_type = SelectField('Holiday Type', choices=[('beach', 'Relaxing beach vacation'),
                                                      ('adventure', 'Adventure and exploration'),
                                                      ('cultural', 'Cultural immersion and sightseeing'),
                                                      ('city', 'Bustling city break')],
                               validators=[DataRequired()])
    travel_duration = IntegerField('Travel Duration (days)', validators=[DataRequired()])
    price_range = SelectField('Price Range', choices=[('budget', 'Budget-friendly (up to $1000)'),
                                                     ('moderate', 'Moderate ($1000-$2500)'),
                                                     ('luxury', 'Luxury (>$2500)')],
                               validators=[DataRequired()])
    travel_time = StringField('Preferred Travel Time', validators=[DataRequired()])
    departure_location = StringField('Departure Location', validators=[DataRequired()])
    additional_info = TextAreaField('Additional Information')
```

### Deployment:

#### Local Deployment:

1. **Clone the Repository:**

   - Clone the repository to your local machine using the following command:

   ```
   git clone <repository_url>
   ```
2. **Install Dependencies:**

   - Navigate to the project directory and install the required dependencies using:

   ```
   pip install -r requirements.txt
   ```
3. **Database Setup:**

   - Ensure you have a local database setup (SQLite, MySQL, PostgreSQL, etc.).
   - Update the database URI in the `config.py` file to point to your local database.
4. **Run the Application:**

   - Start the Flask application using the following command:

   ```
   flask run 
   or 
   python run.py
   ```

   - The application will be accessible at `http://localhost:5000`.

<img src="./travel_planning/static/images/wireframes/heroku_logo.jpg" style="width: 50%; height: 40%;">

#### Deployment to Heroku:

**Create a Heroku Account:**

- Sign up for a Heroku account if you haven't already done so.

**Install Heroku CLI:**

- Install the Heroku CLI tool by following the instructions on the [official Heroku website](https://devcenter.heroku.com/articles/heroku-cli).

**Login to Heroku:**

- Log in to your Heroku account from the command line using:

```
heroku login
```

**Create a New Heroku App:**

- Create a new Heroku app by running:

```
heroku create <app_name>
```

**Configure Environment Variables:**

- Set any necessary environment variables using the Heroku CLI or the Heroku dashboard.

**Database Setup:**

- Provision a Heroku database (Heroku Postgres, ClearDB MySQL, etc.).
- Update the database URI in the Heroku config vars.

**Push to Heroku:**

- Push your local repository to Heroku using Git:

```
git push heroku main
```

**Run Database Migrations:**

- Please be sure you created you app and heroku add-on
- ```
  in powershell ; #for copy of local databse and add to heroku
  #it asks for database password 

  pg_dump -U postgres -d travel_planning | Out-File -FilePath "E:\..\..\..\.\travel_planning\dump.sql"

  #to use dump.sql fil in heroku postgress add-on 

  Invoke-Expression "heroku pg:psql -a your-app-name < dump.sql"


  ```
- Run any necessary database migrations using:

```
heroku run flask db upgrade
```

**Open the App:**

- Open the deployed application in your web browser using:

```
heroku open
```

**Monitor Logs:**

- Monitor the logs for any errors or issues using:

```
heroku logs --tail
```

### Notes:

- Ensure you have proper error handling and logging in your application for both local and Heroku deployments.
- It's recommended to use a separate configuration file for production settings to manage environment variables securely.

---

### Conclusion:

The backend of the Flask application is the core component responsible for handling data processing, business logic, and database interactions. It encompasses routes, models, and forms to create a robust web application.

### Overview:

1. **Routes:**
   * Routes define the endpoints of the application and handle HTTP requests and responses.
   * They contain the logic to render templates, process form submissions, and interact with the database.
   * Routes are responsible for rendering HTML pages, handling user authentication, and executing CRUD (Create, Read, Update, Delete) operations on the database.
2. **Models:**
   * Models represent the structure and behavior of the application's data.
   * They define database tables and relationships between them using ORM (Object-Relational Mapping).
   * Models encapsulate data access and manipulation methods, ensuring data integrity and consistency.
   * Relationships between models enable complex data querying and retrieval.
3. **Forms:**
   * Forms define the structure and validation rules for HTML forms in the application.
   * They handle user input, validate data, and provide error messages for invalid submissions.
   * Forms facilitate secure data transmission between the client and server, preventing common vulnerabilities like CSRF (Cross-Site Request Forgery) and SQL injection.

### Backend Components:

* **User Authentication:** The backend manages user authentication and authorization, allowing users to register, log in, and access protected resources.
* **Database Interactions:** Backend components interact with the database to perform CRUD operations, store and retrieve data, and maintain data consistency.
* **Data Validation:** Forms and backend logic validate user input to ensure data integrity and prevent malicious or incorrect data from being stored in the database.
* **Business Logic:** Backend code implements the application's business rules and logic, orchestrating various components to achieve specific functionalities.
* **Error Handling:** The backend handles errors gracefully, providing informative error messages and logging exceptions for debugging purposes.
* **Security Measures:** Backend components incorporate security measures like password hashing, CSRF protection, and input validation to safeguard against common web vulnerabilities.

### Short Explanations:

* **Routes:** Define application endpoints, handle HTTP requests, and execute backend logic.
* **Models:** Represent database tables and define data structures and relationships.
* **Forms:** Define HTML form structures, validate user input, and facilitate data transmission.

Overall, the backend serves as the foundation of the application, orchestrating various components to deliver a seamless user experience while ensuring data integrity, security, and performance.

---

---

## Technologies Used (all)

### Languages Used

- HTML5
- CSS3
- PYTHON
- FLASK
- JavaScript

### Frameworks, Libraries & Programs Used

- [Python Flask](https://flask.palletsprojects.com/): Micro web framework for building web applications in Python.
- [PostgreSQL](https://www.postgresql.org/): Open-source relational database management system for storing application data.
- [Bootstrap](https://getbootstrap.com/) v5.3: Front-end framework for responsive design.
- [jQuery](https://jquery.com/): JavaScript library for DOM manipulation and event handling.
- [Font Awesome](https://fontawesome.com/): Icon library for scalable vector icons.
- [Google Fonts](https://fonts.google.com/): Source of custom fonts for enhanced typography.
- [Adobe XD](https://www.adobe.com/products/xd.html): Design tool for wireframing and prototyping.
- [GitHub](https://github.com/): Version control and collaboration platform.
- [Git](https://git-scm.com/): Distributed version control system.
- [Visual Studio Code](https://code.visualstudio.com/): Code editor for writing and editing code.

---

#### How to Fork

1. Log in to GitHub and locate the repository: [TravelApp](https://github.com/yourusername/yourtravelapp).
2. At the top right of the page, click the Fork button.
3. After forking, you'll have a copy of the repository in your GitHub account.

#### How to Clone

1. Clone the repository to your local machine using the following command:

   ```
   git clone https://github.com/maisam2004/travel_planning_project.git
   ```
2. Navigate to the project directory:

   ```
   cd travel_planning
   ```
3. Open the home.html file in your browser to view the site locally.

---

## Testing

### Contents

- [Automated Testing](#automated-testing)
  - [W3C Validator](#w3c-validator)
  - [CSS Jigsaw](#css-validator)
  - [JavaScript jshint.com](#javascript-validator)
  - [Lighthouse](#lighthouse)
- [Manual Testing](#manual-testing)
  - [Testing User Stories](#testing-user-stories)
  - [Full Testing](#full-testing)

---

### Automated Testing

Automated testing was conducted using various tools to ensure the quality and performance of TravelApp.

#### W3C Validator

All HTML files were tested using the W3C Markup Validation Service to identify any syntax errors or warnings.

<img src="./travel_planning/static/images/wireframes/home_valid.jpg" style="width: 55%; height: 50%;">- <img src="./travel_planning/static/images/wireframes/explore_valid.jpg" style="width: 30%; height: 50%;">

<img src="./travel_planning/static/images/wireframes/about_valid.jpg" style="width: 40%; height: 50%;">- <img src="./travel_planning/static/images/wireframes/account_valid.jpg" style="width: 33%; height: 50%;">

<img src="./travel_planning/static/images/wireframes/login_valid.jpg" style="width: 40%; height: 50%;">- <img src="./travel_planning/static/images/wireframes/signup_valid.jpg" style="width: 34%; height: 50%;">

#### [CSS Jigsaw](#css-validator)

- for this project we have only 1 file styles.css and validated on css validator

<img src="./travel_planning/static/images/wireframes/css_valid.jpg" style="width: 70%; height: 30%;">

#### Validator (html , css)

* **home.html** : Passed.(homepage had lots of reapeated errors for id of modals then by add dynamic package is it sorted )
* **explore.html** :Passed
* **about.html** : Passed.
* **contact.html** : Passed.
* **account.html** : Passed.
* **login.html** : Passed.
* **signup.html**: Passed.
* **wished_holiday**:passed.
* **style.css** : Passed.
  (css validating first errors was mostly for values and some empty properties but modified)

#### JavaScript Validator

JavaScript code was validated using JSHint to detect any potential errors and  no major issues found.

<img src="./travel_planning/static/images/wireframes/js_valid1.jpg" style="width: 75%; height: 30%;">

scripts.js :passed

#### Lighthouse

Lighthouse audits were performed to assess the site's performance, accessibility, best practices, and SEO.

## Manual Testing

##### TravelApp

TravelApp is a web application that allows users to explore various travel destinations and packages,  and book their next trip seamlessly.

### Testing User Stories

#### First Time Visitors

| Goals                                                                         | How are they achieved?                                                                             |
| ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| I want to look through travel package deals and their destinations.           | The TravelApp website provides a variety of destinations and travel packages for users to explore. |
| I want to easily navigate through the website to find the information I need. | Intuitive navigation and clear calls-to-action are implemented for easy exploration.               |
| I want visually appealing content that showcases destinations and packages.   | High-quality images and well-crafted content are used to visually engage first-time visitors.      |

#### Returning Visitors

| Goals                                                              | How are they achieved?                                                                                 |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| I want to review and compare travel packages efficiently.          | The packages page allows users to view and compare details of various travel packages easily.          |
| I want to find new and exciting destinations to plan my next trip. | The destinations page highlights different travel spots, providing inspiration for returning visitors. |

#### Frequent Visitors

| Goals                                                             | How are they achieved?                                                                                |
| ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| I want to check for any new travel packages or updates regularly. | A blog or news section keeps frequent visitors informed about new packages, travel tips, and updates. |
| I want a seamless booking experience for selected packages.       | The booking process is streamlined, providing an efficient and user-friendly experience.              |

#### Users Posting Holiday Details

| Goals                                                                  | How are they achieved?                                                                                                           |
| ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| I want to share details of my recent holidays with other users.        | The Explore page allows registered users to post details and images of their recent holidays for others to view and be inspired. |
| I want to edit or delete my posted holiday details if needed.          | The Explore page provides options for users to edit or delete their posted holiday details as desired.                           |
| I want to easily navigate and interact with the Explore page features. | Intuitive navigation and clear UI elements are implemented to ensure a seamless user experience on the Explore page.             |

#### Full Testing

Comprehensive testing was performed on all pages, forms, buttons, and interactive elements to ensure proper functionality and responsiveness across devices.

**testing was performed on the following devices:**

**Laptop:**

* SAMSUNG Galaxy Book3 360 15.6

**Mobile Devices:**

* iPhone XR
* iPhone 14 pro
* Google pixel 7

Each device tested the site using the following browsers:

* Google Chrome
* Microsoft Edge
* Firefox

---

    **some of pages features tests**

<div style="border: 2px solid #fff; padding: 6px;">
 <h2>Home Page Features</h2>
</div>

| Feature               | Expected Outcome                                                                  | Testing Performed                                    | Result                                                                | Pass/Fail |
| --------------------- | --------------------------------------------------------------------------------- | ---------------------------------------------------- | --------------------------------------------------------------------- | --------- |
| Hero Section          | Display captivating hero section with carousel showcasing travel app's benefits   | Reviewed hero section on different screen sizes      | Hero section displayed correctly with carousel and compelling content | Pass      |
| Featured Destinations | Present featured destinations with images, descriptions, and pricing information  | Checked display of multiple destinations and details | Destinations displayed properly with relevant information             | Pass      |
| More Deals Button     | Clicking "More Deals" button reveals additional travel packages                   | Clicked on button to confirm functionality           | More deals were loaded and displayed as expected                      | Pass      |
| Why Choose Us Section | Highlight unique selling points of the travel app through card-based presentation | Reviewed card content and layout                     | USPs presented clearly with appropriate graphics and descriptions     | Pass      |
| Reviews Section       | Display customer testimonials with images in a visually appealing manner          | Verified display of multiple reviews                 | Testimonials showcased well with relevant images and glowing feedback | Pass      |
| Wished Holiday Form   | Provide a form for users to express their dream holiday preferences               | Filled out form with test data                       | Form submission successful, data stored and processed correctly       | Pass      |

**Form Submission Data Handling:**

- **Backend Functionality:**
  - **Technology:** Flask framework for backend processing.
  - **Workflow:** Upon form submission, data is validated and stored in the database.
  - **Result:** Data is securely stored and can be accessed for further processing.
  - **Pass/Fail:** Pass

<div style="border: 2px solid #fff; padding: 6px;">
 <h2>Explore Page Features</h2>
</div>

| Feature                             | Expected Outcome                                                                     | Testing Performed                                    | Result                                                              | Pass/Fail |
| ----------------------------------- | ------------------------------------------------------------------------------------ | ---------------------------------------------------- | ------------------------------------------------------------------- | --------- |
| Destination Display                 | Show user's destinations with name, location, and description                        | Checked display of multiple destinations and details | Destinations displayed correctly with relevant information          | Pass      |
| Add New Destination Button          | Allow authenticated users to add new destinations via a collapsible form             | Clicked on button to add new destination             | Form for adding new destination opened and submitted successfully   | Pass      |
| Edit and Delete Buttons             | Enable authenticated users to edit and delete their own destinations                 | Tested edit and delete buttons for authorized user   | Editing and deleting destinations functionality worked as expected  | Pass      |
| Modal Confirmation for Delete       | Prompt user for confirmation before deleting a destination                           | Clicked delete button to confirm action              | Modal displayed asking for confirmation before deleting destination | Pass      |
| Form Validation for New Destination | Validate form fields before adding a new destination to prevent erroneous data entry | Attempted submission with invalid data               | Form prevented submission and displayed appropriate error messages  | Pass      |
| Image Upload for New Destination    | Allow users to upload an image for their new destination                             | Uploaded image during new destination creation       | Image successfully uploaded and displayed with the destination      | Pass      |

**Form Submission Data Handling:**

- **Backend Functionality:**
  - **Technology:** Flask framework for backend processing.
  - **Workflow:** Upon form submission, data is validated, processed, and stored in the database.
  - **Result:** Data is securely stored and can be accessed for further processing.
  - **Pass/Fail:** Pass

<div style="border: 2px solid #fff; padding: 6px;">
 <h2>Signup Page Features</h2>
</div>

| Feature                | Expected Outcome                                                        | Testing Performed                                        | Result                                                                      | Pass/Fail |
| ---------------------- | ----------------------------------------------------------------------- | -------------------------------------------------------- | --------------------------------------------------------------------------- | --------- |
| Username Input         | Allow user to input desired username                                    | Entered username in input field                          | Username entered correctly and displayed in the form                        | Pass      |
| Email Input            | Enable user to input valid email address                                | Entered email address in input field                     | Email address entered correctly and displayed in the form                   | Pass      |
| Password Input         | Provide field for user to input password                                | Entered password in input field                          | Password entered securely and displayed as masked characters                | Pass      |
| Confirm Password Input | Allow user to confirm password by re-entering                           | Entered confirmed password in input field                | Confirmed password matches original password input                          | Pass      |
| Signup Button          | Enable user to submit signup form with valid inputs                     | Clicked signup button to submit form                     | Form submission processed successfully and user redirected appropriately    | Pass      |
| Link to Login Page     | Provide option for users to navigate to login page if already signed up | Clicked on login page link                               | Redirected to login page as expected                                        | Pass      |
| Form Validation        | Validate form inputs to ensure correctness and prevent errors           | Attempted submission with invalid or missing data        | Form prevented submission and displayed appropriate error messages          | Pass      |
| Flash Messages Display | Show error messages if signup fails or if there are validation issues   | Tested signup form with incorrect or missing information | Error messages displayed correctly for validation issues and failed signups | Pass      |

**Form Submission Data Handling:**

- **Backend Functionality:**
  - **Technology:** Flask framework for backend processing.
  - **Workflow:** Upon form submission, data is validated, processed, and stored in the database.
  - **Result:** Data is securely stored, and user accounts are created successfully upon valid submissions.
  - **Pass/Fail:** Pass

<div style="border: 2px solid #fff; padding: 6px;">
 <h2>Account Page Features</h2>
</div>

| Feature                     | Expected Outcome                                            | Testing Performed                                    | Result                                                                     | Pass/Fail |
| --------------------------- | ----------------------------------------------------------- | ---------------------------------------------------- | -------------------------------------------------------------------------- | --------- |
| Profile Image Upload        | Allow user to upload a profile image for their account      | Uploaded profile image with various file formats     | Profile image uploaded successfully and displayed in the user info section | Pass      |
| User Information Display    | Display user's email address and other relevant information | Checked display of user email and other details      | User information displayed accurately and formatted correctly              | Pass      |
| Profile Image Update Button | Provide button for user to update their profile image       | Clicked on update button to upload new profile image | New profile image uploaded successfully and reflected in user info         | Pass      |
| Wished Holidays Display     | Show a list of holidays that the user has wished for        | Checked display of wished holidays list              | Wished holidays listed correctly with relevant details                     | Pass      |
| Delete Wished Holiday       | Allow user to remove a wished holiday from their list       | Attempted deletion of wished holiday from list       | Wished holiday successfully removed upon deletion                          | Pass      |
| No Wished Holidays Message  | Display message if user has not added any wished holidays   | Checked display when no wished holidays are present  | Message shown indicating no wished holidays found                          | Pass      |

**Form Submission Data Handling:**

- **Backend Functionality:**
  - **Technology:** Flask framework for backend processing.
  - **Workflow:** Upon form submission, image data is validated, processed, and stored.
  - **Result:** Uploaded images are securely stored and associated with the user's account.
  - **Pass/Fail:** Pass

<div style="border: 2px solid #fff; padding: 6px;">
 <h2>Reset Password Page Features</h2>
</div>

| Feature                  | Expected Outcome                                              | Testing Performed                               | Result                                        | Pass/Fail |
| ------------------------ | ------------------------------------------------------------- | ----------------------------------------------- | --------------------------------------------- | --------- |
| Form Submission Handling | Allow user to submit a new password through a form            | Submitted new password with various inputs      | Form submitted successfully with new password | Pass      |
| Password Input Field     | Provide input field for user to enter their new password      | Entered new passwords with different lengths    | Password input field displayed correctly      | Pass      |
| Error Message Display    | Show error message if there are validation errors in the form | Entered incorrect passwords and empty fields    | Error messages displayed for invalid inputs   | Pass      |
| Submit Button            | Provide button for user to submit their new password          | Clicked on submit button to submit new password | New password submitted successfully           | Pass      |

**Form Submission Data Handling:**

- **Backend Functionality:**
  - **Technology:** Flask framework for backend processing.
  - **Workflow:** Upon form submission, password data is validated, processed, and updated in the database.
  - **Result:** User's password is securely updated in the database.
  - **Pass/Fail:** Pass

## Credits

### Code Used

- Bootstrap: [https://getbootstrap.com/](https://getbootstrap.com/)
- jQuery: [https://jquery.com/](https://jquery.com/)
- Font Awesome: [https://fontawesome.com/](https://fontawesome.com/)
- Google Fonts: [https://fonts.google.com/](https://fonts.google.com/)

### Content

- Travel guides and destination information sourced from popular travel websites and tourism boards.

### Media

- Images sourced from Unsplash,freepik, Pixabay, and Pexels.
- Icons sourced from Font Awesome.

### Acknowledgments

Special thanks to the following individuals and resources:

- Stack Overflow community for troubleshooting assistance.
- Code Institute tutors for guidance and support.
- Friends and family for feedback and encouragement.

---

[Back to Top](#yourtravelapp)
