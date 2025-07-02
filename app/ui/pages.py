"""
Portfolio pages and navigation for the GenAI Portfolio application.
Creates the main UI structure and page routing.
"""

from nicegui import ui
from typing import Dict, List, Any
from app.core import app_logger, settings
from app.ui.components import (
    create_header, create_card, create_skill_badge, 
    create_project_card, create_contact_form, 
    create_ai_demo_section, create_stats_grid
)

def create_portfolio_pages():
    """Create all portfolio pages and navigation."""
    
    # Navigation setup
    @ui.page('/')
    def home_page():
        create_home_page()
    
    @ui.page('/about')
    def about_page():
        create_about_page()
    
    @ui.page('/projects')
    def projects_page():
        create_projects_page()
    
    @ui.page('/skills')
    def skills_page():
        create_skills_page()
    
    @ui.page('/demos')
    def demos_page():
        create_demos_page()
    
    @ui.page('/contact')
    def contact_page():
        create_contact_page()
    
    app_logger.info("Portfolio pages created successfully")

def create_navigation():
    """Create the main navigation menu."""
    with ui.header().classes('bg-white shadow-sm border-b'):
        with ui.element('div').classes('container mx-auto px-4'):
            with ui.element('nav').classes('flex items-center justify-between h-16'):
                # Logo/Brand
                ui.link(settings.APP_NAME, '/').classes('text-xl font-bold text-blue-600 no-underline')
                
                # Navigation links
                with ui.element('div').classes('hidden md:flex space-x-6'):
                    ui.link('Home', '/').classes('text-gray-700 hover:text-blue-600 no-underline')
                    ui.link('About', '/about').classes('text-gray-700 hover:text-blue-600 no-underline')
                    ui.link('Projects', '/projects').classes('text-gray-700 hover:text-blue-600 no-underline')
                    ui.link('Skills', '/skills').classes('text-gray-700 hover:text-blue-600 no-underline')
                    ui.link('AI Demos', '/demos').classes('text-gray-700 hover:text-blue-600 no-underline')
                    ui.link('Contact', '/contact').classes('text-gray-700 hover:text-blue-600 no-underline')

def create_home_page():
    """Create the home page content."""
    create_navigation()
    
    with ui.element('div').classes('container mx-auto px-4 py-8'):
        # Hero section
        create_header(
            "GenAI Engineer",
            "Transforming businesses with cutting-edge Generative AI solutions"
        )
        
        # Stats section
        stats = [
            {"value": "50+", "label": "AI Projects", "description": "Delivered successfully"},
            {"value": "95%", "label": "Client Satisfaction", "description": "Consistent excellence"},
            {"value": "3+", "label": "Years Experience", "description": "In Generative AI"},
            {"value": "24/7", "label": "Support", "description": "Always available"}
        ]
        create_stats_grid(stats)
        
        # Introduction section
        with ui.element('div').classes('grid md:grid-cols-2 gap-8 mb-8'):
            create_card("About Me", lambda: ui.markdown("""
            I'm a passionate **Generative AI Engineer** specializing in building intelligent systems that solve real-world problems. With expertise in Large Language Models, prompt engineering, and AI application development, I help businesses harness the power of AI to drive innovation and growth.

            **Key Specializations:**
            - Large Language Model integration and fine-tuning
            - Intelligent chatbots and virtual assistants  
            - AI-powered content generation platforms
            - Retrieval-Augmented Generation (RAG) systems
            - Multi-modal AI applications
            """))
            
            create_card("Latest Work", lambda: ui.markdown("""
            **🚀 Recent Achievements:**
            
            - Built an enterprise chatbot serving 10K+ users daily
            - Developed AI content platform reducing creation time by 80%
            - Implemented RAG system improving answer accuracy by 40%
            - Created multi-modal AI app for creative professionals
            
            **🔧 Currently Working On:**
            - Advanced prompt engineering techniques
            - AI agent orchestration systems
            - Custom model fine-tuning pipelines
            """))
        
        # Quick links
        with ui.element('div').classes('grid md:grid-cols-3 gap-6'):
            create_card("Explore Projects", lambda: [
                ui.markdown("Discover my latest AI projects and case studies"),
                ui.button("View Projects", on_click=lambda: ui.navigate.to('/projects')).classes('mt-4 bg-blue-600 text-white px-4 py-2 rounded')
            ])
            
            create_card("Try AI Demos", lambda: [
                ui.markdown("Experience live demonstrations of AI capabilities"),
                ui.button("Try Demos", on_click=lambda: ui.navigate.to('/demos')).classes('mt-4 bg-green-600 text-white px-4 py-2 rounded')
            ])
            
            create_card("Get In Touch", lambda: [
                ui.markdown("Let's discuss your AI project requirements"),
                ui.button("Contact Me", on_click=lambda: ui.navigate.to('/contact')).classes('mt-4 bg-purple-600 text-white px-4 py-2 rounded')
            ])

