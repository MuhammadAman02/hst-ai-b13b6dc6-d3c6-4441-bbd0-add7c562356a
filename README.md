# GenAI Engineer Portfolio

A professional portfolio website showcasing expertise in Generative AI, built with NiceGUI and FastAPI.

## 🚀 Features

### Professional Portfolio Sections
- **Hero Section**: Eye-catching introduction with animated elements
- **About**: Personal and professional background
- **Skills**: Technical expertise with proficiency indicators
- **Projects**: Detailed project showcases with live demos
- **AI Demos**: Interactive AI demonstrations
- **Blog**: Technical articles and insights
- **Contact**: Professional contact form and information

### Interactive AI Demonstrations
- **Text Generation**: AI-powered content creation
- **AI Chat**: Conversational AI assistant
- **Text Analysis**: Sentiment and entity analysis
- **Image Generation**: AI image creation (demo)

### Technical Highlights
- **Modern UI**: Responsive design with professional styling
- **Fast Performance**: Built with FastAPI backend
- **Type Safety**: Comprehensive type hints throughout
- **API Integration**: RESTful API for dynamic content
- **Production Ready**: Proper error handling and logging

## 🛠️ Technology Stack

### Frontend
- **NiceGUI**: Modern Python web framework
- **Tailwind CSS**: Utility-first CSS framework
- **Custom CSS**: Professional animations and styling

### Backend
- **FastAPI**: High-performance API framework
- **Pydantic**: Data validation and settings
- **Python 3.9+**: Modern Python features

### AI Integration
- **OpenAI API**: GPT models for text generation
- **LangChain**: AI application framework
- **Hugging Face**: Additional AI models

## 📦 Installation

### Prerequisites
- Python 3.9 or higher
- pip package manager
- Virtual environment (recommended)

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/genai-engineer/portfolio.git
cd portfolio
```

2. **Create virtual environment**
```bash
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment**
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. **Run the application**
```bash
python main.py
```

6. **Open your browser**
Navigate to `http://localhost:8080`

## ⚙️ Configuration

### Environment Variables

Copy `.env.example` to `.env` and customize:

```env
# Application
APP_NAME="Your Name - GenAI Engineer"
ENGINEER_NAME="Your Name"
ENGINEER_TITLE="Your Title"
ENGINEER_LOCATION="Your Location"

# Contact
CONTACT_EMAIL=your.email@domain.com
GITHUB_URL=https://github.com/yourusername
LINKEDIN_URL=https://linkedin.com/in/yourusername

# AI Services (Optional)
OPENAI_API_KEY=your-openai-api-key
```

### Customization

#### Personal Information
Edit `app/core/config.py` to update:
- Personal details
- Social media links
- Contact information
- Professional background

#### Projects
Modify `app/components/projects.py` to showcase your projects:
- Project descriptions
- Technology stacks
- Demo links
- GitHub repositories

#### Skills
Update `app/components/skills.py` with your expertise:
- Technical skills
- Proficiency levels
- Skill categories

#### Blog Posts
Add your articles in `app/components/blog.py`:
- Technical insights
- Project experiences
- Industry thoughts

## 🎨 Customization Guide

### Styling
- **Colors**: Modify CSS variables in `app/main.py`
- **Fonts**: Update font families in the CSS section
- **Layout**: Adjust component layouts in respective files

### Content
- **About Section**: Edit `app/components/about.py`
- **Projects**: Update project data in `app/components/projects.py`
- **Skills**: Modify skill categories in `app/components/skills.py`

### AI Demos
- **Enable Live Demos**: Add API keys to `.env`
- **Custom Models**: Integrate your own AI models
- **New Demos**: Add components in `app/components/ai_demos.py`

## 🚀 Deployment

### Local Development
```bash
python main.py
```

### Production Deployment

#### Using Docker
```bash
# Build image
docker build -t genai-portfolio .

# Run container
docker run -p 8080:8080 genai-portfolio
```

#### Using Cloud Platforms
- **Heroku**: Add `Procfile` with `web: python main.py`
- **Railway**: Connect GitHub repository
- **Vercel**: Use serverless deployment
- **AWS/GCP**: Deploy with container services

### Environment Setup
```bash
# Production environment
export DEBUG=false
export HOST=0.0.0.0
export PORT=8080
```

## 📁 Project Structure

```
portfolio/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Main application
│   ├── core/                   # Core configuration
│   │   ├── config.py          # Settings
│   │   └── logging.py         # Logging setup
│   ├── components/             # UI components
│   │   ├── layout.py          # Main layout
│   │   ├── hero.py            # Hero section
│   │   ├── about.py           # About section
│   │   ├── skills.py          # Skills section
│   │   ├── projects.py        # Projects showcase
│   │   ├── ai_demos.py        # AI demonstrations
│   │   ├── blog.py            # Blog section
│   │   ├── contact.py         # Contact form
│   │   ├── project_detail.py  # Project details
│   │   └── blog_post.py       # Blog post view
│   └── api/                    # API endpoints
│       ├── __init__.py
│       └── router.py          # API routes
├── main.py                     # Application entry point
├── requirements.txt            # Dependencies
├── .env.example               # Environment template
├── README.md                  # Documentation
└── .gitignore                 # Git ignore rules
```

## 🔧 API Endpoints

### Public Endpoints
- `GET /api/health` - Health check
- `GET /api/projects` - Get all projects
- `GET /api/skills` - Get all skills
- `POST /api/contact` - Submit contact form

### AI Demo Endpoints
- `POST /api/ai/text-generation` - Generate text
- `POST /api/ai/chat` - Chat with AI
- `POST /api/ai/analyze` - Analyze text

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙋‍♂️ Support

For questions or support:
- **Email**: contact@genai-engineer.com
- **GitHub Issues**: Create an issue in this repository
- **LinkedIn**: Connect with me for professional inquiries

## 🌟 Acknowledgments

- **NiceGUI**: For the excellent Python web framework
- **FastAPI**: For the high-performance API framework
- **Tailwind CSS**: For the utility-first CSS framework
- **OpenAI**: For AI model APIs

---

**Built with ❤️ by a GenAI Engineer**

*Showcasing the power of AI in web development*