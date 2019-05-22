""" lecture fichier file.template/ myCV.template en input"""
""" remplace certaines informations avec le fichier settings.py """
""" ecrit le resultat dans le fichier file.html """


def fn_render():
    
    import sys #recuperation des arguments, fichier template
    if len(sys.argv) != 2:
        print("Pas ou trop de parametres saisis en entree")
        print("Il faut un fichier .template")
        sys.exit(0)


    # test ds fichiers en entree
    try:
        file_template = sys.argv[1]
        file_template_begin = file_template.split('.')[0]
        file_template_end = file_template.split('.')[1]
        if file_template_end != 'template':
            print("le fichier",file_template, "en entree n'est pas bon")
            print("Il doit avoir une extension .template")
            sys.exit(0)

        file_settings = 'settings.py'          # fichier des donnees
        file_out = file_template_begin+'.html'    # fichier page html de sortie
        
        # lecture du fichier settings et ecriture d'un dictionnaire
        my_settings = dict()
        with open(file_settings,'r') as f_s:
            for line in f_s:
                line_deb = line.split(' = ')[0]
                line_end = line.strip().split(' = ')[1]
                line_end = line_end.split('"')[1]
                my_settings[line_deb] = line_end

        # les ouvertures de fichiers
        f_o = open(file_out, 'w')
        with open(file_template,'r') as f_t:
            for line in f_t:
                line1 = line.format(**my_settings)
                f_o.write(line1)

    # gestion des erreur fichiers
    except FileNotFoundError as e:
        print("fichier",e.filename,"inexistant")
        print("le message d'erreur est ",e)
        sys.exit(0)
    except PermissionError as e:
        print("l'acces au fichier",e.filename,"n'est pas autorise")
        print("le message d'erreur est ",e)
        sys.exit(0)
    except Exception as e:
        print("toutes les autres erreurs, contacter les developpeurs")
        print("le message d'erreur est ",e)
        sys.exit(0)
#-----------------------------------
if __name__ == '__main__':
	fn_render()
#-----------------------------------


