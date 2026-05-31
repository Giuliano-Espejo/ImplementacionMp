from sqlmodel import SQLModel, Session, create_engine
from sqlalchemy.engine import URL
from app.core.config import settings

engine = create_engine(URL.create(**settings.db_conn_params), echo=False)


def get_session():
    with Session(engine) as session:
        yield session


def create_all_tables():
    import app.modules.products.models
    import app.modules.orders.models
    import app.modules.payments.models
    SQLModel.metadata.create_all(engine)
