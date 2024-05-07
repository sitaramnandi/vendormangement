# Vendor Management System

The Vendor Management System is a Django-based application that allows you to manage vendor profiles, track purchase orders, and calculate vendor performance metrics. The system provides RESTful API endpoints and uses token-based authentication for security.

## Features

- **Vendor Profile Management**: Create, update, and delete vendor profiles.
- **Purchase Order Tracking**: Manage purchase orders, including creation, retrieval, and updates.
- **Vendor Performance Metrics**: Retrieve vendor performance metrics, such as on-time delivery rate, quality rating average, average response time, and fulfillment rate.
- **Token-Based Authentication**: Secure API endpoints with token-based authentication using JSON Web Tokens (JWT).
- **Real-time Updates**: Django signals are used to trigger real-time updates when relevant data changes.

## Installation and Setup

1. **Clone the Repository**: Clone the project repository to your local machine.
   ```bash
   git clone https://github.com/sitaramnandi/new.git
   cd VendorManagement

2-Set Up a Virtual Environment: Create and activate a virtual environment.
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

3-Install Dependencies: Install Django, Django REST Framework, and other required packages.
pip install -r requirements.txt
4-Apply Migrations: Run migrations to set up the database schema.
python manage.py makemigrations
python manage.py migrate
5-Create a Superuser: Create an admin account to access the Django admin panel.
python manage.py createsuperuser
7-Run the Development Server: Start the Django development server.
python manage.py runserver

API Endpoints
Vendor Endpoints
GET http://127.0.0.1:8000/api/vendors/: List all vendors.
POST http://127.0.0.1:8000/api/vendors/ Create a new vendor.
GET http://127.0.0.1:8000/api/vendors/{vendor_id}/: Retrieve a specific vendor's details.
PUT http://127.0.0.1:8000/api/vendors/{vendor_id}/: Update a vendor's details.
DELETE http://127.0.0.1:8000/api/vendors/{vendor_id}/: Delete a vendor.
GET http://127.0.0.1:8000/api/vendors/{vendor_id}/performance/: Retrieve a vendor's performance metrics.
Purchase Order Endpoints
GET http://127.0.0.1:8000/api/purchase_orders/: List all purchase orders.
POST http://127.0.0.1:8000/api/purchase_orders/: Create a new purchase order.
GET http://127.0.0.1:8000/api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
PUT http://127.0.0.1:8000/api/purchase_orders/{po_id}/: Update a purchase order.
DELETE http://127.0.0.1:8000/api/purchase_orders/{po_id}/: Delete a purchase order.
POST http://127.0.0.1:8000/api/purchase_orders/{po_id}/acknowledge/: Acknowledge a purchase order.
Token-Based Authentication Endpoints
POST http://127.0.0.1:8000/api/token/: Obtain a JWT token by providing valid credentials.
POST http://127.0.0.1:8000/api/token/refresh/: Refresh a JWT token when it expires.
