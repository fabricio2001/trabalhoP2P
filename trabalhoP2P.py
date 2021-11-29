import json
import random
import socket
import sys
import _thread

PORT = 12345

node = {
    "id": None,
    "ip": sys.argv[1],
    "id_antecessor": None,
    "ip_antecessor": None,
    "id_sucessor": None,
    "ip_sucessor": None
}

def cliente(udp):
    while True:
        msg, cliente = udp.recvfrom(1024)
        msg_decoded = msg.decode("utf-8")
        print(f"{msg_decoded}\n")
    udp.close()


def servidor(udp):
    while True:
        msg, cliente = udp.recvfrom(1024)
        msg_decoded = msg.decode("utf-8")
        print(msg_decoded)
        print(cliente)
        if msg_decoded:
            msg_json = (json.loads(msg_decoded))
            if msg_json["codigo"] == 0:
                mensagem = {}
                mensagem['codigo'] = 64
                if node["id_sucessor"] == node["id_antecessor"] == node["id"]:
                    if node["id"] < msg_json["id"]:
                        ''' ///////////// Aki esta dando errado /////////////'''
                        mensagem["id_sucesso"] = node["id_sucesso"]
                        mensagem["ip_sucessor"] = node["ip_sucessor"]
                        mensagem["id_antecessor"] = node["id_antecessor"]
                        mensagem["ip_antecessor"] = node["ip_antecessor"]
                    else:
                        mensagem["id_sucesso"] = node["id_antecessor"]
                        mensagem["ip_sucessor"] = node["ip_antecessor"]
                        mensagem["id_antecessor"] = node["id_sucesso"]
                        mensagem["ip_antecessor"] = node["ip_sucessor"]
                        ''' ///////////////////////////////////////////////////////'''
                mensage = json.dumps(mensagem)
                udp.sendto(mensage.encode("utf-8"), cliente)

    print(f"Server closse")


def main():
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.bind(("", PORT))
    opc = None
    while opc != "6":
        informacoes_do_no = f"""
                       ID: {node['id']}
            ID_ANTECESSOR: {node['id_antecessor']}
            IP_ANTECESSOR: {node['ip_antecessor']}
              ID_SUCESSOR: {node['id_sucessor']}
              IP_SUCESSOR: {node['ip_sucessor']}
        """
        print(informacoes_do_no)
        print("######################################")
        print("# 1 - Gerar nodeID ")
        print("# 2 - Iniciar rede P2P (no inicial)")
        print("# 3 - Entrar em uma rede P2P ")
        print("# 4 - Sair da rede P2P")
        print("# 5 - Mostrar informacoes do No")
        print("# 6 - Sair da aplicacao")
        print("#####################################")
        opc = input("Informe uma opcao: ")
        if opc == "1":
            node['id'] = random.randrange(1, 1000)
        elif opc == "2":
            node['id_antecessor'] = node['id']
            node['id_sucessor'] = node['id']
            node['ip_antecessor'] = node['ip']
            node['ip_sucessor'] = node['ip']
            _thread.start_new_thread(servidor, (udp,))
        elif opc == "3":
            endereco_lookup = input("informe o endereco IP: ")
            print(endereco_lookup)
            dest = (endereco_lookup, PORT)

            mensagem = {}
            mensagem['codigo'] = 0
            mensagem['id'] = node["id"]

            message = json.dumps(mensagem)
            udp.sendto(message.encode("utf-8"), dest)
            _thread.start_new_thread(cliente, (udp,))


        elif opc == "5":
            continue
    udp.close()

if __name__ == "__main__":
    main()