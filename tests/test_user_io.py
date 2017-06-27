﻿#!/usr/bin/python
# -*- coding: utf-8 -*-

"""tests for user_io.py"""

import unittest
import mock
import sys
# noinspection PyCompatibility
from StringIO import StringIO  # module not existent in python 3
import test_frame
import user_io
    
    
class TestGeneralOutput(unittest.TestCase):

    def test_normaltext(self):
        out = StringIO()
        sys.stdout = out                  # capture print output in out
        user_io.general_output("hello")   # fill out
        output = out.getvalue().strip()   # save value of out in output
        self.assertEqual(output, "hello")
        
    def test_textwithcapitalsandnumbers(self):
        out = StringIO()
        sys.stdout = out                  # capture print output in out
        user_io.general_output("hEllo2")  # fill out
        output = out.getvalue().strip()   # save value of out in output
        self.assertEqual(output, "hEllo2")
        
    def test_umlauts(self):
        out = StringIO()
        sys.stdout = out                                       # capture print output in out
        user_io.general_output(u"m{}rchen".format(u"\u00E4"))  # fill out
        output = out.getvalue().strip()                        # save value of out in output
        self.assertEqual(output, u"m{}rchen".format(u"\u00E4"))
        
    def test_replacable_signs(self):
        out = StringIO()
        sys.stdout = out                                        # capture print output in out
        user_io.general_output(u"hello {}".format(u"\u263a"))   # fill out
        output = out.getvalue().strip()                         # save value of out in output
        self.assertEqual(output, "hello :-)")
        
    def test_unknown_signs(self):
        out = StringIO()
        sys.stdout = out                                                    # capture print output in out
        user_io.general_output(u"Flag Turkey: {}".format(u"\u262a"))        # fill out
        output = out.getvalue().strip()                                     # save value of out in output
        self.assertEqual(output, u"Flag Turkey: {}".format(u"\u001a"))
  
        
class TestGeneralInput(unittest.TestCase):   

    def test_normaltext(self):
        with mock.patch('__builtin__.raw_input', return_value="hello"):
            self.assertEqual(user_io.general_input(">> "), 'hello')
        
    def test_textwithcapitalsandnumbers(self):
        with mock.patch('__builtin__.raw_input', return_value="hEllo2"):
            self.assertEqual(user_io.general_input(">> "), 'hEllo2')
        
    def test_replacable_signs(self):
        with mock.patch('__builtin__.raw_input', return_value=u"hello {}".format(u"\u263a")): 
            self.assertEqual(user_io.general_input(">> "), u"hello {}".format(u"\u263a"))
        
    def test_umlauts(self):
        with mock.patch('__builtin__.raw_input', return_value=u"m{}rchen".format(u"\u00E4")):
            self.assertEqual(user_io.general_input(">> "), u"m{}rchen".format(u"\u00E4"))
        
    def test_unknown_signs(self):
        with mock.patch('__builtin__.raw_input', return_value=u"Flag Turkey: {}".format(u"\u262a")):
            self.assertEqual(user_io.general_input(">> "), u"Flag Turkey: {}".format(u"\u262a"))
        
    def test_number(self):
        with mock.patch('__builtin__.raw_input', return_value="42"):
            self.assertEqual(user_io.general_input(">> "), "42")
  
        
class TestInputDecode(unittest.TestCase):   

    def test_normaltext(self):
        with mock.patch('__builtin__.raw_input', return_value="hello"):
            self.assertEqual(user_io.input_decode(">> "), 'hello')
        
    def test_textwithcapitalsandnumbers(self):
        with mock.patch('__builtin__.raw_input', return_value="hEllo2"):
            self.assertEqual(user_io.input_decode(">> "), 'hEllo2')
        
    def test_replacable_signs(self):
        with mock.patch('__builtin__.raw_input', return_value=u"hello {}".format(u"\u263a")):
            self.assertRaises(UnicodeEncodeError, user_io.input_decode, ">> ")
        
    def test_umlaute(self):
        with mock.patch('__builtin__.raw_input', return_value='M\xe4rchen'):
            self.assertEqual(user_io.input_decode(">> "), u"Märchen")
        
    def test_unknown_signs(self):
        with mock.patch('__builtin__.raw_input', return_value=u"Flag Turkey: {}".format(u"\u262a")):
            self.assertRaises(UnicodeEncodeError, user_io.input_decode, ">> ")
        
    def test_number(self):
        with mock.patch('__builtin__.raw_input', return_value="42"):
            self.assertEqual(user_io.input_decode(">> "), "42")
 
        
