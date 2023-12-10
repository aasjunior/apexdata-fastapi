from fastapi import APIRouter, HTTPException
from services import services

router = APIRouter()

@router.get("/donut-chart/data")
async def get_data():
    data = services.get_donut_data()
    if data:
        return data
    else:
        raise HTTPException(status_code=404, detail="Data not found")

@router.get("/line-chart/data")
async def get_data():
    data = services.get_line_data()
    if data:
        return data
    else:
        raise HTTPException(status_code=404, detail="Data not found")

@router.get("/spline-chart/data")
async def get_data():
    data = services.get_spline_data()
    if data:
        return data
    else:
        raise HTTPException(status_code=404, detail="Data not found")