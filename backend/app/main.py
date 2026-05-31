from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.database import create_all_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        create_all_tables()
    except Exception:
        pass
    yield


app = FastAPI(
    title="Implementacion MP FastAPI",
    description="API de referencia para integración con MercadoPago",
    version="1.0.0",
    lifespan=lifespan,
)

cors_origins = [o.strip() for o in settings.CORS_ORIGINS.split(",")]
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_ngrok_skip_warning(request: Request, call_next):
    response = await call_next(request)
    response.headers["ngrok-skip-browser-warning"] = "true"
    return response


@app.get("/health")
def health():
    return {"status": "ok", "version": "1.0.0"}


from app.modules.products.router import router as products_router
from app.modules.orders.router import router as orders_router
from app.modules.payments.router import router as payments_router

app.include_router(products_router)
app.include_router(orders_router)
app.include_router(payments_router)
