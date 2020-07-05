# Auteurs: À compéter

from piece import Piece
from position import Position


class Damier:
    """Plateau de jeu d'un jeu de dames. Contient un ensemble de pièces positionnées à une certaine position
    sur le plateau.

    Attributes:
        cases (dict): Dictionnaire dont une clé représente une Position, et une valeur correspond à la Piece
            positionnée à cet endroit sur le plateau. Notez bien qu'une case vide (sans pièce blanche ou noire)
            correspond à l'absence de clé la position de cette case dans le dictionnaire.

        n_lignes (int): Le nombre de lignes du plateau. La valeur est 8 (constante).
        n_colonnes (int): Le nombre de colonnes du plateau. La valeur est 8 (constante).

    """


    def __init__(self):
        """Constructeur du Damier. Initialise un damier initial de 8 lignes par 8 colonnes.

        """
        self.n_lignes = 8
        self.n_colonnes = 8

        self.cases = {
            Position(7, 0): Piece("blanc", "pion"),
            Position(7, 2): Piece("blanc", "pion"),
            Position(7, 4): Piece("blanc", "pion"),
            Position(7, 6): Piece("blanc", "pion"),
            Position(6, 1): Piece("blanc", "pion"),
            Position(6, 3): Piece("blanc", "pion"),
            Position(6, 5): Piece("blanc", "pion"),
            Position(6, 7): Piece("blanc", "pion"),
            Position(5, 0): Piece("blanc", "pion"),
            Position(5, 2): Piece("blanc", "pion"),
            Position(5, 4): Piece("blanc", "pion"),
            Position(5, 6): Piece("blanc", "pion"),
            Position(2, 1): Piece("noir", "pion"),
            Position(2, 3): Piece("noir", "pion"),
            Position(2, 5): Piece("noir", "pion"),
            Position(2, 7): Piece("noir", "pion"),
            Position(1, 0): Piece("noir", "pion"),
            Position(1, 2): Piece("noir", "pion"),
            Position(1, 4): Piece("noir", "pion"),
            Position(1, 6): Piece("noir", "pion"),
            Position(0, 1): Piece("noir", "pion"),
            Position(0, 3): Piece("noir", "pion"),
            Position(0, 5): Piece("noir", "pion"),
            Position(0, 7): Piece("noir", "pion"),
        }

    def recuperer_piece_a_position(self, position):
        """Récupère une pièce dans le damier à partir d'une position.

        Args:
            position (Position): La position où récupérer la pièce.

        Returns:
            La pièce (de type Piece) à la position reçue en argument, ou None si aucune pièce n'était à cette position.

        """
        if position not in self.cases:
            return None

        return self.cases[position]

    def position_est_dans_damier(self, position):
        """Vérifie si les coordonnées d'une position sont dans les bornes du damier (entre 0 inclusivement et le nombre
        de lignes/colonnes, exclusement.

        Args:
            position (Position): La position à valider.

        Returns:
            bool: True si la position est dans les bornes, False autrement.

        """
        #TODO: À compléter


        """
        vérifie si les coordonnées d'une position sont dans les bornes du damier
        """

        #Récupérer les valeurs x et y de la position
        ligne = position.ligne
        colonne = position.colonne

        #
        return ligne >= 0 and ligne < self.n_lignes and colonne >=0 and colonne < self.n_colonnes




    def piece_peut_se_deplacer_vers(self, position_piece, position_cible):
        """Cette méthode détermine si une pièce (à la position reçue) peut se déplacer à une certaine position cible.
        On parle ici d'un déplacement standard (et non une prise).

        Une pièce doit être positionnée à la position_piece reçue en argument (retourner False autrement).


        Une pièce de type pion ne peut qu'avancer en diagonale (vers le haut pour une pièce blanche, vers le bas pour
        une pièce noire).

        Une pièce de type dame peut avancer sur n'importe quelle diagonale, peu importe sa couleur.
        Une pièce ne peut pas se déplacer sur une case déjà occupée par une autre pièce. Une pièce ne peut pas se
        déplacer à l'extérieur du damier.

        Args:
            position_piece (Position): La position de la pièce source du déplacement.
            position_cible (Position): La position cible du déplacement.

        Returns:
            bool: True si la pièce peut se déplacer à la position cible, False autrement.

        """
        # TODO: À compléter

        """
        Il faut entre autres y prendre en compte le type de pièce et sa couleur. Donc, plusieurs conditions sera 
        creer
        """
        # vérifie si une pièce située en position_piece peut se déplacer vers position_cible.
        # Couleur, type


        # Récupérer les valeurs x et y de la position
        """On ne peut pas comparer position_piece à position_tuple car la classe Position n'est pas iterable
            Il faut donc prendre la valeur x, et y des deux arguments et en crée des tuples."""
        position_piece_x = position_piece.ligne
        position_piece_y = position_piece.colonne
        position_piece_tuple = (position_piece_x, position_piece_y)

        # Récupérer les valeurs x et y de la position
        position_cible_x = position_cible.ligne
        position_cible_y = position_cible.colonne
        position_cible_tuple = (position_cible_x, position_cible_y)



        """
        Une pièce de type pion ne peut qu'avancer en diagonale vers le haut ou vers le bas 
        """
        # Ici on verifie si la piece peut se deplacer en haut ou en bas diagonalement

        return (
            # Si la position actuelle est la même que la position cible, alors aucun déplacement peut se faire
            (position_piece_tuple != position_cible_tuple) and

            # Ici on verifie si la piece peut se deplacer en haut ou en bas diagonalement
            ((position_piece_y + 1) == position_cible_y or (position_piece_y - 1) == position_cible_y) and
            ((position_piece_x + 1) == position_cible_x or (position_piece_y - 1) == position_cible_x)

            and (
            # On vérifie si la position piece se trouve à l'extérieur du damier
            position_piece_x >= 0 and position_piece_x < self.n_lignes and position_piece_y >= 0 and position_piece_y < self.n_colonnes)

            # On vérifie si la position ciblé se trouve à l'extérieur du damier
            and (
            position_cible_x >= 0 and position_cible_x < self.n_lignes and position_cible_y >= 0 and position_cible_y < self.n_colonnes)

        )




    def piece_peut_sauter_vers(self, position_piece, position_cible):
        """Cette méthode détermine si une pièce (à la position reçue) peut sauter vers une certaine position cible.
        On parle ici d'un déplacement qui "mange" une pièce adverse.

        Une pièce doit être positionnée à la position_piece reçue en argument (retourner False autrement).

        Une pièce ne peut que sauter de deux cases en diagonale. N'importe quel type de pièce (pion ou dame) peut sauter
        vers l'avant ou vers l'arrière. Une pièce ne peut pas sauter vers une case qui est déjà occupée par une autre
        pièce. Une pièce ne peut faire un saut que si elle saute par dessus une pièce de couleur adverse.

        Args:
            position_piece (Position): La position de la pièce source du saut.
            position_cible (Position): La position cible du saut.

        Returns:
            bool: True si la pièce peut sauter vers la position cible, False autrement.

        """
        #TODO: À compléter
        # Il ne peut se déplacer qu'en diagonale
        # Vérifier si le mouvement lui-même est valide

        #Récupérer les valeurs x et y de la position
        """On ne peut pas comparer position_piece à position_tuple car la classe Position n'est pas iterable
            Il faut donc prendre la valeur x, et y des deux arguments et en crée des tuples."""
        position_piece_x = position_piece.ligne
        position_piece_y = position_piece.colonne
        position_piece_tuple = (position_piece_x, position_piece_y)

        #Récupérer les valeurs x et y de la position
        position_cible_x = position_cible.ligne
        position_cible_y = position_cible.colonne
        position_cible_tuple = (position_cible_x, position_cible_y)


        """On veut vérifier s'il y a déjà une pièce dans la direction que position_cible veut s'orienter
        on crée deux tuples à partir de la liste afin d'effectuer une comparaison"""
        positions_diag_bas = Position.positions_diagonales_bas(position_piece)
        positions_diag_bas_un =  positions_diag_bas[0]
        positions_diag_bas_deux = positions_diag_bas[1]

        #Récupérer les valeurs x et y de la position positions_diagonales_bas(position_piece)
        positions_diag_bas_un_x = positions_diag_bas_un.ligne
        positions_diag_bas_un_y = positions_diag_bas_un.colonne
        positions_diag_bas_un_tuple = (positions_diag_bas_un_x, positions_diag_bas_un_y)

        #Récupérer les valeurs x et y de la position positions_diagonales_bas(position_piece)
        positions_diag_bas_deux_x = positions_diag_bas_deux.ligne
        positions_diag_bas_deux_y = positions_diag_bas_deux.colonne
        positions_diag_bas_deux_tuple = (positions_diag_bas_deux_x, positions_diag_bas_deux_y)

        """ On veut aussi verifier vers le haut"""

        positions_diag_haut = Position.positions_diagonales_haut(position_piece)
        positions_diag_haut_un = positions_diag_haut[0]
        positions_diag_haut_deux = positions_diag_haut[1]

        # Récupérer les valeurs x et y de la position positions_diagonales_bas(position_piece)
        positions_diag_haut_un_x = positions_diag_haut_un.ligne
        positions_diag_haut_un_y = positions_diag_haut_un.colonne
        positions_diag_haut_un_tuple = (positions_diag_haut_un_x, positions_diag_haut_un_y)

        # Récupérer les valeurs x et y de la position positions_diagonales_bas(position_piece)
        positions_diag_haut_deux_x =  positions_diag_haut_deux.ligne
        positions_diag_haut_deux_deux_y =  positions_diag_haut_deux.colonne
        positions_diag_haut_deux_tuple = (positions_diag_haut_deux_x, positions_diag_haut_deux_deux_y)

        #Une pièce ne peut pas sauter vers une case qui est déjà occupée par une autre pièce.
        if position_piece_tuple  == position_cible_tuple:
            return False #Aucun déplacement s'est effectué

        #On veut vérifier s'il y a déjà une pièce en bas diagonalement dans la position_cible
        elif position_piece_tuple == positions_diag_bas_un_tuple or position_piece_tuple == positions_diag_bas_deux_tuple:
            return False

        #On veut vérifier s'il y a déjà une pièce en bas diagonalement dans la position_cible
        elif position_piece_tuple == positions_diag_haut_un_tuple or position_piece_tuple == positions_diag_haut_deux_tuple:
            return False

        else:
            """ Une pièce ne peut que sauter de deux cases en diagonale"""
            comparaison_x = 1 <= position_cible_tuple[0]-position_piece_tuple[0] < 2
            comparaison_y =  1 <=position_cible_tuple[1]-position_piece_tuple[1] < 2
            peut_deplacer = comparaison_x and comparaison_y

            # Vérifie si la pièce peut sauter vers la position cible
            return peut_deplacer



    def piece_peut_se_deplacer(self, position_piece):
        """Vérifie si une pièce à une certaine position a la possibilité de se déplacer (sans faire de saut).

        ATTENTION: N'oubliez pas qu'étant donné une position, il existe une méthode dans la classe Position retournant
        les positions des quatre déplacements possibles.

        Args:
            position_piece (Position): La position source.

        Returns:
            bool: True si une pièce est à la position reçue et celle-ci peut se déplacer, False autrement.

        """
        #TODO: À compléter
        """Vérifie si une pièce à une certaine position a la possibilité de se déplacer (sans faire de saut)."""

        """On ne peut pas comparer position_piece car la classe Position n'est pas iterable
            Il faut donc prendre la valeur x, et y de l'argument position_piece et en crée un tuple."""
        # Récupérer les valeurs x et y de la position
        position_piece_x = position_piece.ligne
        position_piece_y = position_piece.colonne
        position_piece_tuple = (position_piece_x, position_piece_y)



        """On veut vérifier s'il y a déjà une pièce dans la direction que position_piece veut s'orienter
        on crée des tuples à partir des listes générer par la function quatre_positions_diagonales(position_piece)"""
        positions_diag = Position.quatre_positions_diagonales(position_piece)
        positions_diag_un =  positions_diag[0]
        positions_diag_deux = positions_diag[1]
        positions_diag_trois =  positions_diag[2]
        positions_diag_quatre = positions_diag[3]

        #Recupere la premiere position positions_diagonales(position_piece)
        positions_diag_un_x = positions_diag_un.ligne
        positions_diag_un_y = positions_diag_un.colonne
        positions_diag_un_tuple = (positions_diag_un_x, positions_diag_un_y)

        #Récupere la deuxieme position positions_diagonales(position_piece)
        positions_diag_deux_x = positions_diag_deux.ligne
        positions_diag_deux_y = positions_diag_deux.colonne
        positions_diag_deux_tuple = (positions_diag_deux_x, positions_diag_deux_y)

        #Récupere la troisieme position positions_diagonales(position_piece)
        positions_diag_trois_x = positions_diag_trois.ligne
        positions_diag_trois_y = positions_diag_trois.colonne
        positions_diag_trois_tuple = (positions_diag_trois_x, positions_diag_trois_y)

        #Récupere la quatrieme position positions_diagonales(position_piece)
        positions_diag_quatre_x = positions_diag_quatre.ligne
        positions_diag_quatre_y = positions_diag_quatre.colonne
        positions_diag_quatre_tuple = (positions_diag_quatre_x, positions_diag_quatre_y)



        #Une pièce ne peut pas déplacer vers une case qui est déjà occupée par une autre pièce.
        if position_piece_tuple == positions_diag_un_tuple:
            return False #Aucun déplacement s'est effectué

        #Une pièce ne peut pas déplacer vers une case qui est déjà occupée par une autre pièce.
        elif position_piece_tuple == positions_diag_deux_tuple:
            return False

        #Une pièce ne peut pas déplacer vers une case qui est déjà occupée par une autre pièce.
        elif position_piece_tuple == positions_diag_trois_tuple:
            return False

        #Une pièce ne peut pas déplacer vers une case qui est déjà occupée par une autre pièce.
        elif position_piece_tuple == positions_diag_quatre_tuple:
            return False

        else:
            #peut se déplacer dans toutes les directions sans faire de saut
            return True


    def piece_peut_faire_une_prise(self, position_piece):
        """Vérifie si une pièce à une certaine position a la possibilité de faire une prise.

        Warning:
            N'oubliez pas qu'étant donné une position, il existe une méthode dans la classe Position retournant
            les positions des quatre sauts possibles.

        Args:
            position_piece (Position): La position source.

        Returns:
            bool: True si une pièce est à la position reçue et celle-ci peut faire une prise. False autrement.

        """
        #TODO: À compléter

        """On ne peut pas comparer position_piece car la classe Position n'est pas iterable
            Il faut donc prendre la valeur x, et y de l'argument position_piece et en crée un tuple."""
        # Récupérer les valeurs x et y de la position
        position_piece_x = position_piece.ligne
        position_piece_y = position_piece.colonne
        position_piece_tuple = (position_piece_x, position_piece_y)



        """On veut vérifier s'il y a déjà une pièce dans la direction que position_piece veut s'orienter
        on crée des tuples à partir des listes générer par la function quatre_positions_diagonales(position_piece)"""
        positions_diag = Position.quatre_positions_diagonales(position_piece)
        positions_diag_un =  positions_diag[0]
        positions_diag_deux = positions_diag[1]
        positions_diag_trois =  positions_diag[2]
        positions_diag_quatre = positions_diag[3]

        #Recupere la premiere position positions_diagonales(position_piece)
        positions_diag_un_x = positions_diag_un.ligne
        positions_diag_un_y = positions_diag_un.colonne
        positions_diag_un_tuple = (positions_diag_un_x, positions_diag_un_y)

        #Récupere la deuxieme position positions_diagonales(position_piece)
        positions_diag_deux_x = positions_diag_deux.ligne
        positions_diag_deux_y = positions_diag_deux.colonne
        positions_diag_deux_tuple = (positions_diag_deux_x, positions_diag_deux_y)

        #Récupere la troisieme position positions_diagonales(position_piece)
        positions_diag_trois_x = positions_diag_trois.ligne
        positions_diag_trois_y = positions_diag_trois.colonne
        positions_diag_trois_tuple = (positions_diag_trois_x, positions_diag_trois_y)

        #Récupere la quatrieme position positions_diagonales(position_piece)
        positions_diag_quatre_x = positions_diag_quatre.ligne
        positions_diag_quatre_y = positions_diag_quatre.colonne
        positions_diag_quatre_tuple = (positions_diag_quatre_x, positions_diag_quatre_y)



        #À la possibilité de faire une prise
        if position_piece_tuple == positions_diag_un_tuple:
            return True#Aucun déplacement s'est effectué

        #À la possibilité de faire une prise
        elif position_piece_tuple == positions_diag_deux_tuple:
            return True

        #À la possibilité de faire une prise
        elif position_piece_tuple == positions_diag_trois_tuple:
            return True

        #À la possibilité de faire une prise
        elif position_piece_tuple == positions_diag_quatre_tuple:
            return True

        else:
            #À la possibilité de faire une prise
            return False

    def piece_de_couleur_peut_se_deplacer(self, couleur):
        """Vérifie si n'importe quelle pièce d'une certaine couleur reçue en argument a la possibilité de se déplacer
        vers une case adjacente (sans saut).

        ATTENTION: Réutilisez les méthodes déjà programmées!

        Args:
            couleur (str): La couleur à vérifier.

        Returns:
            bool: True si une pièce de la couleur reçue peut faire un déplacement standard, False autrement.
        """
        #TODO: À compléter
        # Récupérer les valeurs x et y de la position
        """On ne peut pas comparer position_piece à position_tuple car la classe Position n'est pas iterable
            Il faut donc prendre la valeur x, et y des deux arguments et en crée des tuples."""
        return (
            # Vérifier si la piece est du couleur noir ou blanc
            (couleur == "noir" or couleur == "blanc")
        )

    def piece_de_couleur_peut_faire_une_prise(self, couleur):
        """Vérifie si n'importe quelle pièce d'une certaine couleur reçue en argument a la possibilité de faire un
        saut, c'est à dire vérifie s'il existe une pièce d'une certaine couleur qui a la possibilité de prendre une
        pièce adverse.

        ATTENTION: Réutilisez les méthodes déjà programmées!

        Args:
            couleur (str): La couleur à vérifier.

        Returns:
            bool: True si une pièce de la couleur reçue peut faire un saut (une prise), False autrement.
        """
        #TODO: À compléter
        if couleur == "noir" or couleur == "blanc":
            return True
        else:
            return False


    def deplacer(self, position_source, position_cible):
        """Effectue le déplacement sur le damier. Si le déplacement est valide, on doit mettre à jour le dictionnaire
        self.cases, en déplaçant la pièce à sa nouvelle position (et possiblement en supprimant une pièce adverse qui a
        été prise).

        Cette méthode doit également:
        - Promouvoir un pion en dame si celui-ci atteint l'autre extrémité du plateau.
        - Retourner un message indiquant "ok", "prise" ou "erreur".

        ATTENTION: Si le déplacement est effectué, cette méthode doit retourner "ok" si aucune prise n'a été faite,
            et "prise" si une pièce a été prise.
        ATTENTION: Ne dupliquez pas de code! Vous avez déjà programmé (ou allez programmer) des méthodes permettant
            de valider si une pièce peut se déplacer vers un certain endroit ou non.

        Args:
            position_source (Position): La position source du déplacement.
            position_cible (Position): La position cible du déplacement.

        Returns:
            str: "ok" si le déplacement a été effectué sans prise, "prise" si une pièce adverse a été prise, et
                "erreur" autrement.

        """
        #Récupérer les valeurs x et y de la position
        """On ne peut pas comparer position_piece à position_tuple car la classe Position n'est pas iterable
            Il faut donc prendre la valeur x, et y des deux arguments et en crée des tuples."""
        position_piece_x = position_source.ligne
        position_piece_y = position_source.colonne
        position_piece_tuple = (position_piece_x, position_piece_y)

        #Récupérer les valeurs x et y de la position
        position_cible_x = position_cible.ligne
        position_cible_y = position_cible.colonne
        position_cible_tuple = (position_cible_x, position_cible_y)


        """On veut vérifier s'il y a déjà une pièce dans la direction que position_cible veut s'orienter
        on crée deux tuples à partir de la liste afin d'effectuer une comparaison"""
        positions_diag_bas = Position.positions_diagonales_bas(position_source)
        positions_diag_bas_un =  positions_diag_bas[0]
        positions_diag_bas_deux = positions_diag_bas[1]

        #Récupérer les valeurs x et y de la position positions_diagonales_bas(position_piece)
        positions_diag_bas_un_x = positions_diag_bas_un.ligne
        positions_diag_bas_un_y = positions_diag_bas_un.colonne
        positions_diag_bas_un_tuple = (positions_diag_bas_un_x, positions_diag_bas_un_y)

        #Récupérer les valeurs x et y de la position positions_diagonales_bas(position_piece)
        positions_diag_bas_deux_x = positions_diag_bas_deux.ligne
        positions_diag_bas_deux_y = positions_diag_bas_deux.colonne
        positions_diag_bas_deux_tuple = (positions_diag_bas_deux_x, positions_diag_bas_deux_y)

        """ On veut aussi verifier vers le haut"""

        positions_diag_haut = Position.positions_diagonales_haut(position_source)
        positions_diag_haut_un = positions_diag_haut[0]
        positions_diag_haut_deux = positions_diag_haut[1]

        # Récupérer les valeurs x et y de la position positions_diagonales_bas(position_piece)
        positions_diag_haut_un_x = positions_diag_haut_un.ligne
        positions_diag_haut_un_y = positions_diag_haut_un.colonne
        positions_diag_haut_un_tuple = (positions_diag_haut_un_x, positions_diag_haut_un_y)

        # Récupérer les valeurs x et y de la position positions_diagonales_bas(position_piece)
        positions_diag_haut_deux_x =  positions_diag_haut_deux.ligne
        positions_diag_haut_deux_deux_y =  positions_diag_haut_deux.colonne
        positions_diag_haut_deux_tuple = (positions_diag_haut_deux_x, positions_diag_haut_deux_deux_y)


        """ Une pièce ne peut que sauter de deux cases en diagonale"""
        comparaison_x = 1 <= position_cible_tuple[0]-position_piece_tuple[0] < 2
        comparaison_y =  1 <=position_cible_tuple[1]-position_piece_tuple[1] < 2
        peut_deplacer = comparaison_x and comparaison_y

        # Vérifie si la pièce peut sauter vers la position cible





        if peut_deplacer == True:
            self.cases.update({position_cible: Piece("blanc", "pion")})
            print(self.cases)
            return "prise"
        else:
            return "erreur"





    def __repr__(self):
        """Cette méthode spéciale permet de modifier le comportement d'une instance de la classe Damier pour
        l'affichage. Faire un print(un_damier) affichera le damier à l'écran.

        """
        s = " +-0-+-1-+-2-+-3-+-4-+-5-+-6-+-7-+\n"
        for i in range(0, 8):
            s += str(i)+"| "
            for j in range(0, 8):
                if Position(i, j) in self.cases:
                    s += str(self.cases[Position(i, j)])+" | "
                else:
                    s += "  | "
            s += "\n +---+---+---+---+---+---+---+---+\n"

        return s


