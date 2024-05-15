from datetime import datetime

from pydantic import BaseModel, field_validator

# a) and b)

class PydanticUser(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friend_ids: list[int] | None = None

    @field_validator("signup_ts")
    def signup_ts_not_in_future(cls, v):
        print("Validating that the signup time is not in the future!")
        assert v <= datetime.now(), 'Signup timestamp cannot be in the future'
        return v

# Uncomment:
# PydanticUser(id=1, signup_ts="definitely not a timestamp")

# c)

class PydanticUser(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friend_ids: list[int] | None = None
    password1: str
    password2: str

    @field_validator("signup_ts")
    def signup_ts_not_in_future(cls, v):
        assert v <= datetime.now(), 'Signup timestamp cannot be in the future'
        return v

    @field_validator('password2')
    def passwords_match(cls, v, info):
        if v != info.data['password1']:
            raise ValueError('passwords do not match')
        return v

external_data = {
    "id": "123",
    "signup_ts": "2019-06-01 12:22",
    "friend_ids": [1, 2, "3"],
    "password1": "passypass",
    "password2": "passypass"
    # "password2": "passypazz"

}

PydanticUser(**external_data)