def create_about_page():
    """Create the about page content."""
    create_navigation()
    
    with ui.element('div').classes('container mx-auto px-4 py-8'):
        create_header("About Me", "My journey in Generative AI and technology")
        
        with ui.element('div').classes('grid md:grid-cols-2 gap-8'):
            create_card("Professional Background", lambda: ui.markdown("""
            With over **3 years of specialized experience** in Generative AI, I've been at the forefront of the AI revolution, helping organizations transform their operations through intelligent automation and AI-powered solutions.

            **Education & Certifications:**
            - M.S. in Computer Science (AI/ML Focus)
            - AWS Certified Machine Learning Specialist
            - Google Cloud Professional ML Engineer
            - OpenAI API Specialist Certification

            **Core Expertise:**
            - **Large Language Models**: GPT-4, Claude, Llama, PaLM
            - **AI Frameworks**: LangChain, LlamaIndex, Haystack
            - **Vector Databases**: Pinecone, Weaviate, Chroma
            - **Cloud Platforms**: AWS, Google Cloud, Azure
            - **Programming**: Python, JavaScript, TypeScript
            """))
            
            create_card("Philosophy & Approach", lambda: ui.markdown("""
            I believe in **responsible AI development** that prioritizes:

            🎯 **User-Centric Design**: Every AI solution should enhance human capabilities, not replace human judgment.

            🔒 **Ethical AI**: Implementing bias detection, privacy protection, and transparent AI systems.

            ⚡ **Performance Excellence**: Building scalable, efficient systems that deliver real business value.

            🤝 **Collaborative Innovation**: Working closely with stakeholders to understand needs and deliver tailored solutions.

            **My Mission**: To democratize AI technology and make it accessible to businesses of all sizes, enabling them to compete in the AI-driven future.
            """))
        
        # Experience timeline
        create_card("Professional Journey", lambda: ui.markdown("""
        **2024 - Present: Senior GenAI Engineer**
        - Leading AI transformation initiatives for enterprise clients
        - Developing custom LLM applications and RAG systems
        - Mentoring junior developers in AI best practices

        **2023 - 2024: AI Solutions Architect**
        - Designed and implemented 20+ AI-powered applications
        - Specialized in chatbot development and NLP solutions
        - Achieved 95% client satisfaction rate

        **2022 - 2023: Machine Learning Engineer**
        - Focused on traditional ML and early LLM experimentation
        - Built recommendation systems and predictive models
        - Transitioned expertise to Generative AI applications

        **2021 - 2022: Software Developer**
        - Full-stack development with focus on data-driven applications
        - Gained foundation in cloud computing and scalable architectures
        - Discovered passion for AI and machine learning
        """))

