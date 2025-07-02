"""API router for the portfolio application."""

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr
from typing import List, Optional
import time
from app.core.logging import app_logger

api_router = APIRouter()

# Pydantic models for API
class ContactMessage(BaseModel):
    name: str
    email: EmailStr
    company: Optional[str] = None
    subject: str
    message: str

class ProjectResponse(BaseModel):
    id: str
    title: str
    description: str
    tech_stack: List[str]
    category: str
    github_url: str
    demo_url: str

class SkillResponse(BaseModel):
    name: str
    category: str
    proficiency: int

# Contact endpoint
@api_router.post("/contact")
async def submit_contact_form(contact: ContactMessage):
    """Submit contact form."""
    try:
        app_logger.info(f"Contact form submission from {contact.email}")
        
        # In a real implementation, this would:
        # 1. Validate the data
        # 2. Send email notification
        # 3. Store in database
        # 4. Send confirmation email
        
        # Simulate processing time
        import asyncio
        await asyncio.sleep(1)
        
        return JSONResponse(
            content={
                "status": "success",
                "message": "Thank you for your message! I'll get back to you soon.",
                "timestamp": time.time()
            }
        )
    except Exception as e:
        app_logger.error(f"Error processing contact form: {e}")
        raise HTTPException(status_code=500, detail="Failed to send message")

# Projects endpoint
@api_router.get("/projects", response_model=List[ProjectResponse])
async def get_projects():
    """Get all projects."""
    try:
        # Mock project data
        projects = [
            {
                "id": "intelligent-chatbot",
                "title": "Intelligent Customer Service Chatbot",
                "description": "Enterprise-grade chatbot powered by GPT-4 with RAG capabilities",
                "tech_stack": ["GPT-4", "LangChain", "Pinecone", "FastAPI", "React"],
                "category": "NLP",
                "github_url": "https://github.com/genai-engineer/intelligent-chatbot",
                "demo_url": "https://demo.chatbot.com"
            },
            {
                "id": "content-generator",
                "title": "AI Content Generation Platform",
                "description": "Multi-modal content creation platform for marketing teams",
                "tech_stack": ["GPT-4", "DALL-E 3", "Stable Diffusion", "Python", "Vue.js"],
                "category": "Multimodal",
                "github_url": "https://github.com/genai-engineer/content-generator",
                "demo_url": "https://demo.contentgen.com"
            }
        ]
        
        return projects
    except Exception as e:
        app_logger.error(f"Error fetching projects: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch projects")

# Skills endpoint
@api_router.get("/skills", response_model=List[SkillResponse])
async def get_skills():
    """Get all skills."""
    try:
        skills = [
            {"name": "Large Language Models", "category": "Generative AI", "proficiency": 95},
            {"name": "Prompt Engineering", "category": "Generative AI", "proficiency": 90},
            {"name": "LangChain", "category": "AI Frameworks", "proficiency": 92},
            {"name": "Python", "category": "Programming", "proficiency": 95},
            {"name": "FastAPI", "category": "Web Development", "proficiency": 88}
        ]
        
        return skills
    except Exception as e:
        app_logger.error(f"Error fetching skills: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch skills")

# Health check endpoint
@api_router.get("/health")
async def health_check():
    """Health check endpoint."""
    return JSONResponse(
        content={
            "status": "healthy",
            "timestamp": time.time(),
            "service": "GenAI Portfolio API"
        }
    )

# AI demo endpoints
@api_router.post("/ai/text-generation")
async def generate_text(prompt: str, style: str = "creative", length: str = "medium"):
    """Generate text using AI (demo endpoint)."""
    try:
        # Simulate AI text generation
        import asyncio
        await asyncio.sleep(2)
        
        mock_response = f"""Generated text based on prompt: "{prompt[:50]}..."

Style: {style.title()}
Length: {length.title()}

This is a demonstration of AI text generation capabilities. In a real implementation, this would connect to actual language models like GPT-4, Claude, or local models.

Key features demonstrated:
✓ Context-aware generation
✓ Style customization  
✓ Length control
✓ Real-time processing"""
        
        return JSONResponse(content={"generated_text": mock_response})
    except Exception as e:
        app_logger.error(f"Error in text generation: {e}")
        raise HTTPException(status_code=500, detail="Text generation failed")

@api_router.post("/ai/chat")
async def chat_with_ai(message: str):
    """Chat with AI assistant (demo endpoint)."""
    try:
        # Simulate AI chat response
        import asyncio
        await asyncio.sleep(1.5)
        
        responses = [
            "That's an interesting question! In a real implementation, I would use advanced language models to provide helpful responses.",
            "I understand what you're asking. This demo showcases how AI chat systems can maintain context and provide relevant responses.",
            "Great point! AI assistants can help with various tasks including answering questions and providing explanations.",
            "Thanks for trying this demo! Real AI systems use sophisticated NLP models for natural conversations."
        ]
        
        import random
        response = random.choice(responses)
        
        return JSONResponse(content={"response": response})
    except Exception as e:
        app_logger.error(f"Error in chat: {e}")
        raise HTTPException(status_code=500, detail="Chat failed")