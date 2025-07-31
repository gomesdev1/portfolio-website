from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from datetime import datetime
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class MultiLanguageField(BaseModel):
    pt: str
    en: str

class ContactInfo(BaseModel):
    email: str
    linkedin: str
    github: str

class PersonalInfo(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    name: str
    title: MultiLanguageField
    subtitle: MultiLanguageField
    description: MultiLanguageField
    location: str
    status: MultiLanguageField
    contact: ContactInfo
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class PersonalInfoUpdate(BaseModel):
    name: Optional[str]
    title: Optional[MultiLanguageField]
    subtitle: Optional[MultiLanguageField]
    description: Optional[MultiLanguageField]
    location: Optional[str]
    status: Optional[MultiLanguageField]
    contact: Optional[ContactInfo]

class Skill(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    category: MultiLanguageField
    technologies: List[str]
    order: int = 0
    is_active: bool = True
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class SkillCreate(BaseModel):
    category: MultiLanguageField
    technologies: List[str]
    order: int = 0

class SkillUpdate(BaseModel):
    category: Optional[MultiLanguageField]
    technologies: Optional[List[str]]
    order: Optional[int]
    is_active: Optional[bool]

class Education(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    institution: str
    degree: MultiLanguageField
    period: str
    status: MultiLanguageField
    order: int = 0
    is_active: bool = True
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class EducationCreate(BaseModel):
    institution: str
    degree: MultiLanguageField
    period: str
    status: MultiLanguageField
    order: int = 0

class EducationUpdate(BaseModel):
    institution: Optional[str]
    degree: Optional[MultiLanguageField]
    period: Optional[str]
    status: Optional[MultiLanguageField]
    order: Optional[int]
    is_active: Optional[bool]

class Project(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    title: MultiLanguageField
    description: MultiLanguageField
    technologies: List[str] = []
    github_url: Optional[str] = None
    live_url: Optional[str] = None
    image_url: Optional[str] = None
    status: str = "development"  # 'active', 'development', 'placeholder'
    featured: bool = False
    order: int = 0
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class ProjectCreate(BaseModel):
    title: MultiLanguageField
    description: MultiLanguageField
    technologies: List[str] = []
    github_url: Optional[str] = None
    live_url: Optional[str] = None
    image_url: Optional[str] = None
    status: str = "development"
    featured: bool = False
    order: int = 0

class ProjectUpdate(BaseModel):
    title: Optional[MultiLanguageField]
    description: Optional[MultiLanguageField]
    technologies: Optional[List[str]]
    github_url: Optional[str]
    live_url: Optional[str]
    image_url: Optional[str]
    status: Optional[str]
    featured: Optional[bool]
    order: Optional[int]

class Goal(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    goal: MultiLanguageField
    order: int = 0
    is_active: bool = True
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class GoalCreate(BaseModel):
    goal: MultiLanguageField
    order: int = 0

class GoalUpdate(BaseModel):
    goal: Optional[MultiLanguageField]
    order: Optional[int]
    is_active: Optional[bool]

class CurrentLearning(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    item: MultiLanguageField
    order: int = 0
    is_active: bool = True
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class CurrentLearningCreate(BaseModel):
    item: MultiLanguageField
    order: int = 0

class CurrentLearningUpdate(BaseModel):
    item: Optional[MultiLanguageField]
    order: Optional[int]
    is_active: Optional[bool]

class PortfolioData(BaseModel):
    personal_info: PersonalInfo
    skills: List[Skill]
    education: List[Education]
    projects: List[Project]
    goals: List[Goal]
    current_learning: List[CurrentLearning]