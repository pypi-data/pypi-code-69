import numpy as np
from kmap.library.id import ID
from kmap.library.orbitaldata import OrbitalData


class OrbitalDataTabModel():

    def __init__(self, controller):

        self.controller = controller

        self.displayed_plot_data = None
        self.orbitals = []

    def load_data_from_path(self, path):

        id_ = ID.new_ID()
        new_orbital = OrbitalData.init_from_file(path, ID=id_)
        self.orbitals.append(new_orbital)

        return new_orbital

    def load_data_from_online(self, url, meta_data={}):

        id_ = ID.new_ID()
        new_orbital = OrbitalData.init_from_online(
            url, ID=id_, meta_data=meta_data)

        self.orbitals.append(new_orbital)

        return new_orbital

    def remove_data_by_object(self, orbital):

        self.orbitals.remove(orbital)

    def remove_data_by_index(self, index):

        del self.orbitals[index]

    def get_orbital_kmap_by_ID(self, ID):

        orbital = self.ID_to_orbital(ID)
        if orbital is None:
            raise IndexError('wrong ID')

        parameters = self.controller.get_parameters(ID)
        # Split of first element
        weight, *other = parameters
        # Get scaled kmap
        kmap = weight * orbital.get_kmap(*other)

        return kmap

    def update_displayed_plot_data(self):

        kmaps = []

        for orbital in self.orbitals:
            ID = orbital.ID

            if self.controller.get_use(ID):
                # Get all parameters for this orbital
                kmap = self.get_orbital_kmap_by_ID(ID)
                kmaps.append(kmap)

        if kmaps:
            # Sum kmaps
            self.displayed_plot_data = np.nansum(kmaps)

        else:
            self.displayed_plot_data = None

        return self.displayed_plot_data

    def remove_orbital_by_ID(self, ID):

        orbital = self.ID_to_orbital(ID)

        if orbital is not None:
            self.orbitals.remove(orbital)

    def ID_to_orbital(self, ID):

        for orbital in self.orbitals:
            if orbital.ID == ID:
                return orbital

        return None
