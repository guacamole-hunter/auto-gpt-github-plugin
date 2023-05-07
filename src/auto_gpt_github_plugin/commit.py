import os
import dotenv


class Commit():
    def check_auth():
        if os.getenv('GITHUB_TOKEN') is None:
            raise Exception('GITHUB_TOKEN not set')
        else:
            return True