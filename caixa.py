# ===================== Tela do caixa eletrônico =====================
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

# ===================== Função de login =====================
def fazer_login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    if usuario == usuario_correto and senha == senha_correta:
        abrir_caixa()
    else:
        messagebox.showerror("Login inválido", "Usuário ou senha incorretos.")

# ===================== Janela principal =====================
janela = tk.Tk()
janela.title("Login - Caixa Eletrônico")
janela.geometry("400x400")
janela.configure(bg="#e0e5ec")
janela.resizable(False, False)

# ===================== Tela de Login =====================
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