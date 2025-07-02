"""Skills section component."""

from nicegui import ui

def create_skills_section():
    """Create the skills section with technical expertise."""
    
    with ui.element('section').props('id=skills').classes('py-20 bg-white'):
        with ui.column().classes('w-full max-w-6xl mx-auto p-8'):
            # Section header
            ui.label('Technical Skills').classes('text-4xl font-bold text-center text-gray-800 mb-4')
            ui.label('My expertise across the AI technology stack').classes('text-xl text-gray-600 text-center mb-12')
            
            # Skills categories
            skills_data = {
                'Generative AI': [
                    {'name': 'Large Language Models (GPT, Claude, Llama)', 'level': 95},
                    {'name': 'Prompt Engineering & Fine-tuning', 'level': 90},
                    {'name': 'RAG (Retrieval Augmented Generation)', 'level': 88},
                    {'name': 'Computer Vision (DALL-E, Midjourney, Stable Diffusion)', 'level': 85},
                    {'name': 'Multimodal AI Systems', 'level': 82},
                ],
                'AI Frameworks & Tools': [
                    {'name': 'LangChain & LangSmith', 'level': 92},
                    {'name': 'OpenAI API & Azure OpenAI', 'level': 90},
                    {'name': 'Hugging Face Transformers', 'level': 88},
                    {'name': 'PyTorch & TensorFlow', 'level': 85},
                    {'name': 'Vector Databases (Pinecone, Weaviate)', 'level': 80},
                ],
                'Software Engineering': [
                    {'name': 'Python & FastAPI', 'level': 95},
                    {'name': 'JavaScript/TypeScript & React', 'level': 85},
                    {'name': 'Docker & Kubernetes', 'level': 80},
                    {'name': 'AWS/GCP Cloud Services', 'level': 82},
                    {'name': 'CI/CD & MLOps', 'level': 78},
                ],
                'Data & Analytics': [
                    {'name': 'Data Engineering & ETL', 'level': 85},
                    {'name': 'SQL & NoSQL Databases', 'level': 88},
                    {'name': 'Data Visualization (Plotly, D3.js)', 'level': 80},
                    {'name': 'Statistical Analysis & A/B Testing', 'level': 82},
                    {'name': 'Big Data (Spark, Kafka)', 'level': 75},
                ]
            }
            
            with ui.grid(columns=2).classes('gap-8 w-full'):
                for category, skills in skills_data.items():
                    with ui.card().classes('p-6 card-hover'):
                        ui.label(category).classes('text-2xl font-bold text-gray-800 mb-6')
                        
                        for skill in skills:
                            with ui.column().classes('mb-4'):
                                with ui.row().classes('justify-between items-center mb-2'):
                                    ui.label(skill['name']).classes('text-gray-700 font-medium')
                                    ui.label(f"{skill['level']}%").classes('text-blue-600 font-semibold')
                                
                                # Skill bar
                                with ui.element('div').classes('w-full bg-gray-200 rounded-full h-2'):
                                    ui.element('div').classes(f'skill-bar h-2 rounded-full').style(f'width: {skill["level"]}%')