class TestShowMainMenu(unittest.TestCase):
    
    def test_nofoundexists(self):
        out = StringIO()
        sys.stdout = out                  # capture print output in out
        user_io.show_main_menu(False)     # fill out
        output = out.getvalue().strip()   # save value of out in output
        expected_output = "Was moechtest du als naechstes tun?\n"
        expected_output += "1: Geocaches aktualisieren\n"
        expected_output += "2: Alle auf dem Geraet gespeicherten Geocaches sortieren und anzeigen\n"
        expected_output += "3: Alle auf dem Geraet gespeicherten Geocaches auf Karte zeigen (INTERNET!!!)\n"
        expected_output += "4: Beschreibung fuer einen bestimmten Cache anzeigen (GC-Code erforderlich)\n"
        expected_output += "5: Geocaches durchsuchen\n" 
        expected_output += "6: https://www.geocaching.com/map aufrufen (INTERNET!!!)\n"
        expected_output += "7: https://www.google.de/maps aufrufen (INTERNET!!!)\n"
        expected_output += "8: Programm verlassen"
        self.assertEqual(output, expected_output)
        
    def test_foundexists(self):
        out = StringIO()
        sys.stdout = out                  # capture print output in out
        user_io.show_main_menu(True)      # fill out
        output = out.getvalue().strip()   # save value of out in output
        expected_output = "Was moechtest du als naechstes tun?\n"
        expected_output += "1: Geocaches aktualisieren\n"
        expected_output += "2: Alle auf dem Geraet gespeicherten Geocaches sortieren und anzeigen\n"
        expected_output += "3: Alle auf dem Geraet gespeicherten Geocaches auf Karte zeigen (INTERNET!!!)\n"
        expected_output += "4: Beschreibung fuer einen bestimmten Cache anzeigen (GC-Code erforderlich)\n"
        expected_output += "5: Geocaches durchsuchen\n" 
        expected_output += "6: Alle gefundenen Caches anzeigen\n"
        expected_output += "7: https://www.geocaching.com/map aufrufen (INTERNET!!!)\n"
        expected_output += "8: https://www.google.de/maps aufrufen (INTERNET!!!)\n"
        expected_output += "9: Programm verlassen"
        self.assertEqual(output, expected_output)
   
        
class TestMainMenu(unittest.TestCase):

    def test_1_nofoundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="1"):
            self.assertEqual(user_io.main_menu(False), 'update')
        
    def test_2_nofoundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="2"):
            self.assertEqual(user_io.main_menu(False), 'show_all')
        
    def test_3_nofoundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="3"):
            self.assertEqual(user_io.main_menu(False), 'show_all_on_map')
            
    def test_4_nofoundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="4"):
            self.assertEqual(user_io.main_menu(False), 'show_one')
        
    def test_5_nofoundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="5"):
            self.assertEqual(user_io.main_menu(False), 'search')
        
    def test_6_nofoundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="6"):
            self.assertEqual(user_io.main_menu(False), 'gc-maps')
        
    def test_7_nofoundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="7"):
            self.assertEqual(user_io.main_menu(False), 'google-maps')
        
    def test_8_nofoundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="8"):
            self.assertEqual(user_io.main_menu(False), 'exit')
        
    def test_9_nofoundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="9"):
            self.assertEqual(user_io.main_menu(False), None)
        
    def test_1_foundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="1"):
            self.assertEqual(user_io.main_menu(True), 'update')
        
    def test_2_foundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="2"):
            self.assertEqual(user_io.main_menu(True), 'show_all')
        
    def test_3_foundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="3"):
            self.assertEqual(user_io.main_menu(True), 'show_all_on_map')
            
    def test_4_foundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="4"):
            self.assertEqual(user_io.main_menu(True), 'show_one')
        
    def test_5_foundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="5"):
            self.assertEqual(user_io.main_menu(True), 'search')
        
    def test_6_foundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="6"):
            self.assertEqual(user_io.main_menu(True), 'show_founds')
        
    def test_7_foundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="7"):
            self.assertEqual(user_io.main_menu(True), 'gc-maps')
        
    def test_8_foundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="8"):
            self.assertEqual(user_io.main_menu(True), 'google-maps')
        
    def test_9_foundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="9"):
            self.assertEqual(user_io.main_menu(True), 'exit')
        
        
