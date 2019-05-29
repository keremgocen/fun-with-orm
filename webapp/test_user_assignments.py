import unittest
from models import User
from datetime import datetime


class UserTests(unittest.TestCase):
    def test_assign_properties_correctly_updates_properties(self):
        email = "test_user@email.com"
        u = User(email)
        u.first_name = "John"
        u.last_name = "Doe"

        new_props = dict([
            ('first_name', 'kerem'),
            ('last_name', None),
            ('some_random_property', datetime.now())
        ])

        u.assign_properties(**new_props)

        self.assertEqual(u.first_name, "kerem")
        self.assertEqual(u.email, email)
        self.assertIsNone(u.last_name)
        self.assertIs(hasattr(u, "some_random_property"), False)

    def test_assign_properties_does_not_modify_dates(self):
        email = "test_user@email.com"
        u = User(email)
        u.first_name = "John"
        u.last_name = "Doe"

        actual_created_time = u.created_at
        actual_updated_time = u.updated_at
        actual_deleted_time = u.deleted_at

        mock_time = datetime.strptime('09/19/18 13:55:26', '%m/%d/%y %H:%M:%S')

        new_props = dict([
            ('created_at', mock_time),
            ('updated_at', mock_time),
            ('deleted_at', mock_time)
        ])

        u.assign_properties(**new_props)

        self.assertNotEqual(actual_created_time, mock_time)
        self.assertNotEqual(actual_updated_time, mock_time)
        self.assertNotEqual(actual_deleted_time, mock_time)

if __name__ == "__main__":
    unittest.main()
