"""
HX711 Load cell amplifier Python Library
Original source: https://gist.github.com/underdoeg/98a38b54f889fce2b237
Documentation source: https://github.com/aguegu/ardulibs/tree/master/hx711
Adapted by 2017 Jiri Dohnalek

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""
from raspcuterie.devices import InputDevice
from raspcuterie.gpio import GPIO


class HX711(InputDevice):

    def __init__(self, name, dout=23, pd_sck=24, gain=128):
        super(HX711, self).__init__(name)
        """
        Set GPIO Mode, and pin for communication with HX711
        :param dout: Serial Data Output pin
        :param pd_sck: Power Down and Serial Clock Input pin
        :param gain: set gain 128, 64, 32
        """

        self.GAIN = 0
        self.offset = 0
        self.scale = 1

        # Setup the gpio pin numbering system
        GPIO.setmode(GPIO.BCM)

        # Set the pin numbers
        self.PD_SCK = pd_sck
        self.DOUT = dout

        # Setup the GPIO Pin as output
        GPIO.setup(self.PD_SCK, GPIO.OUT)

        # Setup the GPIO Pin as input
        GPIO.setup(self.DOUT, GPIO.IN)

        # Power up the chip
        self.power_up()
        self.set_gain(gain)

    def set_offset(self, value):
        self.offset = value

    def set_scale(self, value):
        self.scale = value

    def set_gain(self, gain=128):

        if gain == 128:
            self.GAIN = 3
        elif gain == 64:
            self.GAIN = 2
        elif gain == 32:
            self.GAIN = 1
        else:
            self.GAIN = 3

        GPIO.output(self.PD_SCK, False)
        self.read()

    def read(self):
        """
        Read data from the HX711 chip
        :param void
        :return reading from the HX711
        """

        # Control if the chip is ready
        while not (GPIO.input(self.DOUT) == 0):
            # Uncommenting the print below results in noisy output
            # print("No input from HX711.")
            pass

        # Original C source code ported to Python as described in datasheet
        # https://cdn.sparkfun.com/datasheets/Sensors/ForceFlex/hx711_english.pdf
        # Output from python matched the output of
        # different HX711 Arduino library example
        # Lastly, behaviour matches while applying pressure
        # Please see page 8 of the PDF document

        count = 0

        for i in range(24):
            GPIO.output(self.PD_SCK, True)
            count = count << 1
            GPIO.output(self.PD_SCK, False)
            if GPIO.input(self.DOUT):
                count += 1

        GPIO.output(self.PD_SCK, True)
        count = count ^ 0x800000
        GPIO.output(self.PD_SCK, False)

        # set channel and gain factor for next reading
        for i in range(self.GAIN):
            GPIO.output(self.PD_SCK, True)
            GPIO.output(self.PD_SCK, False)

        return count

    def read_average(self, times=16):
        """
        Calculate average value from
        :param times: measure x amount of time to get average
        """
        sum = 0
        for i in range(times):
            sum += self.read()
        return sum / times

    def get_grams(self, times=16):
        """
        :param times: Set value to calculate average,
        be aware that high number of times will have a
        slower runtime speed.
        :return float weight in grams
        """
        value = self.read_average(times) - self.offset
        grams = value / self.scale
        return grams

    def tare(self, times=16):
        """
        Tare functionality fpr calibration
        :param times: set value to calculate average
        """
        self.offset = self.read_average(times)

    def power_down(self):
        """
        Power the chip down
        """
        GPIO.output(self.PD_SCK, False)
        GPIO.output(self.PD_SCK, True)

    def power_up(self):
        """
        Power the chip up
        """
        GPIO.output(self.PD_SCK, False)

    def get_context(self):
        return dict(weight=self.get_grams())
