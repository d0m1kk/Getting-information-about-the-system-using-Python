import platform

def get_windows_version():
    try:
        windows_version = {
            'Платформа': platform.platform(),
            'Версия': platform.version(),
            'Релиз': platform.release(),
            'Система': platform.system()
        }
        return windows_version
    except Exception as e:
        return {'error': str(e)}

def print_windows_information():
    version_information = get_windows_version()
    if 'error' in version_information:
        print(f'Ошибка при получении информации о версии Windows: {version_information["error"]}')
    else:
        print('Информация о версии Windows:')
        print(f"Платформа: {version_information['Платформа']}")
        print(f"Версия: {version_information['Версия']}")
        print(f"Релиз: {version_information['Релиз']}")
        print(f"Система: {version_information['Система']}")

if __name__ == '__main__':
    print_windows_information()
