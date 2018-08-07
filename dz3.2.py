# -*- coding: utf-8 -*-

import requests

APP_ID = 6653584

USER_ID_1 = 207037824  # Maxim
USER_ID_2 = 10579451  # Angela

TOKEN = '13b5a25dabe0a22d743b3b1caf1559b4a8fffdfd28cf025ffab00c26f0630134ee5970d28000f0d600275'


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

response_user = requests.get(
    'https://api.vk.com/method/users.get',
    params=dict(
        user_ids=483136631,
        access_token=TOKEN,
        v=5.80
    )
)

bitwise = maxim & angela
print('Общие друзья:')
for iter in range(len(bitwise)):
    print(
        globals()[f'user{iter}'].first_name,
        globals()[f'user{iter}'].last_name,
        globals()[f'user{iter}'],
    )
