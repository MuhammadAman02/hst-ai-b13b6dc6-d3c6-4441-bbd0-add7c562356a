"""About section component."""

from nicegui import ui
from app.core.config import settings

def create_about_section():
    """Create the about section with personal and professional information."""
    
    with ui.element('section').props('id=about').classes('py-20 bg-gray-50'):
        with ui.column().classes('w-full max-w-6xl mx-auto p-8'):
            # Section header
            ui.label('About Me').classes('text-4xl font-bold text-center text-gray-800 mb-4')
            ui.label('Get to know the person behind the AI').classes('text-xl text-gray-600 text-center mb-12')
            
            with ui.row().classes('gap-12 items-center'):
                # Left side - Photo and quick facts
                with ui.column().classes('flex-1'):
                    with ui.card().classes('p-6 card-hover'):
                        # Profile image placeholder
                        with ui.element('div').classes('w-64 h-64 bg-gradient-to-br from-blue-400 to-purple-500 rounded-full mx-auto mb-6 flex items-center justify-center'):
                            ui.icon('person', size='8rem').classes('text-white')
                        
                        # Quick facts
                        with ui.column().classes('space-y-3'):
                            with ui.row().classes('items-center'):
                                ui.icon('location_on').classes('text-blue-600 mr-2')
                                ui.label(settings.ENGINEER_LOCATION).classes('text-gray-700')
                            
                            with ui.row().classes('items-center'):
                                ui.icon('work').classes('text-blue-600 mr-2')
                                ui.label(f'{settings.YEARS_EXPERIENCE}+ Years Experience').classes('text-gray-700')
                            
                            with ui.row().classes('items-center'):
                                ui.icon('school').classes('text-blue-600 mr-2')
                                ui.label('MS Computer Science, AI Specialization').classes('text-gray-700')
                
                # Right side - Detailed description
                with ui.column().classes('flex-1 space-y-6'):
                    ui.label(
                        'I\'m a passionate GenAI Engineer with a deep fascination for the intersection '
                        'of artificial intelligence and human creativity. My journey began with traditional '
                        'machine learning, but I found my true calling in the revolutionary world of '
                        'generative AI.'
                    ).classes('text-lg text-gray-700 leading-relaxed')
                    
                    ui.label(
                        'Over the past few years, I\'ve had the privilege of working on cutting-edge '
                        'projects involving large language models, computer vision, and multimodal AI '
                        'systems. I believe in building AI that augments human capabilities rather than '
                        'replacing them.'
                    ).classes('text-lg text-gray-700 leading-relaxed')
                    
                    # Key achievements
                    ui.label('Key Achievements:').classes('text-xl font-semibold text-gray-800 mt-6 mb-4')
                    
                    achievements = [
                        'Led development of GPT-powered customer service chatbot serving 1M+ users',
                        'Published 3 research papers on multimodal AI at top-tier conferences',
                        'Built and deployed 15+ production AI applications',
                        'Mentored 20+ junior engineers in AI/ML best practices',
                        'Speaker at 5 major AI conferences and workshops'
                    ]
                    
                    for achievement in achievements:
                        with ui.row().classes('items-start mb-2'):
                            ui.icon('check_circle').classes('text-green-500 mr-2 mt-1')
                            ui.label(achievement).classes('text-gray-700')