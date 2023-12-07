#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.5.1

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
import math
import numpy as np



from gnuradio import qtgui

class QPSTX(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "QPSTX")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.tabla_de_verdad = tabla_de_verdad = (0.77+0.77j,-0.77+0.77j,-0.77-0.77j,0.77-0.77j)
        self.M = M = len(tabla_de_verdad)
        self.sps = sps = 8
        self.bpsim = bpsim = math.log(M,2)
        self.Rs = Rs = 32000
        self.tablaaa = tablaaa = digital.constellation_qpsk().base()
        self.samp_rate = samp_rate = sps*Rs
        self.h = h = [1]*sps
        self.Freq = Freq = 0
        self.Bit_rate = Bit_rate = Rs*bpsim
        self.Amp = Amp = 0

        ##################################################
        # Blocks
        ##################################################

        self.Menu = Qt.QTabWidget()
        self.Menu_widget_0 = Qt.QWidget()
        self.Menu_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Menu_widget_0)
        self.Menu_grid_layout_0 = Qt.QGridLayout()
        self.Menu_layout_0.addLayout(self.Menu_grid_layout_0)
        self.Menu.addTab(self.Menu_widget_0, 'QPSK')
        self.Menu_widget_1 = Qt.QWidget()
        self.Menu_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Menu_widget_1)
        self.Menu_grid_layout_1 = Qt.QGridLayout()
        self.Menu_layout_1.addLayout(self.Menu_grid_layout_1)
        self.Menu.addTab(self.Menu_widget_1, '8PSK')
        self.Menu_widget_2 = Qt.QWidget()
        self.Menu_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Menu_widget_2)
        self.Menu_grid_layout_2 = Qt.QGridLayout()
        self.Menu_layout_2.addLayout(self.Menu_grid_layout_2)
        self.Menu.addTab(self.Menu_widget_2, 'Decod 8PSK')
        self.Menu_widget_3 = Qt.QWidget()
        self.Menu_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Menu_widget_3)
        self.Menu_grid_layout_3 = Qt.QGridLayout()
        self.Menu_layout_3.addLayout(self.Menu_grid_layout_3)
        self.Menu.addTab(self.Menu_widget_3, 'Decod QPSK')
        self.top_layout.addWidget(self.Menu)
        self.qtgui_time_sink_x_1_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1_0.enable_tags(True)
        self.qtgui_time_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_0.enable_grid(False)
        self.qtgui_time_sink_x_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_0.enable_control_panel(False)
        self.qtgui_time_sink_x_1_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0.qwidget(), Qt.QWidget)
        self.Menu_grid_layout_3.addWidget(self._qtgui_time_sink_x_1_0_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.Menu_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Menu_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.Menu_grid_layout_0.addWidget(self._qtgui_time_sink_x_0_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.Menu_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Menu_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(0.05)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.Menu_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_win, 3, 0, 1, 1)
        for r in range(3, 4):
            self.Menu_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Menu_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
            1024, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.qwidget(), Qt.QWidget)
        self.Menu_grid_layout_0.addWidget(self._qtgui_const_sink_x_0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.Menu_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Menu_grid_layout_0.setColumnStretch(c, 1)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_ccc(8, h)
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.fir_filter_xxx_0_0 = filter.fir_filter_ccc(8, h)
        self.fir_filter_xxx_0_0.declare_sample_delay(0)
        self.digital_constellation_encoder_bc_0 = digital.constellation_encoder_bc(tablaaa)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(tablaaa)
        self.blocks_vector_source_x_0_0 = blocks.vector_source_b((0,0,1,1,2,2,3,3), True, 1, )
        self.blocks_unpacked_to_packed_xx_0_0 = blocks.unpacked_to_packed_bb(8, gr.GR_MSB_FIRST)
        self.blocks_char_to_float_0_0 = blocks.char_to_float(1, 1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.an_noise = analog.noise_source_c(analog.GR_GAUSSIAN, 0.15, 0)
        self._Freq_range = Range(0, 200000, 1000, 0, 200)
        self._Freq_win = RangeWidget(self._Freq_range, self.set_Freq, "Filter Freq", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Freq_win)
        self._Amp_range = Range(0, 1, 0.02, 0, 200)
        self._Amp_win = RangeWidget(self._Amp_range, self.set_Amp, "A_Noise", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Amp_win)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.an_noise, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.fir_filter_xxx_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_char_to_float_0_0, 0), (self.qtgui_time_sink_x_1_0, 0))
        self.connect((self.blocks_unpacked_to_packed_xx_0_0, 0), (self.blocks_char_to_float_0_0, 0))
        self.connect((self.blocks_vector_source_x_0_0, 0), (self.digital_constellation_encoder_bc_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.blocks_unpacked_to_packed_xx_0_0, 0))
        self.connect((self.digital_constellation_encoder_bc_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.fir_filter_xxx_0_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.qtgui_freq_sink_x_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "QPSTX")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_tabla_de_verdad(self):
        return self.tabla_de_verdad

    def set_tabla_de_verdad(self, tabla_de_verdad):
        self.tabla_de_verdad = tabla_de_verdad
        self.set_M(len(self.tabla_de_verdad))

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.set_bpsim(math.log(self.M,2))

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_h([1]*self.sps)
        self.set_samp_rate(self.sps*self.Rs)

    def get_bpsim(self):
        return self.bpsim

    def set_bpsim(self, bpsim):
        self.bpsim = bpsim
        self.set_Bit_rate(self.Rs*self.bpsim)

    def get_Rs(self):
        return self.Rs

    def set_Rs(self, Rs):
        self.Rs = Rs
        self.set_Bit_rate(self.Rs*self.bpsim)
        self.set_samp_rate(self.sps*self.Rs)

    def get_tablaaa(self):
        return self.tablaaa

    def set_tablaaa(self, tablaaa):
        self.tablaaa = tablaaa

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1_0.set_samp_rate(self.samp_rate)

    def get_h(self):
        return self.h

    def set_h(self, h):
        self.h = h
        self.fir_filter_xxx_0_0.set_taps(self.h)
        self.interp_fir_filter_xxx_0.set_taps(self.h)

    def get_Freq(self):
        return self.Freq

    def set_Freq(self, Freq):
        self.Freq = Freq

    def get_Bit_rate(self):
        return self.Bit_rate

    def set_Bit_rate(self, Bit_rate):
        self.Bit_rate = Bit_rate

    def get_Amp(self):
        return self.Amp

    def set_Amp(self, Amp):
        self.Amp = Amp




def main(top_block_cls=QPSTX, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
