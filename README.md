CS50 Commerce Project
CS50 Web Programming with Python and JavaScript — Harvard (2025)

A fully functional e-commerce web application built using Django and JavaScript.
This project simulates an online auction/commerce platform with user authentication, listing management, bidding, commenting, and watchlists.

Table of Contents
Project Overview
Features
Tech Stack
Installation
Project Overview
CS50 Commerce is a web-based platform where users can:

Create accounts and log in securely.
Create and manage product listings.
Place bids on items in an auction-style format.
Comment on listings.
Add listings to a personal watchlist.
Categorize listings for easy browsing.
The project demonstrates full-stack web development principles including backend logic, database design, and frontend interactivity.

Features
User Authentication: Login, logout, and registration system.
Listing Management: Create, edit, and delete product listings.
Bidding System: Users can place bids on active listings.
Comments: Users can add comments to listings.
Watchlist: Add and remove items from a personalized watchlist.
Categories: Browse listings by category.
Responsive Design: Works well on both desktop and mobile.
Tech Stack
Backend: Django
Frontend: HTML, CSS, JavaScript
Database: SQLite (default for Django)
Other Tools: GitHub, Visual Studio Code
Installation
Clone the repository:
git clone https://github.com/Muaz2004/cs50-commerce.git
cd cs50-commerce
Create a virtual environment:

python -m venv env source env/bin/activate # Linux/Mac env\Scripts\activate # Windows

Install dependencies:

pip install -r requirements.txt

Apply migrations:

python manage.py migrate

Create a superuser (for admin access):

python manage.py createsuperuser

Run the development server:

python manage.py runserver
