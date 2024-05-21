from fastapi import APIRouter, Depends, HTTPException
from app.schema.users import UserSchema
from app.config.db import get_db
from app.utils import get_hashed_password, verify_password, create_access_token, create_refresh_token
from sqlalchemy.orm import Session
from app.models.users import User
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer



auth = APIRouter()

oauth = OAuth2PasswordBearer(
    tokenUrl='/login',
    scheme_name='JWT'
)

@auth.post('/singup', tags=['Authentication'])
async def signIn(user: UserSchema, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(
            status_code=500,
            detail= "email already "
        )
    user_details = User(first_name= user.first_name, last_name= user.last_name, email = user.email, password = get_hashed_password(user.password), phone= user.phone)
    db.add(user_details)
    db.commit()
    db.refresh(user_details)
    return user_details


@auth.post('/login', tags=["Authentication"])
async def login(formData: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    fetch_user = db.query(User).filter(User.email == formData.username).first()
    if fetch_user is None:
        raise HTTPException(status_code=400, detail="Incorrect Email or Password")
    
    if not verify_password(formData.password, fetch_user.password):
        raise HTTPException(status_code=400, detail="Incorrect password")
    
    access_token = create_access_token(fetch_user.email)
    refresh_token = create_refresh_token(fetch_user.email)
    return {"status": 200, "access_token": access_token, "refresh_token": refresh_token}


