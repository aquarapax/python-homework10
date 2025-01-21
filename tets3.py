# Задача 3 Генерация кода
# Функция для динамической генерации функций
def generate_complex_function(func_name, param_names, body):
    params = ', '.join(param_names) # Формируем строку с определением функции
    function_code = f"def {func_name}({params}):\n" + '  ' + body # Формируем код функции
    print(function_code) # Печать кода функции для проверки
    
    # Создаем глобальный и локальный контекст для выполнения кода
    global_context = {}
    local_context = {}
    
    exec(function_code, global_context, local_context) # Выполняем exec
        
    return local_context[func_name]# Возвращаем сгенерированную функцию

# Тест
if __name__ == "__main__":
    function_name = 'complex_function' 
    parameters = ['x', 'y'] 
    function_body = """
    if x > y: 
        return x - y 
    else: 
        return y - x
    """
    complex_func = generate_complex_function(function_name, parameters, function_body) 
    
    print(f' result_1 = {complex_func(10, 5)} ')
    print(f' result_2 = {complex_func(5, 10)} ')