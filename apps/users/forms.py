# Импорт модуля форм Django
from django import forms

# Готовая форма для создания пользователя (с логикой паролей)
from django.contrib.auth.forms import UserCreationForm

# Модель пользователя Django
from django.contrib.auth.models import User


# 🧾 Кастомная форма регистрации
class RegisterForm(UserCreationForm):
    # Добавляем поле email (обязательное для заполнения)
    email = forms.EmailField(required=True)

    # ⚙️ Внутренний класс Meta — связывает форму с моделью
    class Meta:
        # Указываем, что форма работает с моделью User
        model = User

        # Поля, которые будут отображаться в форме
        fields = ['username', 'email', 'password1', 'password2']

    # 💾 Переопределяем метод сохранения
    def save(self, commit=True):
        # Создаём объект пользователя, но НЕ сохраняем в базу сразу
        user = super().save(commit=False)

        # Записываем email из формы в объект пользователя
        user.email = self.cleaned_data['email']

        # Если commit=True (по умолчанию) — сохраняем в базу данных
        if commit:
            user.save()

        # Возвращаем объект пользователя
        return user