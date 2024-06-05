import json


def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def save_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def update_test_values(tests, values_dict):
    for test in tests:
        test_id = test['id']
        if test_id in values_dict:
            test['value'] = values_dict[test_id]
        if 'values' in test:
            update_test_values(test['values'], values_dict)


def main(values_path, tests_path, report_path):
    values_data = load_json(values_path)
    tests_data = load_json(tests_path)

    # Создаем словарь из values.json для быстрого доступа
    values_dict = {item['id']: item['value'] for item in values_data['values']}

    # Обновляем структуру tests, заполняя поля values
    update_test_values(tests_data['tests'], values_dict)

    # Сохраняем обновленную структуру в report.json
    save_json(tests_data, report_path)



if __name__ == "__main__":
    # Укажите правильные пути к вашим файлам на вашем компьютере
    values_path = 'C:/Users/User/Desktop/tz/task_3/values.json'
    tests_path = 'C:/Users/User/Desktop/tz/task_3/tests.json'
    report_path = 'C:/Users/User/Desktop/tz/task_3/report.json'
    main(values_path, tests_path, report_path)
