from odmantic import AIOEngine

__all__ = (
    'engine',
)

# Engine for a local database
from config import DATABASE_NAME

engine = AIOEngine(database=DATABASE_NAME)

# Engine for an atlas or hosted database
# from motor.motor_asyncio import AsyncIOMotorClient
# from config import DATABASE_URL
# client = AsyncIOMotorClient(DATABASE_URL)
# engine = AIOEngine(motor_client=client, database='kaggle_30dML')

