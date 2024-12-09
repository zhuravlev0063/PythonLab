#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'court_case.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # Пробуем импортировать Django. В случае ошибки выводим сообщение.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Не удалось найти модуль Django. Убедитесь, что Django установлен."
            )
        raise

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
