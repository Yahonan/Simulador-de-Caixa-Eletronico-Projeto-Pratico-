import tkinter as tk
from tkinter import messagebox

saldo = 1000.0
usuario_correto = "Mozão"
senha_correta = "1234"
historico = []

# Variáveis globais para os widgets
entrada_valor = None
entrada_destinatario = None
janela_senha = None
entrada_nova_senha = None
entrada_boleto = None

def ver_saldo():
    messagebox.showinfo("Saldo", f"Seu saldo atual é: R$ {saldo:.2f}")

def depositar():
    global saldo
    try:
        valor = float(entrada_valor.get())
        if valor <= 0:
            messagebox.showerror("Erro", "Digite um valor maior que zero.")
        else:
            saldo += valor
            messagebox.showinfo("Depósito", f"Depósito de R$ {valor:.2f} realizado com sucesso.")
            entrada_valor.delete(0, tk.END)
            historico.append(f"Depósito de R${valor:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor válido.")

def sacar():
    global saldo
    try:
        valor = float(entrada_valor.get())
        if valor <= 0:
            messagebox.showerror('Erro', 'Digite um valor maior que zero')
        elif valor > saldo:
            messagebox.showerror('Erro', 'Saldo Insuficiente.')
        else:
            saldo -= valor
            historico.append(f"Saque de R${valor:.2f}")
            messagebox.showinfo('Saque', f'Saque de R${valor:.2f} realizado com sucesso')
            entrada_valor.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor válido.")

def mostrar_historico():
    if historico:
        transacoes = "\n".join(historico)
    else:
        transacoes = "Nenhuma transação registrada ainda"
    messagebox.showinfo("Histórico", transacoes)

def trocar_senha():
    global janela_senha, entrada_nova_senha
    janela_senha = tk.Toplevel(janela)
    janela_senha.title("Trocar Senha")
    janela_senha.geometry("300x200")
    janela_senha.configure(bg="#f8f9fa")
    janela_senha.resizable(False, False)
    tk.Label(janela_senha, text="Nova Senha", font=("Segoe UI", 11), bg="#f8f9fa").pack(pady=20)
    entrada_nova_senha = tk.Entry(janela_senha, font=("Segoe UI", 12), show="*", justify="center")
    entrada_nova_senha.pack(pady=5)
    tk.Button(janela_senha, text="Salvar", font=("Segoe UI", 11), bg="#4CAF50", fg="white", command=salvar_nova_senha).pack(pady=10)

def salvar_nova_senha():
    global senha_correta, janela_senha
    nova_senha = entrada_nova_senha.get()
    if len(nova_senha) < 4:
        messagebox.showerror("Erro!", "A senha deve ter pelo menos 4 dígitos")
    else:
        senha_correta = nova_senha
        messagebox.showinfo("Sucesso", "Senha alterada com sucesso!")
        janela_senha.destroy()

def resetar_conta():
    global saldo, historico
    resposta = messagebox.askyesno("Resetar", "Tem certeza que deseja zerar a conta e apagar o histórico?")
    if resposta:
        saldo = 0.0
        historico.clear()
        messagebox.showinfo("Resetado", "Conta zerada com sucesso!")

def pagar_conta():
    global saldo
    try:
        valor_pagamento = float(entrada_valor.get())
        codigo_boleto = entrada_boleto.get()

        if not codigo_boleto:
            messagebox.showerror("Erro", "Digite o código de barras/identificação da conta.")
        elif valor_pagamento <= 0:
            messagebox.showerror("Erro", "Valor do pagamento deve ser positivo.")
        elif valor_pagamento > saldo:
            messagebox.showerror("Erro", "Saldo insuficiente.")
        else:
            saldo -= valor_pagamento
            historico.append(f"Pagamento de conta {codigo_boleto}: R${valor_pagamento:.2f}")
            messagebox.showinfo("Sucesso", f"Pagamento de R${valor_pagamento:.2f} realizado com sucesso.")
        entrada_valor.delete(0, tk.END)
        entrada_boleto.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor de pagamento válido.")

def transferir():
    global saldo
    try:
        valor = float(entrada_valor.get())
        destinatario = entrada_destinatario.get()
        if not destinatario:
            messagebox.showerror("Erro", "Digite um destinatário para realizar a transferência.")
        elif valor <= 0:
            messagebox.showerror("Erro", "Digite um valor válido para a transação.")
        elif valor > saldo:
            messagebox.showerror("Erro", "Você não tem saldo disponível para continuar com a transação!")
        else:
            saldo -= valor
            historico.append(f"Transferência de R${valor:.2f} para {destinatario}")
            messagebox.showinfo("Transferência", f"Transferência de R${valor:.2f} para {destinatario} foi realizada com sucesso!")
            entrada_valor.delete(0, tk.END)
            entrada_destinatario.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor válido para a transação.")

