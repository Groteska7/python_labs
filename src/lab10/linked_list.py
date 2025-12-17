

class Node:
    def __init__(self,value: any,next=None):
        self.value = value
        self.next = next
    
    def __str__(self):
        return self.value



class SinglyLinkedList:
    def __init__(self):
        self.head = None # первый элемент списка (голова)
        self.tail = None # Последний элемент списка (хвост)
        self._size = 0 # кол-во элементов в списке

    def append(self,value) -> None:
        new=Node(value)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new
        self._size += 1

    def prepend(self,value) -> None:
        new = Node(value,next=self.head)
        self.head=new
        self._size += 1
        if self.tail is None: self.tail = new
    
    def insert(self,idx: int, value) -> None:
        if idx<0 or idx>self._size:
            raise IndexError("Неверно указан индекс")
        if idx == 0:
            self.prepend(value)
        elif idx == self._size:
            self.append(value)
        else:
            current = self.head
            for i in range(idx-1):
                current = current.next
            new = Node(value,next=current.next)
            current.next=new
            self._size += 1
    
    def remove_at(self,idx: int) -> None:
        if idx<0 or idx>=self._size:
            raise IndexError("Неверно указан индекс")
        if idx == 0:
            self.head=self.head.next
            self._size -= 1
            if self.head is None:
                self.tail = None
            return None
        else:
            current = self.head
            for i in range(idx-1):
                current = current.next
            current.next=current.next.next
            if current.next is None: self.tail = current
            self._size -= 1
    
    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next
    
    def __len__(self):
        return self._size
    
    def __repr__(self):
        values = list(self)
        return f"SinglyLinkedList({values})"
    
    def b_out(self):
        string=""
        current = self.head
        for x in range(self._size,0,-1):
            string+=" >- "+str(current)
            current = current.next
        string="enoN"+string
        return string[::-1]










if __name__ == "__main__":
    """Тест согласованности tail"""
    print("Тест красивого вывода")
    a=SinglyLinkedList()
    a.prepend("A")
    a.prepend("B")
    a.prepend("C")
    a.prepend("D")
    a.prepend("E")
    print(a.b_out())

    print("\n=== Тест согласованности tail ===")
    
    # 1. После prepend в пустой список
    lst = SinglyLinkedList()
    lst.prepend("A")
    assert lst.tail.value == "A", f"Ошибка: после prepend в пустой список tail должен быть 'A'"
    print("tail корректно обновляется после prepend в пустой список")
    
    # 2. После remove_at последнего элемента
    lst.append("B")
    lst.append("C")
    lst.remove_at(2)  # Удаляем 'C'
    assert lst.tail.value == "B", f"Ошибка: после удаления последнего элемента tail должен быть 'B'"
    print("tail корректно обновляется после удаления последнего элемента")
    
    # 3. После remove_at единственного элемента
    lst2 = SinglyLinkedList()
    lst2.append("X")
    lst2.remove_at(0)
    print(lst2.tail)
    assert lst2.tail is None, f"Ошибка: после удаления единственного элемента tail должен быть None"
    print("tail корректно обновляется после удаления единственного элемента")
    
    # 4. tail всегда указывает на последний элемент при различных операциях
    lst3 = SinglyLinkedList()
    lst3.append("A")      # tail = A
    lst3.prepend("B")     # tail = A (не меняется)
    lst3.append("C")      # tail = C
    lst3.insert(1, "D")   # tail = C (не меняется)
    
    assert lst3.tail.value == "C", f"Ошибка: tail должен быть 'C', а не {lst3.tail.value}"
    print("tail всегда указывает на последний элемент")

    """Тест итерации и магических методов"""
    print("\n=== Тест итерации ===")
    
    lst = SinglyLinkedList()
    
    # 1. Итерация по пустому списку
    assert [x for x in lst] == [], "Ошибка: итерация по пустому списку должна возвращать []"
    print("Итерация по пустому списку работает")
    
    # 2. Итерация по непустому списку
    lst.append("A")
    lst.append("B")
    lst.append("C")
    
    result = []
    for item in lst:
        result.append(item)
    
    assert result == ["A", "B", "C"], f"Ошибка: итерация должна возвращать ['A','B','C'], а не {result}"
    print("Итерация по непустому списку работает")
    
    # 3. Магический метод len
    assert len(lst) == 3, f"Ошибка: len должен быть 3, а не {len(lst)}"
    print("__len__ работает корректно")
    
    # 4. Магический метод repr
    repr_str = repr(lst)
    assert repr_str == "SinglyLinkedList(['A', 'B', 'C'])", f"Ошибка: repr должен быть 'SinglyLinkedList(['A', 'B', 'C'])', а не {repr_str}"
    print("__repr__ работает корректно")
    
    # 5. Преобразование в list
    assert list(lst) == ["A", "B", "C"], f"Ошибка: list(lst) должен быть ['A','B','C'], а не {list(lst)}"
    print("Преобразование в list работает")


