# MVC Description — Event Management System (Phase 4)

## Model (Data layer)
**Location:** `src/repositories/`  
**Responsibilities:** database access (CRUD), queries and returned DTOs.
- `user_repo.py` — user create/get/update
- `event_repo.py` — event create/get/update/list
- `registration_repo.py` — register/unregister
- `feedback_repo.py` — store/list feedback

## View (Presentation layer)
**Location:** `src/templates/` and `static/`  
**Responsibilities:** HTML templates rendered by controllers.
- `base.html` — site layout, navigation, flash
- `login.html`, `signup.html` — auth views
- `dashboard.html` — events listing
- `event_detail.html` — event info, register, feedback

## Controller (Application layer)
**Location:** `src/controllers/` (Flask blueprints)  
**Responsibilities:** handle HTTP requests, validation, call Model, choose View.
- `auth_controller.py` — signup/login/logout endpoints
- `event_controller.py` — event creation, edit, view
- `registration_controller.py` — register endpoint
- `feedback_controller.py` — feedback endpoint
- `main.py` — dashboard route / app glue

## Example flow: Register to event
1. Client clicks Register on `event_detail.html` → POST to `/events/<id>/register`  
2. `registration_controller` checks session → calls `registration_repo.create(user_id, event_id)`  
3. Repo writes DB → controller flashes success → redirect to `/events/<id>` where view reads registrations and shows updated list.

