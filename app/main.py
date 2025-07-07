from fastapi import FastAPI
from app.database import Base, engine
from app.routers import product_router, supplier_router, buyer_router, auth_router, user_router, sell_router, excel_router
from app.models import product, supplier, buyer
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers for different functionalities
app.include_router(auth_router.router, prefix="/auth", tags=["Authentication"])

app.include_router(user_router.router, prefix="/users", tags=["Users"])

app.include_router(product_router.router, prefix="/products", tags=["Products"])
app.include_router(supplier_router.router, prefix="/suppliers", tags=["Suppliers"])
app.include_router(buyer_router.router, prefix="/buyers", tags=["Buyers"])

# Include the sell router for handling sales-related operations
app.include_router(sell_router.router, prefix="/sells", tags=["Sells"])

# Sell data export functionality
app.include_router(excel_router.router, prefix="/exports", tags=["Exports"])

@app.get("/")
def root():
    return {"message": "Inventory API MVC is running"}