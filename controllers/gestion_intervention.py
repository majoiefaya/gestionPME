# Gestion des interventions
def liste_interventions():
     requete = db.intervention.id > 0
     rows = db(requete).select()
     return response.render('gestion_pme/gestion_intervention/liste_intervention.html', dict(interventions=rows))

  #CREATE
def create_intervention():
     form = SQLFORM(db.intervention)
     if form.process().accepted:
         session.flash = 'intervention créée'
         redirect(URL('gestion_intervention', 'liste_interventions'))
     return dict(form=form)

#UPDATE
def edit_intervention():
     intervention = db.intervention(request.args(0)) or redirect(URL('liste_interventions'))
     form = SQLFORM(db.intervention, intervention)
     if form.process().accepted:
         redirect(URL('liste_interventions'))
     return dict(form=form)

        
def delete_intervention():
     intervention_id = request.vars.id
     intervention = db.intervention(intervention_id)
     if not intervention:
         raise HTTP(404, "Le intervention n'existe pas")
     db(db.intervention.id == intervention_id).delete()
     session.flash = 'intervention supprimée'
     redirect(URL('gestion_intervention', 'liste_interventions'))

def gestion_interventions():
     form = SQLFORM(db.intervention)
     if form.process().accepted:
         response.flash = 'intervention ajouté'
     elif form.errors:
         response.flash = 'Erreur dans le formulaire'
     interventions = db(db.intervention).select()
     return dict(form=form, interventions=interventions)

