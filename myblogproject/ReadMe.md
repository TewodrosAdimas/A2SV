# Django Blog API Project

This project is a simple Django-based blog API where users can create accounts, log in, create blog posts, rate blog posts, comment on them, and like them. The project uses JWT authentication for user login and token management.

## Features

1. **User Authentication**
   - Register a new user account.
   - Login using JWT authentication.
   - Update user profile (e.g., bio, profile picture).

2. **Blog Posts**
   - Create, view, update, and delete blog posts.
   
3. **Blog Interactions**
   - Rate a blog post (1-5).
   - Comment on a blog post.
   - Like a blog post.

---

## Architecture

This project follows a **Modular** architecture with a focus on separating concerns into distinct Django apps. The main components are:

1. **Users App**:
   - Handles user registration, authentication (via JWT), and user management.
   - The `User` model is extended to suit the project needs.
   
2. **Posts App**:
   - Manages blog posts.
   - Handles creation and listing of blog posts.
   - Each blog post is associated with a user (author).
   
3. **Blog Interactions App**:
   - Manages interactions on blog posts such as ratings, comments, and likes.
   - The `BlogRating`, `Comment`, and `Like` models track these interactions.

4. **JWT Authentication**:
   - **JSON Web Tokens (JWT)** are used for secure authentication of users.
   - Tokens are issued upon login and are required for accessing protected routes.

5. **Django Rest Framework (DRF)**:
   - DRF is used to build API endpoints.
   - Viewsets, serializers, and generic views handle requests for creating and viewing blog posts, comments, ratings, and likes.

---

## Requirements

- Python 3.x
- Django 4.x
- Django Rest Framework 3.x
- djangorestframework-simplejwt

---

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/TewodrosAdimas/A2SV.git
   cd A2SV/myblogproject/
   ```

2. **Set up the virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Make migrations and migrate the database**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (optional)**:

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

   The server will be running at `http://127.0.0.1:8000/`.

---

## API Endpoints

### **User Authentication**

- **POST** `/users/register/`: Register a new user.
  
  **Request Body**:
  ```json
  {
    "username": "john_doe",
    "email": "john@example.com",
    "password": "passreword123",
    "password2": "passreword123"
  }
  ```

- **POST** `/users/login/`: Login with JWT authentication and obtain an access token.

  **Request Body**:
  ```json
  {
    "email": "john@example.com",
    "password": "password123"
  }
  ```

- **PATCH** `/users/profile/`: Update user profile.
  
  **Request Body**:
  ```json
  {
    "bio": "Updated bio text"
      }
  ```

---

### **Blog Posts**

- **GET** `/blog/`: List all blog posts.
- **POST** `/blog/`: Create a new blog post (requires authentication).

  **Request Body**:
  ```json
  {
    "author": 1,
    "title": "My First Blog Post",
    "content": "This is the content of my first blog post."
  }
  ```

- **PATCH** `/blog/<pk>/update/`: Update a blog post.

  **Request Body**:
  ```json
  {
    "title": "Updated Blog Post Title"
  }
  ```

- **DELETE** `/blog/<pk>/delete/`: Delete a blog post.

  **Headers**:
  ```plaintext
  Authorization: Bearer <your_jwt_token>
  ```

---

### **Blog Interactions**

- **POST** `/interactions/ratings/`: Rate a blog post.

  **Request Body**:
  ```json
  {
    "rating_value": 5,
    "user": 1,
    "blog": 2
  }
  ```

- **PATCH** `/interactions/ratings/<rating_id>/update/`: Update a blog post rating.

  **Request Body**:
  ```json
  {
    "rating": 4
  }
  ```

- **DELETE** `/interactions/ratings/<rating_id>/delete/`: Delete a rating.

  **Headers**:
  ```plaintext
  Authorization: Bearer <your_access_token>
  ```

- **POST** `/interactions/comments/`: Comment on a blog post.

  **Request Body**:
  ```json
  {
    "content": "Great post!",
    "user": 1,
    "blog": 2
  }
  ```

- **PATCH** `/interactions/comments/<comment_id>/update/`: Update a comment.

  **Request Body**:
  ```json
  {
    "content": "Updated comment!"
  }
  ```

- **DELETE** `/interactions/comments/<comment_id>/delete/`: Delete a comment.

  **Headers**:
  ```plaintext
  Authorization: Bearer <your_access_token>
  ```

- **POST** `/interactions/likes/`: Like a blog post.

  **Request Body**:
  ```json
  {
    "blog": 1
  }
  ```

- **PATCH** `/interactions/likes/<like_id>/update/`: Update a like.

  **Request Body**:
  ```json
  {
    "liked": false
  }
  ```

- **DELETE** `/interactions/likes/<like_id>/delete/`: Delete a like.

  **Headers**:
  ```plaintext
  Authorization: Bearer <your_access_token>
  ```

---

