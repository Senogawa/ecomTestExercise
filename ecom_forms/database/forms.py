import re

class FieldType:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def check_email_type(value: str):
        result = re.match(r"^.+@.+\.(com|ru)$", value)
        
        if result:
            return True
        
        return False

    @staticmethod
    def check_phone_type(value: str):
        result = re.match("^\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}$", value)

        if result:
            return True
        
        return False

    @staticmethod
    def check_date_type(value: str):
        result_with_dot = re.match(r"^(([0-2][0-9])|(3[01]))\.((0[1-9])|(1[0-2]))\.[0-9]{4}$", value)
        result_with_dash = re.match(r"^[0-9]{4}-((0[1-9])|(1[0-2]))-(([0-2][0-9])|(3[01]))$", value)

        if result_with_dot or result_with_dash:
            return True
        
        return False


class ValidateForm:
    def __init__(self) -> None:
        pass





if __name__ == "__main__":
    print(FieldType.check_email_type("graubert34@yande5435x.com"))