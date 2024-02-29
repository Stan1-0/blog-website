
# Blog Website using Django Framework
This is a simple blog website built using the Django framework. It allows anadmin to create, read, update, and delete blog posts from the admin panel. Users can only read posts.

## Features
- User authentication: Users can register, login, and logout.
- Responsive design: The website is optimized for both desktop and mobile devices.
- CRUD operations: Users with admin privilleages can create, read, update, and delete their own blog posts.

## Installation
- Clone the repository: git clone https://github.com/Stan1-0/blog-website.git
- Navigate to the project directory: cd blog-website
- Install dependencies: pip install -r requirements.txt
- Run migrations: python manage.py migrate
- Create a superuser (admin): python manage.py createsuperuser
- Create a superuser (admin): python manage.py runserver

- Access the website at http://localhost:8000

## Usage
- To create a new blog post, an admin must log in to the admin panel and navigate to the "Post" page.
- To update or delete a blog post, navigate to the post and click on the "Edit" or "Delete" button.

## Acknowledgements
- BLOGR for the template

## Contributing
Contributions are welcome! If you would like to contribute to this project, please fork the repository and submit a pull request.
