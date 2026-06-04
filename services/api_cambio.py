import requests

URL_BASE = "https://open.er-api.com/v6/latest"

def obter_moedas():
    try:
        resposta = requests.get(
            f"{URL_BASE}/USD",
            timeout=5
        )

        resposta.raise_for_status()

        dados = resposta.json()

        return sorted(dados["rates"].keys())

    except requests.exceptions.RequestException:
        raise Exception(
            "Não foi possível carregar as moedas."
        )


def converter(valor, origem, destino):
    try:
        resposta = requests.get(
            f"{URL_BASE}/{origem}",
            timeout=5
        )

        resposta.raise_for_status()

        dados = resposta.json()

        taxa = dados["rates"][destino]

        return valor * taxa, taxa

    except requests.exceptions.RequestException:
        raise Exception(
            "Não foi possível obter a cotação."
        )