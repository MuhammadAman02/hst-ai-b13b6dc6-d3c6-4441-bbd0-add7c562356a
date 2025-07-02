"""Projects section component."""

from nicegui import ui

def create_projects_section():
    """Create the projects section showcasing key work."""
    
    with ui.element('section').props('id=projects').classes('py-20 bg-gray-50'):
        with ui.column().classes('w-full max-w-6xl mx-auto p-8'):
            # Section header
            ui.label('Featured Projects').classes('text-4xl font-bold text-center text-gray-800 mb-4')
            ui.label('Innovative AI solutions that make a real impact').classes('text-xl text-gray-600 text-center mb-12')
            
            # Project data
            projects = [
                {
                    'id': 'intelligent-chatbot',
                    'title': 'Intelligent Customer Service Chatbot',
                    'description': 'Enterprise-grade chatbot powered by GPT-4 with RAG capabilities, serving 1M+ users with 95% satisfaction rate.',
                    'tech_stack': ['GPT-4', 'LangChain', 'Pinecone', 'FastAPI', 'React'],
                    'category': 'NLP',
                    'image': '🤖',
                    'github': 'https://github.com/genai-engineer/intelligent-chatbot',
                    'demo': 'https://demo.chatbot.com',
                    'featured': True
                },
                {
                    'id': 'content-generator',
                    'title': 'AI Content Generation Platform',
                    'description': 'Multi-modal content creation platform generating text, images, and videos for marketing teams.',
                    'tech_stack': ['GPT-4', 'DALL-E 3', 'Stable Diffusion', 'Python', 'Vue.js'],
                    'category': 'Multimodal',
                    'image': '🎨',
                    'github': 'https://github.com/genai-engineer/content-generator',
                    'demo': 'https://demo.contentgen.com',
                    'featured': True
                },
                {
                    'id': 'document-analyzer',
                    'title': 'Intelligent Document Analyzer',
                    'description': 'AI-powered system for extracting insights from legal documents using advanced NLP and computer vision.',
                    'tech_stack': ['Claude-3', 'OCR', 'spaCy', 'PostgreSQL', 'Docker'],
                    'category': 'Document AI',
                    'image': '📄',
                    'github': 'https://github.com/genai-engineer/document-analyzer',
                    'demo': 'https://demo.docanalyzer.com',
                    'featured': True
                },
                {
                    'id': 'code-assistant',
                    'title': 'AI Code Review Assistant',
                    'description': 'Automated code review tool using fine-tuned models to detect bugs, suggest improvements, and ensure best practices.',
                    'tech_stack': ['CodeT5', 'GitHub API', 'FastAPI', 'Redis', 'TypeScript'],
                    'category': 'Code AI',
                    'image': '💻',
                    'github': 'https://github.com/genai-engineer/code-assistant',
                    'demo': 'https://demo.codeassist.com',
                    'featured': False
                },
                {
                    'id': 'voice-clone',
                    'title': 'Real-time Voice Cloning System',
                    'description': 'Ethical voice synthesis platform for audiobook narration and accessibility applications.',
                    'tech_stack': ['Tortoise TTS', 'PyTorch', 'WebRTC', 'Flask', 'JavaScript'],
                    'category': 'Audio AI',
                    'image': '🎙️',
                    'github': 'https://github.com/genai-engineer/voice-clone',
                    'demo': 'https://demo.voiceclone.com',
                    'featured': False
                },
                {
                    'id': 'recommendation-engine',
                    'title': 'Personalized AI Recommendation Engine',
                    'description': 'Advanced recommendation system using transformer models and collaborative filtering for e-commerce.',
                    'tech_stack': ['Transformers', 'TensorFlow', 'Apache Kafka', 'MongoDB', 'React'],
                    'category': 'Recommendation',
                    'image': '🎯',
                    'github': 'https://github.com/genai-engineer/recommendation-engine',
                    'demo': 'https://demo.recommendations.com',
                    'featured': False
                }
            ]
            
            # Featured projects
            featured_projects = [p for p in projects if p['featured']]
            with ui.grid(columns=1).classes('gap-8 mb-12'):
                for project in featured_projects:
                    create_project_card(project, featured=True)
            
            # Other projects
            ui.label('Other Notable Projects').classes('text-2xl font-bold text-gray-800 mb-6')
            other_projects = [p for p in projects if not p['featured']]
            with ui.grid(columns=3).classes('gap-6'):
                for project in other_projects:
                    create_project_card(project, featured=False)

def create_project_card(project, featured=False):
    """Create a project card component."""
    
    card_classes = 'p-6 card-hover h-full' if not featured else 'p-8 card-hover'
    
    with ui.card().classes(card_classes):
        if featured:
            with ui.row().classes('gap-8 items-center'):
                # Left side - Project info
                with ui.column().classes('flex-1 space-y-4'):
                    # Category badge
                    ui.label(project['category']).classes('inline-block bg-blue-100 text-blue-800 px-3 py-1 rounded-full text-sm font-medium')
                    
                    # Title and description
                    ui.label(project['title']).classes('text-2xl font-bold text-gray-800')
                    ui.label(project['description']).classes('text-gray-600 leading-relaxed')
                    
                    # Tech stack
                    ui.label('Tech Stack:').classes('font-semibold text-gray-800 mt-4')
                    with ui.row().classes('flex-wrap gap-2'):
                        for tech in project['tech_stack']:
                            ui.label(tech).classes('bg-gray-100 text-gray-700 px-2 py-1 rounded text-sm')
                    
                    # Action buttons
                    with ui.row().classes('space-x-4 mt-6'):
                        ui.button('View Demo', on_click=lambda url=project['demo']: ui.open(url, new_tab=True)).classes('bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700')
                        ui.button('GitHub', on_click=lambda url=project['github']: ui.open(url, new_tab=True)).classes('border border-gray-300 text-gray-700 px-6 py-2 rounded-lg hover:bg-gray-50')
                        ui.button('Details', on_click=lambda pid=project['id']: ui.open(f'/project/{pid}')).classes('text-blue-600 px-6 py-2 rounded-lg hover:bg-blue-50')
                
                # Right side - Visual representation
                with ui.column().classes('items-center'):
                    with ui.element('div').classes('w-32 h-32 bg-gradient-to-br from-blue-400 to-purple-500 rounded-2xl flex items-center justify-center text-6xl'):
                        ui.label(project['image'])
        else:
            # Compact card for non-featured projects
            with ui.column().classes('space-y-3'):
                # Icon and category
                with ui.row().classes('items-center justify-between'):
                    ui.label(project['image']).classes('text-3xl')
                    ui.label(project['category']).classes('bg-blue-100 text-blue-800 px-2 py-1 rounded text-xs font-medium')
                
                # Title and description
                ui.label(project['title']).classes('text-lg font-bold text-gray-800')
                ui.label(project['description']).classes('text-gray-600 text-sm leading-relaxed')
                
                # Action buttons
                with ui.row().classes('space-x-2 mt-4'):
                    ui.button('Demo', on_click=lambda url=project['demo']: ui.open(url, new_tab=True)).classes('bg-blue-600 text-white px-3 py-1 rounded text-sm hover:bg-blue-700')
                    ui.button('Code', on_click=lambda url=project['github']: ui.open(url, new_tab=True)).classes('border border-gray-300 text-gray-700 px-3 py-1 rounded text-sm hover:bg-gray-50')