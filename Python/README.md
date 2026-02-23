# 🚀 User Profile Register — Two-Tier DevOps App

## Architecture

```
┌──────────────────────────────────┐     ┌──────────────────────┐
│        TIER 1: App Container     │     │  TIER 2: DB Container │
│                                  │     │                       │
│  ┌─────────────┐  ┌───────────┐  │     │   ┌───────────────┐   │
│  │  HTML/CSS   │  │   Flask   │  │────▶│   │   MySQL 8.0   │   │
│  │  Frontend   │  │  Backend  │  │     │   │  (Port 3306)  │   │
│  └─────────────┘  └───────────┘  │     │   └───────────────┘   │
│       Port 5000 exposed          │     │   Internal only       │
└──────────────────────────────────┘     └──────────────────────┘
         flask_app container                  mysql_db container
                    └──────── two_tier_net ──────────┘
```

## Quick Start (Docker Compose)

```bash
# Clone / navigate to project folder
cd user-profile-app

# Build and run both tiers
docker-compose up --build

# App will be live at:
http://localhost:5000
```

## Run Locally (Without Docker)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set environment variables
export DB_HOST=localhost
export DB_USER=your_user
export DB_PASSWORD=your_password
export DB_NAME=userprofiles

# 3. Run app
python app.py
```

## API Endpoints

| Method | Endpoint      | Description              |
|--------|---------------|--------------------------|
| GET    | `/`           | Main UI (Form page)      |
| POST   | `/api/submit` | Save user profile        |
| GET    | `/api/users`  | Fetch recent 20 profiles |

## Environment Variables

| Variable    | Default      | Description       |
|-------------|--------------|-------------------|
| DB_HOST     | mysql        | MySQL host        |
| DB_PORT     | 3306         | MySQL port        |
| DB_USER     | appuser      | MySQL username    |
| DB_PASSWORD | apppassword  | MySQL password    |
| DB_NAME     | userprofiles | Database name     |

## Files

```
user-profile-app/
├── app.py               ← Flask backend
├── templates/
│   └── index.html       ← Frontend (HTML + CSS + JS)
├── requirements.txt     ← Python dependencies
├── Dockerfile           ← App container
├── docker-compose.yml   ← Two-tier orchestration
└── README.md
```
