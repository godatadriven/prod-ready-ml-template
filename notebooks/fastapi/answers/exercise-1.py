
from dataclasses import dataclass
from datetime import datetime

from pydantic import BaseModel


# a)

class PydanticUser(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None  = None
    friend_ids: list[int] | None = None

# b)

user = PydanticUser(**external_data)
user_dataclass = DataClassUser(**external_data)

# c)

external_data_str = {
    "id": "123",
    "signup_ts": "2023-09-28 12:00",
    "friend_ids": [1, 2, "3"],
}

print("Pydantic: ", PydanticUser(**external_data_str))
print("Data class: ", DataClassUser(**external_data_str))
