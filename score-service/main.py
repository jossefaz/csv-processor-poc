from fastapi import FastAPI
import random
import time

app = FastAPI()


@app.get("/score")
def get_score(student_id: str, course_id: str):
    time.sleep(random.randint(1, 5))
    score = random.randint(0, 100)
    return {"student_id": student_id, "course_id": course_id, "score": score}