def create_projects_page():
    """Create the projects page content."""
    create_navigation()
    
    with ui.element('div').classes('container mx-auto px-4 py-8'):
        create_header("AI Projects", "Showcasing innovative Generative AI solutions")
        
        # Featured projects
        projects = [
            {
                "title": "Enterprise Customer Service Chatbot",
                "description": "Intelligent chatbot powered by GPT-4 with RAG capabilities, serving 10,000+ daily users with 95% satisfaction rate.",
                "tech_stack": ["GPT-4", "LangChain", "Pinecone", "FastAPI", "React", "PostgreSQL"],
                "category": "NLP",
                "github_url": "https://github.com/genai-engineer/enterprise-chatbot",
                "demo_url": "https://demo.chatbot-enterprise.com"
            },
            {
                "title": "AI Content Generation Platform",
                "description": "Multi-modal content creation platform for marketing teams, reducing content creation time by 80%.",
                "tech_stack": ["GPT-4", "DALL-E 3", "Stable Diffusion", "Python", "Vue.js", "Redis"],
                "category": "Multimodal",
                "github_url": "https://github.com/genai-engineer/content-platform",
                "demo_url": "https://demo.contentgen-pro.com"
            },
            {
                "title": "Intelligent Document Analysis System",
                "description": "RAG-powered system for analyzing legal documents with 40% improvement in accuracy over traditional methods.",
                "tech_stack": ["Claude", "LlamaIndex", "Weaviate", "Python", "Streamlit"],
                "category": "Document AI",
                "github_url": "https://github.com/genai-engineer/doc-analyzer",
                "demo_url": "https://demo.doc-ai.com"
            },
            {
                "title": "AI Code Assistant",
                "description": "Intelligent coding companion that helps developers write better code with context-aware suggestions.",
                "tech_stack": ["Codex", "GitHub Copilot API", "TypeScript", "VS Code Extension"],
                "category": "Developer Tools",
                "github_url": "https://github.com/genai-engineer/code-assistant",
                "demo_url": "https://marketplace.visualstudio.com/items?itemName=genai.code-assistant"
            },
            {
                "title": "Personalized Learning Platform",
                "description": "AI-powered educational platform that adapts to individual learning styles and pace.",
                "tech_stack": ["GPT-4", "LangChain", "Neo4j", "Python", "React", "TensorFlow"],
                "category": "EdTech",
                "github_url": "https://github.com/genai-engineer/learning-platform",
                "demo_url": "https://demo.ai-learn.com"
            },
            {
                "title": "Voice-Activated AI Assistant",
                "description": "Multi-language voice assistant for smart home automation with natural conversation capabilities.",
                "tech_stack": ["Whisper", "GPT-4", "Text-to-Speech", "Python", "IoT Integration"],
                "category": "Voice AI",
                "github_url": "https://github.com/genai-engineer/voice-assistant",
                "demo_url": "https://demo.voice-ai.com"
            }
        ]
        
        # Project grid
        with ui.element('div').classes('grid md:grid-cols-2 lg:grid-cols-3 gap-6'):
            for project in projects:
                create_project_card(project)

def create_skills_page():
    """Create the skills page content."""
    create_navigation()
    
    with ui.element('div').classes('container mx-auto px-4 py-8'):
        create_header("Technical Skills", "Comprehensive expertise in Generative AI and related technologies")
        
        # Skills by category
        skills_categories = {
            "Generative AI": [
                ("Large Language Models", 95),
                ("Prompt Engineering", 92),
                ("Fine-tuning & RLHF", 88),
                ("AI Agents & Orchestration", 85),
                ("Multimodal AI", 82)
            ],
            "AI Frameworks & Tools": [
                ("LangChain", 94),
                ("LlamaIndex", 90),
                ("Haystack", 85),
                ("Hugging Face", 88),
                ("OpenAI API", 95)
            ],
            "Programming Languages": [
                ("Python", 95),
                ("JavaScript/TypeScript", 88),
                ("SQL", 90),
                ("Bash/Shell", 85),
                ("Go", 75)
            ],
            "Cloud & Infrastructure": [
                ("AWS", 90),
                ("Google Cloud Platform", 85),
                ("Azure", 80),
                ("Docker & Kubernetes", 88),
                ("Terraform", 82)
            ],
            "Databases & Vector Stores": [
                ("Pinecone", 92),
                ("Weaviate", 88),
                ("Chroma", 85),
                ("PostgreSQL", 90),
                ("Redis", 85)
            ],
            "Web Development": [
                ("FastAPI", 92),
                ("React", 85),
                ("Vue.js", 82),
                ("Node.js", 80),
                ("NiceGUI", 88)
            ]
        }
        
        for category, skills in skills_categories.items():
            create_card(category, lambda s=skills: [
                create_skill_badge(skill, proficiency) for skill, proficiency in s
            ])

