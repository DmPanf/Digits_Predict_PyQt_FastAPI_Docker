from fastapi import FastAPI, UploadFile, File
from PIL import Image
import io

app = FastAPI()

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    # Здесь вы можете добавить свой код для предсказания
    prediction = "Your prediction here"
    return {"filename": file.filename, "prediction": prediction}
