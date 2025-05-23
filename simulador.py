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
    def salvar_nova_senha():
        global senha_correta
        nova = entrada.nova.get()
        if nova.strip() == "":
            messagebox.showerror("Erro", "Senha não pode ser vazia.")
        else:
            senha_correta = nova
            messagebox.showinfo("Sucesso", "Senha alterada com sucesso")
            janela_senha.destroy()
janela_senha = tk.Toplevel(janela)
janela_senha.title("Trocar senha")
janela_senha.geometry("300x150")
janela_senha.configure(bg="#f8f9fa")
tk.Label(janela_senha, text="Nova senha", font="Segoe UI", 11), (bg="#f8f9fa").pack(pady=10)
entrada_nova = tk.Entry(janela_senha, show='*', font=("Segoe UI", 12), justify="center")
entrada_nova.pack()
tk.Button(janela_senha, text="Salvar", bg="#4CAF50", fg="white", font=("Segoe UI"), 11), command= (salvar_nova_senha).pack(pady=10)

def resetar_conta():
    global saldo, historico
    resposta = messagebox.askyesno("Resetar", "Tem certeza que deseja zerar a conta e apagar o historico:")
    if resposta:
        saldo = 0.0
        historico.clear()
        messagebox.showinfo("Resetado", "Conta zerada com sucesso!")
        

def abrir_caixa():
    