class TestSortCaches(unittest.TestCase):

    def test_gccode(self):
        with mock.patch('__builtin__.raw_input', side_effect=['1', '1']):  
            self.assertEqual(user_io.sort_caches(), ["gccode", False])
        
    def test_name(self):
        with mock.patch('__builtin__.raw_input', side_effect=['2', '1']): 
            self.assertEqual(user_io.sort_caches(), ["name", False])

    def test_type(self):
        with mock.patch('__builtin__.raw_input', side_effect=['3', '1']): 
            self.assertEqual(user_io.sort_caches(), ["type", False])
        
    def test_difficulty(self):
        with mock.patch('__builtin__.raw_input', side_effect=['4', '1']): 
            self.assertEqual(user_io.sort_caches(), ["difficulty", False])
        
    def test_terrain(self):
        with mock.patch('__builtin__.raw_input', side_effect=['5', '1']): 
            self.assertEqual(user_io.sort_caches(), ["terrain", False])
        
    def test_size(self):
        with mock.patch('__builtin__.raw_input', side_effect=['6', '1']): 
            self.assertEqual(user_io.sort_caches(), ["size", False])
        
    def test_downloaddate(self):
        with mock.patch('__builtin__.raw_input', side_effect=['7', '1']): 
            self.assertEqual(user_io.sort_caches(), ["downloaddate", False])
        
    def test_available(self):
        with mock.patch('__builtin__.raw_input', side_effect=['8', '1']): 
            self.assertEqual(user_io.sort_caches(), ["available", False])
        
    def test_distance(self):
        with mock.patch('__builtin__.raw_input', side_effect=['9', '1']): 
            self.assertEqual(user_io.sort_caches(), ["distance", False])
            
    def test_gccode_backwards(self):
        with mock.patch('__builtin__.raw_input', side_effect=['1', '2']):  
            self.assertEqual(user_io.sort_caches(), ["gccode", True])
        
    def test_name_backwards(self):
        with mock.patch('__builtin__.raw_input', side_effect=['2', '2']): 
            self.assertEqual(user_io.sort_caches(), ["name", True])

    def test_type_backwards(self):
        with mock.patch('__builtin__.raw_input', side_effect=['3', '2']): 
            self.assertEqual(user_io.sort_caches(), ["type", True])
        
    def test_difficulty_backwards(self):
        with mock.patch('__builtin__.raw_input', side_effect=['4', '2']): 
            self.assertEqual(user_io.sort_caches(), ["difficulty", True])
        
    def test_terrain_backwards(self):
        with mock.patch('__builtin__.raw_input', side_effect=['5', '2']): 
            self.assertEqual(user_io.sort_caches(), ["terrain", True])
        
    def test_size_backwards(self):
        with mock.patch('__builtin__.raw_input', side_effect=['6', '2']): 
            self.assertEqual(user_io.sort_caches(), ["size", True])
        
    def test_downloaddate_backwards(self):
        with mock.patch('__builtin__.raw_input', side_effect=['7', '2']): 
            self.assertEqual(user_io.sort_caches(), ["downloaddate", True])
        
    def test_available_backwards(self):
        with mock.patch('__builtin__.raw_input', side_effect=['8', '2']): 
            self.assertEqual(user_io.sort_caches(), ["available", True])
        
    def test_distance_backwards(self):
        with mock.patch('__builtin__.raw_input', side_effect=['9', '2']): 
            self.assertEqual(user_io.sort_caches(), ["distance", True])
            
    def test_criterion0(self):
        with mock.patch('__builtin__.raw_input', side_effect=['0', '2']): 
            self.assertEqual(user_io.sort_caches(), ["gccode", True])
            
    def test_criterion_invalid(self):
        with mock.patch('__builtin__.raw_input', side_effect=['bla', '1']): 
            self.assertEqual(user_io.sort_caches(), ["gccode", False])
            
    def test_revert_invalid(self):
        with mock.patch('__builtin__.raw_input', side_effect=['1', '0']): 
            self.assertEqual(user_io.sort_caches(), ["gccode", False])
            
    def test_output_normal(self):
        with mock.patch('__builtin__.raw_input', side_effect=['3', '2']):
            out = StringIO()
            sys.stdout = out                   
            user_io.sort_caches()
            output = out.getvalue().strip() 
            expected_output = "Wonach sollen die Geocaches sortiert werden?\n"
            expected_output += "1: GC-Code\n"
            expected_output += "2: Name\n"
            expected_output += "3: Cache-Typ\n"
            expected_output += "4: D-Wertung\n"
            expected_output += "5: T-Wertung\n"
            expected_output += "6: Groesse\n"
            expected_output += "7: Download-Datum\n"
            expected_output += "8: Verfuegbarkeit\n"
            expected_output += "9: Abstand von einer bestimmten Position (Koordinaten erforderlich)\n"   
            expected_output += "In welche Richtung sollen die Caches sortiert werden?\n"
            expected_output += "1: aufsteigend\n"
            expected_output += "2: absteigend"            
            self.assertEqual(output, expected_output)
            
    def test_output_criterion_invalid(self):
        with mock.patch('__builtin__.raw_input', side_effect=['0', '2']):
            out = StringIO()
            sys.stdout = out                   
            user_io.sort_caches()
            output = out.getvalue().strip() 
            expected_output = "Wonach sollen die Geocaches sortiert werden?\n"
            expected_output += "1: GC-Code\n"
            expected_output += "2: Name\n"
            expected_output += "3: Cache-Typ\n"
            expected_output += "4: D-Wertung\n"
            expected_output += "5: T-Wertung\n"
            expected_output += "6: Groesse\n"
            expected_output += "7: Download-Datum\n"
            expected_output += "8: Verfuegbarkeit\n"
            expected_output += "9: Abstand von einer bestimmten Position (Koordinaten erforderlich)\n"   
            expected_output += "Ungueltige Eingabe: Sortierung erfolgt nach GC-Code\n" 
            expected_output += "In welche Richtung sollen die Caches sortiert werden?\n"
            expected_output += "1: aufsteigend\n"
            expected_output += "2: absteigend"             
            self.assertEqual(output, expected_output)
 
                  
