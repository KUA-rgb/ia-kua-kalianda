# Database Schema

## Tables

### users
- id (SERIAL PRIMARY KEY)
- username (VARCHAR UNIQUE)
- email (VARCHAR UNIQUE)
- password_hash (VARCHAR)
- created_at (TIMESTAMP)

### nikah
- id (SERIAL PRIMARY KEY)
- nomor_akta (VARCHAR)
- nama_pengantin_pria (VARCHAR)
- nama_pengantin_wanita (VARCHAR)
- tanggal_nikah (DATE)
- created_at (TIMESTAMP)

### cerai
- id (SERIAL PRIMARY KEY)
- nomor_akta (VARCHAR)
- nama_suami (VARCHAR)
- nama_istri (VARCHAR)
- tanggal_cerai (DATE)
- created_at (TIMESTAMP)

### rujuk
- id (SERIAL PRIMARY KEY)
- nomor_akta (VARCHAR)
- nama_suami (VARCHAR)
- nama_istri (VARCHAR)
- tanggal_rujuk (DATE)
- created_at (TIMESTAMP)
