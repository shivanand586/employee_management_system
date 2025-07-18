from scr.db.models import get_session

def get_db():
    db = get_session()
    try:
        yield db
    finally:
        if db:
            db.close()
            