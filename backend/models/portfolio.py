from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional, Dict, Any
from datetime import datetime
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, handler=None):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, field_schema: Dict[str, Any]) -> Dict[str, Any]:
        field_schema.update(type="string")
        return field_schema

class MultiLanguageField(BaseModel):
    pt: str
    en: str

class ContactInfo(BaseModel):
    email: str
    linkedin: str
    github: str

class PersonalInfo(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str}
    )
    
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

class PersonalInfoUpdate(BaseModel):
    name: Optional[str] = None
    title: Optional[MultiLanguageField] = None
    subtitle: Optional[MultiLanguageField] = None
    description: Optional[MultiLanguageField] = None
    location: Optional[str] = None
    status: Optional[MultiLanguageField] = None
    contact: Optional[ContactInfo] = None

class Skill(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str}
    )
    
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    category: MultiLanguageField
    technologies: List[str]
    order: int = 0
    is_active: bool = True
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

class SkillCreate(BaseModel):
    category: MultiLanguageField
    technologies: List[str]
    order: int = 0

class SkillUpdate(BaseModel):
    category: Optional[MultiLanguageField] = None
    technologies: Optional[List[str]] = None
    order: Optional[int] = None
    is_active: Optional[bool] = None

class Education(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str}
    )
    
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    institution: str
    degree: MultiLanguageField
    period: str
    status: MultiLanguageField
    order: int = 0
    is_active: bool = True
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

class EducationCreate(BaseModel):
    institution: str
    degree: MultiLanguageField
    period: str
    status: MultiLanguageField
    order: int = 0

class EducationUpdate(BaseModel):
    institution: Optional[str] = None
    degree: Optional[MultiLanguageField] = None
    period: Optional[str] = None
    status: Optional[MultiLanguageField] = None
    order: Optional[int] = None
    is_active: Optional[bool] = None

class Project(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str}
    )
    
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
    title: Optional[MultiLanguageField] = None
    description: Optional[MultiLanguageField] = None
    technologies: Optional[List[str]] = None
    github_url: Optional[str] = None
    live_url: Optional[str] = None
    image_url: Optional[str] = None
    status: Optional[str] = None
    featured: Optional[bool] = None
    order: Optional[int] = None

class Goal(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str}
    )
    
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    goal: MultiLanguageField
    order: int = 0
    is_active: bool = True
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

class GoalCreate(BaseModel):
    goal: MultiLanguageField
    order: int = 0

class GoalUpdate(BaseModel):
    goal: Optional[MultiLanguageField] = None
    order: Optional[int] = None
    is_active: Optional[bool] = None

class CurrentLearning(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str}
    )
    
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    item: MultiLanguageField
    order: int = 0
    is_active: bool = True
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

class CurrentLearningCreate(BaseModel):
    item: MultiLanguageField
    order: int = 0

class CurrentLearningUpdate(BaseModel):
    item: Optional[MultiLanguageField] = None
    order: Optional[int] = None
    is_active: Optional[bool] = None

class PortfolioData(BaseModel):
    personal_info: PersonalInfo
    skills: List[Skill]
    education: List[Education]
    projects: List[Project]
    goals: List[Goal]
    current_learning: List[CurrentLearning]