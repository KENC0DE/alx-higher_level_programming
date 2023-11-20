#!/usr/bin/python3
"""First state
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    first_state = session.query(State).filter(State.id == 1).first()
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print()

    session.close()
