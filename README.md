# Dynamic Blog Application with Flask, HTMX, (TailwindCSS, and Authentication) - Part 1 & 2

## ‼️ PLEASE NOTE THAT THIS IS NOT PRODUCTION READY CODE. EDUCATIONAL PURPOSE ONLY  ‼️

## [🔗 Part 1 Blog Link](https://devtoys.io/2024/06/30/building-a-dynamic-blog-with-flask-and-htmx/)

## [🔗 Part 2 Blog Link](https://devtoys.io/2024/07/02/creating-a-dynamic-blog-with-flask-htmx-tailwindcss-and-authentication-part-2/)

This repository demonstrates how to create a dynamic blog application using Flask, HTMX, TailwindCSS, and user authentication. The project is divided into two parts: Part 1 covers the basic blog setup, and Part 2 extends it by adding TailwindCSS and user authentication.

## Features

- Dynamic content loading with HTMX
- Styling with TailwindCSS
- User authentication with Flask-Login and Flask-Bcrypt
- Interactive form submissions
- CRUD operations for blog posts

## Prerequisites

- Python and pip
- Node.js and npm

## Project Structure

```
blog_app/
├── part1/
│   ├── static/
│   │   └── css/
│   │       └── styles.css
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── post.html
│   │   ├── edit_post.html
│   │   └── post_snippet.html
│   ├── app.py
│   └── models.py
├── part2/
│   ├── static/
│   │   ├── css/
│   │   │   ├── tailwind.css
│   │   │   └── styles.css
│   │   └── js/
│   │       └── scripts.js
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── post.html
│   │   ├── edit_post.html
│   │   ├── login.html
│   │   ├── register.html
│   │   └── post_snippet.html
│   ├── app.py
│   └── models.py
```

## Setup Instructions

### Part 1: Basic Blog Setup

#### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/blog_app.git
cd blog_app/part1
```

#### 2. Set Up Python Environment

Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

Install the required Python packages:

```bash
pip install Flask Flask-SQLAlchemy
```

#### 3. Set Up the Database

Initialize the SQLite database:

```bash
flask shell
>>> from app import db
>>> db.create_all()
>>> exit()
```

#### 4. Run the Application

Start the Flask application:

```bash
flask run
```

Open your web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

---

### Part 2: Blog with TailwindCSS and Authentication

#### 1. Navigate to Part 2

```bash
cd ../part2
```

#### 2. Set Up Python Environment

Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

Install the required Python packages:

```bash
pip install Flask Flask-SQLAlchemy Flask-Login Flask-Bcrypt
```

#### 3. Set Up TailwindCSS

Install TailwindCSS and initialize it:

```bash
npm install -D tailwindcss
npx tailwindcss init
```

Configure TailwindCSS by creating a `tailwind.config.js` file:

```javascript
module.exports = {
  content: [
    './templates/**/*.html',
    './static/js/**/*.js',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

Create a TailwindCSS input file `static/css/tailwind.css`:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Add a build script to your `package.json`:

```json
"scripts": {
  "build": "tailwindcss -i ./static/css/tailwind.css -o ./static/css/styles.css --watch"
}
```

Run the build script to generate your CSS:

```bash
npm run build
```

#### 4. Set Up the Database

Initialize the SQLite database:

```bash
flask shell
>>> from app import db
>>> db.create_all()
>>> exit()
```

#### 5. Run the Application

Start the Flask application:

```bash
flask run
```

Open your web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Conclusion

This repository provides a complete guide to creating a dynamic blog application using Flask, HTMX, and TailwindCSS. It covers everything from setting up the environment to adding user authentication and dynamic content loading. By following these steps, you can build modern, interactive web applications with enhanced user experiences. Feel free to explore the code and dive deeper by adding more features and functionalities to the project. Please visit [DevToys.io](https://devtoys.io) to share
your feedbacks and comments.
 Happy coding! 🚀
