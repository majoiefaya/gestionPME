@auth.requires_login()
def liste_employes():
     requete = db.employe.id > 0
     rows = db(requete).select()
     return response.render('gestion_pme/gestion_employe/liste_employe.html', dict(employes=rows))

  #CREATE
@auth.requires_login()
def create_employe():
     form = SQLFORM(db.employe)
     if form.process().accepted:
         session.flash = 'employe créée'
         redirect(URL('gestion_employe', 'liste_employes'))
     return dict(form=form)

#UPDATE
@auth.requires_login()
def edit_employe():
     employe = db.employe(request.args(0)) or redirect(URL('liste_employes'))
     form = SQLFORM(db.employe, employe)
     if form.process().accepted:
         redirect(URL('liste_employes'))
     return dict(form=form)

@auth.requires_login()
def delete_employe():
     employe_id = request.vars.id
     employe = db.employe(employe_id)
     if not employe:
         raise HTTP(404, "Le employe n'existe pas")
     db(db.employe.id == employe_id).delete()
     session.flash = 'employe supprimée'
     redirect(URL('gestion_employe', 'liste_employes'))

@auth.requires_login()
def gestion_employes():
     form = SQLFORM(db.employe)
     if form.process().accepted:
         response.flash = 'employe ajouté'
     elif form.errors:
         response.flash = 'Erreur dans le formulaire'
     employes = db(db.employe).select()
     return dict(form=form, employes=employes)

