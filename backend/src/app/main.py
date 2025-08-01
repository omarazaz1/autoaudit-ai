# src/main.py
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os
from utils.pdf_parser import extract_text_from_pdf

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploaded_docs"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def read_root():
    return {"message": "AutoAudit AI backend is live!"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    # Save file
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    # Extract PDF text
    extracted_text = extract_text_from_pdf(file_path)
    print("\n--- Extracted PDF Text ---\n")
    print(extracted_text[:1000])  # print preview to console

    return {
        "message": f"File '{file.filename}' uploaded and parsed.",
        "text_preview": extracted_text[:300] + "..."
    }
