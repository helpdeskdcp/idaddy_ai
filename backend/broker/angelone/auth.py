from __future__ import annotations

from SmartApi import SmartConnect
import pyotp

from backend.core.settings import get_settings


class AngelAuth:
    """
    Angel One SmartAPI Authentication
    """

    def __init__(self):
        self.settings = get_settings()

        self.client = SmartConnect(
            api_key=self.settings.ANGEL_API_KEY
        )

        self.session = None
        self.jwt_token = None
        self.refresh_token = None
        self.feed_token = None

    def login(self):
        """
        Login to Angel One
        """

        totp = pyotp.TOTP(
            self.settings.ANGEL_TOTP_SECRET
        ).now()

        self.session = self.client.generateSession(
            self.settings.ANGEL_CLIENT_ID,
            self.settings.ANGEL_PASSWORD,
            totp,
        )

        if not self.session["status"]:
            raise Exception(
                self.session.get("message", "Login Failed")
            )

        data = self.session["data"]

        self.jwt_token = data["jwtToken"]
        self.refresh_token = data["refreshToken"]
        self.feed_token = data["feedToken"]

        return self.session

    def logout(self):
        """
        Logout
        """

        try:
            return self.client.terminateSession(
                self.settings.ANGEL_CLIENT_ID
            )
        except Exception:
            return False

    def get_profile(self):
        """
        User Profile
        """

        if self.refresh_token is None:
            raise Exception("Not logged in")

        return self.client.getProfile(
            self.refresh_token
        )

    def get_feed_token(self):
        """
        Feed Token
        """

        if self.feed_token is None:
            raise Exception("Login first")

        return self.feed_token

    def get_client(self):
        """
        Return SmartConnect object
        """

        return self.client
