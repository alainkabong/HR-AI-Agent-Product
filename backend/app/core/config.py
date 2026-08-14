import os
from dotenv import load_dotenv
load_dotenv()

class Settings:
    APP_NAME: str=os.getenv("APP_NAME", "HR AI Agent Backend")
    APP_ENV: str=os.getenv("APP_ENV", "development")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./hr_ai_agent.db")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    AI_PROVIDER: str = os.getenv("AI_PROVIDER", "openai")
    EMAIL_HOST: str = os.getenv("EMAIL_HOST", "smtp.gmail.com")
    EMAIL_PORT: int = int(os.getenv("EMAIL_PORT", "587"))
    EMAIL_USERNAME: str=os.getenv("EMAIL_USERNAME", "")
    EMAIL_PASSWORD: str=os.getenv("EMAIL_PASSWORD", "")
    EMAIL_FROM: str=os.getenv("EMAIL_FROM", "")
    SECRET_KEY: str=os.getenv("SECRET_KEY", "any_secret_key")
    ACCESS_TAKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TAKEN_EXPIRE_MINUTES", "60"))
    

settings = Settings()