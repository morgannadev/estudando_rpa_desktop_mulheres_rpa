from botcity.core import DesktopBot
from botcity.maestro import *

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    bot = DesktopBot()

    # Caminho onde está o executável SiCalc
    path_sicalc = r"C:\Program Files (x86)\Programas RFB\Sicalc Auto Atendimento\SicalcAA.exe"

    # Abre o aplicativo do SiCalc
    bot.execute(path_sicalc)
    
    if bot.find( "popup_contribuinte", matching=0.97, waiting_time=10000):
         bot.click_relative(202, 205)
    
    if not bot.find( "menu_funcoes", matching=0.97, waiting_time=10000):
        not_found("menu_funcoes")
    bot.click()
    
    if not bot.find( "menu_preenchimento_darf", matching=0.97, waiting_time=10000):
        not_found("menu_preenchimento_darf")
    bot.click()
    
    if not bot.find( "campo_cod_receita", matching=0.97, waiting_time=10000):
        not_found("campo_cod_receita")
    bot.click_relative(137, 9)

    # essa opção coloca todo o valor no campo de uma vez, como se fosse ctrl+v
    bot.paste("5629")

    # bot.type_keys("5629") - essa opção digitará tecla por tecla

    bot.tab()
    
    if not bot.find( "campo_pa", matching=0.97, waiting_time=10000):
        not_found("campo_pa")
    bot.click_relative(17, 25)
    bot.paste("310120")
    
    if not bot.find( "campo_valor_reais", matching=0.97, waiting_time=10000):
        not_found("campo_valor_reais")
    bot.click_relative(21, 26)
    bot.paste("10000")
    
    if not bot.find( "botao_calcular", matching=0.97, waiting_time=10000):
        not_found("botao_calcular")
    bot.click()
    
    if not bot.find( "botao_darf", matching=0.97, waiting_time=10000):
        not_found("botao_darf")
    bot.click()
    
    if not bot.find( "campo_nome", matching=0.97, waiting_time=10000):
        not_found("campo_nome")
    bot.click_relative(3, 27)
    bot.paste("Petrobras")
    
    if not bot.find( "campo_telefone", matching=0.97, waiting_time=10000):
        not_found("campo_telefone")
    bot.click_relative(-1, 24)
    bot.paste("1199991234")
    
    if not bot.find( "campo_cnpj", matching=0.97, waiting_time=10000):
        not_found("campo_cnpj")
    bot.click_relative(124, 8)
    bot.paste("33000167000101")
    
    if not bot.find( "campo_referencia", matching=0.97, waiting_time=10000):
        not_found("campo_referencia")
    bot.click_relative(115, 8)
    bot.paste("0")

    # se você tiver impressora configurada, ao clicar no botão de imprimir, vai direcionar para a impressora
    if not bot.find( "botao_imprimir", matching=0.97, waiting_time=10000):
        not_found("botao_imprimir")
    bot.click()
    
    if not bot.find( "tela_salvar_como", matching=0.97, waiting_time=10000):
        not_found("tela_salvar_como")
    bot.click()
    
    # colocar aqui o caminho onde vai salvar o pdf
    bot.paste(r"caminho_aqui\nome_do_arquivo.pdf")
    bot.enter()

    bot.wait(2000)

    bot.alt_f4()
    bot.alt_f4()    
    

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()