def test_edge_cases():
    """Тест граничных случаев"""
    print("\n=== Тест граничных случаев ===")
    
    # 1. Много операций подряд
    lst = SinglyLinkedList()
    for i in range(100):
        lst.append(i)
    
    assert len(lst) == 100, f"Ошибка: после 100 append len должен быть 100, а не {len(lst)}"
    print("100 append подряд работают")
    
    # 2. Чередование append и prepend
    lst2 = SinglyLinkedList()
    lst2.append("A")      # [A]
    lst2.prepend("B")     # [B, A]
    lst2.append("C")      # [B, A, C]
    lst2.prepend("D")     # [D, B, A, C]
    
    assert list(lst2) == ["D", "B", "A", "C"], f"Ошибка: список должен быть ['D','B','A','C'], а не {list(lst2)}"
    print("Чередование append и prepend работает")
    
    # 3. Вставка и удаление в сложном порядке
    lst3 = SinglyLinkedList()
    lst3.append(1)        # [1]
    lst3.prepend(0)       # [0, 1]
    lst3.insert(2, 2)     # [0, 1, 2]
    lst3.remove_at(1)     # [0, 2]
    lst3.insert(1, 3)     # [0, 3, 2]
    lst3.remove_at(0)     # [3, 2]
    
    assert list(lst3) == [3, 2], f"Ошибка: список должен быть [3, 2], а не {list(lst3)}"
    print("Сложная последовательность операций работает")
    """Тест вставки по индексу"""
    print("\n=== Тест insert ===")
    
    lst = SinglyLinkedList()
    
    # Подготовка: создаем список [A, B, C]
    for char in ["A", "B", "C"]:
        lst.append(char)
    
    # 1. Вставка в начало
    lst.insert(0, "X")
    assert list(lst) == ["X", "A", "B", "C"], f"Ошибка: список должен быть ['X','A','B','C'], а не {list(lst)}"
    print("insert(0, value) работает")
    
    # 2. Вставка в конец
    lst.insert(4, "Z")
    assert list(lst) == ["X", "A", "B", "C", "Z"], f"Ошибка: список должен быть ['X','A','B','C','Z'], а не {list(lst)}"
    assert lst.tail.value == "Z", f"Ошибка: tail должен быть 'Z'"
    print("insert(size, value) работает")
    
    # 3. Вставка в середину
    lst.insert(2, "M")
    assert list(lst) == ["X", "A", "M", "B", "C", "Z"], f"Ошибка: список должен быть ['X','A','M','B','C','Z'], а не {list(lst)}"
    print("insert в середину работает")
    
    # 4. Ошибки индексов
    try:
        lst.insert(-1, "error")
        assert False, "Ошибка: insert(-1) должен вызвать IndexError"
    except IndexError:
        print("insert(-1) вызывает IndexError")
    
    try:
        lst.insert(10, "error")
        assert False, "Ошибка: insert(10) должен вызвать IndexError"
    except IndexError:
        print("insert(10) вызывает IndexError")


