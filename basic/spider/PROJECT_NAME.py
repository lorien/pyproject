from grab.spider import Spider, Task
from grab import Grab
from grab.spider.decorators import integrity
from weblib.error import DataNotValid

from project.database import db


class {{ PROJECT_NAME_CAMELCASE }}Spider(Spider):
    def task_generator(self):
        pass
