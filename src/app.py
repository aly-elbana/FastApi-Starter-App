from fastapi import FastAPI, HTTPException
from src.schema import Post
from src.db import PostSchema, create_db_and_tables, get_async_session

app = FastAPI()

text_posts = {
    1: {"title": "Intro to FastAPI", "content": "FastAPI makes backend development super fast and clean."},
    2: {"title": "Python Tips", "content": "Use list comprehensions for cleaner and faster Python code."},
    3: {"title": "C++ for AI", "content": "Leverage C++ performance with modern AI integrations."},
    4: {"title": "React & Node", "content": "Full-stack magic happens when React meets Node.js."},
    5: {"title": "Data Cleaning 101", "content": "Good machine learning starts with good data preprocessing."},
    6: {"title": "Weekend Motivation", "content": "Sometimes, a coffee and a walk solve more bugs than hours of debugging."},
    7: {"title": "Deep Learning", "content": "Neural networks are powerful but remember: garbage in, garbage out."},
    8: {"title": "API Design", "content": "Always document your API endpoints — future you will thank you."},
    9: {"title": "Robotics & AI", "content": "When hardware meets intelligence, the future begins."},
    10: {"title": "Career Advice", "content": "Build projects that show your skills, not just your knowledge."}
}

@app.get("/posts")
async def get_all_posts(limit: int = None):
        
    if limit:
        if limit > len(text_posts):
            return text_posts
        return list(text_posts.values())[:limit]
    
    return text_posts

@app.get("/posts/{id}")
async def get_post(id: int)->Post:
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post Not Found")
    return text_posts.get(id)
    
@app.post("/posts")
async def create_post(post: Post)->Post:
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post