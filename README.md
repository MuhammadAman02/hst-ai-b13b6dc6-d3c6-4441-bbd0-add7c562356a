# GenAI Engineer Portfolio

A professional portfolio showcasing Generative AI expertise with interactive demos and project showcases. Built with NiceGUI and FastAPI for a modern, responsive experience.

## 🚀 Features

- **Interactive Portfolio**: Professional showcase of AI projects and skills
- **Live AI Demos**: Experience text generation and chat capabilities
- **Responsive Design**: Modern, mobile-friendly interface
- **Contact Integration**: Professional contact form with email notifications
- **API Backend**: RESTful API for dynamic content and integrations
- **Production Ready**: Comprehensive logging, error handling, and security

## 🛠️ Technology Stack

- **Frontend**: NiceGUI (Python-based UI framework)
- **Backend**: FastAPI (High-performance Python web framework)
- **Database**: SQLAlchemy with SQLite (easily configurable for PostgreSQL)
- **AI Integration**: OpenAI API, LangChain support
- **Styling**: Tailwind CSS classes with custom themes
- **Deployment**: Docker support with production configurations

## 📋 Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/genai-engineer/portfolio.git
cd portfolio
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

```bash
# Copy environment template
cp .env.example .env

# Edit .env file with your configuration
# At minimum, update:
# - SECRET_KEY (generate a secure random key)
# - CONTACT_EMAIL (your email address)
# - OPENAI_API_KEY (optional, for live AI demos)
```

### 5. Create Required Directories

```bash
mkdir -p data logs uploads static/images static/css static/js
```

## 🚀 Running the Application

### Development Mode

```bash
python main.py
```

The application will be available at `http://localhost:8080`

### Production Mode

```bash
# Set production environment
export DEBUG=false

# Run with production settings
python main.py
```

## 📁 Project Structure

```
portfolio/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Application factory and configuration
│   ├── api/                    # API endpoints and routing
│   │   ├── __init__.py
│   │   └── router.py          # API routes for contact, projects, etc.
│   ├── core/                   # Core application components
│   │   ├── __init__.py
│   │   ├── config.py          # Settings and configuration
│   │   └── logging.py         # Logging configuration
│   ├── models/                 # Data models (future expansion)
│   │   └── __init__.py
│   ├── services/               # Business logic services
│   │   └── __init__.py
│   └── ui/                     # User interface components
│       ├── __init__.py
│       ├── components.py      # Reusable UI components
│       └── pages.py           # Page definitions and routing
├── data/                       # Database and data files
├── logs/                       # Application logs
├── static/                     # Static assets
├── uploads/                    # File uploads
├── main.py                     # Application entry point
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
├── .env                       # Environment variables (create from template)
└── README.md                  # This file
```

## 🔧 Configuration

### Environment Variables

Key configuration options in `.env`:

```bash
# Application
APP_NAME="GenAI Engineer Portfolio"
DEBUG=false
HOST=0.0.0.0
PORT=8080

# Security
SECRET_KEY=your-secure-secret-key

# AI Services (Optional)
OPENAI_API_KEY=your-openai-api-key

# Email (Optional)
SMTP_HOST=smtp.gmail.com
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-app-password

# Contact Information
CONTACT_EMAIL=your-email@domain.com
LINKEDIN_URL=https://linkedin.com/in/your-profile
GITHUB_URL=https://github.com/your-username
```

### Customization

1. **Personal Information**: Update contact details in `.env`
2. **Projects**: Modify project data in `app/ui/pages.py`
3. **Skills**: Update skills and proficiencies in `app/ui/pages.py`
4. **Styling**: Customize themes in `app/ui/components.py`
5. **Content**: Edit page content and descriptions throughout the UI files

## 🎨 Customization Guide

### Adding New Projects

Edit `app/ui/pages.py` in the `create_projects_page()` function:

```python
projects = [
    {
        "title": "Your Project Name",
        "description": "Project description",
        "tech_stack": ["Technology", "Stack", "Used"],
        "category": "Project Category",
        "github_url": "https://github.com/your-repo",
        "demo_url": "https://your-demo.com"
    },
    # Add more projects...
]
```

### Updating Skills

Modify the `skills_categories` dictionary in `create_skills_page()`:

```python
"Your Category": [
    ("Skill Name", proficiency_percentage),
    # Add more skills...
]
```

### Customizing Styling

Update CSS variables in `app/ui/components.py`:

```css
:root {
    --primary-color: #your-color;
    --secondary-color: #your-color;
    /* Customize other colors... */
}
```

## 🔌 API Endpoints

The application provides several API endpoints:

- `GET /api/v1/health` - Health check
- `POST /api/v1/contact` - Contact form submission
- `GET /api/v1/projects` - Get all projects
- `GET /api/v1/skills` - Get all skills
- `POST /api/v1/ai/text-generation` - AI text generation demo
- `POST /api/v1/ai/chat` - AI chat demo

## 🚀 Deployment

### Docker Deployment

```bash
# Build Docker image
docker build -t genai-portfolio .

# Run container
docker run -p 8080:8080 --env-file .env genai-portfolio
```

### Cloud Deployment

The application is ready for deployment on:

- **Heroku**: Use the included `Procfile`
- **AWS**: Deploy with Elastic Beanstalk or ECS
- **Google Cloud**: Use Cloud Run or App Engine
- **DigitalOcean**: Deploy with App Platform

### Environment-Specific Settings

For production deployment:

1. Set `DEBUG=false`
2. Use a strong `SECRET_KEY`
3. Configure proper database (PostgreSQL recommended)
4. Set up email service for contact form
5. Configure domain and SSL certificates

## 🔒 Security Considerations

- **Environment Variables**: Never commit `.env` files to version control
- **Secret Key**: Use a cryptographically secure random key in production
- **CORS**: Configure appropriate CORS origins for your domain
- **Rate Limiting**: Implement rate limiting for API endpoints
- **Input Validation**: All user inputs are validated using Pydantic models

## 🐛 Troubleshooting

### Common Issues

1. **Dependency Conflicts**: Ensure you're using the exact versions in `requirements.txt`
2. **Port Already in Use**: Change the `PORT` in `.env` or stop other services
3. **Permission Errors**: Ensure write permissions for `data/`, `logs/`, and `uploads/` directories
4. **Import Errors**: Verify virtual environment is activated and dependencies are installed

### Dependency Resolution

If you encounter the FastAPI/NiceGUI version conflict:

```bash
# Uninstall conflicting packages
pip uninstall fastapi nicegui

# Install compatible versions
pip install fastapi==0.109.2 nicegui==1.4.21

# Install remaining dependencies
pip install -r requirements.txt
```

### Logs and Debugging

- Check application logs in `logs/portfolio.log`
- Enable debug mode: `DEBUG=true` in `.env`
- Use browser developer tools for frontend issues

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Support

For support and questions:

- **Email**: contact@genai-engineer.com
- **GitHub Issues**: [Create an issue](https://github.com/genai-engineer/portfolio/issues)
- **Documentation**: Check this README and code comments

## 🙏 Acknowledgments

- **NiceGUI**: For the excellent Python-based UI framework
- **FastAPI**: For the high-performance web framework
- **OpenAI**: For AI capabilities and API access
- **Tailwind CSS**: For the utility-first CSS framework

---

**Built with ❤️ by GenAI Engineer**

*Transforming businesses with cutting-edge Generative AI solutions*