from pyautogui import hotkey, sleep, write, press

sleep(2)
print()
sleep(0.5)
escolha = str(input(
    'O que deseja fazer?\n\n[A] Abrir a ferramenta Figma\n[B] Versionar o projeto.\n[C] Abortar o programa.\n\nInsira aqui a letra correspondente a sua opção: ')).upper()
sleep(0.5)

if escolha == 'A':
    def Figma():
        print()
        sleep(0.5)
        print('Abrindo a ferramenta Figma...')
        sleep(0.5)
        press('win')
        sleep(0.5)
        write('Figma')
        sleep(0.5)
        press('enter')
        sleep(10)

if escolha == 'B':
    def Git():
        print()
        sleep(0.5)
        print('Iniciando o versionamento do projeto...')
        sleep(0.5)
        press('win')
        sleep(0.5)
        write('Windows Terminal')
        sleep(0.5)
        press('enter')
        sleep(10)
        write('cd C:\dev\APEDC')
        sleep(0.5)
        press('enter')
        sleep(0.5)
        write('git add .')
        sleep(0.5)
        press('enter')
        sleep(0.5)
        write('git commit -m "Mudanças no projeto."')
        sleep(0.5)
        press('enter')
        sleep(0.5)
        write('git push')
        sleep(0.5)
        press('enter')
        sleep(10)
        hotkey('alt', 'f4')

if escolha == 'C':
    def Logout():
        print()
        sleep(0.5)
        print('Saindo do programa...')
        sleep(3)
        hotkey('alt', 'f4')

if escolha not in 'ABC':

    while escolha not in 'ABC':
        print()
        sleep(0.5)
        escolha = str(input(
            'Opção Inválida.\n\nO que deseja fazer?\n\n[A] Abrir a ferramenta Figma\n[B] Versionar o projeto.\n[C] Abortar o programa.\n\nInsira aqui a letra correspondente a sua opção: ')).upper()
        sleep(0.5)

        if escolha == 'A':

            def Figma():
                print()
                sleep(0.5)
                print('Abrindo a ferramenta Figma...')
                sleep(0.5)
                press('win')
                sleep(0.5)
                write('Figma')
                sleep(0.5)
                press('enter')
                sleep(10)

        if escolha == 'B':
            def Git():
                print()
                sleep(0.5)
                print('Iniciando o versionamento do projeto...')
                sleep(0.5)
                press('win')
                sleep(0.5)
                write('Windows Terminal')
                sleep(0.5)
                press('enter')
                sleep(10)
                write('cd C:\dev\APEDC')
                sleep(0.5)
                press('enter')
                sleep(0.5)
                write('git add .')
                sleep(0.5)
                press('enter')
                sleep(0.5)
                write('git commit -m "Mudanças no projeto."')
                sleep(0.5)
                press('enter')
                sleep(0.5)
                write('git push')
                sleep(0.5)
                press('enter')
                sleep(10)
                hotkey('alt', 'f4')

        if escolha == 'C':
            def Logout():
                print()
                sleep(0.5)
                print('Saindo do programa...')
                sleep(3)
                hotkey('alt', 'f4')
