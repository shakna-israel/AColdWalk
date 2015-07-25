import unittest
import sys
import actions

class ActionsTestSuite(unittest.TestCase):
    """Test the Actions Library"""
    dictIn = {'warmth':100, 'hunger':100,'health':100,'anxiety':100,'friends':0,'status':"TestingStatus",'wood':100,'player':"TestUser", 'event':"none",'stranger':0}

    def test_stokeFire_noWood(self,dictIn=dictIn):
        """Test what happens when a player stokes the fire, and there is no wood"""
        dictIn['wood'] = 0
        results = actions.stoke_fire(dictIn)
        if results['status'] == 'No wood!':
            assert True
        else:
            assert False, "Status was not as expected."

    def test_stokeFire_Wood(self,dictIn=dictIn):
        """Test what happens when a player stokes the fire, and there is wood"""
        results = actions.stoke_fire(dictIn)
        if results['status'] == 'Warm from Stoking Fire':
            assert True
        else:
            assert False, "Status was not as expected."

    def test_stokeFire_valuesWarmthNoFriends(self,dictIn=dictIn):
        """Test what happens to the warmth value when a player stokes the fire, and there is wood, and no friends."""
        dictIn['friends'] = 0
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['warmth']) in range (90,101):
            assert True
        else:
            print("Expected: 91 to 100")
            print("Got: " + str(results['warmth']))
            assert False, "Warmth value was not as expected."

    def test_stokeFire_valuesWarmthOneFriends(self,dictIn=dictIn):
        """Test what happens to the warmth value when a player stokes the fire, and there is wood, and one friends."""
        dictIn['friends'] = 2
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['warmth']) in range (90,111):
            assert True
        else:
            print("Expected: 90 to 110")
            print("Got: " + str(results['warmth']))
            assert False, "Warmth value was not as expected."

    def test_stokeFire_valuesWarmthTwoFriends(self,dictIn=dictIn):
        """Test what happens to the warmth value when a player stokes the fire, and there is wood, and two friends."""
        dictIn['friends'] = 2
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['warmth']) in range (90,121):
            assert True
        else:
            print("Expected: 91 to 120")
            print("Got: " + str(results['warmth']))
            assert False, "Warmth value was not as expected."

    def test_stokeFire_valuesWarmthThreeFriends(self,dictIn=dictIn):
        """Test what happens to the warmth value when a player stokes the fire, and there is wood, and three friends."""
        dictIn['friends'] = 3
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['warmth']) in range (90,131):
            assert True
        else:
            print("Expected: 91 to 130")
            print("Got: " + str(results['warmth']))
            assert False, "Warmth value was not as expected."

    def test_stokeFire_valuesWarmthFourFriends(self,dictIn=dictIn):
        """Test what happens to the warmth value when a player stokes the fire, and there is wood, and four friends."""
        dictIn['friends'] = 4
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['warmth']) in range (90,141):
            assert True
        else:
            print("Expected: 91 to 140")
            print("Got: " + str(results['warmth']))
            assert False, "Warmth value was not as expected."

    def test_stokeFire_valuesWarmthFiveFriends(self,dictIn=dictIn):
        """Test what happens to the warmth value when a player stokes the fire, and there is wood, and five friends."""
        dictIn['friends'] = 5
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['warmth']) in range (90,151):
            assert True
        else:
            print("Expected: 91 to 150")
            print("Got: " + str(results['warmth']))
            assert False, "Warmth value was not as expected."

    def test_stokeFire_valuesWarmthSixFriends(self,dictIn=dictIn):
        """Test what happens to the warmth value when a player stokes the fire, and there is wood, and six friends."""
        dictIn['friends'] = 6
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['warmth']) in range (90,131):
            assert True
        else:
            print("Expected: 91 to 130")
            print("Got: " + str(results['warmth']))
            assert False, "Warmth value was not as expected."

    def test_stokeFire_valuesWarmthSevenFriends(self,dictIn=dictIn):
        """Test what happens to the warmth value when a player stokes the fire, and there is wood, and seven friends."""
        dictIn['friends'] = 7
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['warmth']) in range (90,146):
            assert True
        else:
            print("Expected: 91 to 145")
            print("Got: " + str(results['warmth']))
            assert False, "Warmth value was not as expected."

    def test_stokeFire_valuesWarmthEightFriends(self,dictIn=dictIn):
        """Test what happens to the warmth value when a player stokes the fire, and there is wood, and eight friends."""
        dictIn['friends'] = 8
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['warmth']) in range (90,141):
            assert True
        else:
            print("Expected: 91 to 140")
            print("Got: " + str(results['warmth']))
            assert False, "Warmth value was not as expected."

    def test_stokeFire_valuesWarmthNineFriends(self,dictIn=dictIn):
        """Test what happens to the warmth value when a player stokes the fire, and there is wood, and nine friends."""
        dictIn['friends'] = 9
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['warmth']) in range (90,141):
            assert True
        else:
            print("Expected: 91 to 140")
            print("Got: " + str(results['warmth']))
            assert False, "Warmth value was not as expected."
