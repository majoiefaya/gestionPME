@auth.requires_login()
def liste_clients():
     requete = db.client.id > 0
     rows = db(requete).select()
     return response.render('gestion_pme/gestion_client/liste_client.html', dict(clients=rows))

  #CREATE
@auth.requires_login()
def create_client():
     form = SQLFORM(db.client)
     if form.process().accepted:
         session.flash = 'client créée'
         redirect(URL('gestion_client', 'liste_clients'))
     return dict(form=form)

#UPDATE
@auth.requires_login()
def edit_client():
     client = db.client(request.args(0)) or redirect(URL('liste_clients'))
     form = SQLFORM(db.client, client)
     if form.process().accepted:
         redirect(URL('liste_clients'))
     return dict(form=form)

@auth.requires_login()
def delete_client():
     client_id = request.vars.id
     client = db.client(client_id)
     if not client:
         raise HTTP(404, "Le client n'existe pas")
     db(db.client.id == client_id).delete()
     session.flash = 'client supprimée'
     redirect(URL('gestion_client', 'liste_clients'))

@auth.requires_login()
def gestion_clients():
     form = SQLFORM(db.client)
     if form.process().accepted:
         response.flash = 'Client ajouté'
     elif form.errors:
         response.flash = 'Erreur dans le formulaire'
     clients = db(db.client).select()
     return dict(form=form, clients=clients)

