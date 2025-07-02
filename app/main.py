"""
Main Portfolio Application
Creates the complete GenAI Engineer portfolio with all sections and demos.
"""

from nicegui import ui, app
from fastapi import FastAPI
from app.core.config import settings
from app.core.logging import app_logger
from app.components.layout import create_layout
from app.components.hero import create_hero_section
from app.components.about import create_about_section
from app.components.skills import create_skills_section
from app.components.projects import create_projects_section
from app.components.ai_demos import create_ai_demos_section
from app.components.blog import create_blog_section
from app.components.contact import create_contact_section
from app.api.router import api_router

def create_portfolio_app() -> FastAPI:
    """Create and configure the portfolio FastAPI application."""
    
    # Configure FastAPI app
    fastapi_app = app.fastapi
    fastapi_app.title = "GenAI Engineer Portfolio API"
    fastapi_app.description = "Backend API for the GenAI Engineer Portfolio"
    fastapi_app.version = "1.0.0"
    
    # Include API routes
    fastapi_app.include_router(api_router, prefix="/api")
    
    return fastapi_app

@ui.page('/')
def index():
    """Main portfolio page with all sections."""
    
    with create_layout():
        # Hero Section
        create_hero_section()
        
        # About Section
        create_about_section()
        
        # Skills Section
        create_skills_section()
        
        # Projects Section
        create_projects_section()
        
        # AI Demos Section
        create_ai_demos_section()
        
        # Blog Section
        create_blog_section()
        
        # Contact Section
        create_contact_section()

@ui.page('/project/{project_id}')
def project_detail(project_id: str):
    """Detailed project view."""
    from app.components.project_detail import create_project_detail
    
    with create_layout():
        create_project_detail(project_id)

@ui.page('/blog/{post_id}')
def blog_post(post_id: str):
    """Individual blog post view."""
    from app.components.blog_post import create_blog_post
    
    with create_layout():
        create_blog_post(post_id)

# Add custom CSS for professional styling
ui.add_head_html('''
<style>
    :root {
        --primary-color: #2563eb;
        --secondary-color: #1e40af;
        --accent-color: #3b82f6;
        --text-primary: #1f2937;
        --text-secondary: #6b7280;
        --bg-primary: #ffffff;
        --bg-secondary: #f8fafc;
        --border-color: #e5e7eb;
        --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        --shadow-lg: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
    }
    
    .hero-gradient {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .card-hover {
        transition: all 0.3s ease;
    }
    
    .card-hover:hover {
        transform: translateY(-5px);
        box-shadow: var(--shadow-lg);
    }
    
    .skill-bar {
        background: linear-gradient(90deg, var(--primary-color), var(--accent-color));
        border-radius: 10px;
        height: 8px;
    }
    
    .ai-demo-card {
        background: linear-gradient(145deg, #f0f9ff, #e0f2fe);
        border: 1px solid #0ea5e9;
    }
    
    .typing-animation {
        overflow: hidden;
        border-right: 2px solid var(--primary-color);
        white-space: nowrap;
        animation: typing 3.5s steps(40, end), blink-caret 0.75s step-end infinite;
    }
    
    @keyframes typing {
        from { width: 0 }
        to { width: 100% }
    }
    
    @keyframes blink-caret {
        from, to { border-color: transparent }
        50% { border-color: var(--primary-color) }
    }
    
    .floating-animation {
        animation: float 6s ease-in-out infinite;
    }
    
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
        100% { transform: translateY(0px); }
    }
</style>
''')