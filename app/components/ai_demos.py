"""AI Demos section component with interactive demonstrations."""

from nicegui import ui
import asyncio
import json
from typing import Optional

def create_ai_demos_section():
    """Create the AI demos section with interactive examples."""
    
    with ui.element('section').props('id=demos').classes('py-20 bg-white'):
        with ui.column().classes('w-full max-w-6xl mx-auto p-8'):
            # Section header
            ui.label('Interactive AI Demos').classes('text-4xl font-bold text-center text-gray-800 mb-4')
            ui.label('Experience the power of AI firsthand').classes('text-xl text-gray-600 text-center mb-12')
            
            # Demo tabs
            with ui.tabs().classes('w-full') as tabs:
                text_tab = ui.tab('Text Generation', icon='edit')
                chat_tab = ui.tab('AI Chat', icon='chat')
                analysis_tab = ui.tab('Text Analysis', icon='analytics')
                image_tab = ui.tab('Image Generation', icon='image')
            
            with ui.tab_panels(tabs, value=text_tab).classes('w-full mt-8'):
                # Text Generation Demo
                with ui.tab_panel(text_tab):
                    create_text_generation_demo()
                
                # AI Chat Demo
                with ui.tab_panel(chat_tab):
                    create_chat_demo()
                
                # Text Analysis Demo
                with ui.tab_panel(analysis_tab):
                    create_text_analysis_demo()
                
                # Image Generation Demo
                with ui.tab_panel(image_tab):
                    create_image_generation_demo()

def create_text_generation_demo():
    """Create text generation demo."""
    
    with ui.card().classes('ai-demo-card p-6 w-full'):
        ui.label('AI Text Generation').classes('text-2xl font-bold mb-4')
        ui.label('Generate creative content using advanced language models').classes('text-gray-600 mb-6')
        
        # Input controls
        with ui.row().classes('w-full gap-4 mb-4'):
            prompt_input = ui.textarea('Enter your prompt:', placeholder='Write a story about a robot learning to paint...').classes('flex-1')
            
            with ui.column().classes('space-y-2'):
                ui.label('Style:').classes('font-medium')
                style_select = ui.select(['Creative', 'Professional', 'Technical', 'Casual'], value='Creative').classes('w-40')
                
                ui.label('Length:').classes('font-medium')
                length_select = ui.select(['Short', 'Medium', 'Long'], value='Medium').classes('w-40')
        
        # Generate button and output
        with ui.column().classes('w-full'):
            generate_btn = ui.button('Generate Text', icon='auto_awesome').classes('bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700')
            
            output_area = ui.textarea('Generated text will appear here...').classes('w-full h-40 mt-4')
            output_area.props('readonly')
        
        # Demo functionality
        async def generate_text():
            if not prompt_input.value.strip():
                ui.notify('Please enter a prompt', type='warning')
                return
            
            generate_btn.props('loading')
            output_area.value = 'Generating...'
            
            # Simulate AI text generation
            await asyncio.sleep(2)
            
            # Mock response based on prompt and settings
            mock_response = f"""Based on your prompt "{prompt_input.value[:50]}..." in {style_select.value.lower()} style:

This is a demonstration of AI text generation capabilities. In a real implementation, this would connect to:
- OpenAI GPT-4 API
- Anthropic Claude API  
- Local language models
- Custom fine-tuned models

The generated content would be contextually relevant, creative, and tailored to your specified style and length preferences.

Key features:
✓ Context-aware generation
✓ Style customization
✓ Length control
✓ Real-time processing
✓ Multiple model support"""
            
            output_area.value = mock_response
            generate_btn.props(remove='loading')
            ui.notify('Text generated successfully!', type='positive')
        
        generate_btn.on('click', generate_text)

