
```
# Django Blog API Project

This project is a simple Django-based blog API where users can create accounts, log in, create blog posts, rate blog posts, comment on them, and like them. The project uses JWT authentication for user login and token management.

## Features

1. **User Authentication**
   - Register a new user account.
   - Login using JWT authentication.
   
2. **Blog Posts**
   - Create a new blog post.
   - View blog posts.
   
3. **Blog Interactions**
   - Rate a blog post (1-5).
   - Comment on a blog post.
   - Like a blog post.

## Architecture

This project follows a **Modular** architecture with a focus on separating concerns into distinct Django apps. The main components of the architecture are:

1. **Users App**
   - Handles user registration, authentication (via JWT), and user management.
   - The `User` model is extended to suit the project needs.
   
2. **Posts App**
   - Manages blog posts.
   - Handles the creation and listing of blog posts.
   - Each blog post is associated with a user (author).
   
3. **Blog Interactions App**
   - Manages interactions on the blog posts such as ratings, comments, and likes.
   - The `BlogRating`, `Comment`, and `Like` models are used to track these interactions.

4. **JWT Authentication**
   - **JSON Web Tokens (JWT)** are used for secure authentication of users.
   - Tokens are issued upon login and are required for accessing protected routes.

5. **Django Rest Framework (DRF)**
   - DRF is used for building the API endpoints.
   - Viewsets, serializers, and generic views are used to handle requests for creating and viewing blog posts, comments, ratings, and likes.

6. **Database Models**
   - The project uses relational database models in Django, with ForeignKey relationships between the models to establish connections between users, blog posts, ratings, comments, and likes.

## Requirements

- Python 3.x
- Django 4.x
- Django Rest Framework 3.x
- djangorestframework-simplejwt

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/TewodrosAdimas/A2SV.git
   cd A2SV/myblogproject/
   ```

2. **Set up the virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Make migrations and migrate the database:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser for accessing the admin panel (optional):**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

   The server will be running at `http://127.0.0.1:8000/`.

## API Endpoints

### User Authentication

- **POST** `/users/register/`: Register a new user.

#### Request Body:
```json
{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "passreword123",
    "password2": "passreword123"
}

- **POST** `/users/login/`: Login with JWT authentication and obtain an access token.

{
    "email": "john@example.com",
    "password": "password123"
}


Patch Request: To update a profile

{
  "bio": "Updated bio text",
  "profile_picture": "<base64 encoded image data>"
}


### Blog Posts

- **GET** `/blogs/`: List all blog posts.
- **POST** `/blogs/`: Create a new blog post (requires authentication).
   Request body:

   {
    "author": "1",
   "title": "My First Blog Post",
   "content": "This is the content of my first blog post."
   }



### Blog Interactions

- **POST** `/interactions/ratings/`: Rate a blog post (requires authentication).
  - Request body:
    ```json
    {
      "rating_value": 5,
      "user": 1,
      "blog": 2
    }
    ```
- **POST** `/interactions/comments/`: Comment on a blog post (requires authentication).
  - Request body:
    ```json
    {
      "content": "Great post!",
      "user": 1,
      "blog": 2
    }
    ```
- **POST** `/interactions/likes/`: Like a blog post (requires authentication).
  - Request body:
    ```json
    {
      "user": 1,
      "blog": 2
    }
    ```

