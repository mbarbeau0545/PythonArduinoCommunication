#################################################################################
#  @file        main.py
#  @brief       Template_BriefDescription.
#  @details     TemplateDetailsDescription.\n
#
#  @author      AUDMBA
#  @date        jj/mm/yyyy
#  @version     1.0
################################################################################
#                                       IMPORT
################################################################################
import sys
import os
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QRadioButton, QPushButton, QLabel,QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QComboBox, QListWidget, QAbstractItemView
from PySide6.QtCore import QSize, QEventLoop, Signal, Qt
################################################################################
#                                       DEFINE
################################################################################

################################################################################
#                                       CLASS
################################################################################
class ConfirmedChoice(QWidget):

    def __init__(self, f_benchMode_str, f_sqcrMode_str):
        super().__init__()

        self.benchMode_sqcr = f_benchMode_str
        self.sqcrMode_str = f_sqcrMode_str
        self.userResponse_b = None
        
        self.initUI()  # Appel de la méthode initUI pour créer l'interface utilisateur

    def exec_(self):
        loop = QEventLoop()
        self._closed = loop.quit
        self.show()
        loop.exec()

    def initUI(self):
        self.setWindowTitle("Confirmation")
        self.setGeometry(200,200,300,100)

        layout = QVBoxLayout(self)

        label = QLabel(f"Confirmez vous votre choix ?\n   BenchMode : {self.benchMode_sqcr}\n   SqcrMode : {self.sqcrMode_str}\n")
        layout.addWidget(label)

        confirm_button = QPushButton("Yes")
        cancel_button = QPushButton("No")

        layout.addWidget(confirm_button)
        layout.addWidget(cancel_button)

        confirm_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject) 

    def accept(self):
        self.userResponse_b = True
        self._closed()
        self.close()

    def reject(self):
        self.userResponse_b = False
        self._closed()
        self.close()

