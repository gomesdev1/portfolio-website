from motor.motor_asyncio import AsyncIOMotorClient
from models.portfolio import (
    PersonalInfo, Skill, Education, Project, Goal, CurrentLearning,
    MultiLanguageField, ContactInfo
)
import os
import asyncio
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path

async def seed_database():
    """Seed database with initial portfolio data"""
    
    # Load environment variables
    ROOT_DIR = Path(__file__).parent
    load_dotenv(ROOT_DIR / '.env')
    
    # Database connection
    mongo_url = os.environ['MONGO_URL']
    db_name = os.environ['DB_NAME']
    client = AsyncIOMotorClient(mongo_url)
    db = client[db_name]
    
    print("🌱 Starting database seeding...")
    
    # Clear existing data
    collections = ['personal_info', 'skills', 'education', 'projects', 'goals', 'current_learning']
    for collection in collections:
        await db[collection].delete_many({})
        print(f"Cleared {collection} collection")
    
    # Seed Personal Info
    personal_info = PersonalInfo(
        name="Pedro Gomes",
        title=MultiLanguageField(
            pt="Desenvolvedor Fullstack Junior",
            en="Junior Fullstack Developer"
        ),
        subtitle=MultiLanguageField(
            pt="Estudante de Engenharia de Software",
            en="Software Engineering Student"
        ),
        description=MultiLanguageField(
            pt="Cursando Bacharelado em Engenharia de Software (1º semestre) na Universidade Anhaguera, com formação técnica em suporte de TI. Focado em Java, Spring Boot e tecnologias modernas.",
            en="Currently pursuing a Bachelor's degree in Software Engineering (1st semester) at Anhaguera University, with technical background in IT support. Focused on Java, Spring Boot and modern technologies."
        ),
        location="Brazil",
        status=MultiLanguageField(
            pt="Disponível para estágio",
            en="Available for internship"
        ),
        contact=ContactInfo(
            email="pedroballario@gmail.com",
            linkedin="https://www.linkedin.com/in/pedro-gomes-ba4825354",  
            github="https://github.com/gomesdev1"
        )
    )
    
    await db.personal_info.insert_one(personal_info.dict(by_alias=True, exclude={"id"}))
    print("✅ Personal info seeded")
    
    # Seed Skills
    skills_data = [
        {
            "category": MultiLanguageField(pt="Backend", en="Backend"),
            "technologies": ["Java", "Spring Boot", "MongoDB", "APIs REST", "Orientação a Objetos"],
            "order": 1
        },
        {
            "category": MultiLanguageField(pt="Frontend", en="Frontend"),
            "technologies": ["HTML", "CSS", "JavaScript", "React (aprendendo)"],
            "order": 2
        },
        {
            "category": MultiLanguageField(pt="Ferramentas", en="Tools"),
            "technologies": ["Git", "Linux", "Suporte Técnico", "Redes de Computadores"],
            "order": 3
        },
        {
            "category": MultiLanguageField(pt="Soft Skills", en="Soft Skills"),
            "technologies": ["Autodidata", "Dedicado", "Foco em Aprendizado", "Orientado a Detalhes"],
            "order": 4
        }
    ]
    
    for skill_data in skills_data:
        skill = Skill(**skill_data)
        await db.skills.insert_one(skill.dict(by_alias=True, exclude={"id"}))
    
    print("✅ Skills seeded")
    
    # Seed Education
    education_data = [
        {
            "institution": "Universidade Anhaguera",
            "degree": MultiLanguageField(
                pt="Bacharelado em Engenharia de Software",
                en="Bachelor's in Software Engineering"
            ),
            "period": "2024 - Em andamento",
            "status": MultiLanguageField(
                pt="1º Semestre",
                en="1st Semester"
            ),
            "order": 1
        },
        {
            "institution": "Formação Técnica",
            "degree": MultiLanguageField(
                pt="Suporte de TI",
                en="IT Support"
            ),
            "period": "Concluído",
            "status": MultiLanguageField(
                pt="Redes, Hardware, Software",
                en="Networks, Hardware, Software"
            ),
            "order": 2
        }
    ]
    
    for edu_data in education_data:
        education = Education(**edu_data)
        await db.education.insert_one(education.dict(by_alias=True, exclude={"id"}))
    
    print("✅ Education seeded")
    
    # Seed Projects (placeholder)
    project_data = {
        "title": MultiLanguageField(
            pt="EM DESENVOLVIMENTO",
            en="IN DEVELOPMENT"
        ),
        "description": MultiLanguageField(
            pt="Projetos serão adicionados conforme desenvolvimento",
            en="Projects will be added as development progresses"
        ),
        "technologies": [],
        "status": "placeholder",
        "order": 1
    }
    
    project = Project(**project_data)
    await db.projects.insert_one(project.dict(by_alias=True, exclude={"id"}))
    print("✅ Projects seeded")
    
    # Seed Goals
    goals_data = [
        {
            "goal": MultiLanguageField(
                pt="Conquistar primeira oportunidade de estágio",
                en="Secure first internship opportunity"
            ),
            "order": 1
        },
        {
            "goal": MultiLanguageField(
                pt="Evoluir como desenvolvedor de software",
                en="Evolve as a software developer"
            ),
            "order": 2
        },
        {
            "goal": MultiLanguageField(
                pt="Tornar-se engenheiro de software",
                en="Become a software engineer"
            ),
            "order": 3
        },
        {
            "goal": MultiLanguageField(
                pt="Dominar tecnologias fullstack",
                en="Master fullstack technologies"
            ),
            "order": 4
        }
    ]
    
    for goal_data in goals_data:
        goal = Goal(**goal_data)
        await db.goals.insert_one(goal.dict(by_alias=True, exclude={"id"}))
    
    print("✅ Goals seeded")
    
    # Seed Current Learning
    learning_data = [
        {
            "item": MultiLanguageField(
                pt="Curso Java com Spring Boot",
                en="Java course with Spring Boot"
            ),
            "order": 1
        },
        {
            "item": MultiLanguageField(
                pt="Desenvolvimento de APIs",
                en="API Development"
            ),
            "order": 2
        },
        {
            "item": MultiLanguageField(
                pt="MongoDB e NoSQL",
                en="MongoDB and NoSQL"
            ),
            "order": 3
        },
        {
            "item": MultiLanguageField(
                pt="Frontend com React",
                en="Frontend with React"
            ),
            "order": 4
        },
        {
            "item": MultiLanguageField(
                pt="Boas práticas de desenvolvimento",
                en="Development best practices"
            ),
            "order": 5
        }
    ]
    
    for learning_item in learning_data:
        current_learning = CurrentLearning(**learning_item)
        await db.current_learning.insert_one(current_learning.dict(by_alias=True, exclude={"id"}))
    
    print("✅ Current learning seeded")
    
    client.close()
    print("🎉 Database seeding completed successfully!")

if __name__ == "__main__":
    asyncio.run(seed_database())