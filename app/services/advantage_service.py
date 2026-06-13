import logging

import requests

from app.core.config import settings


logger = logging.getLogger(__name__)


class AdvantageService:

    def send(self, payload: dict) -> bool:

        try:

            response = requests.post(
                settings.ADVANTAGE_URL,
                json=payload,
                timeout=5
            )

            response.raise_for_status()

            logger.info(
                "Event successfully sent to AdVantage"
            )

            return True

        except Exception as e:

            logger.error(
                f"Failed to send event: {e}"
            )

            return False