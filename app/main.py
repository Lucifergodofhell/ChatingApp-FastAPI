from fastapi import FastAPI
from app.core.database import engine
from app.domains.member import friends_model
from app.domains.photos import photo_models
from app.domains.users import user_models,router as user_router
from app.domains.auth import router as auth_router
from app.domains.member import router as friend_router
from app.domains.photos import router as photo_router
from app.domains.chat import router as chat_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI();

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            
    allow_credentials=True,        
    allow_methods=["*"],               
    allow_headers=["*"]
)
user_models.Base.metadata.create_all(bind = engine);
photo_models.Base.metadata.create_all(bind = engine);
friends_model.Base.metadata.create_all(bind = engine);


app.include_router(router=user_router.router)
app.include_router(router=auth_router.router)
app.include_router(router=friend_router.router)
app.include_router(router=photo_router.router)
app.include_router(router=chat_router.router)

