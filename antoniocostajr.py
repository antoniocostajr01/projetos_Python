#Antônio Claudio Costa Junior
#Enunciado da avaliação:

"""OBS: 
- Escreva seu nome completo na primeira linha do programa
- Salve o código com o seunome.py
Competências a serem avaliadas:
- Conhecer os comandos da linguagem
- Saber utilizar os comandos corretamente
- Desenvolver uma solução viável para a atividade proposta
- Códigos iguais = D

Enunciado:

Você foi selecionado para a próxima etapa de um processo de 
seleção para uma vaga de emprego.
Para conquistar a vaga você deverá desenvolver um código
seguindo as instruções abaixo:

Na opção 1, você deverá digitar os dados necessários para
preencher as listas com nome do aluno, sua idade e seu curso. A idade mínima aceita deverá ser 16 anos
O curso digitado deverá ser um dos cursos da lista lst_cursos_disponiveis 

Na opção 2, você deverá imprimir um relatório geral para conferência,
imprimindo o nome do aluno, sua idade e seu curso. 
Imprima essas informações uma ao lado da outra.
No final, mostre o total de alunos e quantos alunos estão na 
faixa etária entre 18 e 25 anos de idade 

Na opção 3, você deverá possibilitar a troca de curso de um aluno.

Na opção 4, você deverá implementar a exclusão de um aluno da lista,
retirando também os dados correspondentes a idade e curso 
deste aluno. 
Sua tarefa é desenvolver o que falta no código abaixo.
menu = ================================
    0- Finaliza o código
    1- Adicionar dados
    2- Listar os dados
    3- Alterar o curso 
        de um aluno
    4- Excluir um aluno
    ================================
"""
"""
lst_cursos_diponiveis = ["RDS", "ADS", "PMM", "DADOS", "SPI"]
lst_aluno = []
lst_idade = []
lst_curso = []
while True:
    print(menu)
    escolha = input("    Escolha: ")
    if escolha == "0":
        # seu código aqui
        pass
    if escolha == "1":
        # seu código aqui
        pass
    if escolha == "2":
        # seu código aqui
        pass
    if escolha == "3":
        # seu código aqui
        pass
    if escolha == "4":
        # seu código aqui
        pass"""

#Inicio do código
import os
from time import sleep

lst_cursos_diponiveis = ["ADM", "ADS", "DDM", "MKT", "PGS", "PMM", "RDS"]
lst_aluno = ['Ana', 'Giovana', 'Igor', 'Maria Fernanda da Silva']
lst_idade = [22,21,30, 25]
lst_curso = ['ADM', 'ADS', 'PMM', 'DDM']

menu = """================================
0- Finaliza o código
1- Adicionar dados
2- Listar os dados
3- Alterar o curso de um aluno
4- Excluir um aluno
================================
"""

exibir_cursos_disponiveis = """[ ADM ] -> Administração
[ ADS ] -> Análise e Desenvolvimento de Sistemas
[ DDM ] -> Design de Moda
[ MKT ] -> Marketing
[ PGS ] -> Processos Gerenciais
[ PMM ] -> Produção Multimídia
[ RDS ] -> Redes de Computadores
"""

def linhas_de_separacao():
    print('=-'*30)
def nome():
    while True:
        nome_do_aluno = input('Digite o NOME do aluno: ').capitalize()
        if nome_do_aluno.isalpha():
            return nome_do_aluno
        else:
            print('Você digitou algo errado! Por favor digite um nome válido.')

def idade():
    while True:
        try:
            idade_do_aluno = int(input('Digite a IDADE do aluno: '))
            if idade_do_aluno < 16:
                os.system('cls')
                print(f'Você não possui a idade mínima para ser cadastrado.')
                print('Voltando para o menu...')
                sleep(3)
                os.system('cls')
                return None  
            return idade_do_aluno
        except ValueError:  
            print("ERRO! Por favor, digite um valor válido.")
            