class TestSearch(unittest.TestCase):

    def test_name(self):
        with mock.patch('__builtin__.raw_input', return_value="1"):  
            self.assertEqual(user_io.search(), "name")
            
    def test_description(self):
        with mock.patch('__builtin__.raw_input', return_value="2"):  
            self.assertEqual(user_io.search(), "description")
            
    def test_type(self):
        with mock.patch('__builtin__.raw_input', return_value="3"):  
            self.assertEqual(user_io.search(), "type")
            
    def test_difficulty(self):
        with mock.patch('__builtin__.raw_input', return_value="4"):  
            self.assertEqual(user_io.search(), "difficulty")
            
    def test_terrain(self):
        with mock.patch('__builtin__.raw_input', return_value="5"):  
            self.assertEqual(user_io.search(), "terrain")
            
    def test_size(self):
        with mock.patch('__builtin__.raw_input', return_value="6"):  
            self.assertEqual(user_io.search(), "size")
            
    def test_downloaddate(self):
        with mock.patch('__builtin__.raw_input', return_value="7"):  
            self.assertEqual(user_io.search(), "downloaddate")
            
    def test_available(self):
        with mock.patch('__builtin__.raw_input', return_value="8"):  
            self.assertEqual(user_io.search(), "available")
            
    def test_attribute(self):
        with mock.patch('__builtin__.raw_input', return_value="9"):  
            self.assertEqual(user_io.search(), "attribute")
            
    def test_distance(self):
        with mock.patch('__builtin__.raw_input', return_value="10"):  
            self.assertEqual(user_io.search(), "distance")
            
    def test_0(self):
        with mock.patch('__builtin__.raw_input', return_value="0"): 
            self.assertEqual(user_io.search(), None)
            
    def test_invalid(self):
        with mock.patch('__builtin__.raw_input', return_value="bla"): 
            self.assertEqual(user_io.search(), None)
            
    def test_output_normal(self):
        with mock.patch('__builtin__.raw_input', return_value="2"):
            out = StringIO()
            sys.stdout = out                   
            user_io.search()
            output = out.getvalue().strip() 
            expected_output = "Wonach willst du suchen?\n"
            expected_output += "1: Name\n"
            expected_output += "2: Beschreibung\n"
            expected_output += "3: Cache-Typ\n"
            expected_output += "4: D-Wertung\n"
            expected_output += "5: T-Wertung\n"
            expected_output += "6: Groesse\n"
            expected_output += "7: Download-Datum\n"
            expected_output += "8: Verfuegbarkeit\n"
            expected_output += "9: Attribut\n"
            expected_output += "10: Abstand von einer bestimmten Position (Koordinaten erforderlich)"    
            self.assertEqual(output, expected_output)
            
    def test_output_invalid(self):
        with mock.patch('__builtin__.raw_input', return_value="bla"):
            out = StringIO()
            sys.stdout = out                   
            user_io.search()
            output = out.getvalue().strip() 
            expected_output = "Wonach willst du suchen?\n"
            expected_output += "1: Name\n"
            expected_output += "2: Beschreibung\n"
            expected_output += "3: Cache-Typ\n"
            expected_output += "4: D-Wertung\n"
            expected_output += "5: T-Wertung\n"
            expected_output += "6: Groesse\n"
            expected_output += "7: Download-Datum\n"
            expected_output += "8: Verfuegbarkeit\n"
            expected_output += "9: Attribut\n"
            expected_output += "10: Abstand von einer bestimmten Position (Koordinaten erforderlich)\n"  
            expected_output += "Ungueltige Eingabe"            
            self.assertEqual(output, expected_output)
      
            
