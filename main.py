from fastapi import FastAPI, Depends, Request, Query
from pagination import PagedResponseSchema, PageParams, paginate
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db import get_db
from user import User

app = FastAPI()

class UserSchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

@app.get("/users", response_model=PagedResponseSchema[UserSchema])
def get_users(request: Request, page_params: PageParams = Depends(PageParams), db: Session = Depends(get_db)):

    # # Add 1000 users to the database

    # for i in range(1000):
    #     db.add(User(id=i, name=f"User {i}"))
    
    # db.commit()

    query = db.query(User)

    return paginate(page_params, query, UserSchema)
