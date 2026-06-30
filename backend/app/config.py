from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://kua_user:kua_password@localhost:5432/ia_kua_kalianda"
    DEBUG: bool = True
    SECRET_KEY: str = "your-secret-key"
    
    class Config:
        env_file = ".env"

settings = Settings()
