from sqlmodel import SQLModel, Session, create_engine
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL, echo=False)


def get_session():
    with Session(engine) as session:
        yield session


def create_all_tables():
    import app.modules.products.models
    import app.modules.orders.models
    import app.modules.payments.models
    SQLModel.metadata.create_all(engine)
