🏥 Healthcare Backend API

A Django REST API for managing patients, doctors, and their mappings in a healthcare system.

🚀 Features

User Registration (/api/auth/register/)

Patients API → CRUD operations

Doctors API → CRUD operations

Patient–Doctor Mappings API → create, fetch, delete mappings

Admin Panel at /admin/

⚙️ Setup
# 1. Create virtual environment
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run migrations
python manage.py migrate

# 4. Start server
python manage.py runserver


Server runs at:

http://127.0.0.1:8000/

🌐 API Endpoints
Authentication

POST /api/auth/register/

Patients

GET /api/patients/

POST /api/patients/

GET /api/patients/{id}/

PUT /api/patients/{id}/

Doctors

GET /api/doctors/

POST /api/doctors/

GET /api/doctors/{id}/

PUT /api/doctors/{id}/

Mappings

GET /api/mappings/

POST /api/mappings/

GET /api/mappings/{patient_id}/

DELETE /api/mappings/{patient_id}/

