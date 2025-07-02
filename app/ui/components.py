"""
UI components and theme setup for the GenAI Portfolio.
Provides reusable components and consistent styling.
"""

from nicegui import ui
from typing import Optional, List, Dict, Any, Callable
from app.core import app_logger, settings

def setup_theme():
    """Setup the application theme and global styles."""
    
    # Custom CSS for professional styling
    ui.add_head_html('''
    <style>
        :root {
            --primary-color: #2563eb;
            --secondary-color: #1e40af;
            --accent-color: #3b82f6;
            --background-color: #f8fafc;
            --surface-color: #ffffff;
            --text-primary: #1e293b;
            --text-secondary: #64748b;
            --border-color: #e2e8f0;
            --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }
        
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background-color: var(--background-color);
            color: var(--text-primary);
        }
        
        .portfolio-header {
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            color: white;
            padding: 2rem;
            border-radius: 0.5rem;
            margin-bottom: 2rem;
        }
        
        .portfolio-card {
            background: var(--surface-color);
            border: 1px solid var(--border-color);
            border-radius: 0.75rem;
            padding: 1.5rem;
            box-shadow: var(--shadow);
            transition: transform 0.2s, box-shadow 0.2s;
        }
        
        .portfolio-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px -5px rgba(0, 0, 0, 0.1);
        }
        
        .skill-badge {
            background: var(--accent-color);
            color: white;
            padding: 0.25rem 0.75rem;
            border-radius: 9999px;
            font-size: 0.875rem;
            font-weight: 500;
        }
        
        .project-tech {
            background: var(--background-color);
            color: var(--text-secondary);
            padding: 0.25rem 0.5rem;
            border-radius: 0.375rem;
            font-size: 0.75rem;
            border: 1px solid var(--border-color);
        }
        
        .contact-form {
            background: var(--surface-color);
            border: 1px solid var(--border-color);
            border-radius: 0.75rem;
            padding: 2rem;
            box-shadow: var(--shadow);
        }
        
        .demo-section {
            background: linear-gradient(to right, #f8fafc, #e2e8f0);
            border: 1px solid var(--border-color);
            border-radius: 0.75rem;
            padding: 1.5rem;
            margin: 1rem 0;
        }
        
        .loading-spinner {
            border: 3px solid var(--border-color);
            border-top: 3px solid var(--primary-color);
            border-radius: 50%;
            width: 24px;
            height: 24px;
            animation: spin 1s linear infinite;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .fade-in {
            animation: fadeIn 0.5s ease-in;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
    ''')
    
    app_logger.info("Theme and styles configured")

def create_header(title: str, subtitle: str) -> None:
    """Create a professional header section."""
    with ui.element('div').classes('portfolio-header fade-in'):
        ui.label(title).classes('text-4xl font-bold mb-2')
        ui.label(subtitle).classes('text-xl opacity-90')

def create_card(title: str, content_func: Callable[[], None], classes: str = "") -> None:
    """Create a styled card container."""
    with ui.element('div').classes(f'portfolio-card fade-in {classes}'):
        if title:
            ui.label(title).classes('text-2xl font-semibold mb-4 text-gray-800')
        content_func()

def create_skill_badge(skill: str, proficiency: int = 0) -> None:
    """Create a skill badge with optional proficiency indicator."""
    with ui.element('div').classes('inline-flex items-center gap-2 m-1'):
        ui.element('span').classes('skill-badge').text = skill
        if proficiency > 0:
            ui.element('span').classes('text-sm text-gray-600').text = f'{proficiency}%'

def create_project_card(project: Dict[str, Any]) -> None:
    """Create a project showcase card."""
    with ui.element('div').classes('portfolio-card'):
        # Project title and description
        ui.label(project.get('title', 'Untitled Project')).classes('text-xl font-semibold mb-2')
        ui.label(project.get('description', 'No description available')).classes('text-gray-600 mb-4')
        
        # Tech stack
        if project.get('tech_stack'):
            ui.label('Technologies:').classes('text-sm font-medium text-gray-700 mb-2')
            with ui.element('div').classes('flex flex-wrap gap-1 mb-4'):
                for tech in project['tech_stack']:
                    ui.element('span').classes('project-tech').text = tech
        
        # Links
        with ui.element('div').classes('flex gap-2'):
            if project.get('github_url'):
                ui.link('GitHub', project['github_url']).classes('text-blue-600 hover:text-blue-800')
            if project.get('demo_url'):
                ui.link('Live Demo', project['demo_url']).classes('text-green-600 hover:text-green-800')

def create_contact_form() -> None:
    """Create a professional contact form."""
    with ui.element('div').classes('contact-form'):
        ui.label('Get In Touch').classes('text-2xl font-semibold mb-4')
        
        # Form fields
        name_input = ui.input('Your Name', placeholder='Enter your full name').classes('w-full mb-4')
        email_input = ui.input('Email Address', placeholder='your.email@company.com').classes('w-full mb-4')
        company_input = ui.input('Company (Optional)', placeholder='Your company name').classes('w-full mb-4')
        subject_input = ui.input('Subject', placeholder='What would you like to discuss?').classes('w-full mb-4')
        message_input = ui.textarea('Message', placeholder='Tell me about your project or inquiry...').classes('w-full mb-4')
        
        # Submit button
        submit_button = ui.button('Send Message', on_click=lambda: handle_contact_submit(
            name_input.value,
            email_input.value,
            company_input.value,
            subject_input.value,
            message_input.value
        )).classes('bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition-colors')
        
        # Status message area
        status_area = ui.element('div').classes('mt-4')
        
        return {
            'name': name_input,
            'email': email_input,
            'company': company_input,
            'subject': subject_input,
            'message': message_input,
            'submit': submit_button,
            'status': status_area
        }

