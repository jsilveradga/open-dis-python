"""designator.py

11 Designator
"""
import enum


# [UID 80]
class DesignatorSystemName(enum.IntEnum):
    """11.1 Designator System Name [UID 80]"""
    NOT_SPECIFIED = 0
    AN_AAQ_4 = 1000
    AN_AAQ_7 = 1100
    AN_AAQ_8 = 1200
    AN_AAQ_14_LANTIRN = 1300
    AN_AAQ_19 = 1400
    AN_AAQ_22A_SAFIRE = 1500
    AN_AAQ_22B_SAFIRE_LP = 1600
    AN_AAQ_22C_Star_SAFIRE_I = 1700
    AN_AAQ_22D_BRITE_Star = 1800
    AN_AAQ_24_DIRCM_Nemesis = 1900
    AN_AAQ_25_LTS = 2000
    AN_AAQ_28_LITENING_II = 2100
    AN_AAQ_30 = 2200
    AN_AAQ_32 = 2300
    AN_AAQ_33_Sniper = 2400
    AN_AAQ_37 = 2500
    AN_AAQ_38 = 2600
    AN_AAS_32 = 2700
    AN_AAS_35V = 2800
    AN_AAS_37 = 2900
    AN_AAS_38 = 3000
    AN_AAS_44V = 3100
    AN_AAS_46 = 3200
    AN_AAS_49 = 3300
    AN_AAS_51 = 3400
    AN_AAS_52 = 3500
    AN_ALQ_10 = 3600
    AN_ASQ_228 = 3700
    AN_AVQ_25 = 4400
    AN_AVQ_26 = 4500
    AN_GVS_5 = 4600
    AN_PED_1_LLDR = 4700
    TADS_LRF_D = 4800
    MMS_LRF_D = 4900
    AH_1_C_NITE = 5000
    MATES = 5100
    TCV_115 = 5200
    TIM = 5300
    TMS_303 = 5400
    TMY_303 = 5500
    ALRAD = 5600
    RFTDL = 5700
    VVLR = 5800
    P0705_HELL = 6000
    P0708_PULSE = 6100
    HELD = 6200
    TYPE_105 = 6300
    TYPE_118 = 6400
    TYPE_121 = 6500
    TYPE_126 = 6600
    TYPE_629 = 6700
    CLDS = 6800
    TAV_38 = 6900
    TMV_630 = 7000
    ALTM_1020 = 7100
    ALATS = 7200
    DARK_STAR_LAMPS = 7300
    GLTD_II = 7400
    MBT_ELRF = 7500
    MARK_VII = 7600
    SIRE_V = 7700
    AN_AAQ_16B = 7800
    AN_AAQ_16D_AESOP = 7900
    AN_AAQ_21_STAR_SAFIRE_III = 8000
    AN_AAQ_22E_BRITE_STAR = 8100
    AN_AAQ_36_STAR_SAFIRE_II = 8200
    AN_AAS_38A_NITE_HAWK = 8300
    AN_AAS_38B_NITE_HAWK = 8400
    AN_AAS_44C_V = 8500
    AN_AAS_53_CSP = 8600
    AN_ASQ_28_ATFLIR = 8700
    AN_DAS_1_MTS_B = 8800
    AN_PAQ_1_LTD = 8900
    AN_PAQ_3_MULE = 9000
    AN_PEQ_1_SOFLAM = 9090
    AN_PEQ_3 = 9100
    AN_PEQ_15_ATPIAL = 9140
    AN_PEQ_18_IZLID_1000P = 9150
    AN_TVQ_2_G_VLLD = 9200
    AN_ZSQ_2_V1_EOS = 9300
    AN_ZSQ_2_V2_EOS = 9400
    CIRCM = 9500
    GUARDIAN = 9600
    IZLID_200P = 9700
    IZLID_1000P_W = 9800
    MMS = 9900
    M_TADS_PNVS_ARROWHEAD = 10000
    RBS_70 = 10100
    RBS_90 = 10200
    TADS_PNVS = 10300


# [UID 81]
class DesignatorCode(enum.IntEnum):
    """11.2 Designator Code [UID 81] (Deprecated)"""
    OTHER = 0
