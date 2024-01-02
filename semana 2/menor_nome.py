def menor_nome(nomes):
    men = len(nomes[0].strip())
    Mnome = nomes[0].strip().capitalize()
    for n in nomes:
        if len(n.strip()) < men:
            Mnome = n.strip().capitalize()
            men = len(n.strip())
    return Mnome

menor_nome(['maria', 'josé', 'PAULO', 'Catarina'])