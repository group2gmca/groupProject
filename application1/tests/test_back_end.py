import unittest

from flask import abort, url_for
from flask_testing import TestCase

from application import app, db
from application.models import Prize
class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testdb'
        app.config.update(
                SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:root@localhost:3306/testdb'        )

        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all()

        # create test admin user
        test1 = Prize(id=1, username="abc12345", prize="£10 gift card")

        # create test non-admin user
        test2 = Prize(id=2, username="123abcde", prize="£30 gift card")
        # save users to database
        db.session.add(test1)
        db.session.add(test2)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()


class TestViews(TestBase):

    def test_homepage_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_prizepage_view(self):
        response = self.client.get('/prize/abc1234')
        self.assertEqual(response.status_code, 200)
