from fastapi import APIRouter, HTTPException, status
from motor.motor_asyncio import AsyncIOMotorClient
from models.portfolio import (
    PersonalInfo, PersonalInfoUpdate,
    Skill, SkillCreate, SkillUpdate,
    Education, EducationCreate, EducationUpdate,
    Project, ProjectCreate, ProjectUpdate,
    Goal, GoalCreate, GoalUpdate,
    CurrentLearning, CurrentLearningCreate, CurrentLearningUpdate,
    PortfolioData
)
from typing import List
from bson import ObjectId
import os
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path

router = APIRouter()

# Load environment variables
ROOT_DIR = Path(__file__).parent.parent
load_dotenv(ROOT_DIR / '.env')

# Database connection
mongo_url = os.environ.get('MONGO_URL')
db_name = os.environ.get('DB_NAME')
if not mongo_url or not db_name:
    raise RuntimeError("MONGO_URL e DB_NAME devem estar definidos no .env")

client = AsyncIOMotorClient(mongo_url)
db = client[db_name]

def object_id_str(obj):
    """Convert ObjectId to string for JSON serialization"""
    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, ObjectId):
                obj[key] = str(value)
            elif isinstance(value, dict):
                object_id_str(value)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        object_id_str(item)
    elif isinstance(obj, list):
        for item in obj:
            if isinstance(item, dict):
                object_id_str(item)
    return obj

# Personal Info Routes
@router.get("/personal-info", response_model=PersonalInfo)
async def get_personal_info():
    """Get personal information"""
    try:
        personal_info = await db.personal_info.find_one()
        if not personal_info:
            raise HTTPException(status_code=404, detail="Personal info not found")
        personal_info = object_id_str(personal_info)
        return PersonalInfo(**personal_info)
    except Exception:
        raise HTTPException(status_code=500, detail="Database error")

@router.put("/personal-info", response_model=PersonalInfo)
async def update_personal_info(personal_info_update: PersonalInfoUpdate):
    """Update personal information"""
    try:
        update_data = personal_info_update.dict(exclude_unset=True)
        update_data["updated_at"] = datetime.utcnow()
        result = await db.personal_info.update_one(
            {},
            {"$set": update_data}
        )
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Personal info not found")
        updated_info = await db.personal_info.find_one()
        updated_info = object_id_str(updated_info)
        return PersonalInfo(**updated_info)
    except Exception:
        raise HTTPException(status_code=500, detail="Database error")

# Skills Routes
@router.get("/skills", response_model=List[Skill])
async def get_skills():
    """Get all active skills ordered"""
    try:
        skills_cursor = db.skills.find({"is_active": True}).sort("order", 1)
        skills = await skills_cursor.to_list(length=None)
        return [Skill(**object_id_str(skill)) for skill in skills]
    except Exception:
        raise HTTPException(status_code=500, detail="Database error")

@router.post("/skills", response_model=Skill)
async def create_skill(skill_data: SkillCreate):
    """Create new skill"""
    try:
        skill = Skill(**skill_data.dict())
        result = await db.skills.insert_one(skill.dict(by_alias=True, exclude={"id"}))
        created_skill = await db.skills.find_one({"_id": result.inserted_id})
        created_skill = object_id_str(created_skill)
        return Skill(**created_skill)
    except Exception:
        raise HTTPException(status_code=500, detail="Database error")

@router.put("/skills/{skill_id}", response_model=Skill)
async def update_skill(skill_id: str, skill_update: SkillUpdate):
    """Update skill"""
    try:
        if not ObjectId.is_valid(skill_id):
            raise HTTPException(status_code=400, detail="Invalid skill ID")
        update_data = skill_update.dict(exclude_unset=True)
        update_data["updated_at"] = datetime.utcnow()
        result = await db.skills.update_one(
            {"_id": ObjectId(skill_id)},
            {"$set": update_data}
        )
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Skill not found")
        updated_skill = await db.skills.find_one({"_id": ObjectId(skill_id)})
        updated_skill = object_id_str(updated_skill)
        return Skill(**updated_skill)
    except Exception:
        raise HTTPException(status_code=500, detail="Database error")

