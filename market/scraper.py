import random
from datetime import date, timedelta
from django.utils import timezone
from .models import FutureData
import logging

logger = logging.getLogger(__name__)

def scrape_enex_data():
    try:
        # Clean up existing data
        FutureData.objects.all().delete()
        
        # Generate mock data for the last 7 days
        instruments = ["GREBY25", "GREBY26"]
        base_price = 80.0
        
        for i in range(7):
            current_date = date.today() - timedelta(days=i)
            
            for instrument in instruments:
                price = round(base_price * random.uniform(0.85, 1.15), 2)
                
                FutureData.objects.create(
                    instrument=instrument,
                    date=current_date,
                    avg_price=price,
                    scraped_at=timezone.now()
                )
        
        logger.info(f"Dados mock gerados: {FutureData.objects.count()} registos")
        return True
        
    except Exception as e:
        logger.error(f"Erro crítico: {str(e)}", exc_info=True)
        return False