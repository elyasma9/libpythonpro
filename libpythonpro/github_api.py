import requests


def buscar_avatar(usuario):
    """[summary]

    Args:
        usuario ([type]): [str com nome do usário no github]
    """
    url = f'https://api.github.com/usuarios/{usuario}'
    response = requests.get(url)
    return response.json()['avatar_url']


if __name__ == "__main__":
    response = buscar_avatar('elyasSantana')
    print(str(response))
