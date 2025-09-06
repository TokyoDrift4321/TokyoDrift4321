from fastapi import FastAPI

# יוצרים מופע של FastAPI (השרת שלנו)
app = FastAPI()

# נקודת קצה בסיסית לבדיקה
@app.get("/health")
def health_check():
    return {"ok": True, "message": "Server is running!"}