class TestSearchType(unittest.TestCase):
    
    def test_return(self):
        with mock.patch('__builtin__.raw_input', return_value="Traditional Cache"): 
            self.assertEqual(user_io.search_type(), "Traditional Cache")
            
    def test_output(self):
        with mock.patch('__builtin__.raw_input', return_value="any_nonsense"):
            out = StringIO()
            sys.stdout = out                 
            user_io.search_type()
            output = out.getvalue().strip()  
            expected_output = "Gib den Cachetyp ein, nach dem du suchen willst.\n"
            expected_output += "Moegliche Typen: Traditional Cache, Multi-cache, Mystery Cache, EarthCache, "
            expected_output += "Letterbox Hybrid, Event Cache, Wherigo Cache, Geocaching HQ, Unknown Type\n"
            expected_output += "Achtung! Gross- und Kleinschreibung beachten!"
            self.assertEqual(output, expected_output)
            
            
class TestSearchAttribute(unittest.TestCase):
    
    def test_return(self):
        with mock.patch('__builtin__.raw_input', return_value="does not need to be an attr"): 
            self.assertEqual(user_io.search_attribute(["attr1", "attr2"]), "does not need to be an attr")
            
    def test_output(self):
        with mock.patch('__builtin__.raw_input', return_value="any_nonsense"):
            out = StringIO()
            sys.stdout = out                 
            user_io.search_attribute(["attr1", "attr2"])
            output = out.getvalue().strip()  
            expected_output = "Gib das Attribut ein, nach dem du suchen willst.\n"
            expected_output += "Moegliche Attribute: attr1, attr2" 
            self.assertEqual(output, expected_output)
 
            
