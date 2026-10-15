from pydantic import BaseModel, ValidationError,StringConstraints, field_validator
from typing import Annotated, Literal
from datetime import date, datetime


class Message (BaseModel):

    ask : Annotated[
        str,
        StringConstraints(strip_whitespace=True, min_length=1)
    ]

class ClassificationResponse (BaseModel):

    intent : Literal[
        "create_appointment",
        "cancel_appointment",
        "check_availability",
        "reschedule_appointment",
        "unknown"
    ]
    date: str | None = None
    time : str | None = None

    @field_validator("date", mode="after")
    @classmethod
    def validate_date(cls, value):

        if value is None :
            return value

        today = date.today()
        convert_date = date.fromisoformat(value)

        if convert_date.isoformat() != value:
            raise ValueError("Invalid date format. Expected YYYY-MM-DD")

        if convert_date < today :
            raise ValueError("Invalid date")

        return value

    @field_validator("time", mode="after")
    @classmethod
    def validate_time (cls, value):

        if value is None:
            return value

        if len(value) != 5 or value[2] != ":":

            raise ValueError ("Invalid time format. Expected HH:MM")

        try:

            datetime.strptime(value, "%H:%M")

            return value
        except ValueError:
            raise ValueError ("Invalid time format. Expected HH:MM")