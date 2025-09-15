from pydantic import BaseModel, EmailStr
class Profile(BaseModel):
    userID: str
    resume: str
    linkedin: EmailStr | None = None
    github: str | None = None
    portfolio: str | None = None
    skills: list[str] | None = []
    experience: list[dict] | None = []
    education: list[dict] | None = []
    projects: list[dict] | None = []
    certifications: list[dict] | None = []
    achievements: list[str] | None = []
    interests: list[str] | None = []
    languages: list[str] | None = []
    references: list[dict] | None = []
    summary: str | None = None
    created_at: str | None = None
    updated_at: str | None = None
    