from fastapi import APIRouter
from scr.routes.employee import router as employee_router

router = APIRouter()

router.include_router(employee_router, tags=["Employee Management"])