class TestActionsAfterSearch(unittest.TestCase):

    def test_1(self):
        with mock.patch('__builtin__.raw_input', return_value="1"):
            self.assertEqual(user_io.actions_after_search(), "show_again")
            
    def test_2(self):
        with mock.patch('__builtin__.raw_input', return_value="2"):
            self.assertEqual(user_io.actions_after_search(), "delete")
            
    def test_3(self):
        with mock.patch('__builtin__.raw_input', return_value="3"):
            self.assertEqual(user_io.actions_after_search(), "show_on_map")
            
    def test_4(self):
        with mock.patch('__builtin__.raw_input', return_value="4"):
            self.assertEqual(user_io.actions_after_search(), "show_one")
            
    def test_5(self):
        with mock.patch('__builtin__.raw_input', return_value="5"):
            self.assertEqual(user_io.actions_after_search(), "back")
            
    def test_other(self):
        with mock.patch('__builtin__.raw_input', return_value="0"):
            self.assertEqual(user_io.actions_after_search(), None)
            
    def test_output(self):
        with mock.patch('__builtin__.raw_input', return_value="1"):
            out = StringIO()
            sys.stdout = out                 
            user_io.actions_after_search()
            output = out.getvalue().strip()  
            expected_output = "Was moechtest du als naechstes tun?\n"
            expected_output += "1: Alle Suchergebnisse erneut anzeigen (bei evtl. Loeschen nicht aktualisiert)\n" 
            expected_output += "2: Alle Suchergebnisse loeschen\n"
            expected_output += "3: Alle Suchergebnisse auf Karte zeigen (INTERNET!!!)\n"
            expected_output += "4: Beschreibung fuer eines der Suchergebnisse anzeigen\n"
            expected_output += "5: zurueck"
            self.assertEqual(output, expected_output)
            
    def test_output_invalid_input(self):
        with mock.patch('__builtin__.raw_input', return_value="bla"):
            out = StringIO()
            sys.stdout = out                 
            user_io.actions_after_search()
            output = out.getvalue().strip()  
            expected_output = "Was moechtest du als naechstes tun?\n"
            expected_output += "1: Alle Suchergebnisse erneut anzeigen (bei evtl. Loeschen nicht aktualisiert)\n" 
            expected_output += "2: Alle Suchergebnisse loeschen\n"
            expected_output += "3: Alle Suchergebnisse auf Karte zeigen (INTERNET!!!)\n"
            expected_output += "4: Beschreibung fuer eines der Suchergebnisse anzeigen\n"
            expected_output += "5: zurueck\n"
            expected_output += "Ungueltige Eingabe"
            self.assertEqual(output, expected_output)
       
            
class TestActionsWithFounds(unittest.TestCase):

    def test_1(self):
        with mock.patch('__builtin__.raw_input', return_value="1"):
            self.assertEqual(user_io.actions_with_founds(), "log")
            
    def test_2(self):
        with mock.patch('__builtin__.raw_input', return_value="2"):
            self.assertEqual(user_io.actions_with_founds(), "delete")
            
    def test_3(self):
        with mock.patch('__builtin__.raw_input', return_value="3"):
            self.assertEqual(user_io.actions_with_founds(), "exit")
            
    def test_other(self):
        with mock.patch('__builtin__.raw_input', return_value="0"):
            self.assertEqual(user_io.actions_after_search(), None)
            
    def test_output(self):
        with mock.patch('__builtin__.raw_input', return_value="3"):
            out = StringIO()
            sys.stdout = out                 
            user_io.actions_with_founds()
            output = out.getvalue().strip()  
            expected_output = "Was moechtest du als naechstes tun?\n"
            expected_output += "1: Gefundene Caches auf geocaching.com loggen "
            expected_output += "(ueber den Upload von drafts / fieldnotes, INTERNET!!!)\n"
            expected_output += "2: Alle gefundenen Caches loeschen\n"
            expected_output += "3: zurueck"
            self.assertEqual(output, expected_output)
            
            
