'''Nesse projeto da aula 01 irei criar um Formulário no formato PDF'''

#input de informações a serem preenchidas no formulário
projeto = str(input('Descrição do projeto: '))
horas_previstas = int(input('Informe a quantidade de horas previstas: '))
valor_hora = float(input('Valor da hora trabalhada: '))
prazo = str(input('Informe o prazo do projeto (meses): '))
#cálculo de tempo x valor
valor_total_projeto = horas_previstas * valor_hora
valor_hora_formatado = f'R$ {valor_hora:.2f}'
valor_total_projeto_formatado = f'{valor_total_projeto:.2f}'
print(f'{valor_total_projeto_formatado}')
#Criando o PDF
from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial')
pdf.image('TemplateAula01.png')#se for baixar o templade coloque o mesmo nome e formato desejado
pdf.text( 125, 158, projeto)
pdf.text(125, 172, str(horas_previstas))
pdf.text(125, 185, str(valor_hora_formatado))
pdf.text(125, 200, str(prazo))
pdf.text(125, 215, str(valor_total_projeto_formatado))
pdf.output('orçamento.pdf')
print('Orçamento gerado com sucesso')