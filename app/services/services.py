from datetime import datetime, timedelta
import random

def get_donut_data():
    return {
        "donutSeries": [466, 861, 182],
        "donutLabels": ["Bom", "Mal", "Sem Resposta"],
        "donutColors": ["#008FFB", "#00E396", "#FEB019"],
    }

def get_line_data():
    return {
            "lineSeries": [
            {
                "name": "Bom",
                "data": [30, 40, 35, 50, 49, 60, 70, 91, 125],
                "color": "#008FFB",
            },
            {
                "name": "Mal",
                "data": [20, 29, 37, 36, 44, 45, 50, 58, 63],
                "color": "#00E396",
            },
            {
                "name": "Sem Resposta",
                "data": [10, 15, 23, 25, 28, 32, 38, 40, 48],
                "color": "#FEB019",
            },
        ],
        "lineCategories": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep"], 
    }
    
def get_spline_data():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 31)
    num_days = (end_date - start_date).days + 1
    monthly_data_bom = generate_monthly_data(30, 125, num_days)
    monthly_data_mal = generate_monthly_data(20, 63, num_days)
    monthly_data_sem_resposta = generate_monthly_data(10, 48, num_days)
    return {
        "splineAreaSeries": [
            {
                "name": "Bom",
                "data": monthly_data_bom,
                "color": "#008FFB",
            },
            {
                "name": "Mal",
                "data": monthly_data_mal,
                "color": "#00E396",
            },
            {
                "name": "Sem Resposta",
                "data": monthly_data_sem_resposta,
                "color": "#FEB019",
            },
        ],
        "splineAreaCategories": [(start_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(num_days)],
    }

def get_realtime_data():
    return {
        "lineSeries": [
            {
                "name": "Bom",
                "data": [random.randint(30, 125) for _ in range(9)],
                "color": "#008FFB",
            },
            {
                "name": "Mal",
                "data": [random.randint(20, 63) for _ in range(9)],
                "color": "#00E396",
            },
            {
                "name": "Sem Resposta",
                "data": [random.randint(10, 48) for _ in range(9)],
                "color": "#FEB019",
            },
        ],
        "lineCategories": [datetime.now().isoformat() for _ in range(9)],
    }

def generate_monthly_data(start_value, end_value, num_days):
    step = (end_value - start_value) / (num_days - 1)
    return [int(start_value + i * step) for i in range(num_days)]