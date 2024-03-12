from fastapi import FastAPI
from fast_zero.schemas import Message, UserSchema, UserList, UserPublic, UserDB

app = FastAPI()


database = []


@app.get('/', status_code=200, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.get('/users/', response_model=UserList)
def read_users():
    return {'users': database}


@app.post('/users/', status_code=201, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_with_id)
    return user_with_id