def create_chat_demo():
    """Create AI chat demo."""
    
    with ui.card().classes('ai-demo-card p-6 w-full'):
        ui.label('AI Chat Assistant').classes('text-2xl font-bold mb-4')
        ui.label('Have a conversation with an AI assistant').classes('text-gray-600 mb-6')
        
        # Chat messages container
        chat_container = ui.column().classes('w-full h-96 overflow-y-auto bg-gray-50 rounded-lg p-4 mb-4')
        
        # Initial message
        with chat_container:
            create_chat_message("Hello! I'm an AI assistant. How can I help you today?", is_user=False)
        
        # Input area
        with ui.row().classes('w-full gap-2'):
            message_input = ui.input('Type your message...').classes('flex-1')
            send_btn = ui.button('Send', icon='send').classes('bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700')
        
        async def send_message():
            if not message_input.value.strip():
                return
            
            user_message = message_input.value
            message_input.value = ''
            
            # Add user message
            with chat_container:
                create_chat_message(user_message, is_user=True)
            
            # Simulate typing
            with chat_container:
                typing_msg = create_chat_message("AI is typing...", is_user=False, is_typing=True)
            
            await asyncio.sleep(1.5)
            
            # Remove typing indicator and add response
            typing_msg.delete()
            
            # Mock AI response
            responses = [
                "That's an interesting question! In a real implementation, I would use advanced language models to provide helpful, accurate responses.",
                "I understand what you're asking. This demo showcases how AI chat systems can maintain context and provide relevant responses.",
                "Great point! AI assistants like this can help with various tasks including answering questions, providing explanations, and offering suggestions.",
                "Thanks for trying out this demo! Real AI chat systems use sophisticated NLP models to understand and respond to user queries effectively."
            ]
            
            import random
            ai_response = random.choice(responses)
            
            with chat_container:
                create_chat_message(ai_response, is_user=False)
            
            # Scroll to bottom
            ui.run_javascript(f'document.querySelector(".q-scrollarea__content").scrollTop = document.querySelector(".q-scrollarea__content").scrollHeight')
        
        send_btn.on('click', send_message)
        message_input.on('keydown.enter', send_message)

def create_chat_message(text: str, is_user: bool, is_typing: bool = False):
    """Create a chat message bubble."""
    
    alignment = 'items-end' if is_user else 'items-start'
    bg_color = 'bg-blue-600 text-white' if is_user else 'bg-white text-gray-800'
    
    with ui.row().classes(f'w-full {alignment} mb-2'):
        if not is_user:
            ui.icon('smart_toy').classes('text-blue-600 mr-2')
        
        message_card = ui.card().classes(f'{bg_color} max-w-xs p-3 rounded-lg shadow-sm')
        with message_card:
            if is_typing:
                ui.label(text).classes('text-sm animate-pulse')
            else:
                ui.label(text).classes('text-sm')
        
        if is_user:
            ui.icon('person').classes('text-gray-600 ml-2')
    
    return message_card

def create_text_analysis_demo():
    """Create text analysis demo."""
    
    with ui.card().classes('ai-demo-card p-6 w-full'):
        ui.label('AI Text Analysis').classes('text-2xl font-bold mb-4')
        ui.label('Analyze text for sentiment, entities, and key insights').classes('text-gray-600 mb-6')
        
        # Input area
        text_input = ui.textarea(
            'Enter text to analyze:', 
            placeholder='Paste any text here for analysis...',
            value='I absolutely love the new AI features in this application! The user interface is intuitive and the performance is outstanding. However, I think the pricing could be more competitive.'
        ).classes('w-full h-32 mb-4')
        
        analyze_btn = ui.button('Analyze Text', icon='analytics').classes('bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 mb-6')
        
        # Results area
        results_container = ui.column().classes('w-full space-y-4')
        
        async def analyze_text():
            if not text_input.value.strip():
                ui.notify('Please enter some text to analyze', type='warning')
                return
            
            analyze_btn.props('loading')
            results_container.clear()
            
            await asyncio.sleep(1.5)
            
            # Mock analysis results
            with results_container:
                # Sentiment Analysis
                with ui.card().classes('p-4'):
                    ui.label('Sentiment Analysis').classes('text-lg font-bold mb-2')
                    with ui.row().classes('items-center gap-4'):
                        ui.label('Overall Sentiment:').classes('font-medium')
                        ui.label('Positive (0.75)').classes('bg-green-100 text-green-800 px-3 py-1 rounded-full')
                        ui.linear_progress(0.75, color='green').classes('flex-1')
                
                # Key Entities
                with ui.card().classes('p-4'):
                    ui.label('Named Entities').classes('text-lg font-bold mb-2')
                    entities = [
                        ('AI features', 'TECHNOLOGY'),
                        ('application', 'PRODUCT'),
                        ('user interface', 'FEATURE'),
                        ('performance', 'QUALITY'),
                        ('pricing', 'BUSINESS')
                    ]
                    
                    with ui.row().classes('flex-wrap gap-2'):
                        for entity, entity_type in entities:
                            ui.label(f'{entity} ({entity_type})').classes('bg-blue-100 text-blue-800 px-2 py-1 rounded text-sm')
                
                # Key Phrases
                with ui.card().classes('p-4'):
                    ui.label('Key Phrases').classes('text-lg font-bold mb-2')
                    phrases = ['absolutely love', 'new AI features', 'intuitive interface', 'outstanding performance', 'competitive pricing']
                    
                    with ui.column().classes('space-y-1'):
                        for phrase in phrases:
                            with ui.row().classes('items-center'):
                                ui.icon('star').classes('text-yellow-500 mr-2')
                                ui.label(phrase).classes('text-gray-700')
            
            analyze_btn.props(remove='loading')
            ui.notify('Analysis completed!', type='positive')
        
        analyze_btn.on('click', analyze_text)

