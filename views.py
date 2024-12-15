class View:
    @staticmethod
    def format_tasks(tasks):
        if not tasks:
            return "У вас нет задач."
        result = []
        for task in tasks:
            status = "✅" if task[2] else "❌"
            result.append(f"{task[0]}. {task[1]} {status}")
        return "\n".join(result)
