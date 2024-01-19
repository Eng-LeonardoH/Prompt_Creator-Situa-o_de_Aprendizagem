import tkinter as tk
from tkinter import messagebox

def gerar_situacao_aprendizagem():
    Curso = entry_curso.get()
    Disciplina = entry_disciplina.get()
    ObjetivoGeral = entry_objetivo.get()
    Capacidades = entry_capacidades.get()
    Conhecimentos = entry_conhecimentos.get()
    CargaHoraria = entry_carga_horaria.get()

    resultado = f"""Você é professor do curso {Curso} e está ministrando a
    disciplina de {Disciplina}, que tem como objetivo geral: {ObjetivoGeral}
    Você precisa desenvolver uma situação de aprendizagem: situações de
    aprendizagem compõem um conjunto de ações que, planejadas pedagogicamente,
    favorecem aprendizagens significativas, por meio da utilização de estratégias
    de aprendizagem desafiadoras e de diferentes estratégias de ensino.
    Considere:
    1. Capacidades a serem desenvolvidas: {Capacidades}

    2. Conhecimentos a serem trabalhados: {Conhecimentos}
    3. Carga horária para desenvolvimento: {CargaHoraria}
    A situação de aprendizagem precisa ter a seguinte estrutura:
    1. Título
    2. Contexto de uma situação real
    3. Desafio, o aluno deve resolver um problema baseado no contexto dentro da
    carga horária estabelecida
    4. Entregas, deve deixar claro ao aluno o que se espera como resultado do
    desafio e o que deve ser entregue"""

    resultado_text.config(state=tk.NORMAL)
    resultado_text.delete(1.0, tk.END)
    resultado_text.insert(tk.END, resultado)
    resultado_text.config(state=tk.DISABLED)

def copiar_resultado():
    resultado_text.clipboard_clear()
    resultado_text.clipboard_append(resultado_text.get(1.0, tk.END))
    resultado_text.update()
    messagebox.showinfo("Copiado", "Texto copiado para a área de transferência!")

# Criar a janela principal
janela = tk.Tk()
janela.title("Gerador de Situação de Aprendizagem")

# Criar e posicionar os widgets na janela
label_curso = tk.Label(janela, text="Digite o nome do curso:")
label_curso.grid(row=0, column=0, sticky="E")
entry_curso = tk.Entry(janela)
entry_curso.grid(row=0, column=1)

label_disciplina = tk.Label(janela, text="Digite o nome da Unidade Curricular:")
label_disciplina.grid(row=1, column=0, sticky="E")
entry_disciplina = tk.Entry(janela)
entry_disciplina.grid(row=1, column=1)

label_objetivo = tk.Label(janela, text="Digite o objetivo geral da unidade curricular:")
label_objetivo.grid(row=2, column=0, sticky="E")
entry_objetivo = tk.Entry(janela)
entry_objetivo.grid(row=2, column=1)

label_capacidades = tk.Label(janela, text="Digite quais capacidades deseja desenvolver:")
label_capacidades.grid(row=3, column=0, sticky="E")
entry_capacidades = tk.Entry(janela)
entry_capacidades.grid(row=3, column=1)

label_conhecimentos = tk.Label(janela, text="Digite quais Conhecimentos a serem trabalhados:")
label_conhecimentos.grid(row=4, column=0, sticky="E")
entry_conhecimentos = tk.Entry(janela)
entry_conhecimentos.grid(row=4, column=1)

label_carga_horaria = tk.Label(janela, text="Digite a carga horária que o aluno trabalhará:")
label_carga_horaria.grid(row=5, column=0, sticky="E")
entry_carga_horaria = tk.Entry(janela)
entry_carga_horaria.grid(row=5, column=1)

btn_gerar = tk.Button(janela, text="Criar prompt para o ChatGPT gerar a situação de aprendizagem", command=gerar_situacao_aprendizagem)
btn_gerar.grid(row=6, column=0, columnspan=2, pady=10)

resultado_text = tk.Text(janela, height=15, width=80, state=tk.DISABLED)
resultado_text.grid(row=7, column=0, columnspan=2)

btn_copiar = tk.Button(janela, text="Copiar Resultado", command=copiar_resultado)
btn_copiar.grid(row=8, column=0, columnspan=2, pady=10)

# Iniciar o loop principal da janela
janela.mainloop()
