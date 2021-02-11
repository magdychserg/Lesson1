class AppError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class AcceptStorageError(AppError):
    def __init__(self, text):
        self.text = f"You cannot add a product to the warehouse:\n {text}"


class TransferStorageError(AppError):
    def __init__(self, text):
        self.text = f"Hardware transfer error:\n {text}"


AddStorageError = AcceptStorageError


class ValidateEquipmentError(AppError):
    pass


class Storage:
    def __init__(self):
        self.__storage = []

    def add(self, equipments):
        if not all([isinstance(equipment, OfficeEquipment) for equipment in equipments]):
            raise AddStorageError(f"You are trying to add non-office equipment to the warehouse")

        self.__storage.extend(equipments)

    def transfer(self, idx: int, department: str):
        if not isinstance(idx, int):
            raise TransferStorageError(f"Invalid type '{type(item)}'")

        item: OfficeEquipment = self.__storage[idx]

        if item.department:
            raise TransferStorageError(f"Equipment {item} already assigned to the department {item.department}")

        item.department = department

    def filter_by(self, **kwargs):
        for id_, item in enumerate(self):
            if all([item.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield id_, item

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        return self.__storage[key]

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        del self.__storage[key]

    def __iter__(self):
        return self.__storage.__iter__()

    def __str__(self):
        return f"In stock now {len(self.__storage)} equipment"


class OfficeEquipment:
    __required_props = ("eq_type", "vendor", "model")

    def __init__(self, eq_type: str = None, vendor: str = "", model: str = ""):
        self.type = eq_type
        self.vendor = vendor
        self.model = model

        self.department = None

    def __setattr__(self, key, value):
        if key in self.__required_props and not value:
            raise AttributeError(f"'{key}' must have a value other than false")

        object.__setattr__(self, key, value)

    def __str__(self):
        return f"{self.type} {self.vendor} {self.model}"

    @staticmethod
    def validate(cnt):
        if not isinstance(cnt, int):
            ValidateEquipmentError(f"'{type(cnt)}'; the number of instances must be of the type 'int'")

    @classmethod
    def create(cls, cnt, **properties):
        cls.validate(cnt)
        return [cls(**properties) for _ in range(cnt)]


class Printer(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Printer', **kwargs)


class Scanner(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Scanner', **kwargs)


class Xerox(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Xerox', **kwargs)



storage = Storage()
storage.add(Printer.create(4, vendor="Epson", model="XP-400"))
storage.add(Scanner.create(3, vendor="OKI", model="5367-AD"))
storage.add(Scanner.create(2, vendor="OKI", model="5368-AD"))
storage.add(Xerox.create(6, vendor="Xerox", model="F123"))
print(storage)

for idx, itm in storage.filter_by(department=None, vendor="OKI", model="5367-AD"):
    print(f"We reserve it {itm} in 'department IT'")
    storage.transfer(idx, 'department IT')

for idx, itm in storage.filter_by(department=None):
    print(idx, f"{itm} not distributed by department")

print(storage)
print("Write off 1 device")
del storage[0]
print(storage)
