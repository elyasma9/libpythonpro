import requests


def buscar_avatar(usuario):
    """[summary]

    Args:
        usuario ([type]): [str com nome do usário no github]
    """
    url = f'https://api.github.com/users/{usuario}'
    response = requests.get(url)
    response = response.json()
    return response['avatar_url']


if __name__ == "__main__":
    response = buscar_avatar('elyasma9')
    print(str(response))
