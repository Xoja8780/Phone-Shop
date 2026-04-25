# Импорт функции для отображения HTML-шаблонов и перенаправления (redirect)
from django.shortcuts import render, redirect

# Импорт функций для работы с аутентификацией (вход, выход, проверка)
from django.contrib.auth import authenticate, login, logout

# Декоратор — ограничивает доступ только для авторизованных пользователей
from django.contrib.auth.decorators import login_required

# Импорт нашей формы регистрации
from .forms import RegisterForm


# 🔐 Представление (view) для регистрации пользователя
def register_view(request):
    # Создаём пустую форму (для GET-запроса)
    form = RegisterForm()

    # Проверяем: если форма отправлена (метод POST)
    if request.method == 'POST':

        # Заполняем форму данными из запроса
        form = RegisterForm(request.POST)

        # Проверяем, валидна ли форма (все ли поля заполнены правильно)
        if form.is_valid():
            # Сохраняем пользователя в базу данных
            user = form.save()

            # Сразу логиним пользователя (автоматический вход после регистрации)
            login(request, user)

            # Перенаправляем на главную страницу
            return redirect('product_list')

    # Если GET-запрос или форма невалидна — показываем страницу регистрации
    return render(request, 'users/signup.html', {'form': form})


# 🔑 Представление для входа пользователя
def login_view(request):
    # Если пользователь уже авторизован — отправляем его на главную
    if request.user.is_authenticated:
        return redirect('product_list')

    # Переменная для хранения ошибки
    error = None

    # Если форма отправлена
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            error = "Пожалуйста, заполните все поля."
        else:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('product_list')
            else:
                error = "Неверный логин или пароль."


    # Показываем страницу входа с возможной ошибкой
    return render(request, 'users/login.html', {'error': error})







# 🚪 Выход из аккаунта
@login_required
def logout_view(request):
    # Разлогиниваем пользователя (удаляем сессию)
    logout(request)

    # Перенаправляем на страницу входа
    return redirect('login')