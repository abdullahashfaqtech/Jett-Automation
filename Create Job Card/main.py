"""
Main script to run the JETT Automation project.
"""
import logging
from job_card import JobCardCreator
from config import ADMIN_CREDENTIALS

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    """Main function to run the automation."""
    job_creator = None
    try:
        # Initialize job card creator
        job_creator = JobCardCreator()
        
        # Login as admin
        job_creator.login(ADMIN_CREDENTIALS)
        
        # Select branch
        job_creator.select_branch()
        
        # Create job card
        plate_number = "58-2760"  # Example plate number
        job_creator.create_job_card(plate_number)
        
        logger.info("Job card creation completed successfully")
        
    except Exception as e:
        logger.error(f"Automation failed: {str(e)}")
        raise
    finally:
        # Clean up
        if job_creator:
            job_creator.quit()

if __name__ == "__main__":
    main() 