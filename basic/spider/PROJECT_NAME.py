from grab.spider import Spider, Task
from grab import Grab

from project.database import db


class {{ PROJECT_NAME_CAMELCASE }}Spider(Spider):
    def task_generator(self):
        pass
