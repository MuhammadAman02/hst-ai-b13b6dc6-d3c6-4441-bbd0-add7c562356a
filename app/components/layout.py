"""Layout components for the portfolio."""

from nicegui import ui
from contextlib import contextmanager
from app.core.config import settings

@contextmanager
def create_layout():
    """Create the main layout with navigation and footer."""
    
    # Navigation Header
    with ui.header().classes('bg-white shadow-md'):
        with ui.row().classes('w-full max-w-6xl mx-auto items-center justify-between p-4'):
            # Logo/Name
            ui.label(settings.ENGINEER_NAME).classes('text-2xl font-bold text-gray-800')
            
            # Navigation Menu
            with ui.row().classes('space-x-6'):
                ui.link('About', '#about').classes('text-gray-600 hover:text-blue-600 transition-colors')
                ui.link('Skills', '#skills').classes('text-gray-600 hover:text-blue-600 transition-colors')
                ui.link('Projects', '#projects').classes('text-gray-600 hover:text-blue-600 transition-colors')
                ui.link('AI Demos', '#demos').classes('text-gray-600 hover:text-blue-600 transition-colors')
                ui.link('Blog', '#blog').classes('text-gray-600 hover:text-blue-600 transition-colors')
                ui.link('Contact', '#contact').classes('text-gray-600 hover:text-blue-600 transition-colors')
    
    # Main Content
    with ui.column().classes('min-h-screen'):
        yield
    
    # Footer
    with ui.footer().classes('bg-gray-800 text-white'):
        with ui.row().classes('w-full max-w-6xl mx-auto items-center justify-between p-6'):
            with ui.column():
                ui.label(f'© 2024 {settings.ENGINEER_NAME}. All rights reserved.').classes('text-gray-300')
                ui.label('Built with NiceGUI and FastAPI').classes('text-gray-400 text-sm')
            
            with ui.row().classes('space-x-4'):
                ui.link('GitHub', settings.GITHUB_URL, new_tab=True).classes('text-gray-300 hover:text-white')
                ui.link('LinkedIn', settings.LINKEDIN_URL, new_tab=True).classes('text-gray-300 hover:text-white')
                ui.link('Twitter', settings.TWITTER_URL, new_tab=True).classes('text-gray-300 hover:text-white')