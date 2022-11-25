import math
from datetime import datetime

# for generating agora token
from agora_token_builder import RtcTokenBuilder

# Agora class containing function to generate token
class Agora:
    app_id = "fd75b2a7d3f84bd4abe49b657bd0d750"
    app_certificate = "350797fde3c142ce9f2f9afe6da73d34"

    def __init__(self):
        self.app_id = "fd75b2a7d3f84bd4abe49b657bd0d750"
        self.app_certificate = "350797fde3c142ce9f2f9afe6da73d34"

    def get_time(self):
        """
        to generate and return privilegeExpiredTs
        """
        current_time = math.floor((datetime.today()).timestamp())
        privilegeExpiredTs = current_time + 36000

        return privilegeExpiredTs

    def generate_token(self, uid):
        """
        to generate Agora Token for a channel
        """
        token = RtcTokenBuilder.buildTokenWithUid(
            self.app_id, self.app_certificate, "helpChannel", uid, True, self.get_time()
        )

        return token
