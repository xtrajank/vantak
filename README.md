# vantak
A full-stack platform that automates threat data ingestion, blocks IPs based on logic or ML scoring, and provides an interactive dashboard for Security Engineers.

# Key Features
- Data Ingestion
- Power BI Dashboard
- Automated Threat Response Module
- Optional: ML Add On

# Development Plan
## Tasks
### Phase 1: Core Arch & Setup
- Frontend/backend setup. Define core data models & routes
1. Backend setup
    - Create FastAPI app skeleton
    - Add .env config loading
    - Postgres, SQLAlchemy connection
2. Frontend setup
    - Scaffold React + Vite
    - Add Tailwind CSS and router
3. Dockerize
    - Write Dockerfile for backend
    - Add docker-compose.yaml (backend + db + redis + frontend)
5. Define base model
    - LogEvent: timestamp, IP, source, event type, severity
    - BlocklistEntry:L IP, blocked_by, reason, timestamp

### Phase 2: Ingestion & Storage
- Ingest mock data from logs/or REST API
- Store in db for analysis
1. Write Ingestion Script
    - Python fetch to log-like data
    - Normalize logs into a constistent schema
2. API Endpoint
    - "/logs/ingest" - accept JSON logs (for manual testing)
3. DB Logging
    - Store each log w source, IP, timestamp
4. Add unit tests
    - ingestion & db saving

### Phase 3: Frontend Visualization
- Display log events and key metrics on frontend
1. Create log viewer component
    - Table listing recent logs
    - Sort/filter by IP, severity
2. Add dashboard
    - count events
    - Bar chart: event type freq
    - Line chart: logs per hr/day
3. Connect to backend
    - Use axios to hit "/logs/recent", "/logs/stats"

### Phase 4: Threat Detection & IP Blocking Automation
- Implement scoring/heuristic logic for blocking IPs
- Automate updates to the blocklist
1. Detection logic
    - if x failed logins from same IP -> score increases
    - if in known blacklist -> flag
2. Blocking decision
    - score > threshold -> add to block list
    - provide "/blocklist" endpoint for viewing
3. Automate with Celery
    - periodic task checks new logs, score IPs
    - Add to blocklist if needed

### Phase 5: Manual Control & Audit UI
- Let user override blocks or approve threats
1. Add frontend controls
    - Manual block/unblock IP
    - View "pending threats" with scores
2. Backend routes
    - "/blocklist/manual-block"
    - "/blocklist/unblock"
3. Audit log
    - track who blocked what and when

### Phase 6: Finalization & Stretch Features
- Polish features, secure endpoints, add stretch goals
1. Security
    - Add basic auth to protect APIs
2. Alerting
    - Email notifications on critical events
3. Power BI Connector
    - Sync PostgresSQL w Power BI
4. Documentation
    - Update README, diagrams, setup instructions


## Tools/Frameworks
### Backend
- Python
- FastAPI
- OAuth
- PostgresSQL
- Pandas
- Redis
- httpx
- SciKit-learn
- python-dotenv

### Frontend
- React + Vite
- Tailwind CSS
- Material UI
- Chart.js

## Project Structure
### backend
- requirements.txt
- .env
- Dockerfile
#### app
- __init__.py
- main.py (FastAPI app)
##### api
- __init__.py
- routes.py (Endpoint definitions)
##### core
- config.py (env loading, app settings)
- security.py (auth, token logic)
##### services
- ingestion.py (pulls from REST API/mock logs)
- detection.py (scoring or heuristic rules)
- blocklist.py (IP blocking logic)
##### models
- log_event.py (pydantic schemas for input/output)
##### db
- base.py
- session.py
- models.py (SQLAlchemy models)
##### tasks
- scheduler.py (cron jobs / periodic pull)
- ip_blocker.py (async IP blocking task)
#### tests
- test_ingestion.py
- test_detection.py
### frontend
- tailwind.config.js
- vite.config.js
- package.json
#### public
#### src
- App.jsx
- main.jsx
##### components
- Dashboard.jsx (Charts, tables)
- LogViewer.jsx (Raw log view)
- IPControl.jsx (Manual IP blocking/unblocking)
##### pages
- Home.jsx
- Logs.jsx
##### services
- api.js (axios/fetch wrappers for API calls)