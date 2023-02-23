from fastapi import FastAPI,Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
import models
from database import engine,SessionLocal
from database_schemes import User,Story,Block


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def index():
    return HTMLResponse("<h1>hi you are at home page</h1>")

@app.post("/user")
def create_user(user:User,db = Depends(get_db)):
    db_user = models.User(username=user.username,email = user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users")
def get_all_users(skip: int = 0, limit: int = 100,db=Depends(get_db)):
    return db.query(models.User).offset(skip).limit(limit).all()


@app.post("/story")
def create_story(story:Story,username:str,db = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == username).first()
    db_story = models.Story(title = story.title,description=story.description,owner=user)
    db.add(db_story)
    db.commit()
    db.refresh(db_story)
    return db_story

@app.get("/stories")
def get_all_stories(skip: int = 0, limit: int = 100,db=Depends(get_db)):
    return db.query(models.Story).offset(skip).limit(limit).all()

@app.get("/stories/{username}")
def get_user_stories(username:str,skip: int = 0, limit: int = 100,db=Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == username).first()
    return db.query(models.Story).filter(models.Story.owner == user).offset(skip).limit(limit).all()

@app.get("/story/{id}")
def get_story_by_id(post_id:int,db = Depends(get_db)):
    story = db.query(models.Story).filter(models.Story.id == post_id).first()
    blocks = db.query(models.Block).filter(models.Block.story == story).all()
    return blocks

@app.post("/block")
def create_story(block:Block,storyid:int,db = Depends(get_db)):
    story = db.query(models.Story).filter(models.Story.id == storyid).first()
    db_block = models.Block(body = Block.body,story = story)
    db.add(db_block)
    db.commit()
    db.refresh(db_block)
    return db_block