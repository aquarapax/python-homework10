# Задача 1 Применение метаклассов
# Метакласс
class AttrLoggingMeta(type):
    
    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs) # Создаем новый класс
                              
        # Переопределяем методы   __getattribute__, __setattr__
        original_getattribute = new_class.__getattribute__
        original_setattr = new_class.__setattr__

        # Метод логирования вызова
        def log_access(name, value): 
            print(f"Calling method '{name}'")

        # Метод логирования чтения
        def log_read(name, value, instance):
            print(f"Reading attribute '{name}'")
            
        # Метод логирования записи
        def log_write(name, value, instance):
            print(f"Writing attribute '{name}' value {value}")
                       
        def new_getattribute(self, name):
            value = original_getattribute(self, name)
            
            if callable(value): # Если метод                
                log_access(name, value) # Логируем вызов
            else:
                log_read(name, value, self) # иначе (атрибут) логируем чтение
            return value

        def new_setattr(self, name, value):
            log_write(name, value, self)
            original_setattr(self, name, value)

        # Заменяем методы
        new_class.__getattribute__ = new_getattribute
        new_class.__setattr__ = new_setattr
        
        return new_class

# Класс использующий метакласс AttrLoggingMeta
class LoggedClass(metaclass=AttrLoggingMeta):
    custom_method = 42 
    
    def other_custom_method(value):
        pass
    
# Тест
if __name__ == "__main__":
    instance = LoggedClass()
    print(instance.custom_method)  # Чтение атрибута
    instance.custom_method = 78    # Запись атрибута
    instance.other_custom_method() # Вызов метода
   