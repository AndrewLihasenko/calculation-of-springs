import sys
import os
import math
import traceback

from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QGridLayout,
                             QToolTip, QPushButton, QComboBox, QDesktopWidget,
                             QSizePolicy, QVBoxLayout, QGroupBox, QHBoxLayout)
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import QCoreApplication


"""Information about errors"""
def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    text += ''.join(traceback.format_tb(tb))
    print(text)
    # QtWidgets.QMessageBox.critical(None, 'Error', text)
    # sys.exit()


sys.excepthook = log_uncaught_exceptions


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.createButtonBox()
        self.createGridGroupBox()
        self.center()

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.gridGroupBox)
        mainLayout.addWidget(self.buttonBox)
        self.setLayout(mainLayout)
        self.setFixedSize(0, 360)

    def createGridGroupBox(self):
        # QToolTip.setFont(QFont('SansSerif', 10))
        # self.setToolTip('This is a <b>QWidget</b> widget')
        self.gridGroupBox = QGroupBox('Исходные данные и результат расчёта')

        work_axial_force = QLabel('Рабочая осевая сила P2, кгс')
        work_axial_force_calc = QLabel('Рабочая осевая сила P2 \n(расчётная), кгс')
        outside_diameter = QLabel('Наружный диаметр пружины D, мм')
        spring_height = QLabel('Высота пружины в свободном \nсостоянии H0, мм')
        spring_height_calc = QLabel('Высота пружины в свободном \nсостоянии (расчетная) H0, мм')
        spring_height_p_two = QLabel('Высота пружины H2 под \nнагрузкой Р2, мм')
        spring_height_compression = QLabel('Высота пружины при заневоливании \nНзан., мм')
        work_turns = QLabel('Число рабочих витков n')
        full_turns = QLabel('Полное число витков n1')
        axial_deformation_p_two = QLabel('Осевая деформация пружины F2 \nпод нагрузкой P2, мм')
        diameter_wire = QLabel('Диаметр проволоки d, мм')
        step = QLabel('Шаг пружины t, мм')
        length_of_spring = QLabel('Длина развёртки пружины L, мм')
        weight_of_spring = QLabel('Масса пружины m, г')
        work_stress = QLabel('Рабочее напряжение Т2, кгс/мм2 ')
        shear_module_factor = QLabel('Коэффициент, учитывающий изменение \nмодуля сдвига Кт')

        ### This parameters is working! They is calculation, but not show in GUI.###

        # pre_pressing_axial_force = QLabel('Осевая сила предварительного поджатия P1, кгс')
        # middle_diameter = QLabel('Средний (расчётный) диаметр пружины D0, мм')
        # axial_deformation_p_one = QLabel('Осевая деформация пружины F1 под нагрузкой P1, мм')
        # axial_deformation_one_turn_f_one = QLabel('Осевая деформация одного витка f1 '
        #                                           'под нагрузкой P1, мм')
        # axial_deformation_one_turn_f_two = QLabel('Осевая деформация одного витка f2 '
        #                                           'под нагрузкой P2, мм')
        # length_one_turn = QLabel('Длина одного витка l, мм')
        # weight_one_turn = QLabel('Масса одного витка m1, г')

        self.work_axial_force_calcEdit = QLabel(self)
        self.spring_height_calcEdit = QLabel(self)
        self.spring_height_p_twoEdit = QLabel(self)
        self.full_turnsEdit = QLabel(self)
        self.axial_deformation_p_twoEdit = QLabel(self)
        self.length_of_springEdit = QLabel(self)
        self.weight_of_springEdit = QLabel(self)
        self.spring_height_compressionEdit = QLabel(self)

        self.work_axial_forceEdit = QLineEdit(self)
        self.work_axial_forceEdit.setText('0')
        self.outside_diameterEdit = QLineEdit(self)
        self.outside_diameterEdit.setText('0')
        self.spring_heightEdit = QLineEdit(self)
        self.spring_heightEdit.setText('0')
        self.work_turnsEdit = QLineEdit(self)
        self.work_turnsEdit.setText('0')
        self.diameter_wireEdit = QLineEdit(self)
        self.diameter_wireEdit.setText('0')
        self.stepEdit = QLineEdit(self)
        self.stepEdit.setText('0')

        ### This parameters is working! They is calculation, but not show in GUI.###

        # self.pre_pressing_axial_forceEdit = QLineEdit(self)
        # self.middle_diameterEdit = QLineEdit(self)
        # self.axial_deformation_p_oneEdit = QLineEdit(self)
        # self.axial_deformation_one_turn_f_oneEdit = QLineEdit(self)
        # self.axial_deformation_one_turn_f_twoEdit = QLineEdit(self)
        # self.length_one_turnEdit = QLineEdit(self)
        # self.weight_one_turnEdit = QLineEdit(self)

        self.combo_work_stress = QComboBox(self)
        self.combo_work_stress.addItems(["72", "66", "59", "54", "50", "44"])
        self.combo_shear_module_factor = QComboBox(self)
        self.combo_shear_module_factor.addItems(["0.985", "0.950"])

        grid = QGridLayout()
        grid.setSpacing(10)

        label_spring = QLabel()
        # pixmap = QPixmap('spring_resize.png')
        # label_spring.setPixmap(pixmap)
        label_spring.setPixmap(QPixmap(resource_path('spring_resize.png')))
        grid.addWidget(label_spring, 1, 4, 8, 1)

        grid.addWidget(spring_height, 1, 0)
        grid.addWidget(self.spring_heightEdit, 1, 1)
        grid.addWidget(outside_diameter, 2, 0)
        grid.addWidget(self.outside_diameterEdit, 2, 1)
        grid.addWidget(diameter_wire, 3, 0)
        grid.addWidget(self.diameter_wireEdit, 3, 1)
        grid.addWidget(work_turns, 4, 0)
        grid.addWidget(self.work_turnsEdit, 4, 1)
        grid.addWidget(work_axial_force, 5, 0)
        grid.addWidget(self.work_axial_forceEdit, 5, 1)
        grid.addWidget(step, 6, 0)
        grid.addWidget(self.stepEdit, 6, 1)

        grid.addWidget(work_stress, 7, 0)
        grid.addWidget(self.combo_work_stress, 7, 1)
        grid.addWidget(shear_module_factor, 8, 0)
        grid.addWidget(self.combo_shear_module_factor, 8, 1)

        grid.addWidget(spring_height_calc, 1, 2)
        grid.addWidget(self.spring_height_calcEdit, 1, 3)
        grid.addWidget(spring_height_p_two, 2, 2)
        grid.addWidget(self.spring_height_p_twoEdit, 2, 3)
        grid.addWidget(spring_height_compression, 3, 2)
        grid.addWidget(self.spring_height_compressionEdit, 3, 3)
        grid.addWidget(full_turns, 4, 2)
        grid.addWidget(self.full_turnsEdit, 4, 3)
        grid.addWidget(work_axial_force_calc, 5, 2)
        grid.addWidget(self.work_axial_force_calcEdit, 5, 3)
        grid.addWidget(length_of_spring, 6, 2)
        grid.addWidget(self.length_of_springEdit, 6, 3)
        grid.addWidget(weight_of_spring, 7, 2)
        grid.addWidget(self.weight_of_springEdit, 7, 3)
        grid.addWidget(axial_deformation_p_two, 8, 2)
        grid.addWidget(self.axial_deformation_p_twoEdit, 8, 3)

        ### This parameters is working! They is calculation, but not show in GUI.###

        # grid.addWidget(axial_deformation_one_turn_f_one, 6, 0)
        # grid.addWidget(self.axial_deformation_one_turn_f_oneEdit, 6, 1)
        # grid.addWidget(axial_deformation_one_turn_f_two, 7, 0)
        # grid.addWidget(self.axial_deformation_one_turn_f_twoEdit, 7, 1)
        # grid.addWidget(pre_pressing_axial_force, 8, 0)
        # grid.addWidget(self.pre_pressing_axial_forceEdit, 8, 1)
        # grid.addWidget(axial_deformation_p_one, 9, 0)
        # grid.addWidget(self.axial_deformation_p_oneEdit, 9, 1)
        # grid.addWidget(length_one_turn, 10, 2)
        # grid.addWidget(self.length_one_turnEdit, 10, 3)
        # grid.addWidget(weight_one_turn, 12, 2)
        # grid.addWidget(self.weight_one_turnEdit, 12, 3)
        # grid.addWidget(middle_diameter, 13, 0)
        # grid.addWidget(self.middle_diameterEdit, 13, 1)

        self.gridGroupBox.setLayout(grid)
        self.setWindowTitle('Расчёт пружин сжатия по ОСТ 1 13553-79')
        # icon = QIcon('icon.png')
        # self.setWindowIcon(icon)
        self.setWindowIcon(QIcon(resource_path('icon.png')))
        self.show()

    def createButtonBox(self):
        self.buttonBox = QGroupBox()
        layout = QHBoxLayout()

        self.cbtn = QPushButton('Рассчитать', self)
        # self.cbtn.setToolTip('This is a <b>QPushButton</b> widget')
        self.cbtn.resize(self.cbtn.sizeHint())
        self.cbtn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.cbtn.clicked.connect(self.calcbtnClicked)

        qbtn = QPushButton('Выход', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.resetbtn = QPushButton('Сброс', self)
        self.resetbtn.resize(self.resetbtn.sizeHint())
        self.resetbtn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.resetbtn.clicked.connect(self.resetbtnClicked)

        aboutbtn = QPushButton('О программе', self)
        aboutbtn.resize(self.cbtn.sizeHint())
        aboutbtn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        aboutbtn.clicked.connect(self.aboutbtnClicked)

        linktoOSTbtn = QPushButton(' Открыть ОСТ 1 13553-79 - пружины сжатия ', self)
        # linktoOSTbtn.resize(self.cbtn.sizeHint())
        linktoOSTbtn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        linktoOSTbtn.clicked.connect(self.linktoOSTbtnClicked)

        layout.addWidget(self.cbtn)
        layout.addWidget(self.resetbtn)
        layout.addWidget(linktoOSTbtn)
        layout.addWidget(qbtn)
        layout.addWidget(aboutbtn)

        self.buttonBox.setLayout(layout)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width())/2, (screen.height() - size.height()) / 2)

    def calcbtnClicked(self):

        """Commented strings - this parameters is working!
        They is calculation, but not show in GUI"""

        if float(self.spring_heightEdit.text()) == 0 \
                or float(self.diameter_wireEdit.text()) == 0 \
                or float(self.outside_diameterEdit.text()) == 0:
            QtWidgets.QMessageBox.information(None, 'Ошибка!', 'Слишком мало данных для расчета')

        step_out = float(self.stepEdit.text())
        if step_out == 0:
            try:
                # format() - round up 3 char after the comma
                step_out = '{0:.1f}'.format((float(self.spring_heightEdit.text()) -
                                             (1.5 * float(self.diameter_wireEdit.text()))) /
                                            float(self.work_turnsEdit.text()))
            except Exception:
                QtWidgets.QMessageBox.information(None, 'Ошибка!',
                                                  'Введите число рабочих витков, n \n или шаг пружины, t')
            self.stepEdit.setText(str(step_out))


        work_turns_out = float(self.work_turnsEdit.text())
        if work_turns_out == 0:
            work_turns_out = '{0:.1f}'.format((float(self.spring_heightEdit.text()) -
                                               (1.5 * float(self.diameter_wireEdit.text()))) /
                                              float(step_out))
        self.work_turnsEdit.setText(str(work_turns_out))


        full_turns_out = float(self.work_turnsEdit.text())
        full_turns_out += 2
        self.full_turnsEdit.setText(str(full_turns_out))


        middle_diameter_out = float(self.outside_diameterEdit.text()) - float(self.diameter_wireEdit.text())
        # self.middle_diameterEdit.setText(str(out_middle_diameter))

        index_spring = '{0:.3f}'.format(float(middle_diameter_out) / float(self.diameter_wireEdit.text()))
        curve_factor_turn = '{0:.3f}'.format((((4 * float(index_spring)) - 1) / ((4 * float(index_spring)) - 4)) +
                                             (0.615 / float(index_spring)))


        work_axial_force_calc_out = '{0:.2f}'.format((math.pi / 8) *
                                                     ((float(self.diameter_wireEdit.text()) ** 3) /
                                                      (float(middle_diameter_out) *
                                                       float(curve_factor_turn))) *
                                                     float(self.combo_work_stress.currentText()))
        self.work_axial_force_calcEdit.setText(str(work_axial_force_calc_out))


        work_axial_force_out = float(self.work_axial_forceEdit.text())
        if work_axial_force_out == 0:
            work_axial_force_out = float(self.work_axial_force_calcEdit.text())
            self.work_axial_forceEdit.setText(str(work_axial_force_out))
        self.work_axial_forceEdit.setText(str(work_axial_force_out))


        pre_pressing_axial_force_out = '{0:.3f}'.format(0.1 * float(self.work_axial_forceEdit.text()))
        # self.pre_pressing_axial_forceEdit.setText(str(pre_pressing_axial_force_out))


        axial_deformation_one_turn_f_one_out = '{0:.3f}'.format((8 * float(pre_pressing_axial_force_out) *
                                                                 (float(middle_diameter_out) ** 3)) /
                                                                ((float(self.diameter_wireEdit.text()) ** 4) * 8000 *
                                                                 float(self.combo_shear_module_factor.currentText())))
        # self.axial_deformation_one_turn_f_oneEdit.setText(str(axial_deformation_one_turn_f_one_out))


        axial_deformation_one_turn_f_two_out = '{0:.3f}'.format((8 * float(self.work_axial_forceEdit.text()) *
                                                                 (float(middle_diameter_out) ** 3)) /
                                                                ((float(self.diameter_wireEdit.text()) ** 4) * 8000 *
                                                                 float(self.combo_shear_module_factor.currentText())))
        # self.axial_deformation_one_turn_f_twoEdit.setText(str(axial_deformation_one_turn_f_two_out))


        axial_deformation_p_one_out = '{0:.3f}'.format((float(axial_deformation_one_turn_f_one_out) *
                                                        float(self.work_turnsEdit.text())))
        # self.axial_deformation_p_oneEdit.setText(str(out_axial_deformation_p_one))


        axial_deformation_p_two_out = '{0:.3f}'.format(float(axial_deformation_one_turn_f_two_out) *
                                                       float(self.work_turnsEdit.text()))
        self.axial_deformation_p_twoEdit.setText(str(axial_deformation_p_two_out))


        spring_height_calc_out = '{0:.1f}'.format((float(self.stepEdit.text()) * float(self.work_turnsEdit.text())) +
                                                  (1.5 * float(self.diameter_wireEdit.text())))
        self.spring_height_calcEdit.setText(str(spring_height_calc_out))


        out_spring_height_p_two = '{0:.1f}'.format(float(self.spring_heightEdit.text()) -
                                                   float(self.axial_deformation_p_twoEdit.text()))
        self.spring_height_p_twoEdit.setText(str(out_spring_height_p_two))


        length_one_turn_out = '{0:.1f}'.format(math.sqrt(((math.pi * float(middle_diameter_out)) ** 2) +
                                                         (float(self.stepEdit.text()) ** 2)))
        # self.length_one_turnEdit.setText(str(out_length_one_turn))


        out_length_of_spring = '{0:.0f}'.format((float(length_one_turn_out) *
                                                 float(self.full_turnsEdit.text())))
        self.length_of_springEdit.setText(str(out_length_of_spring))


        weight_one_turn_out = '{0:.3f}'.format(0.00785 *
                                               ((math.pi * (float(self.diameter_wireEdit.text()) ** 2)) / 4) *
                                               float(length_one_turn_out))
        # self.weight_one_turnEdit.setText(str(out_weight_one_turn))


        weight_of_spring_out = '{0:.1f}'.format(float(weight_one_turn_out) * (float(self.full_turnsEdit.text()) - 0.5))
        self.weight_of_springEdit.setText(str(weight_of_spring_out))


        spring_height_compression_out = '{0:.0f}'.format(float(self.spring_height_calcEdit.text()) -
                                                         (1.15 * float(self.axial_deformation_p_twoEdit.text())))
        self.spring_height_compressionEdit.setText(str(spring_height_compression_out))

    def resetbtnClicked(self):
        self.stepEdit.setText(str('0'))
        self.spring_heightEdit.setText(str('0'))
        self.work_axial_forceEdit.setText(str('0'))
        self.outside_diameterEdit.setText(str('0'))
        self.diameter_wireEdit.setText(str('0'))
        self.work_turnsEdit.setText(str('0'))

    def aboutbtnClicked(self):

        """Modal window"""
        # self.modal = QWidget()
        # self.modal.about_label = QLabel()
        # self.modal.pixmap_label = QLabel()
        # try:
        #     self.modal.file = open("about.txt", 'r') # в файле можно написать информацию о программе
        # except IOError:
        #     print("No file")
        # self.modal.f_read = self.modal.file.read()
        # self.modal.about_label.setText(self.modal.f_read)
        #
        # self.modal.m_grid = QGridLayout()
        # self.modal.m_pixmap = QPixmap('icon_resize.png')
        # self.modal.pixmap_label.setPixmap(self.modal.m_pixmap)
        #
        # self.modal.m_grid.addWidget(self.modal.pixmap_label, 0, 0)
        # self.modal.m_grid.addWidget(self.modal.about_label, 0, 1, 4, 1)
        #
        # try:
        #     self.modal.icon = QIcon('icon.png')
        # except IOError:
        #     print("No file")
        # self.modal.setWindowIcon(self.modal.icon)
        # self.modal.setLayout(self.modal.m_grid)
        # self.modal.setFixedSize(360, 135)
        # self.modal.setWindowTitle('О программе')
        # self.modal.show()

        QtWidgets.QMessageBox.information(None, 'О программе',
                                          'Программа для выполнения расчётов пружин сжатия,\n'
                                          'согласно ОСТ 1 13553-79.\n\n'
                                          'Версия 0.3 beta\n\n'
                                          'Автор: Лихасенко Андрей\n\n'
                                          'По всем вопросам пишите: lihasenko@gmail.com\n\n'
                                          'Программа разработана под лицензией Apache 2.0')

    def linktoOSTbtnClicked(self):

        import subprocess
        subprocess.call(resource_path("OST_1_13553-79-Spring_2A.TIF"), shell=True)


if __name__ == '__main__':

    """ Pyinstaller распаковывает данные во временную папку и сохраняет 
    этот путь каталога в переменной среды _MEIPASS. Чтобы получить _MEIPASS 
    в упакованном режиме и использовать локальный каталог в режиме распаковки: """

    def resource_path(relative):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative)
        else:
            return os.path.join(os.path.abspath("."), relative)

    app = QApplication(sys.argv)
    ex = Widget()
    sys.exit(app.exec_())
