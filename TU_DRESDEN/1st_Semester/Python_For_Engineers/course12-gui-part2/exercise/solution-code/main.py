import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore

import pyqtgraph as pg
import numpy as np
import scipy.integrate

import customwidgets as cw
import cart_pendulum_model



class Gui(QtWidgets.QMainWindow):
    """
    Own class (derived from QMainWindow).
    """

    def __init__(self):
        # call the "constructor" of the base-class
        QtWidgets.QMainWindow.__init__(self)

        self.setWindowTitle("Simulation of the Pendulum")
        self.setWindowIcon(QtGui.QIcon("../data/trolley.png"))

        self.centralwg = QtWidgets.QWidget()
        self.setCentralWidget(self.centralwg)

        self.parameter_mask = cw.ParameterMask(parent=self.centralwg)

        # create a pyqtgraph plot widget
        self.scene = pg.PlotWidget()
        # achieve that x and y have the same scaling factor on the screen
        self.scene.setAspectLocked()

        # iv means initial value
        self.iv_slider_x = cw.IVSlider("x0", limits=(-1000, 1000))
        self.iv_slider_phi = cw.IVSlider("phi0", limits=(-180, 180))

        # slider for pendulum length (task 3)
        self.slider_l = cw.IVSlider("l", limits=(0, 300))

        # layout
        self.hbox = QtWidgets.QGridLayout()
        self.hbox.addWidget(self.parameter_mask, 0, 0)

        self.hbox.addWidget(self.iv_slider_x, 1, 0)
        self.hbox.addWidget(self.iv_slider_phi, 2, 0)

        # task 3
        self.hbox.addWidget(self.slider_l, 3, 0)

        self.hbox.addWidget(self.scene, 0, 1, 4, 1)  # with rowspan=4, colspan=1
        self.centralwg.setLayout(self.hbox)

        # actions for the File menu (Open, Save, Exit)
        # variant 1: with multiple individual function calls
        self.actn_open = QtWidgets.QAction(self)
        self.actn_open.setText("Load...")
        self.actn_open.setShortcut(QtGui.QKeySequence.Open)
        self.actn_open.setIcon(QtGui.QIcon("../data/open.png"))
        self.actn_open.triggered.connect(self.parameter_mask.openfile)

        # variant 2: with one function call (with multiple arguments)
        self.actn_save = QtWidgets.QAction(
            QtGui.QIcon("../data/save.png"),
            "Save...",
            self,
            shortcut=QtGui.QKeySequence.Save,
            statusTip="save parameer file",
            triggered=self.parameter_mask.savefile,
        )

        self.actn_exit = QtWidgets.QAction(
            "Quit", self, shortcut="Ctrl+Q", statusTip="leave program", triggered=self.close
        )

        # save the status whether simulation is running (task 2)
        self.is_playing = False

        # create instance attributes for the coordinates of the mechanical
        # system (x, phi) and pendulum length l (task 3)
        self.x = 0
        self.phi = 0.25 * np.pi
        self.l = 1

        # two actions for controlling the simulation
        self.actn_start_anim = QtWidgets.QAction(self)
        self.actn_start_anim.setText("Play")
        self.actn_start_anim.setIcon(QtGui.QIcon("../data/play.png"))
        self.actn_start_anim.triggered.connect(self.start_animation)

        self.actn_stop_anim = QtWidgets.QAction(self)
        self.actn_stop_anim.setText("Stop")
        self.actn_stop_anim.setIcon(QtGui.QIcon("../data/stop.png"))
        self.actn_stop_anim.triggered.connect(self.stop_animation)

        # new action for toggling the siumlation on and off
        self.actn_toggle_anim = QtWidgets.QAction(self)
        self.actn_toggle_anim.setText("Play")
        self.actn_toggle_anim.setIcon(QtGui.QIcon("../data/play.png"))
        self.actn_toggle_anim.triggered.connect(self.toggle_animation)

        # assemble the menus
        self.menu_file = self.menuBar().addMenu("&File")
        self.menu_file.addAction(self.actn_open)
        self.menu_file.addAction(self.actn_save)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.actn_exit)

        # create toolbar for file menu and feed actions
        self.toolbar_file = QtWidgets.QToolBar("File")
        self.toolbar_file.setIconSize(QtCore.QSize(24, 24))
        self.addToolBar(self.toolbar_file)
        self.toolbar_file.addAction(self.actn_open)
        self.toolbar_file.addAction(self.actn_save)

        # create toolbar for simulation control and feed actions
        self.toolbar_sim = QtWidgets.QToolBar("Simulation")
        self.toolbar_file.setIconSize(QtCore.QSize(24, 24))
        self.addToolBar(self.toolbar_sim)
        self.toolbar_sim.addAction(self.actn_toggle_anim)

        # task 2: do not add the actions for starting and sopping (now we usetoggle)
        # self.toolbar_sim.addAction(self.actn_start_anim)
        # self.toolbar_sim.addAction(self.actn_stop_anim)

        # connect slider-change-signals with respective slots
        self.iv_slider_x.slider.valueChanged.connect(self.setx)
        self.iv_slider_x.slider.valueChanged.connect(self.draw_cart_pendulum)
        self.iv_slider_phi.slider.valueChanged.connect(self.setphi)
        self.iv_slider_phi.slider.valueChanged.connect(self.draw_cart_pendulum)

        self.slider_l.slider.valueChanged.connect(self.change_pendulum_length)
        self.slider_l.slider.valueChanged.connect(self.draw_cart_pendulum)

        # The values of the instance attributes self.x, self.phi und self.l should
        # be displayed by the sliders from the beginning
        self.iv_slider_x.slider.setValue(int(self.x * 1000))
        self.iv_slider_phi.slider.setValue(int(self.phi * 180 / np.pi))
        self.slider_l.slider.setValue(int((self.l - 0.3) * 100))

        self.draw_cart_pendulum()

        # end of self.__init__(...)

    def setx(self, x):
        "take value from slider signal, scale it and store it as instance attribute"
        self.x = x / 1000

    def setphi(self, phi):
        "take value from slider signal, scale it and store it as instance attribute"
        self.phi = phi / 180 * np.pi

    def draw_cart_pendulum(self):
        self.scene.clear()
        x_range = np.array([-2, 2])
        y_range = x_range - 1.0
        self.scene.setRange(xRange=x_range, yRange=y_range)
        dx = 0.1
        dy = 0.05
        # corner points of a rectangle (center point (x, 0) starting at the lower left)
        xvalues_cart = self.x + np.array([-dx, -dx, dx, dx, -dx])
        yvalues_cart = np.array([-dy, dy, dy, -dy, -dy])

        # position of the suspension (joint) and the load ("tip")
        l = self.l
        x_joint = self.x
        y_joint = 0
        x_tip = x_joint + l * np.sin(self.phi)
        y_tip = y_joint - l * np.cos(self.phi)
        self.scene.plot(xvalues_cart, yvalues_cart)
        self.scene.plot([x_joint, x_tip], [y_joint, y_tip], symbol="o")

    def toggle_animation(self):
        """
        Switch between playback and stop
        """

        if self.is_playing:
            self.stop_animation()
            self.is_playing = False

        else:
            self.start_animation()
            self.is_playing = True

    def start_animation(self):
        """
        Starting the simulation and animation. Thereby a timer is simply
        which updates the system every ms.
        """

        # solver
        self.init_solver()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.calc_step)

        # calc step size and start timer
        dt = int(float(self.parameter_mask.dt.getValue()) * 1000)
        self.timer.start(dt)

        self.actn_toggle_anim.setText("Stop")
        self.actn_toggle_anim.setIcon(QtGui.QIcon("../data/stop.png"))

    def stop_animation(self):
        """
        Stops the animation and resets the system to the start values.
        This simply clears the timer that was created in self.startAnimation().
        is deleted.
        """

        # delete the timer attribute
        del self.timer

        self.actn_toggle_anim.setText("Play")
        self.actn_toggle_anim.setIcon(QtGui.QIcon("../data/play.png"))

    def init_solver(self):
        """
        Create solver and pass parameters (step size and masses)
        """

        # solver
        self.solver = scipy.integrate.ode(cart_pendulum_model.rhs)
        initial_state = [self.x, self.phi, 0, 0]
        self.solver.set_initial_value(initial_state)
        self.solver.set_integrator("vode", method="adams", rtol=1e-6, atol=1e-9)

        # step size
        self.dt = self.parameter_mask.dt.value

        # fetch and set current parameters
        m1 = self.parameter_mask.m_trolley.value
        m2 = self.parameter_mask.m_load.value
        self.solver.set_f_params(m1, m2)

    def calc_step(self):
        """
        Function to calculate a single integration step.
        Scene is updated afterwards.
        """

        # solve one step
        xx = self.solver.integrate(self.solver.t + self.dt)
        self.x, self.phi = xx[:2]

        # update scene
        self.draw_cart_pendulum()

    def change_pendulum_length(self, l):
        """
        process slider values for pendulum length
        """
        self.l = l / 100.0 + 0.3  # absolut value and scaling

        # overwrite the global variable `l` in the `cart_pendulum_model` module
        cart_pendulum_model.l = self.l

    # end of class Gui


app = QtWidgets.QApplication([])

gui = Gui()  # create an instance of the new class
gui.show()
app.exec_()