@router.delete("/skills/{skill_id}")
async def delete_skill(skill_id: str):
    """Delete skill"""
    try:
        if not ObjectId.is_valid(skill_id):
            raise HTTPException(status_code=400, detail="Invalid skill ID")
        result = await db.skills.delete_one({"_id": ObjectId(skill_id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Skill not found")
        return {"message": "Skill deleted successfully"}
    except Exception:
        raise HTTPException(status_code=500, detail="Database error")

# Education Routes
@router.get("/education", response_model=List[Education])
async def get_education():
    """Get all active education ordered"""
    try:
        education_cursor = db.education.find({"is_active": True}).sort("order", 1)
        education = await education_cursor.to_list(length=None)
        return [Education(**object_id_str(edu)) for edu in education]
    except Exception:
        raise HTTPException(status_code=500, detail="Database error")

@router.post("/education", response_model=Education)
async def create_education(education_data: EducationCreate):
    """Create new education"""
    try:
        education = Education(**education_data.dict())
        result = await db.education.insert_one(education.dict(by_alias=True, exclude={"id"}))
        created_education = await db.education.find_one({"_id": result.inserted_id})
        created_education = object_id_str(created_education)
        return Education(**created_education)
    except Exception:
        raise HTTPException(status_code=500, detail="Database error")

# Projects Routes
@router.get("/projects", response_model=List[Project])
async def get_projects():
    """Get all projects ordered"""
    try:
        projects_cursor = db.projects.find().sort("order", 1)
        projects = await projects_cursor.to_list(length=None)
        return [Project(**object_id_str(project)) for project in projects]
    except Exception:
        raise HTTPException(status_code=500, detail="Database error")

@router.get("/projects/featured", response_model=List[Project])
async def get_featured_projects():
    """Get featured projects"""
    try:
        projects_cursor = db.projects.find({"featured": True}).sort("order", 1)
        projects = await projects_cursor.to_list(length=None)
        return [Project(**object_id_str(project)) for project in projects]
    except Exception:
        raise HTTPException(status_code=500, detail="Database error")

@router.post("/projects", response_model=Project)
async def create_project(project_data: ProjectCreate):
    """Create new project"""
    try:
        project = Project(**project_data.dict())
        result = await db.projects.insert_one(project.dict(by_alias=True, exclude={"id"}))
        created_project = await db.projects.find_one({"_id": result.inserted_id})
        created_project = object_id_str(created_project)
        return Project(**created_project)
    except Exception:
        raise HTTPException(status_code=500, detail="Database error")

# Goals Routes
@router.get("/goals", response_model=List[Goal])
async def get_goals():
    """Get all active goals ordered"""
    try:
        goals_cursor = db.goals.find({"is_active": True}).sort("order", 1)
        goals = await goals_cursor.to_list(length=None)
        return [Goal(**object_id_str(goal)) for goal in goals]
    except Exception:
        raise HTTPException(status_code=500, detail="Database error")

@router.post("/goals", response_model=Goal)
async def create_goal(goal_data: GoalCreate):
    """Create new goal"""
    try:
        goal = Goal(**goal_data.dict())
        result = await db.goals.insert_one(goal.dict(by_alias=True, exclude={"id"}))
        created_goal = await db.goals.find_one({"_id": result.inserted_id})
        created_goal = object_id_str(created_goal)
        return Goal(**created_goal)
    except Exception:
        raise HTTPException(status_code=500, detail="Database error")

# Current Learning Routes
@router.get("/current-learning", response_model=List[CurrentLearning])
async def get_current_learning():
    """Get all active current learning items ordered"""
    try:
        learning_cursor = db.current_learning.find({"is_active": True}).sort("order", 1)
        learning = await learning_cursor.to_list(length=None)
        return [CurrentLearning(**object_id_str(item)) for item in learning]
    except Exception:
        raise HTTPException(status_code=500, detail="Database error")

@router.post("/current-learning", response_model=CurrentLearning)
async def create_current_learning(learning_data: CurrentLearningCreate):
    """Create new current learning item"""
    try:
        learning = CurrentLearning(**learning_data.dict())
        result = await db.current_learning.insert_one(learning.dict(by_alias=True, exclude={"id"}))
        created_learning = await db.current_learning.find_one({"_id": result.inserted_id})
        created_learning = object_id_str(created_learning)
        return CurrentLearning(**created_learning)
    except Exception:
        raise HTTPException(status_code=500, detail="Database error")

# Portfolio Data (Aggregate)
@router.get("/portfolio")
async def get_portfolio_data():
    """Get all portfolio data in one call"""
    try:
        personal_info = await db.personal_info.find_one()
        skills_cursor = db.skills.find({"is_active": True}).sort("order", 1)
        skills = await skills_cursor.to_list(length=None)
        education_cursor = db.education.find({"is_active": True}).sort("order", 1)
        education = await education_cursor.to_list(length=None)
        projects_cursor = db.projects.find().sort("order", 1)
        projects = await projects_cursor.to_list(length=None)
        goals_cursor = db.goals.find({"is_active": True}).sort("order", 1)
        goals = await goals_cursor.to_list(length=None)
        learning_cursor = db.current_learning.find({"is_active": True}).sort("order", 1)
        current_learning = await learning_cursor.to_list(length=None)
        if not personal_info:
            raise HTTPException(status_code=404, detail="Personal info not found")
        portfolio_data = {
            "personal_info": object_id_str(personal_info),
            "skills": [object_id_str(skill) for skill in skills],
            "education": [object_id_str(edu) for edu in education],
            "projects": [object_id_str(project) for project in projects],
            "goals": [object_id_str(goal) for goal in goals],
            "current_learning": [object_id_str(item) for item in current_learning]
        }
        return {
            "success": True,
            "data": portfolio_data
        }
    except Exception:
        raise HTTPException(status_code=500, detail="Database error")