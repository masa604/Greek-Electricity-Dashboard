from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FutureData
from datetime import date, timedelta

# View for the dashboard
def dashboard(request):
    return render(request, 'market/dashboard.html')

# API endpoint for fetching futures data
@api_view(['GET'])
def futures_data(request):
    end_date = date.today()
    start_date = end_date - timedelta(days=7)
    
    data = FutureData.objects.filter(
        date__range=[start_date, end_date],
        instrument__startswith='GREBY'
    ).order_by('date')
    
    response_data = []
    previous_price = None
    
    for item in data:
        current_price = item.avg_price
        if previous_price is not None and previous_price != 0:
            pct_change = ((current_price - previous_price) / previous_price) * 100
        else:
            pct_change = 0
        
        response_data.append({
            'date': item.date.strftime('%Y-%m-%d'),
            'price': current_price,
            'pct_change': round(pct_change, 2)
        })
        
        previous_price = current_price
    
    return Response({'data': response_data})