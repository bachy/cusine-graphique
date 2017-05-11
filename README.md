# cusine-graphique


## Introduction terminal

### ~ (home)
Lorsque vous ouvrez votre terminal, par default vous vous trouvez dans votre Home, simbolisé par ce signe ~

### ls (liste)

ls : __l__i__s__te
Lister les contenus du dossier ou vous vous trouvez

```ls```

### cd (*c*hange *d*irectory)
il faut vous déplacer dans vos dossier pour aller là ou vous voulez travailler, pour cela on utilise la commande ```cd```
cd : __c__hange __d__irectory
```cd dossier/dossier/dossier```

## récupérer

Une fois que vous êtes au bon endroit dans vos dossiers, vous allez récupérer le dépos git de travail (repository en anglais)

```git clone https://github.com/bachy/cusine-graphique.git```

cette commande crée la où vous êtes un dossier _cusine-graphique_ (attention a la faute de frappe dans le nom du dépo)

on se déplace maintenant dans le dossier créé

```cd cusine-graphique```

Il n'est pas nécessaire de faire ```git init``` car ce dossier est deja un dossier git

par contre on peut faire un ```git status``` pour voir ou en ai le dépo

## Travailler

on liste les contenus de ce dossier

```ls```

on liste le contenu du dossier _page_

```ls pages/```

le dossier _pages_ contient un dossier _master_ qui est votre modele de départ

on duplique le dossier _master_ pour faire votre dossier de travail personel
pour cela on utilise la commande _cp_ : _c_o_p_ier (copy)

```cp pages/master pages/mon_nom_mon_prenom```

on ouvre le dossier avec atom ou un autre éditeur de code.

les deux fichiers avec les quels vous allez travailler sont _index.html_ est _styles.css_



## Add, Commite

L'enregistrement de votre travail avec git se fais en deux étapes, d'abords add puis commit

Je vérifie ce qui a changer

```git status```

j'ajoutte (add) les changements à la liste

```
git add page/mon_nom_mon_prenom/index.html
git add page/mon_nom_mon_prenom/styles.css
```

j'enregistre (commit)

```git commit -m "mon message de commit que je personnalise à chaque fois"```

## Push, Pull

