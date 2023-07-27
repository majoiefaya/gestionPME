# Gestion des contrats
@auth.requires_login()
def liste_contrats():
     requete = db.contrat.id > 0
     rows = db(requete).select()
     return response.render('gestion_pme/gestion_contrat/liste_contrat.html', dict(contrats=rows))

  #CREATE4
@auth.requires_login()
def create_contrat():
     form = SQLFORM(db.contrat)
     if form.process().accepted:
         session.flash = 'contrat créée'
         redirect(URL('gestion_contrat', 'liste_contrats'))
     return dict(form=form)

#UPDATE
@auth.requires_login()
def edit_contrat():
     contrat = db.contrat(request.args(0)) or redirect(URL('liste_contrats'))
     form = SQLFORM(db.contrat, contrat)
     if form.process().accepted:
         redirect(URL('liste_contrats'))
     return dict(form=form)

@auth.requires_login()    
def delete_contrat():
     contrat_id = request.vars.id
     contrat = db.contrat(contrat_id)
     if not contrat:
         raise HTTP(404, "Le contrat n'existe pas")
     db(db.contrat.id == contrat_id).delete()
     session.flash = 'contrat supprimée'
     redirect(URL('gestion_contrat', 'liste_contrats'))

@auth.requires_login()
def gestion_contrats():
     form = SQLFORM(db.contrat)
     if form.process().accepted:
         response.flash = 'contrat ajouté'
     elif form.errors:
         response.flash = 'Erreur dans le formulaire'
     contrats = db(db.contrat).select()
     return dict(form=form, contrats=contrats)