class GenerateTestList(QWidget):
     # Déclarer un signal personnalisé avec une liste comme argument
    testlist_generated_ac = Signal(list)
    def __init__(self):
        super().__init__()

        self.SuperfolderPath_str = "Script"
        self.initUI()

    def exec_(self):
        loop = QEventLoop()
        self._closed = loop.quit
        self.show()
        loop.exec()

    def initUI(self):
        self.setWindowTitle("Script Selector")
        self.setGeometry(200, 200, 800, 400)

        layout = QHBoxLayout()

        # Menu déroulant pour choisir le dossier
        self.folder_combobox = QComboBox()
        self.populate_combobox()
        self.folder_combobox.currentIndexChanged.connect(self.populate_file_list)
        layout.addWidget(self.folder_combobox)

        # Liste des fichiers dans le dossier sélectionné
        self.file_list_widget = QListWidget()
        self.file_list_widget.setSelectionMode(QAbstractItemView.MultiSelection)
        layout.addWidget(self.file_list_widget)

        buttons_layout = QVBoxLayout()
        
        # Bouton pour ajouter les fichiers sélectionnés
        self.add_button = QPushButton("Add ->")
        self.add_button.clicked.connect(self.add_selected_files)
        buttons_layout.addWidget(self.add_button)

        # Bouton pour supprimer les fichiers sélectionnés
        self.remove_button = QPushButton("<- Remove")
        self.remove_button.clicked.connect(self.remove_selected_files)
        buttons_layout.addWidget(self.remove_button)
        
        # Bouton pour ajouter tous les fichiers du dossier
        self.add_all_button = QPushButton("Add All ->")
        self.add_all_button.clicked.connect(self.add_all_files)
        buttons_layout.addWidget(self.add_all_button)

        # Bouton pour supprimer tous les fichiers de la liste de test
        self.remove_all_button = QPushButton("<- Remove All")
        self.remove_all_button.clicked.connect(self.remove_all_files)
        buttons_layout.addWidget(self.remove_all_button)        
        
        layout.addLayout(buttons_layout)

        # Liste des fichiers sélectionnés
        self.selected_files_widget = QListWidget()
        layout.addWidget(self.selected_files_widget)

        # Bouton pour générer la liste de test
        generate_button = QPushButton("Generate Testlist")
        layout.addWidget(generate_button)

        # Connecter le signal clicked du bouton à la méthode close de la fenêtre
        generate_button.clicked.connect(self.quitWindow)

        self.setLayout(layout)

    def populate_combobox(self):
        # Effacer toutes les entrées précédentes
        self.folder_combobox.clear()
        
        # Ajouter "Search Folder" comme première option
        self.folder_combobox.addItem("Search Folder")

        # Chemin du dossier "scripts"
        script_folder_path = self.SuperfolderPath_str
        # Vérifier si le dossier existe
        if os.path.isdir(script_folder_path):
            # Parcourir les dossiers dans le dossier "scripts"
            for folder_name in os.listdir(script_folder_path):
                # Vérifier si le chemin est un dossier
                folder_path = os.path.join(script_folder_path, folder_name)
                if os.path.isdir(folder_path):
                    # Ajouter le nom du dossier au menu déroulant
                    self.folder_combobox.addItem(folder_name)

    def populate_file_list(self):
        # Effacer la liste des fichiers actuelle
        self.file_list_widget.clear()

        # Récupérer le nom du dossier sélectionné
        selected_folder_name = self.folder_combobox.currentText()

        # Chemin complet du dossier
        folder_path = os.path.join(self.SuperfolderPath_str, selected_folder_name)

        # Vérifier si le dossier existe
        if os.path.isdir(folder_path):
            # Parcourir les fichiers dans le dossier
            for file_name in os.listdir(folder_path):
                # Vérifier si le chemin est un fichier
                file_path = os.path.join(folder_path, file_name)
                if os.path.isfile(file_path):
                    # Ajouter le nom du fichier à la liste des fichiers
                    self.file_list_widget.addItem(file_name)


    def add_selected_files(self):
    # Récupérer les éléments sélectionnés dans la liste des fichiers
        selected_items = self.file_list_widget.selectedItems()
        
        # Ajouter les fichiers sélectionnés à la liste des fichiers sélectionnés
        for item in selected_items:
            isPresent_b = False
            # Parcourir tous les éléments de la QListWidget
            for TestList_Item in range(self.selected_files_widget.count()):
                # Vérifier si l'élément est déjà présent
                if item.text() == self.selected_files_widget.item(TestList_Item).text():
                    isPresent_b = True
                    break
            # Si l'élément n'est pas présent, l'ajouter
            if not isPresent_b:
                self.selected_files_widget.addItem(item.text())
        
        # Dé-sélectionner les éléments dans la liste des fichiers
        self.file_list_widget.clearSelection()

    def remove_selected_files(self):
        # Récupérer les éléments sélectionnés dans la liste des fichiers sélectionnés
        selected_items = self.selected_files_widget.selectedItems()

        # Supprimer les fichiers sélectionnés de la liste des fichiers sélectionnés
        for item in selected_items:
            self.selected_files_widget.takeItem(self.selected_files_widget.row(item))

        # Dé-sélectionner tous les éléments dans la liste des fichiers
        self.selected_files_widget.clearSelection()


    def add_all_files(self):
        # Ajouter tous les éléments de la liste des fichiers à la testlist
        for index in range(self.file_list_widget.count()):
            item = self.file_list_widget.item(index)
            self.selected_files_widget.addItem(item.text())

        # Dé-sélectionner tous les éléments dans la liste des fichiers
        self.file_list_widget.clearSelection()

    def remove_all_files(self):
        # Supprimer tous les éléments de la testlist
        self.selected_files_widget.clear()

    def quitWindow(self):
        selected_files = [item.text() for item in self.selected_files_widget.findItems("*", Qt.MatchWildcard)]
        self.testlist_generated_ac.emit(selected_files)
        self._closed()
        self.close()


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.testList = []
        self.initUI()
        self.BenchMode_str = None
        self.SqcrMode_str = None

    def initUI(self):
        self.setWindowTitle('Sélecteur de mode')
        self.setGeometry(100, 100, 600, 400)

        # Layout principal
        layout = QVBoxLayout()

        # Groupe pour le mode
        mode_group = QGroupBox('Mode')
        mode_layout = QVBoxLayout()
        self.hil_radio = QRadioButton('HIL')
        self.sil_radio = QRadioButton('SIL')
        mode_layout.addWidget(self.hil_radio)
        mode_layout.addWidget(self.sil_radio)
        mode_group.setLayout(mode_layout)

        # Groupe pour le séquenceur
        sequencer_group = QGroupBox('Séquenceur')
        sequencer_layout = QVBoxLayout()
        self.auto_radio = QRadioButton('Automatique')
        self.manual_radio = QRadioButton('Manuel')
        sequencer_layout.addWidget(self.auto_radio)
        sequencer_layout.addWidget(self.manual_radio)
        sequencer_group.setLayout(sequencer_layout)

        # Boutons
        button_layout = QHBoxLayout()
        self.run_button = QPushButton()
        self.run_button.setIcon(QIcon('Pictures\\runjpg.jpg'))
        self.run_button.setIconSize(QSize(64, 64))

        self.stop_button = QPushButton()
        self.stop_button.setIcon(QIcon('Pictures\\Stop.jpg'))  # Remplacez 'stop_icon.png' par le chemin de votre image pour Stop
        self.stop_button.setIconSize(QSize(64, 64))

        button_layout.addWidget(self.run_button)
        button_layout.addWidget(self.stop_button)

        layout.addWidget(mode_group)
        layout.addWidget(sequencer_group)
        layout.addLayout(button_layout)  # Ajouter le layout horizontal des boutons
        
        self.setLayout(layout)

        # Connecter les signaux aux slots
        self.run_button.clicked.connect(self.run_application)
        self.stop_button.clicked.connect(self.stop_application)



    def run_application(self):
        # Fonction à appeler lorsqu'on clique sur le bouton Run
        if(self.hil_radio.isChecked()):
            self.mode_str = "HIL"
        elif(self.sil_radio.isChecked()):
            self.mode_str = "SIL"
        if(self.auto_radio.isChecked()):
            self.SqcrMode_str = "Auto"
        elif(self.manual_radio.isChecked()):
            self.SqcrMode_str = "Manuel"

        Confirmed_Window = ConfirmedChoice(self.mode_str, self.SqcrMode_str)
        Confirmed_Window.exec_()
        if Confirmed_Window.userResponse_b == True:
            print(f'Run Application with Mode: {self.mode_str}, Sequencer: {self.SqcrMode_str}')
        else:
            print('L\'application n\'a pas été lancée.')
        if(self.SqcrMode_str == "Manuel"):
            self.Show_ScriptSelector()
        else:
            print("We take it from here")
           
    
    def handle_testlist_generation(self, f_testList):
        self.testList = f_testList
        print(f"testlist generated : {self.testList}")
    

    def Show_ScriptSelector(self):
        script_selector = GenerateTestList()
        script_selector.testlist_generated_ac.connect(self.handle_testlist_generation)
        self.testList = script_selector.exec_()




    def stop_application(self):
        # Fonction à appeler lorsqu'on clique sur le bouton Stop
        print('Arrêt de l\'application...')
################################################################################
#                              FUNCTION DECLARATION
################################################################################

################################################################################
#                             FUNCTION IMPLMENTATION
################################################################################
def main()-> None:
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())
    return
################################################################################
#			                MAIN
################################################################################
if (__name__ == '__main__'):
    main()

################################################################################
#		                    END OF FILE
################################################################################
##########################
# Function_name
##########################

######################################################
#
# @brief
# @details
#
#
#
#
# @params[in]
# @params[out]
# @retval
#
#####################################################

