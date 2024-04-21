import requests

CLIENT_ID = 'YOUR_CLIENT_ID'
SECRET_KEY = 'YOUR_SECRET_KEY'
subr = 'pythonsandlot'
#Перед запуском вставить сюда рефреш токен, полученный из gettoken.py
REFRESH_TOKEN = 'YOUR_REFRES_TOKEN'

headers = {'User-Agent': 'script by DIMA_SURKOV_FIT1'}

def error_check(response):
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")

# Получение access token
auth_url = 'https://www.reddit.com/api/v1/access_token'
auth_params = {
'grant_type': 'refresh_token',
'refresh_token': REFRESH_TOKEN,
}

auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)
response = requests.post(auth_url, params=auth_params, auth=auth, headers=headers)
mas = response.json()

access_token = mas['access_token']

# Установка заголовков авторизации
headers['Authorization'] = f'Bearer {access_token}'

# Получение информации о пользователе
me_url = 'https://oauth.reddit.com/api/v1/me'
response = requests.get(me_url, headers=headers)
error_check(response)
user = response.json()
username = user['name']
print(username)

b = True


while (b == True):
    a = int(input('Выберите операцию :\n1) Создать пост\n2) Прочитать пост \n'
                    '3)Изменить пост пост \n4)Удалить пост\n5) Закончить это всё\n'))

    #Генерация поста
    if(a == 1):
        url = f'https://oauth.reddit.com/api/submit'
        aa = int(input("Выберите\n1) Запостить много постов\n2) Запостить один пост\n"))
        if(aa == 1):

            aaa = int(input("Сколько постов запостить: "))
            for i in range(aaa):
                new_post = {
                    'title': f'lab1_{i+1}post',
                    'text': (i+1)*(i+1),
                    'sr': subr,
                    'kind': 'self',
                }
                response_create = requests.post(url, headers=headers, data = new_post)
                error_check(response_create)
            print(f"\nЗапощщено {i+1} постов")

        if(aa == 2):
            new_post_title = input("Введите заголовок: ")
            new_post_content = input("Введите содержимое: ")

            new_post = {
                'title': new_post_title,
                'text': new_post_content,
                'sr': subr,
                'kind': 'self',
            }
            response_create = requests.post(url, headers=headers, data=new_post)
            error_check(response_create)
            print(f"\nПост запощщен")

    #Чтение поста
    if(a == 2):

        user_posts_url = f'https://oauth.reddit.com/r/{subr}/new'
        response = requests.get(user_posts_url, headers=headers)
        error_check(response)
        masup = response.json()
        print("Списки заголовков постов: ")
        for post in masup['data']['children']:
            author = post['data']['author']
            title = post['data']['title']
            if author == username:
                print(title)

        read_post = input("Введите заголовок поста, который нужно прочитать: ")

        ppost = None

        for post in masup['data']['children']:
            post_title = post['data']['title']
            if post_title == read_post and post['data']['author'] == username:
                ppost = post
                break
        if ppost:
            print(ppost['data']['selftext'])
        else:
            print("Пост не найден")

    #Редактирование поста
    if(a==3):

        user_posts_url = f'https://oauth.reddit.com/r/{subr}/new'
        response = requests.get(user_posts_url, headers=headers)
        error_check(response)
        masup = response.json()
        print("Список заголовков постов")
        for i, post in enumerate(masup['data']['children'], start = 1):
            author = post['data']['author']
            title = post['data']['title']
            if author == username:
                print(f"{i}) {title}")

        aa = int(input("Введите номер поста, который нужно изменить: "))

        post_edit = None
        for i, post in enumerate(masup['data']['children'], start=1):
            if i == aa and post['data']['author'] == username:
                post_edit = post
                break

        if post_edit:
            post_id_to_edit = post_edit['data']['id']
            edit_url = 'https://oauth.reddit.com/api/editusertext'

            new_post_content = input("Введите новое содержимое: ")


            edit_post_dict = {
                'api_type': 'json',
                'text': new_post_content,
                'thing_id': f't3_{post_id_to_edit}',
            }
            response_edit = requests.post(edit_url, headers=headers, data=edit_post_dict)
            error_check(response_edit)

        else:
            print(f"\nПост не найде")

    #Удаление поста
    if(a == 4):

        user_posts_url = f'https://oauth.reddit.com/r/{subr}/new'
        response = requests.get(user_posts_url, headers=headers)
        error_check(response)
        masup = response.json()

        print("Список постов:")
        for i, post in enumerate(masup['data']['children'], start=1):
            author = post['data']['author']
            title = post['data']['title']
            if author == username:
                print(f"{i}) {title}")

        delnum = int(input("Введите номер поста для удаления: "))
        del_post = None
        for i, post in enumerate(masup['data']['children'], start=1):
            if i == delnum and post['data']['author'] == username:
                del_post= post
                break


        if del_post:
            del_post_id = del_post['data']['id']
            del_url = f'https://oauth.reddit.com/api/del'
            del_post_dict = {
                'id': f't3_{del_post_id}'
            }
            response_delete = requests.post(del_url, headers=headers, data=del_post_dict)

        else:
            print(f"\nПост не найден.")

    if(a == 5):
        b = False

