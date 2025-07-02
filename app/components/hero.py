"""Hero section component."""

from nicegui import ui
from app.core.config import settings

def create_hero_section():
    """Create the hero section with introduction and call-to-action."""
    
    with ui.element('section').props('id=hero').classes('hero-gradient min-h-screen flex items-center'):
        with ui.row().classes('w-full max-w-6xl mx-auto items-center p-8'):
            # Left side - Text content
            with ui.column().classes('flex-1 space-y-6 text-white'):
                ui.label('Hello, I\'m').classes('text-xl opacity-90')
                ui.label(settings.ENGINEER_NAME).classes('text-5xl font-bold mb-2')
                ui.label(settings.ENGINEER_TITLE).classes('text-2xl font-light mb-4 typing-animation')
                
                ui.label(
                    'Passionate about building the future with Generative AI. '
                    'I create intelligent systems that understand, generate, and transform '
                    'human language and creativity into powerful applications.'
                ).classes('text-lg opacity-90 max-w-2xl leading-relaxed')
                
                with ui.row().classes('space-x-4 mt-8'):
                    ui.button('View My Work', on_click=lambda: ui.run_javascript('document.getElementById("projects").scrollIntoView({behavior: "smooth"})')).classes('bg-white text-blue-600 px-8 py-3 rounded-lg font-semibold hover:bg-gray-100 transition-colors')
                    ui.button('Contact Me', on_click=lambda: ui.run_javascript('document.getElementById("contact").scrollIntoView({behavior: "smooth"})')).classes('border-2 border-white text-white px-8 py-3 rounded-lg font-semibold hover:bg-white hover:text-blue-600 transition-colors')
            
            # Right side - Animated illustration
            with ui.column().classes('flex-1 items-center'):
                with ui.card().classes('p-8 bg-white bg-opacity-10 backdrop-blur-sm floating-animation'):
                    ui.icon('psychology', size='8rem').classes('text-white mb-4')
                    ui.label('AI Innovation').classes('text-white text-xl font-semibold')
                    ui.label('Transforming Ideas into Reality').classes('text-white opacity-90')