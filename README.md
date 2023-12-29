# ImageBazzaar Web Application

## Introduction

ImageBazzaar is a web application built using the Django framework that allows users to manage and showcase their image collection. It provides features for uploading images, organizing them into categories, and viewing images in a gallery format. The application also supports user authentication, allowing users to create accounts, log in, and manage their own image collections.

## Features

1. **User Authentication:**
   - Users can sign up, log in, and log out.
   - Authentication ensures that each user has a personalized experience and control over their uploaded images.

2. **Image Management:**
   - Users can upload images, providing details such as title, description, and category.
   - Uploaded images are organized into categories for easy navigation.

3. **Gallery Display:**
   - View images in a visually appealing gallery format.
   - Clicking on an image opens a detailed view with additional information.

4. **Category Sorting:**
   - Filter and sort images based on predefined categories.

## Setting Up the Project

### Prerequisites

- Python installed on your machine
- Django framework installed (`pip install django`)

### Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/samagra44/ImageBazzaar.git
   ```

2. **Navigate to Project Directory:**
   ```bash
   cd ImageBazzaar
   ```

3. **Create and Apply Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a Superuser Account:**
   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create a superuser account. This account will have administrative access to the Django admin panel.

5. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the Application:**
   Open your web browser and go to [http://localhost:8000/](http://localhost:8000/) to access the ImageBazzaar application.

7. **Access the Admin Panel:**
   Navigate to [http://localhost:8000/admin/](http://localhost:8000/admin/) and log in with the superuser credentials created earlier. Here, you can manage users, images, and categories.

## Project Structure

The project follows a typical Django project structure with additional directories for templates and static files. The main components include:

- **ImageBazzaar App (`imagebazaar`):**
  - Models define the structure of images and categories.
  - Views handle the logic for displaying images, uploading images, and managing categories.
  - Templates contain HTML files for rendering pages.

- **User Authentication (`accounts`):**
  - Handles user registration, login, and logout.
  - Utilizes Django's built-in authentication system.

- **Django Admin Panel:**
  - Accessible at [http://localhost:8000/admin/](http://localhost:8000/admin/) for managing users, images, and categories.

Feel free to explore and customize the project based on your preferences. You can enhance the application by adding features such as image tags, search functionality, or user profiles.

![Capture](https://github.com/samagra44/ImageBazaar/assets/77968722/8e23e55b-fab3-4b76-9f6d-f5ae34393c82)
