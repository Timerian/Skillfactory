class Queue:
    # Конструктор нашего класса, в нём происходит нужная инициализация объекта
    def __init__(self, max_size):
        self.max_size = max_size  # размер очереди
        self.task_num = 0  # будем хранить сквозной номер задачи

        self.tasks = [0 for _ in range(self.max_size)]  # инициализируем список с нулевыми элементами
        self.head = 0  # указатель на начало очереди
        self.tail = 0

    def is_empty(self):
        if self.head == self.tail and self.tasks[self.head] == 0:
            return True
        return False

    def size(self):
        if not self.is_empty():
            if self.tail == self.head:
                return self.max_size
            elif self.tail < self.head:
                return self.max_size - self.head + self.tail
            else:
                return self.tail - self.head
        return 0

    def add(self):
        self.task_num += 1  # увеличиваем порядковый номер задачи
        self.tasks[self.tail] = self.task_num  # добавляем его в очередь
        print(f"Задача №{self.tasks[self.tail]} добавлена")
        self.tail = (self.tail + 1) % self.max_size

    def show(self):  # выводим приоритетную задачу
        print(f"Задача №{self.tasks[self.head]} в приоритете")

    def do(self):  # выполняем приоритетную задачу
        print(f"Задача №{self.tasks[self.head]} выполнена")
        # после выполнения зануляем элемент по указателю
        self.tasks[self.head] = 0
        # и циклично перемещаем указатель
        self.head = (self.head + 1) % self.max_size


q = Queue(5)
s = [i for i in range(4)]
for k in s:
    q.add()

for i in range(q.size()):
    q.do()

