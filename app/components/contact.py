"""Contact section component."""

from nicegui import ui
import asyncio
from app.core.config import settings

def create_contact_section():
    """Create the contact section with form and information."""
    
    with ui.element('section').props('id=contact').classes('py-20 bg-white'):
        with ui.column().classes('w-full max-w-6xl mx-auto p-8'):
            # Section header
            ui.label('Get In Touch').classes('text-4xl font-bold text-center text-gray-800 mb-4')
            ui.label('Let\'s discuss how AI can transform your business').classes('text-xl text-gray-600 text-center mb-12')
            
            with ui.row().classes('gap-12 items-start'):
                # Left side - Contact form
                with ui.column().classes('flex-1'):
                    with ui.card().classes('p-8'):
                        ui.label('Send me a message').classes('text-2xl font-bold text-gray-800 mb-6')
                        
                        # Form fields
                        name_input = ui.input('Full Name *', placeholder='Your full name').classes('w-full mb-4')
                        email_input = ui.input('Email Address *', placeholder='your.email@company.com').classes('w-full mb-4')
                        company_input = ui.input('Company', placeholder='Your company (optional)').classes('w-full mb-4')
                        subject_input = ui.select(
                            ['General Inquiry', 'Project Collaboration', 'Consulting Services', 'Speaking Opportunity', 'Other'],
                            label='Subject *',
                            value='General Inquiry'
                        ).classes('w-full mb-4')
                        message_input = ui.textarea(
                            'Message *', 
                            placeholder='Tell me about your project or how I can help...'
                        ).classes('w-full h-32 mb-6')
                        
                        # Submit button
                        submit_btn = ui.button('Send Message', icon='send').classes('bg-blue-600 text-white px-8 py-3 rounded-lg hover:bg-blue-700 font-semibold')
                        
                        # Form submission handler
                        async def submit_form():
                            # Validate required fields
                            if not all([name_input.value, email_input.value, message_input.value]):
                                ui.notify('Please fill in all required fields', type='warning')
                                return
                            
                            # Validate email format
                            if '@' not in email_input.value:
                                ui.notify('Please enter a valid email address', type='warning')
                                return
                            
                            submit_btn.props('loading')
                            
                            # Simulate form submission
                            await asyncio.sleep(2)
                            
                            # In a real implementation, this would send the email
                            form_data = {
                                'name': name_input.value,
                                'email': email_input.value,
                                'company': company_input.value,
                                'subject': subject_input.value,
                                'message': message_input.value
                            }
                            
                            # Clear form
                            name_input.value = ''
                            email_input.value = ''
                            company_input.value = ''
                            subject_input.value = 'General Inquiry'
                            message_input.value = ''
                            
                            submit_btn.props(remove='loading')
                            ui.notify('Message sent successfully! I\'ll get back to you soon.', type='positive')
                        
                        submit_btn.on('click', submit_form)
                
                # Right side - Contact information and social links
                with ui.column().classes('flex-1 space-y-8'):
                    # Contact info
                    with ui.card().classes('p-6'):
                        ui.label('Contact Information').classes('text-xl font-bold text-gray-800 mb-4')
                        
                        contact_items = [
                            ('email', 'Email', settings.CONTACT_EMAIL),
                            ('location_on', 'Location', settings.ENGINEER_LOCATION),
                            ('schedule', 'Response Time', 'Usually within 24 hours'),
                            ('language', 'Languages', 'English, Mandarin, Python 😉')
                        ]
                        
                        for icon, label, value in contact_items:
                            with ui.row().classes('items-center mb-3'):
                                ui.icon(icon).classes('text-blue-600 mr-3')
                                with ui.column():
                                    ui.label(label).classes('font-medium text-gray-800')
                                    ui.label(value).classes('text-gray-600')
                    
                    # Social links
                    with ui.card().classes('p-6'):
                        ui.label('Connect with me').classes('text-xl font-bold text-gray-800 mb-4')
                        
                        social_links = [
                            ('GitHub', settings.GITHUB_URL, 'View my code and projects'),
                            ('LinkedIn', settings.LINKEDIN_URL, 'Professional network'),
                            ('Twitter', settings.TWITTER_URL, 'Latest thoughts and updates')
                        ]
                        
                        for platform, url, description in social_links:
                            with ui.row().classes('items-center mb-3 cursor-pointer hover:bg-gray-50 p-2 rounded').on('click', lambda u=url: ui.open(u, new_tab=True)):
                                ui.icon('link').classes('text-blue-600 mr-3')
                                with ui.column():
                                    ui.label(platform).classes('font-medium text-gray-800')
                                    ui.label(description).classes('text-gray-600 text-sm')
                    
                    # Availability status
                    with ui.card().classes('p-6 bg-green-50 border border-green-200'):
                        with ui.row().classes('items-center mb-2'):
                            ui.icon('check_circle').classes('text-green-600 mr-2')
                            ui.label('Available for Projects').classes('font-bold text-green-800')
                        
                        ui.label('Currently accepting new consulting opportunities and collaborations.').classes('text-green-700 text-sm')
                        
                        # Calendly-style booking button (placeholder)
                        ui.button('Schedule a Call', on_click=lambda: ui.notify('Calendar booking coming soon!')).classes('bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700 mt-3')