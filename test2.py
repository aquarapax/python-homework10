# Задача 2 Динамическое создание класса
# Функция для динамического создания класса
def create_class_with_methods(class_name, attributes, methods):
    new_class = type(class_name, (object,), {**attributes, **methods})  # Создаем класс с помощью type
    return new_class # Возвращаем созданный класс

# Тест
if __name__ == "__main__":
    attributes = { 'species': 'Human', 'age': 25 } 
    methods = { 'greet': lambda self: f"Hello, I am a {self.species} and I am {self.age} years old." } 
    DynamicClass = create_class_with_methods('DynamicClass', attributes, methods) 
    instance = DynamicClass() 
    print(instance.greet())