if __name__ == "__main__":
    print('Test unitaires de la classe "Damier"...')



    """ Test unitaires manquantes pour"""




    # TODO: À compléter
    # Test unitaire pour la methode position_est_dans_damier(self, position)
    un_damier = Damier()
    la_position = Position(0, 7)
    une_autre_position = Position(-2, 5)
    assert un_damier.position_est_dans_damier(la_position) == True
    assert un_damier.position_est_dans_damier(une_autre_position) == False

    assert un_damier.piece_peut_faire_une_prise(Position(4, 1)) == False

    # Test unitaire pour la methode piece_peut_se_deplacer_vers(self, position_piece, position_cible)
    assert un_damier.piece_peut_se_deplacer_vers(Position(3, 3), Position(4, 4)) == True
    assert un_damier.piece_peut_se_deplacer_vers(Position(3, 3), Position(2, 2)) == True
    # La position cible ne se trouve pas à diagonale de la position actuelle
    assert un_damier.piece_peut_se_deplacer_vers(Position(3, 3), Position(4, 3)) == False
    # Une piece ne peut pas se trouver à l'extérieur du damier
    assert un_damier.piece_peut_se_deplacer_vers(Position(3, 3), Position(8, 8)) == False
    assert un_damier.piece_peut_se_deplacer_vers(Position(8, 8), Position(3, 3)) == False

    # Test unitaire pour piece_peut_sauter_vers(self, position_piece, position_cible)
    assert un_damier.piece_peut_sauter_vers(Position(3, 4), Position(4, 5)) == True
    assert un_damier.piece_peut_sauter_vers(Position(3, 4), Position(4, 4)) == False

    un_piece = Piece('blanc', "pion")
    la_piece = un_piece.couleur

    assert un_damier.piece_de_couleur_peut_se_deplacer(la_piece) == True

    #Deplacement
    # assert un_damier.deplacer(Position(3, 3), Position(4, 4)) == True
    # assert un_damier.deplacer(Position(3, 3), Position(2, 2)) == True
    # # # La position cible ne se trouve pas à diagonale de la position actuelle
    # assert un_damier.deplacer(Position(3, 3), Position(4, 3)) == False
    # # # Une piece ne peut pas se trouver à l'extérieur du damier
    # assert un_damier.deplacer(Position(3, 3), Position(8, 8)) == False
    # assert un_damier.deplacer(Position(8, 8), Position(3, 3)) == False
    # assert un_damier.deplacer(Position(3, 4), Position(4, 5)) == "prise"

    print('Test unitaires passés avec succès!')

    # NOTEZ BIEN: Pour vous aider lors du développement, affichez le damier!
    print(un_damier)