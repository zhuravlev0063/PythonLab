import re

def is_html_image_tag(html_string):
    # Определяем регулярное выражение для проверки HTML-тега <img>
    img_tag_pattern = r'<img\s+[^>]*src=["\'][^"\']+["\'][^>]*>'
    # Возвращаем True, если строка соответствует шаблону, иначе False
    return bool(re.fullmatch(img_tag_pattern, html_string))

def validate_html_image_tag(html_string):
    # Проверяем, является ли строка HTML-кодом изображения
    if is_html_image_tag(html_string):
        return html_string
    else:
        # Если строка некорректна, выбрасываем исключение
        raise ValueError("Некорректный HTML-код изображения")

# Примеры использования
try:
    html_code = '<img src="image.jpg" alt="Example">'
    print(is_html_image_tag(html_code))  # Должно вернуть True
    print(validate_html_image_tag(html_code))  # Должно вернуть сам html_code

    invalid_html_code = '<div>Not an image tag</div>'
    print(is_html_image_tag(invalid_html_code))  # Должно вернуть False
    print(validate_html_image_tag(invalid_html_code))  # Должно выбросить исключение
except ValueError as e:
    print(e)
