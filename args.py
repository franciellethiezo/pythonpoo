def series (**kwargs):
    comedia = kwargs.get('comedia')

    if comedia is not None:
        print(f'Esta é uma série de comédia: {comedia}')

series(drama = 'Sons of Anarchy', fantasia ='O Estranho Mundo de Sabrina', comedia ='How I Met Your Mother', suspense ='Orphan Black')
