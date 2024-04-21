import praw

client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_SECRET_KEY'
user_agent = 'script by DIMA_SURKOV_FIT1'
redirect_uri = 'http://localhost:8088'

# Создание экземпляра реддита
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    redirect_uri=redirect_uri
)

# Метод для создания УРЛ адреса

authorization_url = reddit.auth.url(
    scopes=['identity', 'read', 'submit', 'edit'],
    state='UniqueState',
    duration='permanent'
)


print("Перейдитb для авторизации: ", authorization_url)
code = input("Введите код: ")
refresh_token = reddit.auth.authorize(code)
print("Рефреш токен: ", refresh_token)
