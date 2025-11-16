"""
Database Schemas for IFMSA Local Committee Website

Each Pydantic model represents a collection in MongoDB.
Collection name will be the lowercase of the class name (by convention in this project).
"""
from typing import List, Optional
from pydantic import BaseModel, Field, HttpUrl, EmailStr


class Committee(BaseModel):
    name: str = Field(..., description="Committee name e.g., SCORA, SCOPH")
    color: str = Field(..., description="Hex color e.g., #FF3B30")
    icon: str = Field(..., description="Lucide icon name to render on frontend")
    summary: str = Field(..., description="One-line summary of what they do")
    description: Optional[str] = Field(None, description="Longer description")
    annual_campaigns: List[str] = Field(default_factory=list)
    how_to_join: Optional[str] = None


class Project(BaseModel):
    title: str
    description: str
    images: List[HttpUrl] = Field(default_factory=list)
    impact_numbers: Optional[str] = Field(None, description="e.g., Reached 500 students")
    committee: Optional[str] = Field(None, description="Associated committee code e.g., SCOPH")
    year: Optional[int] = None


class TeamMember(BaseModel):
    name: str
    role: str
    bio: Optional[str] = None
    photo_url: Optional[HttpUrl] = None
    email: Optional[EmailStr] = None


class Post(BaseModel):
    title: str
    summary: str
    content: str
    image: Optional[HttpUrl] = None
    tags: List[str] = Field(default_factory=list)
    author: Optional[str] = None


class Partner(BaseModel):
    name: str
    logo: Optional[HttpUrl] = None
    description: Optional[str] = None
    website: Optional[HttpUrl] = None
    category: Optional[str] = Field(None, description="University, Hospital, NGO, Academic, Sponsor")


class Opportunity(BaseModel):
    title: str
    description: str
    category: str = Field(..., description="Local or National")
    link: Optional[HttpUrl] = None


class ContactMessage(BaseModel):
    name: str
    email: EmailStr
    subject: str
    message: str
