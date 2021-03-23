import os 
import time 

class ManagerFile:
    
    def deleta_cria_file():

        get_path_atual = os.getcwd()
        #os.chdir("/home/site/wwwroot") #azure
        chdir = os.chdir(get_path_atual)
        path_file = os.path.join(get_path_atual,"log_file.txt")
        print(get_path_atual)

        for root, dirs, files in os.walk(".", topdown=False):
            for file_name in files:
                if "log_file.txt" == file_name:
                    print(True)
                    os.remove(path_file)
                    print("-"*80)
                    print("Arquivo log_file.txt removido.......")

        time.sleep(5)
        print("Arquivo criado")
        os.system("python test.py")