def abrir_caixa():
    global entrada_valor, entrada_destinatario, entrada_boleto

    login_frame.destroy()

    # Aumente também o tamanho dos frames internos
    largura_frame = 800
    altura_frame = 800

    sombra = tk.Frame(janela, bg="#a3b1c6", width=largura_frame+10, height=altura_frame+10)
    sombra.place(relx=0.5, rely=0.5, anchor="center")

    frame = tk.Frame(janela, bg="#f8f9fa", width=largura_frame, height=altura_frame)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text=f"Bem-vindo, {usuario_correto}!", font=("Segoe UI", 12), bg="#f8f9fa", fg="#333").place(x=30, y=10)
    tk.Label(frame, text="Caixa Eletrônico", font=("Segoe UI", 20, "bold"), bg="#f8f9fa").place(relx=0.5, y=50, anchor="center")

    # Campo para código de barras (boleto)
    tk.Label(frame, text="Código de Barras:", font=("Segoe UI", 13), bg="#f8f9fa").place(x=30, y=100)
    entrada_boleto = tk.Entry(frame, font=("Segoe UI", 14), width=25, bd=1, relief="solid", justify="center")
    entrada_boleto.place(x=30, y=130)

    # Campo para valor
    tk.Label(frame, text="Valor (R$):", font=("Segoe UI", 13), bg="#f8f9fa").place(x=30, y=180)
    entrada_valor = tk.Entry(frame, font=("Segoe UI", 14), width=25, bd=1, relief="solid", justify="center")
    entrada_valor.place(x=30, y=210)

    # Campo para destinatário
    tk.Label(frame, text="Destinatário:", font=("Segoe UI", 13), bg="#f8f9fa").place(x=30, y=260)
    entrada_destinatario = tk.Entry(frame, font=("Segoe UI", 14), width=25, bd=1, relief="solid", justify="center")
    entrada_destinatario.place(x=30, y=290)

    estilo_botao = {"font": ("Segoe UI", 12, "bold"), "width": 25, "height": 1, "bd": 0, "relief": "flat"}

    tk.Button(frame, text="Pagar Conta", bg="#0F99DF", fg="white", command=pagar_conta, **estilo_botao).place(x=30, y=340)
    tk.Button(frame, text="Ver Saldo", bg="#0F99DF", fg="white", command=ver_saldo, **estilo_botao).place(x=30, y=400)
    tk.Button(frame, text="Depositar", bg="#2196F3", fg="white", command=depositar, **estilo_botao).place(x=30, y=460)
    tk.Button(frame, text="Sacar", bg="#0F99DF", fg="white", command=sacar, **estilo_botao).place(x=30, y=520)
    tk.Button(frame, text="Transferir", bg="#0F99DF", fg="white", command=transferir, **estilo_botao).place(x=30, y=580)

    tk.Button(frame, text="Histórico", bg="#0F99DF", fg="white", command=mostrar_historico, **estilo_botao).place(x=270, y=400)
    tk.Button(frame, text="Trocar Senha", bg="#FA9600", fg="black", command=trocar_senha, **estilo_botao).place(x=270, y=460)
    tk.Button(frame, text="Resetar Conta", bg="#ff0000", fg="white", command=resetar_conta, **estilo_botao).place(x=270, y=520)
    tk.Button(frame, text="Sair", bg="#ff0000", fg="white", command=janela.destroy, **estilo_botao).place(x=270, y=580)

def fazer_login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    if usuario == usuario_correto and senha == senha_correta:
        abrir_caixa()
    else:
        messagebox.showerror("Login inválido", "Usuário ou senha incorretos.")

janela = tk.Tk()
janela.title("Login - Caixa Eletrônico")
janela.geometry("900x900")  # Se quiser aumentar o tamanho da Janela é só alterar através dessa linha!
janela.configure(bg="#e0e5ec")
janela.resizable(False, False)

login_frame = tk.Frame(janela, bg="#f8f9fa", width=310, height=250)
login_frame.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(login_frame, text="Login", font=("Segoe UI", 16, "bold"), bg="#f8f9fa").pack(pady=20)

tk.Label(login_frame, text="Usuário:", font=("Segoe UI", 11), bg="#f8f9fa").pack()
entrada_usuario = tk.Entry(login_frame, font=("Segoe UI", 12), justify="center")
entrada_usuario.pack(pady=5)

tk.Label(login_frame, text="Senha:", font=("Segoe UI", 11), bg="#f8f9fa").pack()
entrada_senha = tk.Entry(login_frame, font=("Segoe UI", 12), show="*", justify="center")
entrada_senha.pack(pady=5)

tk.Button(login_frame, text="Entrar", font=("Segoe UI", 11, "bold"), bg="#4CAF50", fg="white", width=15, command=fazer_login).pack(pady=15)

janela.mainloop()
