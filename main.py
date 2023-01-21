import sqlite3
import os
import sys
import time


from PyQt5 import QtCore, QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QDesktopWidget

from map import *
from object_handler import *
from object_renderer import *
from pathfinding import *
from player import *
from raycasting import *
from sound import *
from weapon import *
from settings import *

paused = False
whichlvl = 0
textofcutscenes = ['', 'nah, that was wild. I wonder whats waiting me on the next floor',
                   'im glad that im out of this prison, i should find some vehicle so i can drive to my base',
                   'Walkie Talkie comms: A-6-6 I need you to find launch codes otherwise makarov will nuke us...'
                   '123', '124']

def showdialog(text):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Warning)
    msgBox.setText(text)
    msgBox.setWindowTitle('Warning')
    msgBox.setStandardButtons(QMessageBox.Ok)
    returnValue = msgBox.exec()

class Finalmenu(QDialog):
    def __init__(self):
        super(Finalmenu, self).__init__()
        uic.loadUi("resources/uies/Finalmenu.ui", self)
        self.ene.hide()
        self.kills.hide()
        self.time.hide()
        self.time2.hide()
        self.nice.hide()
        self.hideb.clicked.connect(self.showresults)
        self.nice.clicked.connect(self.goodbye)
        self.move(320, 180)

    def showresults(self):
        self.ene.show()
        self.kills.show()
        self.time.show()
        self.time2.show()
        self.nice.show()
        self.hideb.hide()
        self.died.hide()

    def goodbye(self):
        final.close()
        pg.quit()



class Pause(QDialog):
    def __init__(self):
        super(Pause, self).__init__()
        uic.loadUi("resources/uies/pause.ui", self)
        self.resume.clicked.connect(self.resumedef)
        self.x.clicked.connect(self.exit)

    def keyPressEvent(self, event):
        if not event.key() == QtCore.Qt.Key_Escape:
            super(Pause, self).keyPressEvent(event)

    def exit(self):
        pausewind.close()
        pg.quit()


    def resumedef(self):
        global paused
        pausewind.close()
        paused = False


class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        uic.loadUi("resources/uies/LoginUi3.ui", self)
        pg.init()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.singnup.clicked.connect(self.loginfunction)
        self.x.clicked.connect(self.exit)

    def exit(self):
        mywin.close()

    def loginfunction(self):
        global user
        user = self.loginfield.text()
        password = self.password.text()


        if not user or not password:
            showdialog('Enter your login or password')
        else:
            conn = sqlite3.connect("resources/database/users.db")
            cur = conn.cursor()
            res = cur.execute('SELECT password FROM users WHERE name = ?', (user,)).fetchone()
            if res is None:
                showdialog('Incorrect login or password')
            else:
                if res[0] == password:
                    with open('resources/database/user.txt', 'w') as file:
                        file.write(f'{user}')
                        file.close
                        pass
                    pg.mixer.music.load('resources/sound/menutheme.mp3')
                    pg.mixer.music.set_volume(0.2)
                    pg.mixer.music.play(-1)
                    time.sleep(0.2)
                    mywin.close()
                    widget.show()
                else:
                    QMessageBox.warning(self, 'Warning', 'Incorrect login or password', QMessageBox.Ok)


