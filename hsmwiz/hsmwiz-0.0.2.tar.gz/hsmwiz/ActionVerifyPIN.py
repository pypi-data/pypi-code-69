#	hsmwiz - Simplified handling of Hardware Security Modules
#	Copyright (C) 2018-2020 Johannes Bauer
#
#	This file is part of hsmwiz.
#
#	hsmwiz is free software; you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation; this program is ONLY licensed under
#	version 3 of the License, later versions are explicitly excluded.
#
#	hsmwiz is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#	Johannes Bauer <JohannesBauer@gmx.de>

import sys
from .BaseAction import BaseAction
from .HardwareSecurityModule import HardwareSecurityModule

class ActionVerifyPIN(BaseAction):
	def __init__(self, cmdname, args):
		BaseAction.__init__(self, cmdname, args)

		if not args.verify_sopin:
			hsm = HardwareSecurityModule(verbose = (self.args.verbose > 0), so_path = self.args.so_path, pin = self.args.pin)
			if hsm.login():
				print("PIN correct.", file = sys.stderr)
			else:
				print("PIN was WRONG!", file = sys.stderr)
		else:
			hsm = HardwareSecurityModule(verbose = (self.args.verbose > 0), so_path = self.args.so_path, sopin = self.args.pin)
			if hsm.login(with_sopin = True):
				print("SO-PIN correct.", file = sys.stderr)
			else:
				print("SO-PIN was WRONG!", file = sys.stderr)
