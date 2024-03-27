'''Nesse projeto iremos usar a biblioteca yfinance para buscar dados no Yahoo finance.
Tambem iremos aprender a usar pyautogui e pyperclip para automatizar informaçoes via e-mail'''
import yfinance as yf
import pyautogui
import pyperclip
import webbrowser
codigo = input('Digite o Código da ação desejada: ') #PETR4.SA AÇÃO EXEMPLO
dados = yf.Ticker(codigo).history('6mo')
print(dados)
fechamento = dados['Close']
# Agora pegamos o fechamento do último item
ultimo_fechamento = fechamento.iloc[-1]
# Arredondamos o valor do fechamento
ultimo_fechamento_arredondado = round(ultimo_fechamento, 2)
#fechamento.plot() pra mostrar um gráfico
maxima = fechamento.max()
minima = fechamento.min()
#onde -1 retorna o ultimo valor
atual = fechamento.iloc[-1]
pyautogui.PAUSE = 3
#abrir aba
webbrowser.open_new_tab("http://www.gmail.com")
#digitar na barra de endereço e dar enter
pyperclip.copy('www.gmail.com')
pyautogui.hotkey('ctrl','v')
pyautogui.hotkey('enter')
#licar no botão escrever
pyautogui.click(x=133, y=249)
#escrever destinatario
pyperclip.copy('lucastavora05@gmail.com')
pyautogui.hotkey('ctrl','v')
pyautogui.hotkey('tab')
#escrever assunto
pyperclip.copy('aula teste')
pyautogui.hotkey('ctrl','v')
pyautogui.hotkey('tab')
#escrever informação
mensagem = f'''Seguem as análises das ações de código {codigo} nos úmtimos seis meses
cotação mínima R$ {round(minima, 2)}
cotação máxima R$ {round(maxima, 2)}
cotação atual R$ {round(atual,2)}
fim teste.'''
pyperclip.copy(mensagem)
pyautogui.hotkey('ctrl','v')
pyautogui.click(x=1228, y=981)

