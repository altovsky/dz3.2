# -*- coding: utf-8 -*-

import requests

APP_ID = 6653584

USER_ID_1 = 207037824  # Maxim
USER_ID_2 = 10579451  # Angela

TOKEN = '5b091937e4df56b5b6db3402f5f4750af39c3f1e63c81283b7f444f58ed077b7a711531558edb00a779af'
# TOKEN = '1680eedb986792cf949d90b9ef4e776ee81d41aecfc41372aab4cf8e9f24015e64132c81b2a01d2f5e8d4'


class User:
    def __init__(self, id, first_name, last_name, domain):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.token = TOKEN
        self.domain = domain

    def __str__(self):
        return f'https://vk.com/{self.domain}'

    def __and__(self, other):
        response = requests.get(
            'https://api.vk.com/method/friends.getMutual',
            params=dict(
                source_uid=self.id,
                target_uid=other.id,
                access_token=self.token,
                v=5.80
            )
        )
        id_list = response.json()['response']
        user_list = []
        for i, user in enumerate(id_list):
            response_user = requests.get(
                'https://api.vk.com/method/users.get',
                params=dict(
                    user_ids=user,
                    fields='domain',
                    access_token=TOKEN,
                    v=5.80
                )
            )
            globals()[f'user{i}'] = User(
                **response_user.json()['response'][0]
            )
            user_list.append(globals()[f'user{i}'])
        return user_list


response_user = requests.get(
    'https://api.vk.com/method/users.get',
    params=dict(
        user_ids=USER_ID_1,
        fields='domain',
        access_token=TOKEN,
        v=5.80
    )
)
maxim = User(
    **response_user.json()['response'][0]
)

response_user = requests.get(
    'https://api.vk.com/method/users.get',
    params=dict(
        user_ids=USER_ID_2,
        fields='domain',
        access_token=TOKEN,
        v=5.80
    )
)
angela = User(
    **response_user.json()['response'][0]
)

bitwise = maxim & angela

print('Общие друзья:')
for iter in range(len(bitwise)):
    print(
        globals()[f'user{iter}'].first_name,
        globals()[f'user{iter}'].last_name,
        globals()[f'user{iter}'],
    )
