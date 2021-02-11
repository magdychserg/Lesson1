class StorageError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class AddStorageError(StorageError):
    def __init__(self, text):
        self.text = f"You cannot add a product to the warehouse:\n {text}"


class TransferStorageError(StorageError):
    def __init__(self, text):
        self.text = f"Hardware transfer error:\n {text}"


class Storage:
    def __init__(self):
        self.__storage = []

    def add(self, item: "OfficeEquipment"):
        if not isinstance(item, OfficeEquipment):
            raise AddStorageError(f"{item} not office equipment")

        self.__storage.append(item)

    def transfer(self, idx: int, department: str):
        if not isinstance(idx, int):
            raise TransferStorageError(f"Invalid type '{type(item)}'")

        item: OfficeEquipment = self.__storage[idx]

        if item.department:
            raise TransferStorageError(f"Equipment {item} already assigned to the department {item.department}")

        item.department = department

    def filter_by(self, **kwargs):
        for idx, item in enumerate(self):
            a: OfficeEquipment = item
            if all([a.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield idx, item

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
    def __init__(
            self,
            eq_type: str,
            vendor: str,
            model: str,
    ):
        self.type = eq_type
        self.vendor = vendor
        self.model = model

        self.department = None

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)

    def __str__(self):
        return f"{self.type} {self.vendor} {self.model}"


class Printer(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('Printer', *args)


class Scanner(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('scanner', *args)


class Xerox(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('xerox', *args)



storage = Storage()
storage.add(Printer("Epson", "XP-400"))
storage.add(Scanner("OKI", "5367-AD"))
storage.add(Xerox("Xerox", "F123"))
print(storage)

last_idx = None
for idx, itm in storage.filter_by(department=None):
    print(idx, itm)
    last_idx = idx

print("Transmitting 1 device")
storage.transfer(last_idx, 'department')

for idx, itm in storage.filter_by(department=None):
    print(idx, itm)

print(storage)
print("Delete 1 device")
del storage[last_idx]
print(storage)
