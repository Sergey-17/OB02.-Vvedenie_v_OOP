class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False  # По умолчанию задача не выполнена

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):      # задает удобное строковое представление объекта.
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Описание: {self.description}, Срок: {self.due_date}, Статус: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        new_task = Task(description, due_date)
        self.tasks.append(new_task)
        print(f"Задача '{description}' добавлена")

    def mark_task_completed(self, description):
        for task in self.tasks:
            if task.description == description and not task.completed:
                task.mark_as_completed()
                print(f"Задача '{description}' отмечена как выполненная")
                return
        print(f"Задача '{description}' не найдена или уже выполнена")

    def show_current_tasks(self):
        current_tasks = [task for task in self.tasks if not task.completed]
        if not current_tasks:
            print("Нет текущих задач.")
            return

        print("Текущие задачи (не выполненные):")
        for i, task in enumerate(current_tasks, 1):
            print(f"{i}. {task}")


# Пример использования
if __name__ == "__main__":
    manager = TaskManager()

    # Добавляем задачи
    manager.add_task("Купить молоко", "2023-12-01")
    manager.add_task("Сделать домашнее задание", "2023-12-05")
    manager.add_task("Позвонить маме", "2023-12-10")

    # Показываем текущие задачи
    manager.show_current_tasks()

    # Отмечаем задачу как выполненную
    manager.mark_task_completed("Купить молоко")

    # Снова показываем текущие задачи
    manager.show_current_tasks()