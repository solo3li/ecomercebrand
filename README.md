# Bervado Ecommerce Platform

Bervado is a premium, minimalist ecommerce platform built with Django. It embodies the "Old Money" aesthetic—focusing on quiet elegance, simple navigation, and sophisticated design without loud visual noise.

## 🌟 Features

- **"Old Money" Aesthetic:** A beautifully curated color palette (Cream, Navy, Olive, Gold) with sophisticated typography (Playfair Display & Open Sans).
- **Smooth Animations:** Minimalist fade-in transitions tied to intersection observers for a luxurious scrolling experience.
- **Dynamic Splash Screen:** A beautiful, pulse-animated brand splash screen that greets users once per session.
- **Advanced Filtering:** Dynamically filter the shop catalog by Category, Size, Color, and Custom Price Ranges.
- **Product Variants:** Full support for unique product variations linking specific sizes and colors to stock.
- **Complete Shopping Cart:** Add to cart, view total, and securely checkout.
- **Order Tracking Stepper:** An elegant visual progress tracker for active orders (Placed -> Processing -> Shipped -> Delivered).
- **User Dashboard:** A refined profile page displaying a beautiful layout of user details and order history.
- **Authentication:** Custom, aesthetically matching Registration and Login split-screen views.

## 💻 Tech Stack

- **Backend:** Django (Python)
- **Database:** SQLite
- **Frontend:** HTML, Vanilla CSS, Vanilla JavaScript
- **Containerization:** Docker & Docker Compose

## 🚀 Local Development Setup

To run this project locally using a virtual environment:

1. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Populate the database with sample products:**
   ```bash
   python populate_variants.py
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
   Navigate to `http://127.0.0.1:8000` in your browser.

## 🐳 Docker Setup

This project is fully dockerized for quick deployment and testing.

1. **Build and run the containers:**
   ```bash
   docker-compose up --build
   ```

2. **Access the application:**
   The site will be running on `http://localhost:8000`.

*Note: Since the database is stored via volume mounts or within the container, make sure to execute the `migrate` and `populate_variants.py` scripts inside the web container if you are starting entirely fresh inside Docker.*

## 🔑 Default Credentials

A default superuser is included in the current database for easy testing:
- **Username:** `admin`
- **Password:** `admin`

Access the Django Admin panel at `http://127.0.0.1:8000/admin/` to manage products, categories, variants, and orders.
