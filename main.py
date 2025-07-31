# Importa os widgets e caixas de diálogo necessários do PyQt5
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                             QPushButton, QInputDialog, QMessageBox)

# Importa as funções 'adicionar' e 'remover' de um módulo externo chamado 'atividades'
from atividades import adicionar 
from atividades import remover

# Importa o módulo 'sys' para lidar com argumentos do sistema e encerrar o programa
import sys

# Define a classe principal da interface gráfica
class TelaPrincipal(QWidget):

    def __init__(self):
        super().__init__()

        # Define o título da janela e seu tamanho inicial
        self.setWindowTitle("Sistema de Notas")
        self.resize(300, 300)

        # Cria um dicionário vazio para armazenar os alunos e suas notas
        self.alunos = {} 

        # Criação dos botões com seus respectivos textos
        botao_adicionar = QPushButton("Adicionar um aluno e nota")
        botao_remover = QPushButton("Remover um aluno")
        botao_listar = QPushButton("Listar alunos e notas")
        botao_sair = QPushButton("Sair do programa")

        # Cria o layout vertical e adiciona os botões à interface
        layout = QVBoxLayout(self)
        layout.addWidget(botao_adicionar)
        layout.addWidget(botao_remover)
        layout.addWidget(botao_listar)
        layout.addWidget(botao_sair)

        # Conecta cada botão à sua função correspondente
        botao_sair.clicked.connect(self.close)            # Fecha a janela
        botao_adicionar.clicked.connect(self.adicionar)   # Chama a função para adicionar aluno
        botao_remover.clicked.connect(self.remover)       # Chama a função para remover aluno
        botao_listar.clicked.connect(self.listar)         # Chama a função para listar alunos

    # Função que solicita nome e nota, e adiciona no dicionário
    def adicionar(self):
        nome, ok = QInputDialog.getText(self, "Adicionar", "Digite o nome do aluno")
        nota, ok2 = QInputDialog.getText(self, "Adicionar", "Digite a nota")

        # Verifica se os campos foram preenchidos corretamente
        if not (ok and nome):
            return
        
        if not (ok2 and nota):
            return
        
        # Usa a função externa 'adicionar' para guardar os dados no dicionário
        adicionar(self.alunos, nome.lower(), nota)

        # Exibe mensagem de sucesso
        QMessageBox.information(
            self, "Sucesso",
            f"Aluno '{nome}' adicionado com nota {nota}"
        )

    # Função que solicita o nome e remove o aluno, se existir
    def remover(self):
        nome, ok = QInputDialog.getText(self, "Remover", "Digite o nome do aluno")

        if not (ok and nome):
            return

        # Verifica se o nome existe no dicionário antes de remover
        if nome.lower() in self.alunos:
            remover(self.alunos, nome.lower())
            QMessageBox.information(
                self, "Sucesso",
                f"Aluno '{nome}' removido com sucesso"
            )
        else:
            QMessageBox.information(
                self, "Falha",
                f"Aluno '{nome}' não existe"
            )

    # Função que mostra todos os alunos e suas respectivas notas
    def listar(self):
        # Se o dicionário estiver vazio, informa que não há alunos
        if not self.alunos:
            QMessageBox.information(self, "Lista de Alunos", "Nenhum aluno cadastrado.")
            return

        # Monta o texto com todos os alunos e notas
        texto = "Alunos e Notas:\n"
        for nome, nota in self.alunos.items():
            texto += f"{nome.capitalize()}: {nota}\n"

        # Exibe os dados em uma caixa de informação
        QMessageBox.information(self, "Lista de Alunos", texto)


# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    app = QApplication(sys.argv)   # Cria a aplicação
    tela = TelaPrincipal()         # Cria a janela principal
    tela.show()                    # Exibe a janela
    sys.exit(app.exec_())          # Inicia o loop da aplicação e espera o encerramento

    #criar a aplicacao
    #sys.argv - fornece os argumentos que serao utilizados no progama

    app = QApplication(sys.argv)

    #criando a tela
    tela = TelaPrincipal()

    #exibir a tela
    tela.show()

    #manter a janela aberta
    #app.exec_() - fornece o numero 0 - app ta rodando
    #quando apertamos no X ele fornece o numero 1
    #e pede para o sistema fechar a app
    sys.exit(app.exec_())


'''
def main():
    alunos = {}

    while True:
        print("Menu de Opções:")
        print("1 - Adicionar aluno com nota")
        print("2 - Remover aluno")
        print("3 - Atualizar nota de aluno")
        print("4 - Listar alunos e notas")  
        print("5 - Sair")  
        print()

        opcao = int(input("Digite sua opção: "))

        if opcao == 1:
            nome = input("Digite o nome do aluno: ").lower()
            nota = input("Digite a nota do aluno (0 a 10): ")
            adicionar(alunos, nome, nota)
            print()

        elif opcao == 2:
            nome = input("Digite o nome do aluno para remover: ").lower()
            remover(alunos, nome)
            print()

        elif opcao == 3:
            nome = input("Digite o nome do aluno: ").lower()
            nota_antiga = input("Digite a nota que deseja atualizar: ")
            nota_nova = input("Digite a nova nota: ")
            atualizar(alunos, nome, nota_antiga, nota_nova)
            print()

        elif opcao == 4:
            print("\nLista de alunos e suas notas:")
            if len(alunos) == 0:
                print("Nenhum aluno registrado.")
            else:
                for nome in alunos:
                    print(f"{nome}: {alunos[nome]}")
            print()

        elif opcao == 5:
            print("Saindo . . .")
            break

        else:
            print("Opção inválida.")
            print()
'''