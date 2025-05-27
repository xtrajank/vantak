'''FastAPI app'''
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

BASE_URL = 'http://localhost:5173'

app = FastAPI(title='vantak')

app.add_middleware(
    CORSMiddleware, 
    allow_origins=[BASE_URL],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)