import os
import time
import psutil
import subprocess



def linha(tam = 42):
    return "-" * tam


def titulo(txt):
    print(linha())
    print(txt)
    print(linha())


def ler_inteiro(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print("Erro, Digite um numero valido!")
            continue
        else:
            return n


def menu(lista):
    c = 1
    for i in lista:
        print(f"{c} - {i}")
        c += 1
    print(linha())
    opc = ler_inteiro("Sua opção: ")
    return opc


def teste_funcao1():

    print("Diretorios e arquivos: ")

    lista = os.listdir()
    dic_arq = {}
    lista_dir = []

    for i in lista:
        if os.path.isfile(i):
            ext = os.path.splitext(i)[1]
            if not ext in dic_arq:
                dic_arq[ext] = []
            dic_arq[ext].append(i)
        else:
            lista_dir.append(i)
        
    for i in dic_arq:
        print("Arquivos " + i)
        for j in dic_arq[i]:
            print("\t" + j)
        print(" ")


    if len(lista) > 0:
        print("Diretorios: ")
        for i in lista_dir:
            print("\t"+ i)
        print(" ")


    print("informações: ")


    lista = os.listdir()
    dic = {}

    for i in lista:
        if(os.path.isfile(i)):
            dic[i] = []
            dic[i].append(os.stat(i).st_size)
            dic[i].append(os.stat(i).st_atime)
            dic[i].append(os.stat(i).st_mtime)

    titulo = '{:11}'.format("Tamanho")

    titulo = titulo +  '{:27}'.format("Data de Modificação")

    titulo = titulo +  '{:27}'.format("Data de Criação")

    titulo = titulo + "Nome"

    print(titulo)

    for  i in dic:
        kb = dic[i][0]/1000
        tamanho = '{:10}'.format(str('{:.2f}'.format(kb) + 'KB'))
        print(tamanho, time.ctime(dic[i][2]), " ", time.ctime(dic[i][1]), " ", i)


def teste_funcao2():
    def mostra_info(pid):
        try:
            p = psutil.Process(pid)
            texto = '{:6}'.format(pid)
            texto = texto + '{:11}'.format(p.num_threads())
            texto = texto + " " + time.ctime(p.create_time()) + " "
            texto = texto + '{:8.2f}'.format(p.cpu_times().user)
            texto = texto + '{:8.2f}'.format(p.cpu_times().system)
            texto = texto + '{:10.2f}'.format(p.memory_percent()) + " MB"
            rss = p.memory_info().rss/1024/1024
            texto = texto + '{:10.2f}'.format(rss) + " MB"
            vms = p.memory_info().vms/1024/1024
            texto = texto + '{:10.2f}'.format(vms) + " MB"
            texto = texto + " " + p.exe()
            print(texto)
        except:
            pass  

    titulo = '{:^7}'.format("PID")
    titulo = titulo + '{:^11}'.format("# Threads")
    titulo = titulo + '{:^26}'.format("Criação")
    titulo = titulo + '{:^9}'.format("T. Usu.")
    titulo = titulo + '{:^9}'.format("T. Sis.")
    titulo = titulo + '{:^12}'.format("Mem. (%)")
    titulo = titulo + '{:^12}'.format("RSS")
    titulo = titulo + '{:^12}'.format("VMS")
    titulo = titulo + " Executável"
    print(titulo)

    lista = psutil.pids()

    for i in lista:
        mostra_info(i)


titulo("tp4".center(42))

while True:
    opcao = menu(["Função para retornar Diretorio e Arquivos", "Função para retornar informações sobre os processos do sistema"])
    if(opcao == 1):
        teste_funcao1()
        break
    elif(opcao == 2):
        teste_funcao2()
        break
    else:
        print("digite uma opcao valida")
        