def test_remove_at():
    """Тест удаления по индексу"""
    print("\n=== Тест remove_at ===")
    
    lst = SinglyLinkedList()
    
    # Подготовка: создаем список [A, B, C, D]
    for char in ["A", "B", "C", "D"]:
        lst.append(char)
    
    # 1. Удаление из середины
    lst.remove_at(2)  # Удаляем 'C'
    assert list(lst) == ["A", "B", "D"], f"Ошибка: список должен быть ['A','B','D'], а не {list(lst)}"
    assert len(lst) == 3, f"Ошибка: len должен быть 3, а не {len(lst)}"
    print("remove_at из середины работает")
    
    # 2. Удаление головы
    lst.remove_at(0)  # Удаляем 'A'
    assert list(lst) == ["B", "D"], f"Ошибка: список должен быть ['B','D'], а не {list(lst)}"
    assert lst.head.value == "B", f"Ошибка: head должен быть 'B'"
    print("remove_at(0) работает")
    
    # 3. Удаление последнего элемента
    lst.remove_at(1)  # Удаляем 'D'
    assert list(lst) == ["B"], f"Ошибка: список должен быть ['B'], а не {list(lst)}"
    assert lst.tail.value == "B", f"Ошибка: tail должен быть 'B' после удаления последнего"
    print("remove_at последнего элемента работает (tail обновляется)")
    
    # 4. Удаление единственного элемента
    lst.remove_at(0)
    assert list(lst) == [], f"Ошибка: список должен быть пустым, а не {list(lst)}"
    assert lst.head is None, f"Ошибка: head должен быть None"
    assert lst.tail is None, f"Ошибка: tail должен быть None после удаления единственного элемента"
    print("remove_at единственного элемента работает")
    
    # 5. Ошибки индексов
    try:
        lst.remove_at(0)  # Пустой список
        assert False, "Ошибка: remove_at из пустого списка должен вызвать IndexError"
    except IndexError:
        print("remove_at из пустого списка вызывает IndexError")
    
    lst.append("X")
    try:
        lst.remove_at(-1)
        assert False, "Ошибка: remove_at(-1) должен вызвать IndexError"
    except IndexError:
        print("remove_at(-1) вызывает IndexError")
    
    try:
        lst.remove_at(2)  # size=1, индекс 2 > size
        assert False, "Ошибка: remove_at(2) при size=1 должен вызвать IndexError"
    except IndexError:
        print("remove_at с индексом > size вызывает IndexError")
        """Тест базовых операций"""
    print("=== Тест базовых операций ===")
    
    lst = SinglyLinkedList()
    
    # 1. Пустой список
    assert len(lst) == 0, f"Ошибка: len пустого списка должен быть 0, а не {len(lst)}"
    assert list(lst) == [], f"Ошибка: пустой список должен быть [], а не {list(lst)}"
    print("Пустой список создан корректно")
    
    # 2. Append
    lst.append("A")
    assert len(lst) == 1, f"Ошибка: после append len должен быть 1, а не {len(lst)}"
    assert list(lst) == ["A"], f"Ошибка: список должен быть ['A'], а не {list(lst)}"
    assert lst.head.value == "A", f"Ошибка: head должен быть 'A'"
    assert lst.tail.value == "A", f"Ошибка: tail должен быть 'A'"
    print("Append одного элемента работает")
    
    # 3. Append нескольких элементов
    lst.append("B")
    lst.append("C")
    assert len(lst) == 3, f"Ошибка: len должен быть 3, а не {len(lst)}"
    assert list(lst) == ["A", "B", "C"], f"Ошибка: список должен быть ['A','B','C'], а не {list(lst)}"
    assert lst.head.value == "A", f"Ошибка: head должен быть 'A'"
    assert lst.tail.value == "C", f"Ошибка: tail должен быть 'C'"
    print("Append нескольких элементов работает")


def test_prepend():
    """Тест добавления в начало"""
    print("\n=== Тест prepend ===")
    
    lst = SinglyLinkedList()
    
    # 1. Prepend в пустой список
    lst.prepend("A")
    assert list(lst) == ["A"], f"Ошибка: список должен быть ['A'], а не {list(lst)}"
    assert lst.head.value == "A", f"Ошибка: head должен быть 'A'"
    assert lst.tail.value == "A", f"Ошибка: tail должен быть 'A' (после prepend в пустой список)"
    print("Prepend в пустой список работает")
    
    # 2. Prepend в непустой список
    lst.prepend("B")
    assert list(lst) == ["B", "A"], f"Ошибка: список должен быть ['B','A'], а не {list(lst)}"
    assert lst.head.value == "B", f"Ошибка: head должен быть 'B'"
    assert lst.tail.value == "A", f"Ошибка: tail должен быть 'A'"
    print("Prepend в непустой список работает")