class Mainmenu(QDialog):
    def __init__(self):
        super(Mainmenu, self).__init__()
        uic.loadUi("resources/uies/MainMenu.ui", self)
        self.hidden = True
        self.restartoflag = False
        self.playhidden = True
        self.exithidden = True
        self.blackex.hide()
        self.sureq.hide()
        self.yes.hide()
        self.no.hide()
        self.blackpla.hide()
        self.cont.hide()
        self.newg.hide()
        self.restarto.hide()
        self.volumela.hide()
        self.volumeli.hide()
        self.fpslo.hide()
        self.fpslock.hide()
        self.res.hide()
        self.resol.hide()
        self.mousela.hide()
        self.mousesens.hide()
        self.blacksett.hide()
        self.apply.hide()
        self.start.clicked.connect(self.showbuttons)
        self.newg.clicked.connect(self.runnewgame)
        self.cont.clicked.connect(self.runthegame)
        self.x.clicked.connect(self.exit)
        self.yes.clicked.connect(self.forsureexit)
        self.no.clicked.connect(self.dontexit)
        self.tab.clicked.connect(self.hide)
        self.apply.clicked.connect(self.applyset)

    def showbuttons(self):
        if self.hidden and self.playhidden and self.exithidden:
            self.blackpla.show()
            self.cont.show()
            self.newg.show()
            self.playhidden = False
        else:
            self.blackpla.hide()
            self.cont.hide()
            self.newg.hide()
            self.playhidden = True

    def runthegame(self):
        widget.close()
        game = Game()
        game.run()

    def runnewgame(self):
        conn = sqlite3.connect("resources/database/users.db")
        cur = conn.cursor()
        cur.execute(f'UPDATE users SET level = {int(0)} WHERE name = ?',
                    (user,))
        conn.commit()
        conn.close()
        widget.close()
        game = Game()
        game.run()


    def exit(self):
        if self.hidden and self.playhidden and self.exithidden:
            self.blackex.show()
            self.sureq.show()
            self.yes.show()
            self.no.show()
            self.exithidden = False
        else:
            self.blackex.hide()
            self.sureq.hide()
            self.yes.hide()
            self.no.hide()
            self.exithidden = True

    def forsureexit(self):
        widget.close()
        pg.quit()

    def dontexit(self):
        self.blackex.hide()
        self.sureq.hide()
        self.yes.hide()
        self.no.hide()
        self.exithidden = True

    def hide(self):
        if self.hidden and self.playhidden and self.exithidden:
            self.fpslo.show()
            self.fpslock.show()
            self.res.show()
            self.resol.show()
            self.blacksett.show()
            self.apply.show()
            self.mousela.show()
            self.mousesens.show()
            self.volumela.show()
            self.volumeli.show()
            self.hidden = False
            if self.restartoflag:
                self.restarto.show()
        else:
            self.restarto.hide()
            self.fpslo.hide()
            self.fpslock.hide()
            self.res.hide()
            self.resol.hide()
            self.blacksett.hide()
            self.apply.hide()
            self.mousela.hide()
            self.mousesens.hide()
            self.volumela.hide()
            self.volumeli.hide()
            self.hidden = True

    def applyset(self):
        self.restarto.show()
        self.restartoflag = True
        if self.resol.currentText() == '1920 by 1080':
            conn = sqlite3.connect("resources/database/users.db")
            cur = conn.cursor()
            WIDTH = 1920
            HEIGHT = 1080
            cur.execute(f'UPDATE users SET height = {HEIGHT} WHERE name = ?', (user,))
            conn.commit()
            cur.execute(f'UPDATE users SET width = {WIDTH} WHERE name = ?', (user,))
            conn.commit()
            conn.close()
        elif self.resol.currentText() == '1600 by 900':
            conn = sqlite3.connect("resources/database/users.db")
            cur = conn.cursor()
            WIDTH = 1600
            HEIGHT = 900
            cur.execute(f'UPDATE users SET height = {HEIGHT} WHERE name = ?', (user,))
            conn.commit()
            cur.execute(f'UPDATE users SET width = {WIDTH} WHERE name = ?', (user,))
            conn.commit()
            conn.close()
        elif self.resol.currentText() == '1280 by 720':
            conn = sqlite3.connect("resources/database/users.db")
            cur = conn.cursor()
            WIDTH = 1280
            HEIGHT = 720
            cur.execute(f'UPDATE users SET height = {HEIGHT} WHERE name = ?', (user,))
            conn.commit()
            cur.execute(f'UPDATE users SET width = {WIDTH} WHERE name = ?', (user,))
            conn.commit()
            conn.close()
        if self.mousesens.text():
            conn = sqlite3.connect("resources/database/users.db")
            cur = conn.cursor()
            sensitivityn = float(self.mousesens.text())
            cur.execute(f'UPDATE users SET sensitivity = {sensitivityn} WHERE name = ?', (user,))
            conn.commit()
            conn.close()
        if self.fpslo.text():
            conn = sqlite3.connect("resources/database/users.db")
            cur = conn.cursor()
            FPS = int(self.fpslo.text())
            cur.execute(f'UPDATE users SET fpslock = {FPS} WHERE name = ?', (user,))
            conn.commit()
            conn.close()
        if self.volumeli.text():
            pg.mixer.music.set_volume(float(self.volumeli.text()))


class Scenemenu(QDialog):
    def __init__(self):
        super(Scenemenu, self).__init__()
        uic.loadUi("resources/uies/cutscenes.ui", self)
        self.x.clicked.connect(self.exit)
        self.textofcuts2.hide()
        self.move(320, 180)

    def exit(self):
        global paused
        cutscene.close()
        paused = False



