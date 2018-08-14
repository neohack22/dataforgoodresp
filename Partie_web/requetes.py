# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 15:32:57 2018

@author: nisha
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 16:38:45 2018

@author: nisha
"""

from connectionBD import connection_BD

def insertion_commentaire(): #un select
    com = connection_BD()
    cursor = com.cursor() 
    select_bd = "SELECT comment_id, contenu FROM commentaire where commentaire_label is NULL;" #on demande de récupérer les commentaires non labellisés
    cursor.execute(select_bd) #récupére les commentaires
    data = cursor.fetchall()#fetchall permet d'envoyer tous le resultats de ma requête dans cette variable
    com.commit()
    cursor.close()
    com.close()
    return data

def update_commentaire(id_comment, positif_ou_non):
    cnx = connection_BD()
    cursor = cnx.cursor()
    add_label_commentaire = 'UPDATE my_app.commentaire SET commentaire_label = %s WHERE comment_id = %s;'
    cursor.execute(add_label_commentaire, (positif_ou_non, id_comment))
    cnx.commit()
    cursor.close()
    cnx.close()
    
def récupération_labels():
    cnx = connection_BD()
    cursor = cnx.cursor()
    #query = "update my_app.commentaire set commentaire_label = {} where comment_id = {}".format(0, id_comment), a ne pas faire
    add_label_commentaire = "SELECT comment_id, contenu, commentaire_label FROM commentaire where commentaire_label is NOT NULL;"
    cursor.execute(add_label_commentaire)
    data = cursor.fetchall()
    cnx.commit()
    cursor.close()
    cnx.close()
    print(data)
    return data