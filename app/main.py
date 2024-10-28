from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.database import Session 

def main ():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    # Solicitando dados para o usuario
    print("\nAdicionando usuário: ")
    nome = input("Digite o seu nome: ")
    email = input("Digite o seu email: ")
    senha = input("Digite o seu senha: ")

    service.criar_usuario(nome=nome, email=email, senha=senha)

    # Listar todos os usuarios cadastrados
    print("\nLista de todos os usuários cadastrados: ")
    lista_usuarios = service.listar_todos_usuarios()
    for usuario in lista_usuarios:
        print(f"Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")
        
if __name__ == "__main__":
    main()