class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode((RES), pg.NOFRAME)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)
        conn = sqlite3.connect("resources/database/users.db")
        cur = conn.cursor()
        reslvl = cur.execute('SELECT level FROM users WHERE name = ?', (user,)).fetchone()
        self.current_lvl = reslvl[0]
        if self.current_lvl == 0:
            cutscene.show()
            cutscene.textofcuts.setText('Our helicopter was shot down by locals.'
                                        ' I dont know where is my team,'
                                        ' but I should get out of here.')
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)
        self.pathfinding = PathFinding(self)
        pg.mixer.music.play(-1)

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.object_renderer.draw()
        self.weapon.draw()
        # self.map.draw()
        # self.player.draw()

    def check_events(self):
        self.global_trigger = False
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                global paused
                pausewind.show()
                paused = True
            if event.type == self.global_event:
                self.global_trigger = True
            if keys[pg.K_r] and self.player.bullets != 30:
                self.player.reload()
                self.sound.reload.play()
            if event.type == pg.KEYUP and keys[pg.K_g]:
                    self.current_lvl += 1
                    if self.current_lvl == 4:
                        paused = True
                        final.kills.setText(str(randint(40, 70)))
                        vremya = str(int(time.process_time()))
                        final.time2.setText(f'{vremya} sec')
                        final.show()
                        pg.mixer.music.set_volume(0.0)
                        os.startfile('makarov.mp4')
                    else:
                        conn = sqlite3.connect("resources/database/users.db")
                        cur = conn.cursor()
                        cur.execute(f'UPDATE users SET level = {int(self.current_lvl)} WHERE name = ?', (user,))
                        conn.commit()
                        conn.close()
                        global textofcutscenes
                        cutscene.textofcuts.setText(textofcutscenes[self.current_lvl])
                        cutscene.show()
                        if self.current_lvl == 3:
                            cutscene.textofcuts2.show()
                        else:
                            cutscene.textofcuts2.hide()
                        paused = True
                        print(self.current_lvl)
                        self.object_handler.restart_after_win()
            if (event.type == pg.KEYUP and keys[pg.K_SPACE]) and self.object_handler.check_win():
                self.current_lvl += 1
                if self.current_lvl == 4:
                    paused = True
                    final.kills.setText(str(randint(40, 70)))
                    vremya = str(int(time.process_time()))
                    final.time2.setText(f'{vremya} sec')
                    final.show()
                    pg.mixer.music.set_volume(0.0)
                    os.startfile('makarov.mp4')
                else:
                    conn = sqlite3.connect("resources/database/users.db")
                    cur = conn.cursor()
                    cur.execute(f'UPDATE users SET level = {int(self.current_lvl)} WHERE name = ?', (user,))
                    conn.commit()
                    conn.close()
                    cutscene.textofcuts.setText(textofcutscenes[self.current_lvl])
                    cutscene.show()
                    if self.current_lvl == 3:
                        cutscene.textofcuts2.show()
                    else:
                        cutscene.textofcuts2.hide()
                    paused = True
                    print(self.current_lvl)
                    self.object_handler.restart_after_win()
            if pg.mouse.get_pressed()[0]:
                self.player.single_fire_event(event)
            else:
                self.player.shot = False

    def run(self):
        global paused
        while True:
            self.check_events()
            if not paused:
                self.update(), self.draw()


if __name__ == '__main__':
    app2 = QtWidgets.QApplication(sys.argv)
    global final
    final = Finalmenu()
    final.setWindowTitle('Goodbye')
    final.setFixedWidth(1280)
    final.setFixedHeight(720)
    app4 = QtWidgets.QApplication(sys.argv)
    global cutscene
    cutscene = Scenemenu()
    cutscene.setWindowTitle('Cutscene')
    cutscene.setFixedWidth(1280)
    cutscene.setFixedHeight(720)
    cutscene.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    app3 = QtWidgets.QApplication(sys.argv)
    global pausewind
    pausewind = Pause()
    pausewind.setFixedWidth(600)
    pausewind.setFixedHeight(600)
    pausewind.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    pausewind.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    app = QtWidgets.QApplication(sys.argv)
    global mywin
    mywin = LoginScreen()
    mywin.setFixedWidth(600)
    mywin.setFixedHeight(500)
    mywin.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    mywin.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    mywin.show()
    app1 = QApplication(sys.argv)
    mainmenu = Mainmenu()
    global widget
    widget = QtWidgets.QStackedWidget()
    widget.setWindowTitle('Game')
    widget.addWidget(mainmenu)
    widget.setFixedWidth(1280)
    widget.setFixedHeight(720)
    sys.exit(app1.exec_())
    app2 = QtWidgets.QApplication(sys.argv)
