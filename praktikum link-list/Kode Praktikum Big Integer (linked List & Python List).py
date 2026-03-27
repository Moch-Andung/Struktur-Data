# ==============================
# BIG INTEGER - LINKED LIST
# ==============================

class Node:
    def __init__(self, digit):
        self.digit = digit
        self.next = None


class BigIntegerLL:
    def __init__(self, initValue="0"):
        self.head = None
        for d in reversed(str(initValue)):
            self._append(int(d))

    def _append(self, digit):
        node = Node(digit)
        node.next = self.head
        self.head = node

    def toString(self):
        digits = []
        curr = self.head
        while curr:
            digits.append(str(curr.digit))
            curr = curr.next
        return ''.join(reversed(digits))

    def _to_int(self):
        return int(self.toString())

    def _from_int(self, value):
        self.head = None
        for d in reversed(str(value)):
            self._append(int(d))

    # comparison
    def comparable(self, other):
        if self._to_int() > other._to_int():
            return 1
        elif self._to_int() < other._to_int():
            return -1
        return 0

    # arithmetic
    def add(self, other):
        return BigIntegerLL(self._to_int() + other._to_int())

    def sub(self, other):
        return BigIntegerLL(self._to_int() - other._to_int())

    def mul(self, other):
        return BigIntegerLL(self._to_int() * other._to_int())

    def floordiv(self, other):
        return BigIntegerLL(self._to_int() // other._to_int())

    def mod(self, other):
        return BigIntegerLL(self._to_int() % other._to_int())

    def pow(self, other):
        return BigIntegerLL(self._to_int() ** other._to_int())

    # bitwise
    def bit_or(self, other):
        return BigIntegerLL(self._to_int() | other._to_int())

    def bit_and(self, other):
        return BigIntegerLL(self._to_int() & other._to_int())

    def bit_xor(self, other):
        return BigIntegerLL(self._to_int() ^ other._to_int())

    def lshift(self, other):
        return BigIntegerLL(self._to_int() << other._to_int())

    def rshift(self, other):
        return BigIntegerLL(self._to_int() >> other._to_int())

    # assignment operators
    def iadd(self, other):
        self._from_int(self._to_int() + other._to_int())

    def isub(self, other):
        self._from_int(self._to_int() - other._to_int())

    def imul(self, other):
        self._from_int(self._to_int() * other._to_int())

    def ifloordiv(self, other):
        self._from_int(self._to_int() // other._to_int())

    def imod(self, other):
        self._from_int(self._to_int() % other._to_int())

    def ipow(self, other):
        self._from_int(self._to_int() ** other._to_int())

    def ilshift(self, other):
        self._from_int(self._to_int() << other._to_int())

    def irshift(self, other):
        self._from_int(self._to_int() >> other._to_int())

    def ior(self, other):
        self._from_int(self._to_int() | other._to_int())

    def iand(self, other):
        self._from_int(self._to_int() & other._to_int())

    def ixor(self, other):
        self._from_int(self._to_int() ^ other._to_int())


# ==============================
# BIG INTEGER - PYTHON LIST
# ==============================

class BigIntegerList:
    def __init__(self, initValue="0"):
        self.digits = [int(d) for d in str(initValue)]

    def toString(self):
        return ''.join(map(str, self.digits))

    def _to_int(self):
        return int(self.toString())

    def _from_int(self, value):
        self.digits = [int(d) for d in str(value)]

    def comparable(self, other):
        if self._to_int() > other._to_int():
            return 1
        elif self._to_int() < other._to_int():
            return -1
        return 0

    # arithmetic
    def add(self, other):
        return BigIntegerList(self._to_int() + other._to_int())

    def sub(self, other):
        return BigIntegerList(self._to_int() - other._to_int())

    def mul(self, other):
        return BigIntegerList(self._to_int() * other._to_int())

    def floordiv(self, other):
        return BigIntegerList(self._to_int() // other._to_int())

    def mod(self, other):
        return BigIntegerList(self._to_int() % other._to_int())

    def pow(self, other):
        return BigIntegerList(self._to_int() ** other._to_int())

    # bitwise
    def bit_or(self, other):
        return BigIntegerList(self._to_int() | other._to_int())

    def bit_and(self, other):
        return BigIntegerList(self._to_int() & other._to_int())

    def bit_xor(self, other):
        return BigIntegerList(self._to_int() ^ other._to_int())

    def lshift(self, other):
        return BigIntegerList(self._to_int() << other._to_int())

    def rshift(self, other):
        return BigIntegerList(self._to_int() >> other._to_int())

    # assignment
    def iadd(self, other):
        self._from_int(self._to_int() + other._to_int())

    def isub(self, other):
        self._from_int(self._to_int() - other._to_int())

    def imul(self, other):
        self._from_int(self._to_int() * other._to_int())

    def ifloordiv(self, other):
        self._from_int(self._to_int() // other._to_int())

    def imod(self, other):
        self._from_int(self._to_int() % other._to_int())

    def ipow(self, other):
        self._from_int(self._to_int() ** other._to_int())

    def ilshift(self, other):
        self._from_int(self._to_int() << other._to_int())

    def irshift(self, other):
        self._from_int(self._to_int() >> other._to_int())

    def ior(self, other):
        self._from_int(self._to_int() | other._to_int())

    def iand(self, other):
        self._from_int(self._to_int() & other._to_int())

    def ixor(self, other):
        self._from_int(self._to_int() ^ other._to_int())


# ==============================
# CONTOH PENGGUNAAN
# ==============================

if __name__ == "__main__":
    print("=== LINKED LIST VERSION ===")
    a = BigIntegerLL("12345678901234567890")
    b = BigIntegerLL("10")

    print("a + b =", a.add(b).toString())
    print("a - b =", a.sub(b).toString())
    print("a * b =", a.mul(b).toString())
    print("a // b =", a.floordiv(b).toString())
    print("a % b =", a.mod(b).toString())
    print("a ** 2 =", a.pow(BigIntegerLL("2")).toString())

    a.iadd(b)
    print("a += b ->", a.toString())

    print("\n=== PYTHON LIST VERSION ===")
    x = BigIntegerList("98765432109876543210")
    y = BigIntegerList("5")

    print("x + y =", x.add(y).toString())
    print("x * y =", x.mul(y).toString())

    x.imul(y)
    print("x *= y ->", x.toString())
