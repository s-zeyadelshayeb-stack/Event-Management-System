# Phase 4 — Core Functionality Prototype — Progress Report
**Course:** CSAI 203 — Fall 2025  
**Team:** Zeyad, Retaj, Sara, Ameer  
**Date:** 2025-12-07

---

## 1. Executive Summary
This deliverable contains the team's Phase 4 prototype: core features implemented (~50%). The project is a simple Event Management System (EMS). The prototype includes user authentication, events listing and details, registration, and feedback submission.

## 2. Mapping to SRS (summary)
- **User Authentication (SRS §2.x):** Signup, login, logout — *Completed* (Retaj).
- **Event CRUD (SRS §3.x):** Create, Read implemented; Update partial; Delete pending — *Partial* (Zeyad).
- **Registration (SRS §4.x):** Register/unregister to events — *Completed* (Sara).
- **Feedback (SRS §5.x):** Submit and view feedback per event — *Completed* (Ameer).

## 3. Completed features (detailed)
### Auth (branch: `feature/retaj-auth`) — Retaj
- Files: `src/controllers/auth_controller.py`, `src/repositories/user_repo.py`, `templates/login.html`, `templates/signup.html`
- How to test: run `init_db.py`, open `/signup` → create user → `/login` → redirect to dashboard.

### Events (branch: `feature/zeyad-events`) — Zeyad
- Files: `src/controllers/event_controller.py`, `src/repositories/event_repo.py`, `templates/dashboard.html`, `templates/event_detail.html`
- How to test: login → `/dashboard` → create/view event.

### Registration (branch: `feature/sara-registration`) — Sara
- Files: `src/controllers/registration_controller.py`, `src/repositories/registration_repo.py`
- How to test: open event detail → click Register → check registrations table.

### Feedback (branch: `feature/ameer-feedback`) — Ameer
- Files: `src/controllers/feedback_controller.py`, `src/repositories/feedback_repo.py`, `templates/event_detail.html`
- How to test: open event detail → submit feedback → feedback appears below.

_Note:_ Replace branch names and file lists with exact ones if different.

## 4. Database schema (summary)
Main tables (SQLite):
Seed / init: `python init_db.py` creates schema and sample data.

## 5. How to run locally (environment)
1. `python -m venv venv`  
2. `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Linux/Mac)  
3. `pip install -r requirements.txt`  
4. `python init_db.py`  
5. `python app.py` → open `http://127.0.0.1:5000`

## 6. Testing checklist (what we tested)
- [x] Signup (valid/duplicate email)
- [x] Login (correct/incorrect password)
- [x] Dashboard events listing
- [x] Event detail view
- [x] Register for event
- [x] Submit feedback

## 7. Pending work (short)
- Delete event endpoint (organizer) — ETA 2 days
- Better validation & error handling — ETA 3 days
- Unit tests (basic) — ETA 4 days

## 8. Contributions summary (short)
See `contribution_summary.md` for detailed commit counts and PR links.

## 9. Screenshots
See `deliverables/phase4/screens/` for four UI images: `login.png`, `signup.png`, `dashboard.png`, `event_detail.png`.

---

Prepared by: Zeyad (on behalf of team)
