# Setup Guide

## Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

## Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Database Setup
```bash
creatdb ia_kua_kalianda
```

## Docker
```bash
docker-compose up -d
```
