"""Project detail page component."""

from nicegui import ui

def create_project_detail(project_id: str):
    """Create detailed project view."""
    
    # Mock project data (in real app, this would come from database)
    projects_data = {
        'intelligent-chatbot': {
            'title': 'Intelligent Customer Service Chatbot',
            'description': 'Enterprise-grade chatbot powered by GPT-4 with RAG capabilities, serving 1M+ users with 95% satisfaction rate.',
            'long_description': '''This project represents a comprehensive solution for enterprise customer service automation. The chatbot leverages state-of-the-art language models combined with retrieval-augmented generation to provide accurate, contextual responses to customer inquiries.

Key innovations include:
- Custom fine-tuning on domain-specific data
- Real-time knowledge base integration
- Multi-language support with automatic translation
- Sentiment analysis for escalation management
- Advanced conversation flow management

The system processes over 10,000 conversations daily with a 95% customer satisfaction rate and has reduced response times by 80% compared to traditional support channels.''',
            'tech_stack': ['GPT-4', 'LangChain', 'Pinecone', 'FastAPI', 'React', 'PostgreSQL', 'Redis', 'Docker'],
            'category': 'NLP',
            'image': '🤖',
            'github': 'https://github.com/genai-engineer/intelligent-chatbot',
            'demo': 'https://demo.chatbot.com',
            'metrics': {
                'Users Served': '1M+',
                'Satisfaction Rate': '95%',
                'Response Time': '<2 seconds',
                'Languages Supported': '12'
            },
            'challenges': [
                'Handling complex multi-turn conversations',
                'Maintaining context across long sessions',
                'Integrating with legacy CRM systems',
                'Ensuring data privacy and security'
            ],
            'solutions': [
                'Implemented advanced conversation state management',
                'Used vector embeddings for context preservation',
                'Built custom API adapters for legacy integration',
                'Applied end-to-end encryption and data anonymization'
            ]
        }
    }
    
    project = projects_data.get(project_id)
    
    if not project:
        ui.label('Project not found').classes('text-2xl text-center text-gray-600 mt-20')
        ui.button('Back to Portfolio', on_click=lambda: ui.open('/')).classes('mx-auto mt-4')
        return
    
    # Project header
    with ui.row().classes('w-full max-w-6xl mx-auto p-8 items-center'):
        ui.button('← Back to Portfolio', on_click=lambda: ui.open('/')).classes('text-blue-600 hover:text-blue-800 mb-4')
    
    with ui.column().classes('w-full max-w-6xl mx-auto p-8 space-y-8'):
        # Title and basic info
        with ui.card().classes('p-8'):
            with ui.row().classes('items-center gap-6'):
                ui.label(project['image']).classes('text-6xl')
                with ui.column().classes('flex-1'):
                    ui.label(project['title']).classes('text-4xl font-bold text-gray-800')
                    ui.label(project['category']).classes('bg-blue-100 text-blue-800 px-3 py-1 rounded-full text-sm font-medium inline-block mt-2')
                    ui.label(project['description']).classes('text-lg text-gray-600 mt-4')
            
            # Action buttons
            with ui.row().classes('space-x-4 mt-6'):
                ui.button('Live Demo', on_click=lambda: ui.open(project['demo'], new_tab=True)).classes('bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700')
                ui.button('View Code', on_click=lambda: ui.open(project['github'], new_tab=True)).classes('border border-gray-300 text-gray-700 px-6 py-3 rounded-lg hover:bg-gray-50')
        
        # Key metrics
        with ui.card().classes('p-6'):
            ui.label('Key Metrics').classes('text-2xl font-bold text-gray-800 mb-4')
            with ui.grid(columns=4).classes('gap-4'):
                for metric, value in project['metrics'].items():
                    with ui.card().classes('p-4 text-center bg-blue-50'):
                        ui.label(value).classes('text-2xl font-bold text-blue-600')
                        ui.label(metric).classes('text-gray-700 text-sm')
        
        # Detailed description
        with ui.card().classes('p-6'):
            ui.label('Project Overview').classes('text-2xl font-bold text-gray-800 mb-4')
            ui.label(project['long_description']).classes('text-gray-700 leading-relaxed whitespace-pre-line')
        
        # Technology stack
        with ui.card().classes('p-6'):
            ui.label('Technology Stack').classes('text-2xl font-bold text-gray-800 mb-4')
            with ui.row().classes('flex-wrap gap-3'):
                for tech in project['tech_stack']:
                    ui.label(tech).classes('bg-gray-100 text-gray-800 px-4 py-2 rounded-lg font-medium')
        
        # Challenges and solutions
        with ui.row().classes('gap-6'):
            # Challenges
            with ui.card().classes('p-6 flex-1'):
                ui.label('Challenges').classes('text-xl font-bold text-gray-800 mb-4')
                for challenge in project['challenges']:
                    with ui.row().classes('items-start mb-3'):
                        ui.icon('warning').classes('text-orange-500 mr-2 mt-1')
                        ui.label(challenge).classes('text-gray-700')
            
            # Solutions
            with ui.card().classes('p-6 flex-1'):
                ui.label('Solutions').classes('text-xl font-bold text-gray-800 mb-4')
                for solution in project['solutions']:
                    with ui.row().classes('items-start mb-3'):
                        ui.icon('check_circle').classes('text-green-500 mr-2 mt-1')
                        ui.label(solution).classes('text-gray-700')