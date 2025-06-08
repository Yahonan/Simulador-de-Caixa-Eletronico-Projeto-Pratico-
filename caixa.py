import tkinter as tk
from tkinter import messagebox

saldo = 1000.0
usuario_correto = "Mozão"
senha_correta = "1234"
historico = []

# Variável do modo escuro
modo_escuro = False

# Variáveis globais para os widgets
entrada_valor = None
entrada_destinatario = None
janela_senha = None
entrada_nova_senha = None
entrada_boleto = None
frame = None

# Função para alternar modo escuro/claro
def alternar_modo():
    global modo_escuro, frame
    modo_escuro = not modo_escuro
    if modo_escuro:
        cor_fundo = "#222831"
        cor_frame = "#393E46"
        cor_texto = "#EEEEEE"
        cor_botao = "#00ADB5"
        cor_botao_fg = "#EEEEEE"
    else:
        cor_fundo = "#e0e5ec"
        cor_frame = "#f8f9fa"
        cor_texto = "#333"
        cor_botao = "#0F99DF"
        cor_botao_fg = "white"

    janela.configure(bg=cor_fundo)
    # Atualiza widgets da janela
    for widget in janela.winfo_children():
        try:
            widget.configure(bg=cor_frame, fg=cor_texto)
        except:
            pass
    # Atualiza widgets do frame principal
    if frame:
        for widget in frame.winfo_children():
            if isinstance(widget, tk.Button):
                widget.configure(bg=cor_botao, fg=cor_botao_fg)
            else:
                try:
                    widget.configure(bg=cor_frame, fg=cor_texto)
                except:
                    pass

def ver_saldo():
    messagebox.showinfo("Saldo", f"Seu saldo atual é: R$ {saldo:.2f}")

def depositar():
    global saldo
    try:
        valor_str = entrada_valor.get().replace(',', '.')
        valor = float(valor_str)
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
        valor_str = entrada_valor.get().replace(',', '.')
        valor = float(valor_str)
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
        valor_pagamento_str = entrada_valor.get().replace(',', '.')
        valor_pagamento = float(valor_pagamento_str)
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
        valor_str = entrada_valor.get().replace(',', '.')
        valor = float(valor_str)
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
    global entrada_valor, entrada_destinatario, entrada_boleto, frame

    login_frame.destroy()

    largura_frame = 1100
    altura_frame = 400

    sombra = tk.Frame(janela, bg="#a3b1c6", width=largura_frame+10, height=altura_frame+10)
    sombra.place(relx=0.5, rely=0.5, anchor="center")

    canvas = tk.Canvas(janela, bg="#f8f9fa", width=largura_frame, height=altura_frame, highlightthickness=0)
    canvas.place(relx=0.5, rely=0.5, anchor="center")

    scrollbar = tk.Scrollbar(janela, orient="vertical", command=canvas.yview)
    scrollbar.place(relx=0.97, rely=0.5, anchor="center", height=altura_frame)

    frame = tk.Frame(canvas, bg="#f8f9fa", width=largura_frame, height=900)
    frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.create_window((0, 0), window=frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    def _on_mouse_wheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    canvas.bind_all("<MouseWheel>", _on_mouse_wheel)

    tk.Label(frame, text=f"Bem-vindo, {usuario_correto}!", font=("Segoe UI", 12), bg="#f8f9fa", fg="#333").place(x=30, y=10)
    tk.Label(frame, text="Caixa Eletrônico", font=("Segoe UI", 20, "bold"), bg="#f8f9fa").place(relx=0.5, y=50, anchor="center")

    tk.Label(frame, text="Código de Barras:", font=("Segoe UI", 13), bg="#f8f9fa").place(x=30, y=100)
    global entrada_boleto
    entrada_boleto = tk.Entry(frame, font=("Segoe UI", 14), width=25, bd=1, relief="solid", justify="center")
    entrada_boleto.place(x=30, y=130)

    tk.Label(frame, text="Valor (R$):", font=("Segoe UI", 13), bg="#f8f9fa").place(x=30, y=180)
    global entrada_valor
    entrada_valor = tk.Entry(frame, font=("Segoe UI", 14), width=25, bd=1, relief="solid", justify="center")
    entrada_valor.place(x=30, y=210)

    tk.Label(frame, text="Destinatário:", font=("Segoe UI", 13), bg="#f8f9fa").place(x=30, y=260)
    global entrada_destinatario
    entrada_destinatario = tk.Entry(frame, font=("Segoe UI", 14), width=25, bd=1, relief="solid", justify="center")
    entrada_destinatario.place(x=30, y=290)

    estilo_botao = {"font": ("Segoe UI", 12, "bold"), "width": 25, "height": 1, "bd": 0, "relief": "flat"}

    espacamento = 60
    y_inicial = 340

    tk.Button(frame, text="Pagar Conta", bg="#0F99DF", fg="white", command=pagar_conta, **estilo_botao).place(x=30, y=y_inicial + espacamento*0)
    tk.Button(frame, text="Ver Saldo", bg="#0F99DF", fg="white", command=ver_saldo, **estilo_botao).place(x=30, y=y_inicial + espacamento*1)
    tk.Button(frame, text="Depositar", bg="#2196F3", fg="white", command=depositar, **estilo_botao).place(x=30, y=y_inicial + espacamento*2)
    tk.Button(frame, text="Sacar", bg="#0F99DF", fg="white", command=sacar, **estilo_botao).place(x=30, y=y_inicial + espacamento*3)
    tk.Button(frame, text="Transferir", bg="#0F99DF", fg="white", command=transferir, **estilo_botao).place(x=30, y=y_inicial + espacamento*4)
    tk.Button(frame, text="Histórico", bg="#0F99DF", fg="white", command=mostrar_historico, **estilo_botao).place(x=30, y=y_inicial + espacamento*5)
    tk.Button(frame, text="Trocar Senha", bg="#FA9600", fg="black", command=trocar_senha, **estilo_botao).place(x=30, y=y_inicial + espacamento*6)
    tk.Button(frame, text="Resetar Conta", bg="#ff0000", fg="white", command=resetar_conta, **estilo_botao).place(x=30, y=y_inicial + espacamento*7)
    tk.Button(frame, text="Sair", bg="#ff0000", fg="white", command=janela.destroy, **estilo_botao).place(x=30, y=y_inicial + espacamento*8)
    tk.Button(frame, text="Modo Escuro", bg="#222831", fg="#EEEEEE", command=alternar_modo, **estilo_botao).place(x=30, y=y_inicial + espacamento*9)

def fazer_login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    if usuario == usuario_correto and senha == senha_correta:
        abrir_caixa()
    else:
        messagebox.showerror("Login inválido", "Usuário ou senha incorretos.")

janela = tk.Tk()
janela.title("Login - Caixa Eletrônico")
janela.geometry("1200x800")
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