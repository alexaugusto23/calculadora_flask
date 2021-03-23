class ReadFile:

    def leitura_arquivo():
    
        with open('log_file.txt','r', encoding='utf-8') as file:
            lista = []
            for linha in file:
                valores = linha.split()
                lista.append(valores)
            print(lista[2])
            new_lista = lista[2]+lista[4]
            #print(new_lista)
            log = ' '.join(new_lista)
            #print(log)    
            file.close()
        return log