class TestConfirmDeletion(unittest.TestCase):

    def test_yes(self):
        with mock.patch('__builtin__.raw_input', return_value="y"):
            self.assertEqual(user_io.confirm_deletion(), True)
            
    def test_no(self):
        with mock.patch('__builtin__.raw_input', return_value="n"):
            self.assertEqual(user_io.confirm_deletion(), False)
            
    def test_nonsense(self):
        with mock.patch('__builtin__.raw_input', return_value="any_nonsense"):
            self.assertEqual(user_io.confirm_deletion(), False)


class TestShowOne(unittest.TestCase):

    def test_1(self):
        with mock.patch('__builtin__.raw_input', return_value="1"):
            self.assertEqual(user_io.show_one(), "delete")
            
    def test_2(self):
        with mock.patch('__builtin__.raw_input', return_value="2"):
            self.assertEqual(user_io.show_one(), "gc.com")
            
    def test_3(self):
        with mock.patch('__builtin__.raw_input', return_value="3"):
            self.assertEqual(user_io.show_one(), "dist")
            
    def test_4(self):
        with mock.patch('__builtin__.raw_input', return_value="4"):
            self.assertEqual(user_io.show_one(), "gc-map")
            
    def test_5(self):
        with mock.patch('__builtin__.raw_input', return_value="5"):
            self.assertEqual(user_io.show_one(), "googlemaps")
            
    def test_6(self):
        with mock.patch('__builtin__.raw_input', return_value="6"):
            self.assertEqual(user_io.show_one(), None)
            
    def test_other(self):
        with mock.patch('__builtin__.raw_input', return_value="0"):
            self.assertEqual(user_io.show_one(), None)
            
    def test_output(self):
        with mock.patch('__builtin__.raw_input', return_value="bla"):
            out = StringIO()
            sys.stdout = out                 
            user_io.show_one()
            output = out.getvalue().strip()  
            expected_output = "Was moechtest du als naechstes tun?\n"
            expected_output += "1: diesen Cache loeschen\n" 
            expected_output += "2: diesen Cache auf geocaching.com oeffnen (INTERNET!!!)\n"
            expected_output += "3: Abstand dieses Caches zu einer bestimmten Position berechnen\n"
            expected_output += "4: Position des Caches auf der Karte "
            expected_output += "https://www.geocaching.com/map anzeigen (INTERNET!!!)\n"
            expected_output += "5: Position des Caches auf der Karte https://www.google.de/maps anzeigen (INTERNET!!!)\n"
            expected_output += "6: zurueck"
            self.assertEqual(output, expected_output)


class TestCoordinatesInput(unittest.TestCase):
    
    def test_return(self):
        with mock.patch('__builtin__.raw_input', return_value="X XX\xb0XX.XXX, X XXX\xb0XX.XXX"): 
            self.assertEqual(user_io.coordinates_input(), u"X XX°XX.XXX, X XXX°XX.XXX")
            
    def test_output(self):
        with mock.patch('__builtin__.raw_input', return_value="any_nonsense"):
            out = StringIO()
            sys.stdout = out                 
            user_io.coordinates_input()
            output = out.getvalue().strip()  
            expected_output = u"Gib die Koordinaten ein "
            expected_output += u"(Format: X XX°XX.XXX, X XXX°XX.XXX oder URL (google maps oder geocaching.com/map))"
            self.assertEqual(output, expected_output)     


class TestAskForPath(unittest.TestCase): 

    def test_output(self):
        with mock.patch('__builtin__.raw_input', return_value="any_nonsense"):
            out = StringIO()
            sys.stdout = out                 
            user_io.ask_for_path()
            output = out.getvalue().strip()  
            expected_output = "Gib den Pfad zum GPS-Geraet ein (NICHT zum Unterordner 'GPX').\n"
            expected_output += "Falls Standardpfad 'F:\Garmin' uebernommen werden soll: keine Eingabe"
            self.assertEqual(output, expected_output) 

    def test_return(self):
        with mock.patch('__builtin__.raw_input', return_value="any_path"): 
            self.assertEqual(user_io.ask_for_path(), "any_path")

    def test_default_return(self):
        with mock.patch('__builtin__.raw_input', return_value=""): 
            self.assertEqual(user_io.ask_for_path(), r"F:\Garmin")


