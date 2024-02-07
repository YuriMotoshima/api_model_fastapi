from fastapi import FastAPI

from fast_zero.schemas import (Message,UserSchema,UserPublic)

app = FastAPI()


@app.get('/', status_code=200, response_model=Message)
def read_root():
    return {'message': 'Olá mundo'}

@app.post('/users/', status_code=201, response_model=UserPublic)
def create_user(user:UserSchema):
    ...