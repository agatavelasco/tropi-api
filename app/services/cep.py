import requests

def consultar_via_cep(cep: str):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resp = requests.get(url, timeout=5)
    if resp.status_code != 200:
        raise RuntimeError(f"ViaCEP retornou HTTP {resp.status_code}")
    data = resp.json()
    if data.get("erro"):
        raise ValueError("CEP não encontrado.")
    return {
        "cep": data.get("cep"),
        "logradouro": data.get("logradouro"),
        "complemento": data.get("complemento"),
        "bairro": data.get("bairro"),
        "localidade": data.get("localidade"),
        "uf": data.get("uf"),
        "estado": "",
    }

def consultar_brasil_api(cep: str):
    url = f"https://brasilapi.com.br/api/cep/v1/{cep}"
    resp = requests.get(url, timeout=5)
    if resp.status_code != 200:
        raise RuntimeError("BrasilAPI falhou")
    data = resp.json()
    return {
        "cep": data.get("cep"),
        "logradouro": data.get("street"),
        "complemento": "",
        "bairro": data.get("neighborhood"),
        "localidade": data.get("city"),
        "uf": data.get("state"),
        "estado": "",
    }

def consultar_awesome_api(cep: str):
    url = f"https://cep.awesomeapi.com.br/json/{cep}"
    resp = requests.get(url, timeout=5)
    if resp.status_code != 200:
        raise RuntimeError("AwesomeAPI falhou")
    data = resp.json()
    return {
        "cep": data.get("cep"),
        "logradouro": data.get("address"),
        "complemento": "",
        "bairro": data.get("district"),
        "localidade": data.get("city"),
        "uf": data.get("state"),
        "estado": "",
    }

def consultar_cep(cep: str) -> dict:
    cep = "".join(filter(str.isdigit, cep or ""))
    if len(cep) != 8:
        raise ValueError("CEP deve ter exatamente 8 dígitos.")

    # Tentativa 1: ViaCEP
    try:
        return consultar_via_cep(cep)
    except Exception:
        pass  # tenta o próximo provedor

    # Tentativa 2: BrasilAPI
    try:
        return consultar_brasil_api(cep)
    except Exception:
        pass

    # Tentativa 3: AwesomeAPI
    try:
        return consultar_awesome_api(cep)
    except Exception:
        pass

    raise RuntimeError("Nenhum serviço de CEP respondeu.")
