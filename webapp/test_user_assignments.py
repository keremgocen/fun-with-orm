import unittest
from models import User


class UserTests(unittest.TestCase):
    def test_assign_properties_correctly_updates_properties(self):
        email = "test_user@email.com"
        u = User(email)
        u.first_name = "John"
        u.last_name = "Doe"

        new_props = dict([
            ('first_name', 'kerem'),
            ('last_name', None),
            ('some_random_property', 5)
        ])

        u.assign_properties(**new_props)

        self.assertEqual(u.first_name, "kerem")
        self.assertEqual(u.email, email)
        self.assertIsNone(u.last_name)
        self.assertIs(hasattr(u, "some_random_property"), False)

if __name__ == "__main__":
    unittest.main()
