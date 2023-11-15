import unittest
from ecom_forms.forms_functions.forms import ValidateForm, FieldType


class TestFormsFunctions(unittest.TestCase):

    users_form1 = {
            "vestibule": "west",
            "address": "West boston 45"
        }
    form1 = ValidateForm(users_form1)

    users_form2 = {
        "birthday_hum": "Jason",
        "another": "some text"
    }
    form2 = ValidateForm(users_form2)

    users_form3 = {
        "birthday_hum": "Jason",
        "birthday_date": "14.04.2022"

    }
    form3 = ValidateForm(users_form3)

    users_form4 = {
        "some_shop": "Diksia",
        "phone": "+7 435 645 23 43"
    }
    form4 = ValidateForm(users_form4)

    users_form5 = {
        "phone_number": "+7 345 235 34 67"
    }
    form5 = ValidateForm(users_form5)

    users_form6 = {
        "birthday_date": "2022-03-13"

    }
    form6 = ValidateForm(users_form6)

    users_form7 = {
        "website_name": "google"
    }
    form7 = ValidateForm(users_form7)

    def test_validation(self):
        self.assertEqual(TestFormsFunctions.form1.find_suitable_form(), TestFormsFunctions.form1.fields_values)
        self.assertEqual(TestFormsFunctions.form2.find_suitable_form(), TestFormsFunctions.form2.fields_values)
        self.assertEqual(TestFormsFunctions.form3.find_suitable_form(), "Birthdays")
        self.assertEqual(TestFormsFunctions.form4.find_suitable_form(), TestFormsFunctions.form4.fields_values)
        self.assertEqual(TestFormsFunctions.form5.find_suitable_form(), "Store")
        self.assertEqual(TestFormsFunctions.form6.find_suitable_form(), "Birthdays")
        self.assertEqual(TestFormsFunctions.form7.find_suitable_form(), "Website")

    def test_types(self):
        self.assertEqual(
            TestFormsFunctions.form1.fields_values,
            {
                "vestibule": "text",
                "address": "text"
            }
        )
        self.assertEqual(
            TestFormsFunctions.form2.fields_values,
            {
                "birthday_hum": "text",
                "another": "text"
            }
        )
        self.assertEqual(
            TestFormsFunctions.form3.fields_values,
            {
                "birthday_hum": "text",
                "birthday_date": "date"
            }
        )
        self.assertEqual(
            TestFormsFunctions.form4.fields_values,
            {
                "some_shop": "text",
                "phone": "phone"
            }
        )
        self.assertEqual(
            TestFormsFunctions.form5.fields_values,
            {
                "phone_number": "phone"
            }
        )
        self.assertEqual(
            TestFormsFunctions.form6.fields_values,
            {
                "birthday_date": "date"
            }
        )
        self.assertEqual(
            TestFormsFunctions.form7.fields_values,
            {
                "website_name": "text"
            }
        )

    def test_regulars(self):

        FieldType._FieldType__check_email_type
        FieldType._FieldType__check_phone_type
        FieldType._FieldType__check_date_type

        self.assertEqual(FieldType._FieldType__check_email_type("graus@yandex.com"), True)
        self.assertEqual(FieldType._FieldType__check_email_type("graus@yandex.ru"), True)
        self.assertEqual(FieldType._FieldType__check_email_type("grausyandex.com"), False)

        self.assertEqual(FieldType._FieldType__check_phone_type("+7 495 789 23 56"), True)
        self.assertEqual(FieldType._FieldType__check_phone_type("+7 495 789 23 563"), False)
        self.assertEqual(FieldType._FieldType__check_phone_type("85647235234"), False)

        self.assertEqual(FieldType._FieldType__check_date_type("14.05.2022"), True)
        self.assertEqual(FieldType._FieldType__check_date_type("32.05.2002"), False)
        self.assertEqual(FieldType._FieldType__check_date_type("2012-03-12"), True)

        field1 = FieldType("graus@yandex.com")
        field2 = FieldType("some text")
        field3 = FieldType("20.12.2012")
        field4 = FieldType("+7 985 345 23 12")
        field5 = FieldType("+7 53 235 23 42")

        self.assertEqual(field1.type, "email")
        self.assertEqual(field2.type, "text")
        self.assertEqual(field3.type, "date")
        self.assertEqual(field4.type, "phone")
        self.assertEqual(field5.type, "text")


