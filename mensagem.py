def join(node):
    mensagem = {}
    mensagem['codigo'] = 0
    mensagem['id'] = node["id"]

    return mensagem

def leave(node):
    mensagem = {}
    mensagem['codigo'] = 1
    mensagem['id'] = node["id"]
    mensagem['id_sucessor'] = node["id_sucessor"]
    mensagem['ip_sucessor'] = node["ip_sucessor"]
    mensagem['id_antecessor'] = node["id_antecessor"]
    mensagem['ip_antecessor'] = node["ip_antecessor"]

    return mensagem

def lookup(node):
    mensagem = {}
    mensagem['codigo'] = 2
    mensagem['id_origem_busca'] = node["id"]
    mensagem['ip_origem_busca'] = node["ip"]
    mensagem['id_busca'] = node["id_sucessor"]

    return mensagem

def update(node):
    mensagem = {}
    mensagem['codigo'] = 3
    mensagem['id'] = node["id"]
    mensagem['id_sucessor'] = node["id_sucessor"]
    mensagem['ip_sucessor'] = node["ip_sucessor"]

    return mensagem

def resposta_do_join():
    pass

def resposta_do_leave():
    pass

def resposta_do_lookup():
    pass

def resposta_do_update():
    pass