def create_demos_page():
    """Create the AI demos page content."""
    create_navigation()
    
    with ui.element('div').classes('container mx-auto px-4 py-8'):
        create_header("AI Capabilities Demo", "Experience the power of Generative AI firsthand")
        
        ui.markdown("""
        **Try these interactive demonstrations** to see how AI can transform your business processes. 
        These demos showcase real capabilities that can be integrated into your applications.
        """).classes('text-lg text-gray-600 mb-8')
        
        # AI Demo sections
        create_ai_demo_section()
        
        # Additional demo info
        create_card("Demo Information", lambda: ui.markdown("""
        **About These Demos:**
        
        These interactive demonstrations showcase core AI capabilities that I implement in real-world projects:

        🤖 **Text Generation**: Advanced language models for content creation, copywriting, and documentation
        
        💬 **Conversational AI**: Intelligent chatbots and virtual assistants for customer service and support
        
        📊 **Document Analysis**: AI-powered document processing and information extraction
        
        🎨 **Creative AI**: Multi-modal content generation including text, images, and multimedia
        
        **Ready to implement these capabilities in your business?** [Contact me](/contact) to discuss your specific requirements.
        """))

def create_contact_page():
    """Create the contact page content."""
    create_navigation()
    
    with ui.element('div').classes('container mx-auto px-4 py-8'):
        create_header("Get In Touch", "Let's discuss your AI project requirements")
        
        with ui.element('div').classes('grid md:grid-cols-2 gap-8'):
            # Contact form
            create_card("Send a Message", lambda: create_contact_form())
            
            # Contact information
            create_card("Contact Information", lambda: ui.markdown(f"""
            **Ready to transform your business with AI?** I'm here to help you navigate the exciting world of Generative AI and build solutions that drive real results.

            **📧 Email**: {settings.CONTACT_EMAIL}
            
            **💼 LinkedIn**: [Connect with me]({settings.LINKEDIN_URL})
            
            **🐙 GitHub**: [View my code]({settings.GITHUB_URL})
            
            **🌍 Location**: Available for remote work worldwide
            
            **⏰ Response Time**: I typically respond within 24 hours
            
            ---
            
            **What I can help you with:**
            - AI strategy and roadmap development
            - Custom AI application development
            - LLM integration and optimization
            - AI team training and mentorship
            - Technical architecture and consulting
            
            **Project Types:**
            - Enterprise chatbots and virtual assistants
            - Content generation and automation platforms
            - Document analysis and processing systems
            - AI-powered recommendation engines
            - Custom AI model development and fine-tuning
            """))
        
        # FAQ section
        create_card("Frequently Asked Questions", lambda: ui.markdown("""
        **Q: What's your typical project timeline?**
        A: Project timelines vary based on complexity, but most AI applications can be delivered within 4-12 weeks.

        **Q: Do you work with startups or only enterprises?**
        A: I work with organizations of all sizes, from startups to Fortune 500 companies.

        **Q: Can you help with AI strategy, not just development?**
        A: Absolutely! I provide strategic consulting to help you identify the best AI opportunities for your business.

        **Q: What's your approach to data privacy and security?**
        A: I follow industry best practices for data protection and can work within your security requirements.

        **Q: Do you provide ongoing support after project completion?**
        A: Yes, I offer various support packages to ensure your AI systems continue to perform optimally.
        """))