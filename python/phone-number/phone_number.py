import re

class PhoneNumber:
    def __init__(self, phone_number):
        exp = '([+]1)*\D*([2-9]\d\d)\D*([2-9]\d\d)\D*(\d\d\d\d)(\d*)'
        result = re.search(exp, phone_number)
        
        if (result is None) or (len(result.group(5)) > 0):
            raise ValueError('.+')

        self.area_code = result.group(2)
        self.number = result.group(2)+result.group(3)+result.group(4)
    
    def pretty(self):
        exp = '([+]1)*\D*([2-9]\d\d)\D*([2-9]\d\d)\D*(\d\d\d\d)'
        result = re.search(exp, self.number)
        return f"({result.group(2)})-{result.group(3)}-{result.group(4)}"
