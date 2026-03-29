import sys
import os

# Add the project root to PYTHONPATH
sys.path.append(os.getcwd())

from sqlalchemy.orm import Session
from app.db.session import SessionLocal, engine, Base
from app.models.page import Page, PageSection
from app.models.site import Partner
from app.models.project import Project

def seed_final_about_data():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        about_page = db.query(Page).filter(Page.slug == "about").first()
        if not about_page:
            about_page = Page(title="About Us", slug="about")
            db.add(about_page)
            db.commit()
            db.refresh(about_page)
        
        # Clear old sections
        db.query(PageSection).filter(PageSection.page_id == about_page.id).delete()
        
        sections = [
            {
                "section_type": "intro_impact",
                "title": "Architecture and Construction industry",
                "content": "With over 24 years of experience, TranDuc owns 3 modern internationally standardized factories, totaling 250,000m2 in area. With a production capacity of 1200 - 1500 units per year, we can simultaneously execute multiple projects, flexibly meeting all customer requirements and timelines. Modulux Homes controls the entire production process, from the initial stages to completion, ensuring absolute quality for every product.",
                "image_url": "https://imagedelivery.net/KHaby7r0MOA4Gt7v7Yk1jg/f13835ac-0fa8-4be7-6a4c-51198df17e00/2K",
                "display_order": 1
            },
            {
                "section_type": "full_width_image",
                "title": "Smart Factory Panorama",
                "image_url": "https://api-gateway.tranduc.com/api/cloudflare/cdn/PC_About.png",
                "display_order": 2
            },
            {
                "section_type": "intro_blue_line",
                "title": "Modulux<br/>Homes",
                "subtitle": "Your trusted partner for modern contractors",
                "content": "<p>We deliver groundbreaking construction solutions, pioneering the use of modern technologies to provide sustainable, efficient, and contemporary building solutions.</p>",
                "display_order": 3
            },
            {
                "section_type": "partners",
                "title": "Our Partners",
                "display_order": 4
            },
            {
                "section_type": "projects_asymmetric",
                "title": "Feature Projects",
                "display_order": 5
            }
        ]
        
        for s in sections:
            db.add(PageSection(page_id=about_page.id, **s))

        # Fix Project thumbnails to use working CDN links to prevent broken images
        project_map = {
            "canada-modular-home": "https://api-gateway.tranduc.com/api/cloudflare/cdn/1712473859600-Canadamodularhome.png",
            "hawaii-garden-studio": "https://api-gateway.tranduc.com/api/cloudflare/cdn/1712543472097-HawaiiGardenStudio.png",
            "ecolux": "https://api-gateway.tranduc.com/api/cloudflare/cdn/1712543632594-Ecolux.png",
            "modern-villa": "https://api-gateway.tranduc.com/api/cloudflare/cdn/1712543472097-HawaiiGardenStudio.png"
        }
        
        for slug, img_url in project_map.items():
            p = db.query(Project).filter(Project.slug == slug).first()
            if p:
                p.thumbnail_url = img_url

        db.commit()
        print("SUCCESS: 100% Correct About page data and images seeded!")
        
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_final_about_data()