def curso():
    print(exibir_cursos_disponiveis)
    while True:
        curso_do_aluno = input('Digite o CURSO conforme a legenda: ').upper()
        if curso_do_aluno in lst_cursos_diponiveis:
            return curso_do_aluno
        else:
            print('Curso inválido. Por favor, escolha um curso válido.')

def cadastrar_dados(aluno, idade, curso):
    lst_aluno.append(aluno)
    lst_idade.append(idade)
    lst_curso.append(curso)

"""Na opção 2, você deverá imprimir um relatório geral para conferência,
imprimindo o nome do aluno, sua idade e seu curso. 
Imprima essas informações uma ao lado da outra.
No final, mostre o total de alunos e quantos alunos estão na 
faixa etária entre 18 e 25 anos de idade"""
def alunos_entre_18_e_25():
    cont_alunos_25_e_25 = 0
    for idade in lst_idade:
        if 18 <= idade <=25:
            cont_alunos_25_e_25 += 1
        else:
            pass
    if cont_alunos_25_e_25 == 0:
        print('Nenhum aluno possui idade entre 18 e 25 anos.')
    else:
        print(f'{cont_alunos_25_e_25} alunos possuem idade entre 18 e 25 anos.')

def mostrar_conteudo_das_listas():
    os.system('cls')
    dados_alunos = []
    for i in range(len(lst_aluno)):
        dados_alunos.append((lst_aluno[i], lst_idade[i], lst_curso[i]))

    print('Relatório Geral do Cadastro de Alunos')
    
    # Função interna para calcular a largura de cada coluna
    def calcular_largura_coluna(dados, cabecalhos):
        larguras = [len(titulo) for titulo in cabecalhos]
        for linha in dados:
            for i, valor in enumerate(linha):
                larguras[i] = max(larguras[i], len(str(valor)))
        return larguras

    # Função interna para imprimir uma linha com separadores
    def imprimir_linha_separadora(larguras):
        linha = "+"
        for largura in larguras:
            linha += "-" * (largura + 2) + "+"
        print(linha)

    # Função interna para imprimir uma linha de dados ou cabeçalho
    def imprimir_linha(linha, larguras):
        linha_formatada = "|"
        for i, valor in enumerate(linha):
            linha_formatada += f" {str(valor):<{larguras[i]}} |"
        print(linha_formatada)

    cabecalho = ["Nome", "Idade", "Curso"]
    larguras = calcular_largura_coluna(dados_alunos, cabecalho)

    # Imprimir a tabela
    print("\nInformações dos Alunos:")
    imprimir_linha_separadora(larguras)
    imprimir_linha(cabecalho, larguras)
    imprimir_linha_separadora(larguras)
    for linha in dados_alunos:
        imprimir_linha(linha, larguras)
    imprimir_linha_separadora(larguras)

#Na opção 3, você deverá possibilitar a troca de curso de um aluno.
def alterar_dados():
    while True:
        # Etapa para encontrar o índice do aluno e verificar se está cadastrado
        nome_para_alteracao = input('Digite o nome do aluno que deseja trocar de curso: ').capitalize()
        if nome_para_alteracao in lst_aluno:
            indice_da_alteracao = lst_aluno.index(nome_para_alteracao)
            curso_atual = lst_curso[indice_da_alteracao]
            break
        else:
            print(f'{nome_para_alteracao} não consta na lista.')
            return 
    print()
    print(exibir_cursos_disponiveis)
    
    while True:  #Verificação do novo curso
        novo_curso = input(f'Digite o novo curso que {nome_para_alteracao} vai fazer conforme a legenda:  ').upper()
        if novo_curso not in lst_cursos_diponiveis:
            print(f'A legenda {novo_curso} não corresponde a nenhum curso disponível. Tente novamente!')
            continue
        if novo_curso == curso_atual:
            print(f'{nome_para_alteracao} já faz o curso de {novo_curso} e a alteração não é necessária.')
            return         
        break
    
    while True: #Verifica a confirmação da troca, caso ela vá ocorrer
        op = input(f'Tem certeza que deseja alterar o curso de {nome_para_alteracao} para {novo_curso}?  [Sim/Não]: ').upper()
        if op in ('SIM'):
            break
        elif op in ('NÃO','NAO'):
            return  # Retorna ao menu principal se o usuário não confirmar a alteração
        else:
            print('Opção inválida, tente novamente')
            continue
    
    # Realizar a alteração de curso
    lst_curso[indice_da_alteracao] = novo_curso
    linhas_de_separacao()
    print(f'{nome_para_alteracao} teve seu curso alterado para {novo_curso} com sucesso!')
    linhas_de_separacao()


