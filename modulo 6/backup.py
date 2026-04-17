import shutil
import os

def realizar_backup(pasta_origem, pasta_destino):
    if os.path.exists(pasta_origem):
        
        
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)
            print(f"Pasta de destino '{pasta_destino}' criada.")

       
        arquivos = os.listdir(pasta_origem)
        
        for arquivo in arquivos:
            caminho_completo_origem = os.path.join(pasta_origem, arquivo)
            caminho_completo_destino = os.path.join(pasta_destino, arquivo)
            
            
            if os.path.isfile(caminho_completo_origem):
                shutil.copy2(caminho_completo_origem, caminho_completo_destino)
                print(f"Arquivo '{arquivo}' copiado com sucesso!")
        
        print("\nBackup concluído com sucesso!")
    else:
        print("Erro: A pasta de origem não foi encontrada.")


origem = "meus_documentos"
destino = "backup_sistema"

realizar_backup(origem, destino)