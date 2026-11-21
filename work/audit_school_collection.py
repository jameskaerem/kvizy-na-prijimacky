"""Generate a numbered coverage ledger for the large Budějovice PDF."""

from collections import Counter
import csv
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / 'work'

# PDF starting pages, original question counts and test labels.
BLOCKS = [
    (1, 50, 'Biologie 2020'), (8, 50, 'Biologie 2020, druhý sken'),
    (15, 50, 'Všeobecná informovanost 2020'), (21, 50, 'Všeobecná informovanost 2020, druhý sken'),
    (27, 30, 'Motivační test 2020'), (31, 30, 'Motivační test 2020, druhý sken'),
    (35, 30, 'Motivační test 2020, další varianta'), (39, 50, 'Biologie 2020, další varianta'),
    (46, 50, 'Všeobecná informovanost 2021 v2'), (52, 50, 'Všeobecná informovanost 2021 v1'),
    (58, 50, 'Biologie 2021 v1'), (64, 50, 'Biologie 2021 v2'), (70, 50, 'Biologie 2021 v3'),
    (76, 30, 'Motivační test 2021 v3'), (80, 50, 'Všeobecná informovanost 2021 v3'),
    (86, 30, 'Motivační test 2021 v1'), (90, 30, 'Motivační test 2021 v2'),
    (94, 40, 'Biologie 2019, radiologický asistent I'),
    (99, 30, 'Všeobecná informovanost 2019, radiologický asistent I'),
    (103, 50, 'Biologie 2019, zdravotnický záchranář'),
    (109, 50, 'Všeobecná informovanost 2019, zdravotnický záchranář'),
    (115, 40, 'Biologie 2019, zdravotní laborant'),
    (120, 26, 'Všeobecná informovanost 2019, zdravotní laborant'),
    (123, 40, 'Biologie 2019, radiologický asistent II'),
    (128, 30, 'Všeobecná informovanost 2019, radiologický asistent II'),
    (132, 50, 'Biologie 2019, pediatrické ošetřovatelství'),
    (138, 50, 'ZSV 2019, pediatrické ošetřovatelství'),
    (144, 50, 'Biologie 2019, všeobecná sestra'),
    (150, 50, 'Všeobecná informovanost 2019, všeobecná sestra'),
    (157, 50, 'Biologie 2019, nutriční terapeut'),
    (163, 50, 'Všeobecná informovanost 2019, nutriční terapeut'),
    (169, 50, 'Biologie 2019, zdravotně-sociální péče'),
    (175, 50, 'ZSV 2019, zdravotně-sociální péče'),
    (181, 50, 'Všeobecná informovanost 2019, společná sada'),
    (187, 50, 'Biologie 2019, porodní asistentka'),
    (193, 50, 'Všeobecná informovanost 2019, porodní asistentka'),
    (199, 50, 'Biologie 2019, společná sada'),
    (205, 50, 'Všeobecná informovanost 2019, opakování I'),
    (211, 50, 'Všeobecná informovanost 2019, opakování II'),
    (217, 50, 'Všeobecná informovanost 2019, opakování III'),
    (223, 50, 'Všeobecná informovanost 2019, další společná sada'),
    (229, 50, 'Všeobecná informovanost 2019, opakování IV'),
    (235, 100, 'ZSV 2019, sociální práce'),
    (246, 50, 'Biologie 2019, opakování I'), (252, 50, 'Biologie 2019, opakování II'),
    (258, 50, 'Biologie 2019, opakování III'),
    (264, 40, 'Biologie 2019, radiologický asistent a laborant'),
    (270, 50, 'Biologie 2019, další společná sada'),
]

COPIES = {
    8: 1, 21: 15, 31: 27,
    157: 144, 169: 144, 187: 144,
    163: 150, 175: 150, 193: 150,
    205: 181, 211: 181, 217: 181, 229: 181,
    246: 199, 252: 199, 258: 199,
}

