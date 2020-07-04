# Auteurs: À compéter


class Position:
    """Une position à deux coordonnées: ligne et colonne. La convention utilisée est celle de la notation matricielle :
    le coin supérieur gauche d'une matrice est dénoté (0, 0) (ligne 0 et colonne 0). On additionne une unité de colonne
    lorsqu'on se déplace vers la droite, et une unité de ligne lorsqu'on se déplace vers le bas.

    +-------+-------+-------+-------+
    | (0,0) | (0,1) | (0,2) |  ...  |
    | (1,0) | (1,1) | (1,2) |  ...  |
    | (2,0) | (2,1) | (2,2) |  ...  |
    |  ...  |  ...  |  ...  |  ...  |
    +-------+-------+-------+-------+

    Attributes:
        ligne (int): La ligne associée à la position.
        colonne (int): La colonne associée à la position

    """
    def __init__(self, ligne, colonne):
        """Constructeur de la classe Position. Initialise les deux attributs de la classe.

        Args:
            ligne (int): La ligne à considérer dans l'instance de Position.
            colonne (int): La colonne à considérer dans l'instance de Position.

        """
        self.ligne = int(ligne)
        self.colonne = int(colonne)

    def positions_diagonales_bas(self):
        """Retourne une liste contenant les deux positions diagonales bas à partir de la position actuelle.

        Note:
            Dans cette méthode et les prochaines, vous n'avez pas à valider qu'une position est "valide", car dans le
            contexte de cette classe toutes les positions (même négatives) sont permises.

        Returns:
            list: La liste des deux positions.

        """
        return [Position(self.ligne + 1, self.colonne - 1), Position(self.ligne + 1, self.colonne + 1)]

    def positions_diagonales_haut(self):
        """Retourne une liste contenant les deux positions diagonales haut à partir de la position actuelle.

        Returns:
            list: La liste des deux positions.

        """
        return [Position(self.ligne - 1, self.colonne -1), Position(self.ligne - 1, self.colonne + 1)]

    def quatre_positions_diagonales(self):
        """Retourne une liste contenant les quatre positions diagonales à partir de la position actuelle.

        Returns:
            list: La liste des quatre positions.

        """
        return [Position(self.ligne + 1, self.colonne - 1), Position(self.ligne + 1, self.colonne + 1),
                Position(self.ligne - 1, self.colonne - 1), Position(self.ligne - 1,self.colonne + 1)]

    def quatre_positions_sauts(self):
        """Retourne une liste contenant les quatre "sauts" diagonaux à partir de la position actuelle. Les positions
        retournées sont donc en diagonale avec la position actuelle, mais a une distance de 2.

        Returns:
            list: La liste des quatre positions.

        """
        return [Position(self.ligne + 2, self.colonne -2), Position(self.ligne + 2, self.colonne + 2),
                Position(self.ligne - 2, self.colonne - 2), Position(self.ligne - 2, self.colonne + 2)]

    def __eq__(self, other):
        """Méthode spéciale indiquant à Python comment vérifier si deux positions sont égales. On compare simplement
        la ligne et la colonne de l'objet actuel et de l'autre objet.

        """
        return self.ligne == other.ligne and self.colonne == other.colonne

    def __repr__(self):
        """Méthode spéciale indiquant à Python comment représenter une instance de Position par une chaîne de
        caractères. Notamment utilisé pour imprimer une position à l'écran.

        """
        return '({}, {})'.format(self.ligne, self.colonne)

    def __hash__(self):
        """Méthode spéciale indiquant à Python comment "hasher" une Position. Cette méthode est nécessaire si on veut
        utiliser une classe que nous avons définie nous mêmes comme clé d'un dictionnaire.
        Les étudiants(es) curieux(ses) peuvent consulter wikipédia pour en savoir plus:
            https://fr.wikipedia.org/wiki/Fonction_de_hachage

        """
        return hash(str(self))




if __name__ == '__main__':
    print('Test unitaires de la classe "Position"...')
    position_bas_droite=Position(4,4)
    position_bas_gauche=Position(6,0)
    position_haut_droite=Position(0,4)
    position_haut_gauche=Position(0,0)
    position_saut_bas_droite=Position(6,6)
    position_saut_bas_gauche=Position(10,0)
    position_saut_haut_droite=Position(0,8)
    une_position_saut=Position(12,14)
    une_position_4_positions_diagonales_droite=Position(10,10)
    une_position_4_positions_diagonales_gauche=Position(14,0)
    assert position_bas_droite.positions_diagonales_bas()
    assert position_bas_gauche.positions_diagonales_bas()
    assert position_haut_droite.positions_diagonales_haut()
    assert position_haut_gauche.positions_diagonales_haut()
    assert position_saut_bas_droite.quatre_positions_sauts()
    assert position_saut_bas_gauche.quatre_positions_sauts()
    assert position_saut_haut_droite.quatre_positions_sauts()
    assert une_position_saut.quatre_positions_sauts()
    assert une_position_4_positions_diagonales_droite.quatre_positions_diagonales()
    assert une_position_4_positions_diagonales_gauche.quatre_positions_diagonales()
    print('Test unitaires passés avec succès!')