Bonjour et bienvenu sur Machos !
Le site de rencontre Geek (sans aucune interface graphique)

############## Générer les données ########

Pour générer les personnes sur lesquelles nous allons effectuer la recherche
utilisez la commande suivante :
python3 generate.py

ce script va utiliser le fichier csv caract.csv pour générer les données dont nous aurons besoin pour utiliser l'algorithme.

Vous pourrez avoir le détail des données choisies pour le maching dans le fichier modeldetail.csv

################ le concept ####

Je ne souhaitais pas faire un algorithme qui recherche les données similaires.
En effet on peut constater autours de nous que de nombreuses personnes sont bien mieux avec seulement quelques similitudes et beaucoup de différences.
C'est pourquoi une partie des donnés sélectionnées sont des données que le client veut trouver chez son partenaire mais qui ne seront pas nécessairement identiques aux leurs.

le script fast.py, plus rapide que good.py ne trouvera pas systématiquement les personnes qui machent le mieux, en revanche l'opération sera plus rapide.
Le concept est de lancer la recherche et d'attribuer une note pour chaque critère du candidat. Dans le cas du script rapide, la recherche s'arrête lorsque le candidat a reçu une note suffisamment élevée aux regard de nos critères.

Dans le cas du script plus lent : good.py, le principe de notation est le même, toutefois on attribue une valeur plus précise en fonction des données et le processus de matching ne s'arrête que lorsque chaque candidat a été testé. Ce, afin de proposer le meilleur candidat possible.

Esperons que vous trouverez l'amour!      
