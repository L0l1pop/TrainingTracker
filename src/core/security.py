from authx import AuthX, AuthXConfig

from src.core.config import settings


access_config = AuthXConfig(
    JWT_SECRET_KEY=settings.JWT_SECRET,
    JWT_TOKEN_LOCATION=["headers"],
)


refresh_config = AuthXConfig(
    JWT_SECRET_KEY=settings.JWT_REFRESH_SECRET,
    JWT_TOKEN_LOCATION=["headers"],
)


access_security = AuthX(config=access_config)
refresh_security = AuthX(config=refresh_config)