def create_image_generation_demo():
    """Create image generation demo."""
    
    with ui.card().classes('ai-demo-card p-6 w-full'):
        ui.label('AI Image Generation').classes('text-2xl font-bold mb-4')
        ui.label('Generate images from text descriptions using AI').classes('text-gray-600 mb-6')
        
        # Input controls
        with ui.column().classes('w-full space-y-4 mb-6'):
            prompt_input = ui.input(
                'Image prompt:', 
                placeholder='A futuristic robot painting a landscape...',
                value='A friendly robot sitting at an easel, painting a beautiful sunset landscape with mountains in the background, digital art style'
            ).classes('w-full')
            
            with ui.row().classes('gap-4'):
                style_select = ui.select(
                    ['Digital Art', 'Photorealistic', 'Oil Painting', 'Watercolor', 'Sketch'], 
                    value='Digital Art',
                    label='Style:'
                ).classes('flex-1')
                
                size_select = ui.select(
                    ['512x512', '768x768', '1024x1024'], 
                    value='512x512',
                    label='Size:'
                ).classes('flex-1')
        
        generate_img_btn = ui.button('Generate Image', icon='image').classes('bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 mb-4')
        
        # Image display area
        image_container = ui.column().classes('w-full items-center')
        
        async def generate_image():
            if not prompt_input.value.strip():
                ui.notify('Please enter an image prompt', type='warning')
                return
            
            generate_img_btn.props('loading')
            image_container.clear()
            
            with image_container:
                ui.label('Generating image...').classes('text-gray-600 mb-4')
                ui.spinner(size='lg').classes('text-blue-600')
            
            await asyncio.sleep(3)
            
            image_container.clear()
            
            # Mock image generation result
            with image_container:
                # Placeholder for generated image
                with ui.element('div').classes('w-96 h-96 bg-gradient-to-br from-purple-400 via-pink-500 to-red-500 rounded-lg flex items-center justify-center mb-4'):
                    with ui.column().classes('items-center text-white'):
                        ui.icon('image', size='4rem').classes('mb-2')
                        ui.label('Generated Image').classes('text-xl font-bold')
                        ui.label('(Demo Placeholder)').classes('text-sm opacity-75')
                
                ui.label(f'Prompt: "{prompt_input.value}"').classes('text-gray-600 text-center max-w-md')
                ui.label(f'Style: {style_select.value} | Size: {size_select.value}').classes('text-gray-500 text-center text-sm')
                
                # Action buttons
                with ui.row().classes('space-x-2 mt-4'):
                    ui.button('Download', icon='download').classes('bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700')
                    ui.button('Regenerate', icon='refresh').classes('border border-gray-300 text-gray-700 px-4 py-2 rounded-lg hover:bg-gray-50')
            
            generate_img_btn.props(remove='loading')
            ui.notify('Image generated successfully!', type='positive')
        
        generate_img_btn.on('click', generate_image)