async def handle_contact_submit(name: str, email: str, company: str, subject: str, message: str) -> None:
    """Handle contact form submission."""
    try:
        # Validate required fields
        if not all([name.strip(), email.strip(), subject.strip(), message.strip()]):
            ui.notify('Please fill in all required fields', type='warning')
            return
        
        # Show loading state
        ui.notify('Sending message...', type='info')
        
        # Simulate API call (replace with actual API call)
        import asyncio
        await asyncio.sleep(1)
        
        # Success message
        ui.notify('Thank you! Your message has been sent successfully.', type='positive')
        app_logger.info(f"Contact form submitted by {email}")
        
    except Exception as e:
        ui.notify('Failed to send message. Please try again.', type='negative')
        app_logger.error(f"Contact form error: {e}")

def create_ai_demo_section() -> None:
    """Create an interactive AI demo section."""
    with ui.element('div').classes('demo-section'):
        ui.label('AI Capabilities Demo').classes('text-2xl font-semibold mb-4')
        
        # Text generation demo
        with ui.expansion('Text Generation Demo', icon='edit').classes('w-full mb-4'):
            prompt_input = ui.input('Enter a prompt', placeholder='Write a story about...').classes('w-full mb-2')
            style_select = ui.select(['Creative', 'Professional', 'Technical', 'Casual'], value='Creative').classes('mb-2')
            length_select = ui.select(['Short', 'Medium', 'Long'], value='Medium').classes('mb-2')
            
            generate_button = ui.button('Generate Text', on_click=lambda: handle_text_generation(
                prompt_input.value, style_select.value, length_select.value
            )).classes('bg-green-600 text-white px-4 py-2 rounded')
            
            result_area = ui.element('div').classes('mt-4 p-4 bg-gray-50 rounded border min-h-[100px]')
        
        # Chat demo
        with ui.expansion('AI Chat Demo', icon='chat').classes('w-full'):
            chat_input = ui.input('Ask me anything...', placeholder='What can you help me with?').classes('w-full mb-2')
            chat_button = ui.button('Send', on_click=lambda: handle_chat_message(chat_input.value)).classes('bg-blue-600 text-white px-4 py-2 rounded')
            
            chat_area = ui.element('div').classes('mt-4 p-4 bg-gray-50 rounded border min-h-[200px] max-h-[400px] overflow-y-auto')

async def handle_text_generation(prompt: str, style: str, length: str) -> None:
    """Handle AI text generation demo."""
    try:
        if not prompt.strip():
            ui.notify('Please enter a prompt', type='warning')
            return
        
        ui.notify('Generating text...', type='info')
        
        # Simulate AI generation (replace with actual AI call)
        import asyncio
        await asyncio.sleep(2)
        
        mock_response = f"""Generated text for prompt: "{prompt[:50]}..."

Style: {style}
Length: {length}

This is a demonstration of AI text generation capabilities. In a real implementation, this would connect to language models like GPT-4, Claude, or other AI services to generate contextually relevant content based on the user's prompt and preferences.

Key features demonstrated:
✓ Prompt-based generation
✓ Style customization
✓ Length control
✓ Real-time processing"""
        
        # Display result (in a real app, you'd update the result_area)
        ui.notify('Text generated successfully!', type='positive')
        app_logger.info(f"Text generation demo used with prompt: {prompt[:50]}...")
        
    except Exception as e:
        ui.notify('Text generation failed', type='negative')
        app_logger.error(f"Text generation demo error: {e}")

async def handle_chat_message(message: str) -> None:
    """Handle AI chat demo message."""
    try:
        if not message.strip():
            ui.notify('Please enter a message', type='warning')
            return
        
        ui.notify('AI is thinking...', type='info')
        
        # Simulate AI response (replace with actual AI call)
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
        
        # Display response (in a real app, you'd update the chat_area)
        ui.notify('AI responded!', type='positive')
        app_logger.info(f"Chat demo used with message: {message[:50]}...")
        
    except Exception as e:
        ui.notify('Chat failed', type='negative')
        app_logger.error(f"Chat demo error: {e}")

def create_loading_spinner() -> ui.element:
    """Create a loading spinner element."""
    return ui.element('div').classes('loading-spinner')

def create_stats_grid(stats: List[Dict[str, Any]]) -> None:
    """Create a grid of statistics/metrics."""
    with ui.element('div').classes('grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-8'):
        for stat in stats:
            with ui.element('div').classes('portfolio-card text-center'):
                ui.label(stat.get('value', '0')).classes('text-3xl font-bold text-blue-600 mb-2')
                ui.label(stat.get('label', 'Metric')).classes('text-gray-600')
                if stat.get('description'):
                    ui.label(stat['description']).classes('text-sm text-gray-500 mt-1')