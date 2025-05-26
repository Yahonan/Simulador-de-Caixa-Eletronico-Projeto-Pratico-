import tkinter as tk
from tkinter import messagebox

saldo = 1000.0
usuario_correto = "admin"
senha_correta = "1234"
historico = []

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
        messagebox.showinfo("Historico:", transacoes)

def trocar_senha():
    global janela
    global nova_senha
    janela_senha = tk.Toplevel(janela)
    janela_senha.title("Trocar Senha")
    janela_senha.geometry("300x200")
    janela_senha.configure(bg="#f8f9fa")
    janela_senha.resizable(False, False)
    tk.Label(janela_senha, text="Nova Senha", font=("Segoe UI", 11), bg="#f8f9fa").pack(pady=20)
    nova_senha.entry = tk.Entry(janela_senha, font=("Segoe UI", 12), show="*", justify="center")
    nova_senha_entry.pack(pady=5)

def salvar_nova_senha():
    global senha_correta  
    nova_senha = entrada_nova_senha.get()
    if len(nova_senha) < 4:
        messagebox.showerror("Erro!", "A senha deve ter pelo menos mais de 4 digítos")
    else:
        senha_correta = nova_senha
        messagebox.showinfo("Sucesso", "Senha alterada com sucesso!")
        janela_senha.destroy()
        
def resetar_conta():
    global saldo, historico
    resposta = messagebox.askyesno("Resetar", "Tem certeza que deseja zerar a conta e apagar o historico:")
    if resposta:
        saldo = 0.0
        historico.clear()
        messagebox.showinfo("Resetado", "Conta zerada com sucesso!")

def abrir_caixa():
    login_frame.destroy()

    sombra = tk.Frame(janela, bg="#a3b1c6", width=310, height=340)
    sombra.place(x=48, y=38)

    frame = tk.Frame(janela, bg="#f8f9fa", width=310, height=340)
    frame.place(x=40, y=30)

    tk.Label(frame, text="Caixa Eletrônico", font=("Segoe UI", 16, "bold"), bg="#f8f9fa").place(relx=0.5, y=30, anchor="center")

    tk.Label(frame, text="Valor (R$):", font=("Segoe UI", 11), bg="#f8f9fa").place(x=30, y=80)

    global entrada_valor
    entrada_valor = tk.Entry(frame, font=("Segoe UI", 12), width=20, bd=1, relief="solid", justify="center")
    entrada_valor.place(x=30, y=110)

    estilo_botao = {"font": ("Segoe UI", 11, "bold"), "width": 20, "height": 1, "bd": 0, "relief": "flat"}

    tk.Button(frame, text="Ver Saldo", bg="#4CAF50", fg="white", command=ver_saldo, **estilo_botao).place(x=30, y=160)
    tk.Button(frame, text="Depositar", bg="#2196F3", fg="white", command=depositar, **estilo_botao).place(x=30, y=200)
    tk.Button(frame, text="Sacar", bg="#FF9800", fg="white", command=sacar, **estilo_botao).place(x=30, y=240)
    tk.Button(frame, text="Sair", bg="#f44336", fg="white", command=janela.destroy, **estilo_botao).place(x=30, y=280)

def fazer_login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    if usuario == usuario_correto and senha == senha_correta:
        abrir_caixa()
    else:
        messagebox.showerror("Login inválido", "Usuário ou senha incorretos.")
        
janela = tk.Tk()
janela.title("Login - Caixa Eletrônico")
janela.geometry("400x400")
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