"""Na opção 4, você deverá implementar a exclusão de um aluno da lista,
retirando também os dados correspondentes a idade e curso 
deste aluno. """
def remover_dados():
    while True:
        nome_para_remocao = input('Digite o nome do aluno que deseja excluir o cadastro: ').capitalize()
        if nome_para_remocao in lst_aluno:
            indice_de_remocao = lst_aluno.index(nome_para_remocao)
            break
        else:
            linhas_de_separacao()
            print(f'O nome {nome_para_remocao} não consta no cadastro. Tente novamente.')
            linhas_de_separacao()
            continue
    while True:
        op = input(f'Tem certeza que deseja excluir todos os dados de {nome_para_remocao} do cadastro [Sim/Não] = ').upper()
        if op in ('SIM' , 'NÃO', 'NAO'):
            if op in ('NÃO', 'NAO'):
                return None
            else:
                break
        else:
            print('Opção inválida, tente novamente')
            continue         
    del lst_aluno[indice_de_remocao]
    del lst_idade[indice_de_remocao]
    del lst_curso[indice_de_remocao]
    print(f'Os dados de {nome_para_remocao} foram removidos com sucesso.')

def mensagem_inicial():
    mensagem = "     CADASTRO DE ALUNOS     "
    largura_total = len(mensagem)+4 # A largura inclui a mensagem + 2 espaços de margem em cada lado
    print("-" * largura_total)
    print(f"| {mensagem} |")
    print("-" * largura_total)


# Programa principal
while True:
    mensagem_inicial()
    print(menu)
    try:
        escolha =int(input("Escolha: "))
    except ValueError:
        print('Opção inválida, tente novamente!')
        continue
    
    if escolha == 1:
        os.system('cls')
        nome_do_aluno = nome()
        linhas_de_separacao()
        idade_do_aluno = idade()
        if idade_do_aluno is None:
            continue
        linhas_de_separacao()
        curso_do_aluno = curso()
        cadastrar_dados(nome_do_aluno, idade_do_aluno, curso_do_aluno)
        linhas_de_separacao()
        print('Aluno cadastrado com SUCESSO!')
        linhas_de_separacao()
        voltar_cadastro = input('\nPressione ENTER para voltar ao menu.')
        os.system('cls')

    if escolha == 2:
        mostrar_conteudo_das_listas()
        alunos_entre_18_e_25()
        voltar_cadastro = input('\nPressione ENTER para voltar ao menu.')
        os.system('cls')

    if escolha == 3:
        os.system('cls')
        alterar_dados()
        voltar_cadastro = input('\nPressione ENTER para voltar ao menu.')
        os.system('cls')

    if escolha == 4:
        os.system('cls')
        remover_dados()
        voltar_cadastro = input('\nPressione ENTER para voltar ao menu.')
        os.system('cls')

    if escolha == 0:
        while True:
            linhas_de_separacao()
            op = input(f'Tem certeza que deseja encerrar o programa [Sim/Não]? ').strip().lower()
            linhas_de_separacao()
            if op in ('sim', 'não', 'nao'):
                if op in ('não', 'nao'):
                    break
                else:
                    print("Finalizando o programa...")
                    sleep(1)
                    os.system('cls')
                    exit('ATÉ A PRÓXIMA!')
            else:
                print('Opção inválida, tente novamente')
                continue
