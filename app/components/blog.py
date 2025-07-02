"""Blog section component."""

from nicegui import ui
from datetime import datetime, timedelta

def create_blog_section():
    """Create the blog section with recent articles."""
    
    with ui.element('section').props('id=blog').classes('py-20 bg-gray-50'):
        with ui.column().classes('w-full max-w-6xl mx-auto p-8'):
            # Section header
            ui.label('Latest Blog Posts').classes('text-4xl font-bold text-center text-gray-800 mb-4')
            ui.label('Insights and thoughts on the future of AI').classes('text-xl text-gray-600 text-center mb-12')
            
            # Blog posts data
            blog_posts = [
                {
                    'id': 'future-of-rag',
                    'title': 'The Future of RAG: Beyond Simple Retrieval',
                    'excerpt': 'Exploring advanced techniques in Retrieval Augmented Generation and how they\'re reshaping AI applications.',
                    'date': datetime.now() - timedelta(days=3),
                    'read_time': '8 min read',
                    'category': 'Technical',
                    'tags': ['RAG', 'LLM', 'AI Architecture']
                },
                {
                    'id': 'multimodal-ai-trends',
                    'title': 'Multimodal AI: The Next Frontier in Human-Computer Interaction',
                    'excerpt': 'How combining text, image, and audio processing is creating more intuitive AI systems.',
                    'date': datetime.now() - timedelta(days=7),
                    'read_time': '6 min read',
                    'category': 'Industry Insights',
                    'tags': ['Multimodal', 'Computer Vision', 'NLP']
                },
                {
                    'id': 'ethical-ai-development',
                    'title': 'Building Ethical AI: A Practical Framework',
                    'excerpt': 'Practical guidelines for developing AI systems that are fair, transparent, and beneficial for society.',
                    'date': datetime.now() - timedelta(days=12),
                    'read_time': '10 min read',
                    'category': 'Ethics',
                    'tags': ['AI Ethics', 'Responsible AI', 'Best Practices']
                },
                {
                    'id': 'prompt-engineering-mastery',
                    'title': 'Mastering Prompt Engineering: Advanced Techniques',
                    'excerpt': 'Deep dive into advanced prompt engineering strategies for getting the best results from language models.',
                    'date': datetime.now() - timedelta(days=18),
                    'read_time': '12 min read',
                    'category': 'Tutorial',
                    'tags': ['Prompt Engineering', 'GPT', 'LLM Optimization']
                }
            ]
            
            # Featured post (first one)
            featured_post = blog_posts[0]
            with ui.card().classes('p-8 mb-8 card-hover'):
                ui.label('Featured Post').classes('bg-blue-100 text-blue-800 px-3 py-1 rounded-full text-sm font-medium mb-4 inline-block')
                
                with ui.row().classes('gap-8 items-center'):
                    # Content
                    with ui.column().classes('flex-1 space-y-4'):
                        ui.label(featured_post['title']).classes('text-3xl font-bold text-gray-800')
                        ui.label(featured_post['excerpt']).classes('text-lg text-gray-600 leading-relaxed')
                        
                        # Meta information
                        with ui.row().classes('items-center space-x-4 text-gray-500'):
                            ui.label(featured_post['date'].strftime('%B %d, %Y')).classes('text-sm')
                            ui.label('•').classes('text-sm')
                            ui.label(featured_post['read_time']).classes('text-sm')
                            ui.label('•').classes('text-sm')
                            ui.label(featured_post['category']).classes('text-sm')
                        
                        # Tags
                        with ui.row().classes('flex-wrap gap-2 mt-4'):
                            for tag in featured_post['tags']:
                                ui.label(tag).classes('bg-gray-100 text-gray-700 px-2 py-1 rounded text-sm')
                        
                        # Read more button
                        ui.button('Read Full Article', on_click=lambda: ui.open(f'/blog/{featured_post["id"]}')).classes('bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 mt-4')
                    
                    # Featured image placeholder
                    with ui.element('div').classes('w-64 h-48 bg-gradient-to-br from-blue-400 to-purple-500 rounded-lg flex items-center justify-center'):
                        ui.icon('article', size='4rem').classes('text-white')
            
            # Other posts
            ui.label('Recent Articles').classes('text-2xl font-bold text-gray-800 mb-6')
            
            with ui.grid(columns=3).classes('gap-6'):
                for post in blog_posts[1:]:
                    create_blog_card(post)
            
            # View all posts button
            with ui.row().classes('justify-center mt-8'):
                ui.button('View All Posts', on_click=lambda: ui.notify('Blog archive coming soon!')).classes('border border-blue-600 text-blue-600 px-8 py-3 rounded-lg hover:bg-blue-50 font-semibold')

def create_blog_card(post):
    """Create a blog post card."""
    
    with ui.card().classes('p-6 card-hover h-full'):
        with ui.column().classes('space-y-3 h-full'):
            # Category badge
            ui.label(post['category']).classes('bg-gray-100 text-gray-700 px-2 py-1 rounded text-xs font-medium self-start')
            
            # Title and excerpt
            ui.label(post['title']).classes('text-lg font-bold text-gray-800 leading-tight')
            ui.label(post['excerpt']).classes('text-gray-600 text-sm leading-relaxed flex-1')
            
            # Meta info
            with ui.column().classes('space-y-2 mt-auto'):
                with ui.row().classes('items-center justify-between text-gray-500 text-xs'):
                    ui.label(post['date'].strftime('%b %d, %Y'))
                    ui.label(post['read_time'])
                
                # Tags
                with ui.row().classes('flex-wrap gap-1'):
                    for tag in post['tags'][:2]:  # Show only first 2 tags
                        ui.label(tag).classes('bg-gray-100 text-gray-600 px-2 py-1 rounded text-xs')
                
                # Read more link
                ui.button('Read More', on_click=lambda pid=post['id']: ui.open(f'/blog/{pid}')).classes('text-blue-600 hover:text-blue-800 text-sm font-medium self-start mt-2')