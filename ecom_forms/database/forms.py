import re

class FieldType:
    def __init__(self, field_value: str) -> None:

        type_defined = False
        if FieldType.__check_date_type(field_value):
            self.type = "date"
            type_defined = True

        if FieldType.__check_phone_type(field_value):
            self.type = "phone"
            type_defined = True

        if FieldType.__check_email_type(field_value):
            self.type = "email"
            type_defined = True

        if not type_defined:
            self.type = "text"


    @staticmethod
    def __check_email_type(value: str):
        result = re.match(r"^.+@.+\.(com|ru)$", value)
        
        if result:
            return True
        
        return False

    @staticmethod
    def __check_phone_type(value: str):
        result = re.match("^\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}$", value)

        if result:
            return True
        
        return False

    @staticmethod
    def __check_date_type(value: str):
        result_with_dot = re.match(r"^(([0-2][0-9])|(3[01]))\.((0[1-9])|(1[0-2]))\.[0-9]{4}$", value)
        result_with_dash = re.match(r"^[0-9]{4}-((0[1-9])|(1[0-2]))-(([0-2][0-9])|(3[01]))$", value)

        if result_with_dot or result_with_dash:
            return True
        
        return False


class ValidateForm:
    def __init__(self, fields_values: dict) -> None:

        self.fields_values = fields_values

        for name, value in self.fields_values.items():
            self.fields_values[name] = FieldType(value).type

        print(self.fields_values)
            






if __name__ == "__main__":
    form = ValidateForm({"amobus": "graubert34@yandex.ru", "bebus": "+7 185 678 23 43", "agugus": "gdfgdfg"})