import enum


class Status(enum.Enum):
    DEP = "dep"
    PROC = "proc"
    AUTH = "auth"
    REPL = "repl"
    AUCO = "auco"
    AUXS = "auxs"
    AUXU = "auxu"
    HOLD = "hold"
    HPUB = "hpub"
    OBS = "obs"
    POLC = "polc"
    REL = "rel"
    REUP = "reup"
    WAIT = "wait"
    WDRN = "wdrn"


class ExperimentTypes(enum.Enum):
    XRAY = "xray"
    EM = "em"
    EC = "ec"
    SSNMR = "ssnmr"
    NMR = "nmr"
    NEUTRON = "neutron"
    FIBER = "fiber"

    def to_cif(self):
        """Mapping between this enum and the values used
        in the cif file
        """
        mapping = {
            self.XRAY: "X-RAY DIFFRACTION",
            self.EM: "ELECTRON MICROSCOPY",
            self.EC: "ELECTRON CRYSTALLOGRAPHY",
            self.SSNMR: "SOLUTION NMR",
            self.NMR: "SOLID-STATE NMR",
            self.NEUTRON: "NEUTRON DIFFRACTION",
            self.FIBER: "FIBER DIFFRACTION",
        }

        return mapping[self]