# Cross references are checked independently of the bank's own source labels.
REVIEWED = {
    1: {10: '621', 17: 'X:Proměnlivá klidová frekvence, chybí podmínky',
        22: '30', 23: '35', 24: '670', 34: '31', 39: 'E116', 42: '117', 45: 'E119'},
    15: {1: '74', 7: '78', 8: '69', 9: '243', 10: '79', 15: '59',
         18: '62', 19: '63', 22: 'X:Jedna věková hranice závisí na definici',
         23: '622', 28: 'X:Historický výčet síťových služeb', 29: '505',
         32: 'X:Problematické spojení subjektivity a uznání státu', 35: '648',
         37: '618', 38: '623', 39: '624', 43: '392',
         45: 'X:Klíč směšuje úrok a zisk', 47: '50'},
    27: {2: 'X:Subjektivní kombinace osobnostních předpokladů', 6: 'X:Bez vymezení roztoku a postupu nelze určit jedinou disociující sůl',
         8: 'X:Záleží na programu a popisu studia', 10: 'E654',
         17: 'X:Paušální zákaz invazivních metod', 19: '626',
         21: '654', 24: '627', 25: '170', 28: '671', 30: 'X:Časově podmíněné tvrzení o aktuálních osobnostech oboru'},
    35: {1: '170', 2: '326', 3: '671', 4: 'X:Časově podmíněné tvrzení o aktuálních osobnostech oboru', 5: '303', 7: '170',
         8: '654', 10: '171', 11: '683',
         14: '160', 17: '172', 21: 'X:Otázka vydává jedinou okolnost za příčinu plochonoží',
         22: '156', 23: 'X:Příliš obecný popis odborné způsobilosti', 24: '173',
         25: '678', 26: 'X:Bez vymezení roztoku a postupu nelze určit jedinou disociující sůl', 27: '161', 28: '168', 29: '627', 30: '162'},
    39: {2: '607', 6: '155', 9: 'E102',
         12: '636', 16: '25', 17: '90', 19: '162', 20: '102', 21: '21',
         22: '46', 24: '105',
         25: 'X:Délka tenkého střeva závisí na metodě měření',
         26: '22', 27: '30', 29: 'E47', 30: 'E109', 35: '594', 36: 'E113',
         37: '637', 39: 'E202', 42: '203', 44: 'E119', 47: '121',
         48: '207', 49: 'X:Zadání je na konci strany uříznuté'},
    46: {1: '677', 3: 'X:Vznik filozofie nelze spolehlivě přiřadit jediné univerzální situaci',
         5: '656', 6: '125', 7: '73', 8: '68', 9: '77', 10: '647', 13: '212', 19: '622',
         16: '649', 20: '78', 21: '217', 22: '562', 23: '625', 26: '150', 28: '623', 29: '69',
         30: 'X:Zařazení mezi romanticky orientované filozofy závisí na vymezení směru',
         31: '137', 32: '131', 33: '511', 35: 'E130', 36: '135',
         37: '130', 38: '62', 41: 'X:Příliš obecné tvrzení o filozofii 20. století',
         42: '132', 44: '624', 45: '58', 46: '603'},
    52: {2: '561', 4: '67', 5: 'E618', 6: '59', 8: '232', 9: '351',
         10: '672', 15: 'X:Právní otázka vyžaduje ověřenou formulaci',
         16: '69', 17: '682',
         19: '664', 21: 'X:Zdravotněprávní otázka vyžaduje ověřenou formulaci',
         23: '566', 24: '149', 25: '128', 28: '392', 30: '673',
         31: 'X:Dorozumívání i sdělování jsou obhajitelná vyjádření',
         32: '150', 34: '63', 35: 'E130',
         36: 'X:Paušální historické hodnocení směrů', 39: '79', 40: '130', 43: '80',
         45: '152', 46: '352', 50: '141'},
    58: {1: '663', 2: '185', 3: '186', 4: '90', 5: '621', 6: '94',
         8: '25', 9: '99', 10: '100', 11: '101', 12: '21', 13: '195',
         14: '105', 15: 'X:Délka tenkého střeva závisí na metodě měření',
         16: '22', 17: '30', 18: '196', 19: 'E47', 20: '109', 21: '197',
         22: '111', 23: '31', 24: '594', 26: '198', 30: '638',
         34: '372', 38: 'X:Tvarová klasifikace klíční a pánevní kosti není v nabídce spolehlivě rozlišena',
         40: '85', 43: '254', 45: '38'},
    64: {1: '183', 2: '86', 3: '187', 4: 'E102', 5: '636', 6: '193',
         7: 'X:Klidová tepová frekvence není univerzální hodnota', 8: '194',
         9: '162', 10: '102', 11: '103', 12: '106', 13: 'E107', 14: 'E109',
         15: '199', 16: '460', 17: '255', 19: '26', 20: '27', 24: '621',
         27: '189', 28: '256', 29: '111', 31: '8', 33: '45', 34: '172',
         35: '374', 36: 'X:Zařazení horních dýchacích cest je v nabídce nejednoznačné',
         38: '254', 43: '657', 44: '639', 46: '84', 47: '629', 50: '110'},
    70: {1: '86', 2: '88', 3: '90', 4: '188', 5: '667', 6: '94', 7: '252',
         8: '25', 9: '99', 10: '670', 11: '103', 12: '30', 13: '196',
         14: '109', 15: '111', 16: '200', 18: '198', 19: 'E267', 20: '279',
         21: '668', 23: '372', 24: '261',
         25: 'X:Tvarová klasifikace klíční a pánevní kosti není v nabídce spolehlivě rozlišena',
         26: '277', 27: '111', 31: 'X:Zařazení horních dýchacích cest je v nabídce nejednoznačné',
         32: '283', 34: '284', 36: '639', 37: '287', 38: '319', 39: '268',
         40: '665', 41: '289', 48: '94'},
    76: {1: '171', 2: '156', 9: 'X:Jednostrannost sportu nemá v zadání definované kritérium',
         13: '653', 16: '167', 19: '176', 20: '160', 21: '179',
         22: 'X:Paušální zákaz invazivních metod',
         23: '168', 24: 'E173', 25: '627', 26: '678',
         27: '654', 28: 'E654', 30: '157'},
    80: {1: '561', 2: '230', 3: 'E618', 4: '231', 5: '232', 7: '233', 8: '236',
         9: 'X:Právní otázka vyžaduje ověřenou formulaci', 11: '682',
         10: '69', 12: '238', 13: 'X:Zdravotněprávní otázka vyžaduje ověřenou formulaci',
         14: '566', 15: '149', 16: '128', 17: '240', 18: '392', 19: '673',
         20: '150', 21: '63', 22: 'X:Obecný vztah literárního směru k tématu mravní svobody',
         23: '79', 24: '130', 25: '247', 26: '248', 28: '250', 29: '66',
         30: '209', 31: '125', 32: '73', 33: '77', 34: '210', 35: '213', 36: '214',
         37: '215', 38: '622', 39: '562', 40: '218', 41: '64', 42: '623', 43: '137', 44: '131',
         45: 'E130', 46: '62', 47: '58', 48: '226', 49: '227', 50: '659'},
    86: {1: '626', 3: '303',
         4: 'X:Zadání mísí vznik švédské gymnastiky s atribucí masáže a rozporným datováním',
         5: '676', 6: '306', 7: '308',
         8: 'X:Kontraindikace závisí na konkrétní metodě a druhu implantátu',
         9: '309', 10: '310', 12: '653', 13: '312', 15: '167',
         16: '176', 17: '170', 19: '163', 20: '165', 21: '179', 22: '172',
         23: 'X:Paušální zákaz invazivních metod',
         24: '182', 25: '168', 26: 'E169', 27: 'E173', 28: '627',
         29: '654', 30: 'X:Zadání nestanovuje kritérium nejdůležitějšího předpokladu'},
    90: {1: '171', 2: '156', 5: '305', 6: '307',
         7: 'X:Jednostrannost sportu nemá v zadání definované kritérium',
         10: '311', 11: '653', 13: '312', 14: '313', 15: '314', 16: '315',
         17: '170', 18: '160', 19: '165', 20: '172', 21: '182',
         22: 'X:Zadání vydává jedinou okolnost za příčinu plochonoží',
         23: 'E173', 24: '627', 25: '678', 26: '654', 27: 'E654',
         28: 'X:Zadání nestanovuje kritérium nejdůležitějšího předpokladu', 29: '157'},
    94: {1: '85', 3: '289', 5: 'X:Tekutina není určená a nabídka neobsahuje běžné arteriální pH', 6: '104', 7: '105', 8: '26',
         10: '29', 11: '192', 13: '675', 14: '362', 15: '98', 16: 'E37',
         18: '110', 20: 'E10', 24: '185', 26: 'E95', 27: '599',
         28: '273', 30: '377', 33: 'X:Klíč přisuzuje systolický tlak jedinému faktoru',
         34: '17', 36: '280', 38: '552'},
    99: {1: '66', 2: '68', 4: '562', 6: '656', 8: '131', 10: '251',
         11: '249', 12: '250', 13: '614', 14: '227', 17: '630', 18: '615',
         19: '58', 20: '59', 21: '655', 22: '63',
         23: 'X:Historický výčet síťových služeb', 24: '142', 25: '631',
         26: '83', 27: '50', 28: '153', 30: '150'},
    103: {1: '85', 2: '10', 4: '662', 5: '295', 7: '338',
          8: 'X:Klíč přisuzuje systolický tlak jedinému faktoru',
          9: '98', 12: '629', 14: 'X:Zařazení horních dýchacích cest je v nabídce nejednoznačné',
          17: '669', 18: '635', 20: 'E31', 21: '594', 22: '38', 23: '275',
          26: '185', 27: 'E263', 29: '285', 30: 'E261', 32: '172',
          33: '45', 36: '11', 41: 'E103', 44: '354',
          46: 'X:Průměrný tep závisí na podmínkách měření', 47: '666'},
    109: {1: '73', 2: '66', 3: '68', 4: '67', 6: '71',
          7: 'X:Původní formulace neuvádí všechny zákonné podmínky',
          8: 'X:Rozdělení disciplín závisí na zvolené klasifikaci filozofie',
          9: '656', 10: '346', 12: '347', 13: '251', 14: '250',
          15: '226', 16: '348', 17: '618', 18: '632', 19: '82',
          21: '615', 22: '633', 23: '634', 24: '619', 25: '57',
          26: '221', 27: '62', 28: '64', 29: 'X:Historický výčet síťových služeb',
          32: 'X:Zadání závisí na roce, místě a dostupné síti',
          34: '631', 35: '48', 36: '217', 37: '50', 38: '49',
          39: '53', 41: '153', 46: '231', 50: '150'},
    115: {1: '85', 2: '10', 3: '662', 4: '295', 5: '354', 6: '338',
          7: 'X:Klíč zjednodušuje systolický tlak na jediný faktor',
          8: '98', 9: '355', 10: '356', 11: '629', 12: 'X:Nabídka směšuje stavbu sklípků s nepřesným označením pleury',
          13: '358', 14: '669', 15: 'X:Klíč zaměňuje tvrdost skloviny a stavbu celého zubu', 16: 'E31', 17: '594',
          18: '38', 19: '275', 20: '364', 21: '365', 22: '285',
          23: 'E261', 24: '366', 25: '45', 26: '367', 27: '11',
          28: '369', 29: '371', 30: '372', 31: 'E103', 32: '373',
          33: '374', 34: '354', 35: '375',
          36: 'X:Průměrný tep závisí na podmínkách měření',
          37: '666', 38: '376', 39: '377', 40: '378'},
    120: {1: '66', 2: '67', 3: 'X:Historické znění právní otázky',
          4: '656', 5: '346', 6: '380', 7: '347', 8: '251', 9: '250',
          10: '226', 11: '348', 12: '82', 13: '615', 14: '619', 15: '57',
          16: '221', 17: '62', 18: '64', 19: 'X:Historický výčet síťových služeb',
          20: '382', 21: '384', 22: '631',
          23: '217', 24: '50', 25: '49', 26: '385'},
    123: {2: '85', 3: '657', 4: '105', 5: '264', 6: '357',
          7: '192', 8: 'E359', 10: 'E25', 13: '162', 15: '363',
          16: 'E45', 18: '43', 19: '607', 20: '172', 21: '335',
          22: '292', 23: '372', 24: '185', 25: '273', 26: '374',
          27: 'X:Průměrný tep závisí na podmínkách měření',
          28: '47', 29: '46', 30: '41', 31: '38', 32: 'E37',
          34: '635', 35: '183',
          36: 'X:Zařazení horních dýchacích cest je v nabídce nejednoznačné',
          37: '21', 38: '254', 39: '280'},
    128: {2: '238', 3: '345', 4: '656', 6: '562', 7: '58', 8: '655',
          9: '225', 10: 'X:Historický výčet síťových služeb', 11: '382',
          12: '631', 13: '630', 14: '83',
          15: 'X:Původní možnosti nezohledňují novější právní úpravu práce mladistvých',
          16: '48', 18: '50', 21: '56', 22: '50', 23: '59', 24: '221',
          25: '63', 26: '65', 27: '66', 28: '68',
          29: '677', 30: '78'},
    132: {1: '2', 2: '3', 3: '4', 4: '393', 5: '5', 6: '7',
          7: '85', 8: '10', 9: '11',
          11: 'X:Výrok o genetickém materiálu všech buněk má výjimky například u zralých erytrocytů',
          12: '102', 13: '13', 15: '14', 16: '15', 17: '16', 18: '657',
          19: '105', 20: '17', 21: '280',
          22: 'X:Přesný počet ovariálních hormonů závisí na jeho vymezení', 23: '19', 24: '254',
          25: 'X:Volně vymezený pojem fyziologický porod nelze ztotožnit jen s týdnem těhotenství',
          26: '21', 27: '22', 28: '264',
          29: 'X:Více uvedených úseků střeva má imunitní funkce',
          30: '24', 31: '25', 32: '26', 34: '27', 35: '28', 36: '357',
          37: '29', 38: '192', 39: 'X:Zařazení horních dýchacích cest je v nabídce nejednoznačné',
          40: '30', 41: '669', 43: '32', 44: 'E25', 45: '33',
          46: '395', 47: '35', 48: '396', 49: '399', 50: 'E37'},
    138: {1: '238', 2: '66', 3: '78', 4: '68', 6: '344', 7: '71',
          8: '562', 9: 'X:Původní formulace neuvádí všechny zákonné podmínky',
          10: 'X:Rozdělení disciplín závisí na zvolené klasifikaci filozofie',
          11: '656', 12: '346', 13: '131', 14: '380', 15: '347', 17: '251',
          18: '249', 19: '250', 20: '614', 21: '226', 22: '227', 23: '348', 24: '349',
          25: 'X:Zadání nerozlišuje typ odpovědnosti a zákonné podmínky',
          26: '630', 27: '615', 28: '640', 29: '641', 30: '58', 31: '57',
          32: '655', 33: '62', 34: '63', 35: '392', 36: '631', 37: '83',
          38: '48', 39: '217', 40: '50', 41: '49', 42: '51', 43: '153',
          44: '350', 45: '386', 48: '647', 49: '231', 50: '150'},
    223: {3: '27', 4: '177', 7: '251', 9: '51', 11: '163',
          16: '642', 18: '239', 19: '624', 21: '77', 22: '238', 26: '167',
          27: '59', 29: '61', 33: '150', 34: '647', 35: '643', 37: '75',
          38: '603', 40: '386',
          41: 'X:Rozdělení disciplín závisí na zvolené klasifikaci filozofie',
          44: '644', 45: '645', 48: '646', 49: '677',
          50: 'X:Největší autorita nemá objektivní kritérium'},
    235: {1: '401', 2: '238', 3: '74', 4: '66', 5: '78', 6: '68', 8: '67',
          9: '410', 10: '379', 11: '344', 12: '71', 13: '562',
          14: 'X:Původní formulace neuvádí všechny zákonné podmínky', 15: '72',
          16: 'X:Rozdělení disciplín závisí na zvolené klasifikaci filozofie',
          17: '345', 18: '656', 20: '346', 21: '131', 22: '380', 24: '347',
          25: '411', 26: '251', 27: '249', 28: '250', 29: '614', 30: '226',
          31: '227', 32: '348', 35: '349', 36: '81',
          37: 'X:Zadání nerozlišuje typ odpovědnosti a zákonné podmínky',
          38: '82', 39: '630', 40: '381', 41: '650', 42: '615', 43: '640',
          44: '633', 45: '651', 46: '634', 47: '624', 48: '641', 49: '58',
          50: '57', 51: '59', 52: '221', 53: '655', 54: '62', 55: '63',
          56: '64', 57: '225', 58: 'X:Historický výčet síťových služeb',
          59: '659', 60: '382', 62: '383', 63: '142',
          64: 'X:Zadání závisí na roce, místě a dostupné síti', 65: '352',
          66: '384', 67: '674', 68: '631', 69: '83', 70: '48', 71: '50',
          72: '217', 73: '405', 74: '50', 75: '60', 76: '49', 77: '51',
          78: '53', 80: '385', 82: '153', 83: '350', 84: '386',
          86: '387', 87: '412', 88: '388', 89: '413', 90: '389',
          91: '647', 92: '231', 94: '390', 95: '652', 96: '391',
          98: '392', 100: '150'},
    264: {1: 'X:Více problémových tvrzení v nabídce', 2: '361', 3: '598',
          4: 'E106', 5: '670', 6: '38', 7: '25',
          8: 'X:Průměrný klidový tep není jedna univerzální hodnota',
          9: '40', 10: '397', 12: '394', 13: '273', 14: '85',
          16: '332', 17: '88', 19: '372', 20: '666', 23: '108', 24: '196',
          27: '282', 28: 'X:Počet cyklů závisí na řadě individuálních faktorů',
          30: 'X:Vitální kapacita závisí mimo jiné na tělesné výšce a věku', 33: '255', 34: '657',
          35: '200', 36: '594', 37: '661', 38: '173', 39: '460', 40: 'E599'},
    270: {41: '109', 42: '514', 43: '595', 44: '628',
          45: 'X:Nabídka zaměňuje původ čočky a dalších struktur oka', 46: '26',
          47: '596', 48: '291', 49: '597', 50: 'E114'},
}


