Portfolio API

This is a personal portfolio project built with Python (Flask) for the backend and HTML/CSS for the frontend. The project showcases my professional experience, skills, hobbies, and GitHub projects. It also includes images to make the portfolio visually appealing.

Features

- Dynamic Web Application: Built using Flask to serve dynamic content.
- Responsive Design: Styled with CSS for a modern and clean user interface.
- Personalized Content: Includes sections for:
  - About Me
  - Skills and Tools
  - Hobbies
  - Contact Form (connected to an email handler)
  - GitHub Project Links
- Images: Enhances the portfolio with images related to skills, hobbies, and more.

Technology Stack

- Backend: Flask (Python)
- Frontend: HTML and CSS
- Email Integration: Flask with SMTP for sending contact form messages.
- Hosting: (Specify if hosted on platforms like Heroku, AWS, or GitHub Pages)

How to Run Locally

- cd portfolio-api
- Create a virtual environment:
- python -m venv venv
- source venv/bin/activate  
- pip install -r requirements.txt
- flask run
- Open your browser and navigate to http://127.0.0.1:5000.

Folder Structure

portfolio-api/
├── static/
│   ├── css/
│   │   └── styles.css
│   ├── images/
│       ├── automotive.png
│       ├── github_logo.png
│       ├── gym.png
│       └── photography.png
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── projects.html
│   └── contact.html
├── app.py
├── requirements.txt
└── README.md

Screenshots

Home Page
Contact Page
Contributing

Feel free to fork this project and create pull requests. All contributions are welcome!
