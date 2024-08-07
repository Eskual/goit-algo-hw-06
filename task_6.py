from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
class Name(Field):
    
	pass

class Phone(Field):
    def __init__(self, value):
        super(Phone, self).__init__(value)
        if len(value) != 10 or not value.isdigit():
            raise ValueError
        else:
            pass     
  
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        
    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def remove_phone(self, str_phone: str):
        for phone_in_class in self.phones:
            if phone_in_class.value == str_phone:
                self.phones.remove(phone_in_class)
            else:
                pass
    
    def edit_phone(self, old_phone: str, new_phone: str):               
        flag = True
        for phone_in_class in self.phones:
            if phone_in_class.value == old_phone:
                self.phones.append(Phone(new_phone))
                self.phones.remove(phone_in_class)
                flag = False
                break
            else:
                pass
        if flag:
            print('There is not record with such specified phone to replace')
    
    def find_phone(self, phone:str):
        for phone_in_class in self.phones:
            if phone_in_class.value == phone:
                return self.phones[self.phones.index(phone_in_class)]
            else:    
                return None
        
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record
 
    def find(self, name: str):
        for item in self.data:
            if item == name:
                return self.data[name]
            else:
                continue
        return None
    
    def delete(self, name: str):
        if name in self.data:
            del self.data[name]
        else:
            raise Exception
    
    def __str__(self):  
        result = ''                                              
        phones = self.data.values()
        for el in phones:
            result += f'{el}\n'
        return result