class TestShowAllOnMapStart(unittest.TestCase):

    def test_output(self):
        with mock.patch('__builtin__.raw_input', return_value="any_nonsense"):
            out = StringIO()
            sys.stdout = out
            user_io.show_all_on_map_start()
            output = out.getvalue().strip()
            expected_output = "Nach dem Klicken werden sich mehrere Fenster oeffnen. Eines davon ist der Editor, "
            expected_output += "das andere die Seite mapcustomizer.com in deinem Browser.\n"
            expected_output += "Um die Caches auf der Karte anzuzeigen, kopiere den vollstaendigen Inhalt der Textdatei "
            expected_output += "aus deinem Editor in das Feld 'Bulk Entry' im Browser.\n"
            expected_output += "Die Caches werden in folgenden Farben angezeigt:\n"
            expected_output += "Gruen: Traditional Cache\n"
            expected_output += "Rot: Multi-cache\n"
            expected_output += "Blau: Mystery Cache\n"
            expected_output += "Braun: EarthCache\n"
            expected_output += "Grau: Letterbox, Geocaching HQ\n"
            expected_output += "Gelb: Event Cache, Wherigo Cache\n"
            expected_output += "Pink: unbekannter Typ\n"
            expected_output += "Gib nun den Pfad zu deinem Editor an: (bei Benutzung von Windows sollte das unnoetig sein)"
            self.assertEqual(output, expected_output) 
            
    def test_return(self):
        with mock.patch('__builtin__.raw_input', return_value="any_editor"): 
            self.assertEqual(user_io.show_all_on_map_start(), "any_editor")
            
    def test_default_return(self):
        with mock.patch('__builtin__.raw_input', return_value=""): 
            self.assertEqual(user_io.show_all_on_map_start(), "notepad.exe")


class TestShowAllOnMapEnd(unittest.TestCase):

    def test_output(self):
        with mock.patch('__builtin__.raw_input', return_value="any_nonsense"):
            out = StringIO()
            sys.stdout = out
            user_io.show_all_on_map_end()
            output = out.getvalue().strip()
            expected_output = "Schliesse den Editor und druecke Enter."
            self.assertEqual(output, expected_output) 


def create_testsuite():
    """creates a testsuite with out of all tests in this file"""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGeneralOutput))
    suite.addTest(unittest.makeSuite(TestGeneralInput))
    suite.addTest(unittest.makeSuite(TestInputDecode))
    suite.addTest(unittest.makeSuite(TestShowMainMenu))
    suite.addTest(unittest.makeSuite(TestMainMenu))
    suite.addTest(unittest.makeSuite(TestSortCaches))
    suite.addTest(unittest.makeSuite(TestSearch))
    suite.addTest(unittest.makeSuite(TestSearchType))
    suite.addTest(unittest.makeSuite(TestSearchAttribute))
    suite.addTest(unittest.makeSuite(TestActionsAfterSearch))
    suite.addTest(unittest.makeSuite(TestActionsWithFounds))
    suite.addTest(unittest.makeSuite(TestConfirmDeletion))
    suite.addTest(unittest.makeSuite(TestShowOne))
    suite.addTest(unittest.makeSuite(TestCoordinatesInput))
    suite.addTest(unittest.makeSuite(TestAskForPath))
    suite.addTest(unittest.makeSuite(TestShowAllOnMapStart))
    suite.addTest(unittest.makeSuite(TestShowAllOnMapEnd))
    return suite


def main(v):
    """runs the testsuite"""
    return test_frame.run(v, create_testsuite, "user_io.py")

if __name__ == '__main__':
    main(2)
