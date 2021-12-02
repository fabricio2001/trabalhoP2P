import json
import random
import socket
import sys
import _thread
import os
import time 
import mensagem as m

clear = lambda: os.system('clear')

PORT = 12345

node = {
    "id": None,
    "ip": sys.argv[1],
    "id_antecessor": None,
    "ip_antecessor": None,
    "id_sucessor": None,
    "ip_sucessor": None
}

def menu_usuario():
    informacoes_do_no = f"""
                       ID: {node['id']}
                       IP: {node['ip']}
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
        

def cliente(udp):
    while True:
        msg, cliente = udp.recvfrom(1024)
        msg_decoded = msg.decode("utf-8")
        
        json_decode = json.loads(msg_decoded)

        node["ip_antecessor"] = json_decode["ip_antecessor"]
        node["ip_sucessor"] = json_decode["ip_sucessor"]
        node["id_antecessor"] = json_decode["id_antecessor"]
        node["id_sucessor"] = json_decode["id_sucessor"]
  
    udp.close()


def servidor(udp):
    while True:
        msg, cliente = udp.recvfrom(1024)
        msg_decoded = msg.decode("utf-8")
        if msg_decoded:
            msg_json = (json.loads(msg_decoded))
            if msg_json["codigo"] == 0:
                mensagem = {}
                mensagem['codigo'] = 64
                if node["id_sucessor"] == node["id_antecessor"] == node["id"]:
                    if node["id"] < msg_json["id"]:
                        mensagem["id_sucessor"] = node["id_sucessor"]
                        mensagem["ip_sucessor"] = node["ip_sucessor"]
                        mensagem["id_antecessor"] = node["id_antecessor"]
                        mensagem["ip_antecessor"] = node["ip_antecessor"]
                    else:
                        mensagem["id_sucessor"] = node["id_antecessor"]
                        mensagem["ip_sucessor"] = node["ip_antecessor"]
                        mensagem["id_antecessor"] = node["id_sucessor"]
                        mensagem["ip_antecessor"] = node["ip_sucessor"]
                mensage = json.dumps(mensagem)
                udp.sendto(mensage.encode("utf-8"), cliente)

            elif msg_json["codigo"] == 1:
                pass

            elif msg_json["codigo"] == 2:
                pass

            elif msg_json["codigo"] == 3:
                pass

            elif msg_json["codigo"] == 64:
                pass

            elif msg_json["codigo"] == 65:
                pass

            elif msg_json["codigo"] == 66:
                pass

            elif msg_json["codigo"] == 67:
                pass
            

    print(f"Server closse")


def main():
    clear()
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.bind(("", PORT))
    opc = None
    while opc != "6":

        menu_usuario()
        opc = input("Informe uma opcao: ")
        
        if opc == "1":
            clear()
            node['id'] = str(random.randrange(1, 1000))

        elif opc == "2":
            clear()
            node['id_antecessor'] = node['id']
            node['id_sucessor'] = node['id']
            node['ip_antecessor'] = node['ip']
            node['ip_sucessor'] = node['ip']
            _thread.start_new_thread(servidor, (udp, ))

        elif opc == "3":
            clear()
            endereco_lookup = input("informe o endereco IP: ")
            clear()

            dest = (endereco_lookup, PORT)

            mensagem = m.join(node)

            message = json.dumps(mensagem)
            udp.sendto(message.encode("utf-8"), dest)
            _thread.start_new_thread(cliente, (udp,))
            time.sleep(0.001)  
        
        elif opc == "4":
            pass

        elif opc == "5":
            continue
    udp.close()

if __name__ == "__main__":
    main()