def original_map(path, label):
    rows = [row for row in path.read_text(encoding='utf-8').splitlines() if row.startswith(label)]
    assert len(rows) == 1, label
    row = rows[0]
    return row.split(':** ', 1)[1].split(' · ') if row.startswith('-') else row.split('|')[3].strip().split(' · ')


def parse_status(cell):
    if cell is None:
        return 'nepotvrzeno', '', 'Přiřazení ani absence zatím nejsou doložené.'
    if cell.startswith('X:'):
        return 'vyřazeno', '', cell[2:]
    if cell.startswith('P'):
        return 'částečně', cell[1:], ''
    if cell.startswith('E'):
        return 've vysvětlení', cell[1:], ''
    return 'přiřazeno', cell, ''


def main():
    bank = [
        q for path in sorted(WORK.glob('budejovice-*.json'))
        for q in json.loads(path.read_text(encoding='utf-8'))
    ]
    valid_ids = {q['id'] for q in bank}
    counts = {start: count for start, count, _ in BLOCKS}
    mappings = {start: {} for start in counts}
    for question in bank:
        ident = question['id']
        if not (84 <= ident <= 462 or ident in (551, 552, 553) or 594 <= ident <= 599 or 621 <= ident <= 678 or ident == 683):
            continue
        ref = question['bookRef']
        page = int(re.search(r'PDF\s+(\d+)', ref)[1])
        match = re.search(r'úloha\s+(\d+)|(?:Biologie|informovanost|Motivační test)(?: v\d)?\s+(\d+)\s*·\s*str\.', ref)
        if match is None:
            continue
        number = int(match[1] or match[2])
        start = max(start for start in counts if start <= page)
        assert 1 <= number <= counts[start], (ident, ref)
        mappings[start][number] = str(ident)
    archive = WORK / 'BUDEJOVICE-MAPA-ZADANI-6393.md'
    originals = WORK / 'BUDEJOVICE-MAPA-PUVODNI-PDF.md'
    for start, label in {181: '| 31 |', 199: '| 01 |'}.items():
        cells = original_map(archive, label)
        assert len(cells) == counts[start]
        mappings[start].update(enumerate(cells, 1))
    for start, label in {144: '- **PDF 1–6, biologie', 150: '- **PDF 7–12, všeobecná'}.items():
        cells = original_map(originals, label)
        assert len(cells) == counts[start]
        mappings[start].update(enumerate(cells, 1))
    for start, entries in REVIEWED.items():
        mappings[start].update(entries)
    for number in range(1, 41):
        if number in mappings[264]:
            mappings[270][number] = mappings[264][number]
    stats = Counter()
    with (WORK / 'BUDEJOVICE-2019-2022-ULOHY.csv').open('w', encoding='utf-8-sig', newline='') as stream:
        writer = csv.writer(stream, delimiter=';')
        writer.writerow(['PDF od', 'PDF do', 'Sada', 'Původní úloha', 'Stav', 'ID v kvízu', 'Podklad'])
        for i, (start, count, title) in enumerate(BLOCKS):
            end = BLOCKS[i + 1][0] - 1 if i + 1 < len(BLOCKS) else 275
            end = {150: 155, 264: 268}.get(start, end)
            reference = COPIES.get(start, start)
            for number in range(1, count + 1):
                cell = mappings[reference].get(number)
                status, ident, note = parse_status(cell)
                if ident:
                    assert int(ident) in valid_ids
                if reference != start and status != 'nepotvrzeno':
                    note = f'Stejné číslování jako PDF {reference}. {note}'.strip()
                elif start == 270 and number <= 40 and status != 'nepotvrzeno':
                    note = f'Stejné číslování jako PDF 264. {note}'.strip()
                stats[status] += 1
                writer.writerow([start, end, title, number, status, ident, note])
    assert sum(stats.values()) == sum(counts.values())
    print(dict(stats))


if __name__ == '__main__':
    main()
