# KPA Form Data Project

A Django REST Framework project for saving and retrieving wheel and bogie form data, as per the KPA Form Data API specification.

## Tech Stack
- Python 3.x
- Django 5.x
- Django REST Framework
- PostgreSQL

## Setup Instructions
1. **Clone this repo**
2. **Create and activate a virtual environment**
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Create a PostgreSQL database** (e.g., `kpa_db`)
5. **Create a `.env` file** in the project root with:
   ```env
   DB_NAME=your_db_name
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=localhost
   DB_PORT=5432
   ```
6. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
7. **Start the server:**
   ```bash
   python manage.py runserver
   ```

## Implemented APIs

### 1. Wheel Specification
- **POST** `/api/forms/wheel-specifications/`  
  Create a new wheel specification form.
- **GET** `/api/forms/wheel-specifications/`  
  List/filter wheel specification forms.

### 2. Bogie Checksheet
- **POST** `/api/forms/bogie-checksheets/`  
  Create a new bogie checksheet form.
- **GET** `/api/forms/bogie-checksheets/`  
  List/filter bogie checksheet forms.


## Postman Collection
- Import the provided Postman collection (`Md_Sohail_Ali_postman_collection.json`) into Postman.
- Use the sample requests to test the APIs.

## Limitations & Assumptions
- No authentication is implemented (for demo purposes).
- Only basic validation is performed.


## Contact
For any queries, contact: sohailt7x@gmail.com 
