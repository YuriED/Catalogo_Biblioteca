import tkinter as tk
from tkinter import ttk

class Livro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

class No:
    def __init__(self, livro):
        self.livro = livro
        self.esquerda = None
        self.direita = None

class AVLNode:
    def __init__(self, livro):
        self.livro = livro
        self.esquerda = None
        self.direita = None
        self.altura = 1

class ArvoreTitulo:
    def __init__(self):
        self.raiz = None

    def adicionar_livro(self, livro):
        self.raiz = self._adicionar_livro(self.raiz, livro)

    def _adicionar_livro(self, no, livro):
        if not no:
            return No(livro)
        
        if livro.titulo < no.livro.titulo:
            no.esquerda = self._adicionar_livro(no.esquerda, livro)
        elif livro.titulo > no.livro.titulo:
            no.direita = self._adicionar_livro(no.direita, livro)
        
        return no

    def remover_livro(self, no, titulo):
        if not no:
            return no

        if titulo < no.livro.titulo:
            no.esquerda = self.remover_livro(no.esquerda, titulo)
        elif titulo > no.livro.titulo:
            no.direita = self.remover_livro(no.direita, titulo)
        else:
            if not no.esquerda:
                return no.direita
            elif not no.direita:
                return no.esquerda

            temp = self.encontrar_minimo(no.direita)
            no.livro = temp.livro
            no.direita = self.remover_livro(no.direita, temp.livro.titulo)

        return no

    def encontrar_minimo(self, no):
        while no.esquerda:
            no = no.esquerda
        return no

    def em_ordem(self, no, lista):
        if no:
            self.em_ordem(no.esquerda, lista)
            lista.append(no.livro)
            self.em_ordem(no.direita, lista)

    def obter_lista_livros(self):
        lista = []
        self.em_ordem(self.raiz, lista)
        return lista

class AVLTree:
    def __init__(self):
        self.raiz = None

    def altura(self, no):
        if not no:
            return 0
        return no.altura

    def rotacao_direita(self, z):
        y = z.esquerda
        T3 = y.direita

        y.direita = z
        z.esquerda = T3

        z.altura = max(self.altura(z.esquerda), self.altura(z.direita)) + 1
        y.altura = max(self.altura(y.esquerda), self.altura(y.direita)) + 1

        return y

    def rotacao_esquerda(self, y):
        x = y.direita
        T2 = x.esquerda

        x.esquerda = y
        y.direita = T2

        y.altura = max(self.altura(y.esquerda), self.altura(y.direita)) + 1
        x.altura = max(self.altura(x.esquerda), self.altura(x.direita)) + 1

        return x

    def fator_balanceamento(self, no):
        if not no:
            return 0
        return self.altura(no.esquerda) - self.altura(no.direita)

    def adicionar_livro(self, livro):
        self.raiz = self._adicionar_livro(self.raiz, livro)

    def _adicionar_livro(self, no, livro):
        if not no:
            return AVLNode(livro)

        if livro.autor < no.livro.autor:
            no.esquerda = self._adicionar_livro(no.esquerda, livro)
        elif livro.autor > no.livro.autor:
            no.direita = self._adicionar_livro(no.direita, livro)
        else:
            return no

        no.altura = 1 + max(self.altura(no.esquerda), self.altura(no.direita))

        fator = self.fator_balanceamento(no)

        # Caso Esquerda-Esquerda
        if fator > 1 and livro.autor < no.esquerda.livro.autor:
            return self.rotacao_direita(no)

        # Caso Direita-Direita
        if fator < -1 and livro.autor > no.direita.livro.autor:
            return self.rotacao_esquerda(no)

        # Caso Esquerda-Direita
        if fator > 1 and livro.autor > no.esquerda.livro.autor:
            no.esquerda = self.rotacao_esquerda(no.esquerda)
            return self.rotacao_direita(no)

        # Caso Direita-Esquerda
        if fator < -1 and livro.autor < no.direita.livro.autor:
            no.direita = self.rotacao_direita(no.direita)
            return self.rotacao_esquerda(no)

        return no

    def remover_livro(self, no, titulo):
        if not no:
            return no

        if titulo < no.livro.titulo:
            no.esquerda = self.remover_livro(no.esquerda, titulo)
        elif titulo > no.livro.titulo:
            no.direita = self.remover_livro(no.direita, titulo)
        else:
            if not no.esquerda:
                return no.direita
            elif not no.direita:
                return no.esquerda

            temp = self.encontrar_minimo(no.direita)
            no.livro = temp.livro
            no.direita = self.remover_livro(no.direita, temp.livro.titulo)

        no.altura = 1 + max(self.altura(no.esquerda), self.altura(no.direita))

        fator = self.fator_balanceamento(no)

        # Caso Esquerda-Esquerda
        if fator > 1 and self.fator_balanceamento(no.esquerda) >= 0:
            return self.rotacao_direita(no)

        # Caso Direita-Direita
        if fator < -1 and self.fator_balanceamento(no.direita) <= 0:
            return self.rotacao_esquerda(no)

        # Caso Esquerda-Direita
        if fator > 1 and self.fator_balanceamento(no.esquerda) < 0:
            no.esquerda = self.rotacao_esquerda(no.esquerda)
            return self.rotacao_direita(no)

        # Caso Direita-Esquerda
        if fator < -1 and self.fator_balanceamento(no.direita) > 0:
            no.direita = self.rotacao_direita(no.direita)
            return self.rotacao_esquerda(no)

        return no

    def encontrar_minimo(self, no):
        while no.esquerda:
            no = no.esquerda
        return no

    def em_ordem(self, no, lista):
        if no:
            self.em_ordem(no.esquerda, lista)
            lista.append(no.livro)
            self.em_ordem(no.direita, lista)

    def obter_lista_livros(self):
        lista = []
        self.em_ordem(self.raiz, lista)
        return lista

class CatalogoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Catálogo de Livros")

        self.arvore_titulo = ArvoreTitulo()
        self.arvore_autor = AVLTree()

        self.arvore_titulo_treeview = ttk.Treeview(root, columns=('Autor', 'Título', 'Páginas'))
        self.arvore_titulo_treeview.heading('Autor', text='Autor')
        self.arvore_titulo_treeview.heading('Título', text='Título')
        self.arvore_titulo_treeview.heading('Páginas', text='Páginas')
        self.arvore_titulo_treeview.pack(padx=10, pady=10)

        self.arvore_autor_treeview = ttk.Treeview(root, columns=('Título', 'Páginas'))
        self.arvore_autor_treeview.heading('Título', text='Título')
        self.arvore_autor_treeview.heading('Páginas', text='Páginas')
        self.arvore_autor_treeview.pack(padx=10, pady=10)

        self.titulo_entry = tk.Entry(root, width=30)
        self.autor_entry = tk.Entry(root, width=30)
        self.paginas_entry = tk.Entry(root, width=30)

        tk.Label(root, text='Título:').pack(pady=5)
        self.titulo_entry.pack(pady=5)
        tk.Label(root, text='Autor:').pack(pady=5)
        self.autor_entry.pack(pady=5)
        tk.Label(root, text='Páginas:').pack(pady=5)
        self.paginas_entry.pack(pady=5)

        ttk.Button(root, text='Adicionar Livro', command=self.adicionar_livro).pack(pady=10)
        ttk.Button(root, text='Remover Livro', command=self.remover_livro).pack(pady=5)

    def adicionar_livro(self):
        titulo = self.titulo_entry.get()
        autor = self.autor_entry.get()
        paginas = self.paginas_entry.get()

        if titulo and autor and paginas:
            livro = Livro(titulo, autor, paginas)

            self.arvore_titulo.adicionar_livro(livro)
            self.arvore_autor.adicionar_livro(livro)

            self.titulo_entry.delete(0, tk.END)
            self.autor_entry.delete(0, tk.END)
            self.paginas_entry.delete(0, tk.END)

            self.atualizar_arvores()

    def remover_livro(self):
        titulo = self.titulo_entry.get()

        if titulo:
            self.arvore_titulo.raiz = self.arvore_titulo.remover_livro(self.arvore_titulo.raiz, titulo)
            self.arvore_autor.raiz = self.arvore_autor.remover_livro(self.arvore_autor.raiz, titulo)

            self.titulo_entry.delete(0, tk.END)

            self.atualizar_arvores()

    def atualizar_arvore(self, livros, treeview):
        for item in treeview.get_children():
            treeview.delete(item)

        for livro in livros:
            treeview.insert('', 'end', values=(livro.autor, livro.titulo, livro.num_paginas))

    def atualizar_arvores(self):
        lista_titulo = self.arvore_titulo.obter_lista_livros()
        lista_autor = self.arvore_autor.obter_lista_livros()

        self.atualizar_arvore(lista_titulo, self.arvore_titulo_treeview)
        self.atualizar_arvore(lista_autor, self.arvore_autor_treeview)

if __name__ == "__main__":
    root = tk.Tk()
    app = CatalogoApp(root)
    root.mainloop()

