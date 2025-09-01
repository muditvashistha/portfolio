# app.py
from flask import Flask, render_template
import json
import os

app = Flask(__name__)

def load_portfolio_data():
    """Load portfolio data from JSON file or return hardcoded data"""
    
   
    try:
        with open('data/portfolio_data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        
        return get_hardcoded_data()

def get_hardcoded_data():
    """Hardcoded portfolio data as fallback"""
    return {
        "personal_info": {
            "name": "John Doe",
            "title": "Full Stack Developer",
            "tagline": "Passionate about creating innovative web solutions",
            "email": "john.doe@example.com",
            "phone": "+1 (555) 123-4567",
            "location": "New York, NY",
            "profile_image": "images/profile.jpg"
        },  
        "about": {
            "description": "I'm a passionate full-stack developer with 3+ years of experience in building web applications. I love solving complex problems and creating user-friendly interfaces.",
            "resume_link": "path/to/resume.pdf"
        },
        "skills": [
            {"name": "Python", "level": 90},
            {"name": "JavaScript", "level": 85},
            {"name": "React", "level": 80},
            {"name": "Flask", "level": 85},
            {"name": "SQL", "level": 75},
            {"name": "Docker", "level": 70}
        ],
        "projects": [
            {
                "id": 1,
                "title": "E-commerce Platform",
                "description": "A full-stack e-commerce solution with payment integration",
                "technologies": ["Python", "Flask", "PostgreSQL", "React"],
                "image": "images/projects/ecommerce.jpg",
                "github_link": "https://github.com/johndoe/ecommerce",
                "live_link": "https://myecommerce.com",
                "featured": True
            },
            {
                "id": 2,
                "title": "Task Management App",
                "description": "A collaborative task management tool with real-time updates",
                "technologies": ["Node.js", "Socket.io", "MongoDB", "Vue.js"],
                "image": "images/projects/taskapp.jpg",
                "github_link": "https://github.com/johndoe/taskapp",
                "live_link": "https://mytaskapp.com",
                "featured": True
            },
            {
                "id": 3,
                "title": "Weather Dashboard",
                "description": "A responsive weather application with location-based forecasts",
                "technologies": ["JavaScript", "API Integration", "CSS3", "HTML5"],
                "image": "images/projects/weather.jpg",
                "github_link": "https://github.com/johndoe/weather",
                "live_link": "https://myweather.com",
                "featured": False
            }
        ],
        "experience": [
            {
                "position": "Senior Frontend Developer",
                "company": "Tech Solutions Inc.",
                "duration": "2022 - Present",
                "description": "Led frontend development for multiple client projects, implemented responsive designs and optimized performance."
            },
            {
                "position": "Full Stack Developer",
                "company": "StartupXYZ",
                "duration": "2020 - 2022",
                "description": "Developed and maintained web applications using Python, Flask, and React. Collaborated with cross-functional teams."
            }
        ],
        "education": [
            {
                "degree": "Bachelor of Science in Computer Science",
                "institution": "University of Technology",
                "year": "2020",
                "gpa": "3.8/4.0"
            }
        ],
        "social_links": {
            "github": "https://github.com/johndoe",
            "linkedin": "https://linkedin.com/in/johndoe",
            "twitter": "https://twitter.com/johndoe",
            "portfolio": "https://johndoe.dev"
        }
    }

@app.route('/')
def portfolio():
    """Main route that renders the single-page portfolio"""
    
    
    data = load_portfolio_data()
    
    
    featured_projects = [project for project in data['projects'] if project.get('featured', False)]
    
    # Pass all data to template
    return render_template('index.html', 
                         projects=data['projects'],
                         social_links=data['social_links'])

@app.route('/api/projects')
def get_projects():
    """Optional: API endpoint to get projects data (for AJAX calls)"""
    data = load_portfolio_data()
    return data['projects']

if __name__ == '__main__':
    app.run(debug=True)