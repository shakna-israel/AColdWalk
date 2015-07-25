import unittest
import sys
import actions

class ActionsTestSuite(unittest.TestCase):
    """Test the Actions Library"""
    dictIn = {'warmth':100, 'hunger':100,'health':100,'anxiety':100,'friends':0,'status':"TestingStatus",'wood':100,'player':"TestUser", 'event':"none",'stranger':0}

    ## stoke_fire tests

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
            print("Expected: 90 to 100")
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
            print("Expected: 90 to 120")
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
            print("Expected: 90 to 130")
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
            print("Expected: 90 to 140")
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
            print("Expected: 90 to 150")
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
            print("Expected: 90 to 130")
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
            print("Expected: 90 to 145")
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
            print("Expected: 90 to 140")
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
        if int(results['warmth']) in range (90,146):
            assert True
        else:
            print("Expected: 90 to 145")
            print("Got: " + str(results['warmth']))
            assert False, "Warmth value was not as expected."

    def test_stokeFire_valuesWarmthTenFriends(self,dictIn=dictIn):
        """Test what happens to the warmth value when a player stokes the fire, and there is wood, and ten friends."""
        dictIn['friends'] = 10
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['warmth']) in range (90,151):
            assert True
        else:
            print("Expected: 90 to 150")
            print("Got: " + str(results['warmth']))
            assert False, "Warmth value was not as expected."

    def test_stokeFire_valuesWarmthElevenFriends(self,dictIn=dictIn):
        """Test what happens to the warmth value when a player stokes the fire, and there is wood, and eleven friends."""
        dictIn['friends'] = 11
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['warmth']) in range (90,119):
            assert True
        else:
            print("Expected: 90 to 118")
            print("Got: " + str(results['warmth']))
            assert False, "Warmth value was not as expected."

    def test_stokeFire_valuesWarmthTwelveFriends(self,dictIn=dictIn):
        """Test what happens to the warmth value when a player stokes the fire, and there is wood, and twelve friends."""
        dictIn['friends'] = 12
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['warmth']) in range (90,121):
            assert True
        else:
            print("Expected: 90 to 120")
            print("Got: " + str(results['warmth']))
            assert False, "Warmth value was not as expected."

    def test_stokeFire_valuesHungerNoFriends(self,dictIn=dictIn):
        """Test what happens to the hunger value when a player stokes the fire, and there is wood, and no friends."""
        dictIn['friends'] = 0
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        dictIn['hunger'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['hunger']) in range (80,91):
            assert True
        else:
            print("Expected: 80 to 91")
            print("Got: " + str(results['hunger']))
            assert False, "Hunger value was not as expected."

    def test_stokeFire_valuesHungerOneFriends(self,dictIn=dictIn):
        """Test what happens to the hunger value when a player stokes the fire, and there is wood, and one friends."""
        dictIn['friends'] = 1
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        dictIn['hunger'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['hunger']) in range (80,91):
            assert True
        else:
            print("Expected: 80 to 91")
            print("Got: " + str(results['hunger']))
            assert False, "Hunger value was not as expected."

    def test_stokeFire_valuesHungerTwoFriends(self,dictIn=dictIn):
        """Test what happens to the hunger value when a player stokes the fire, and there is wood, and two friends."""
        dictIn['friends'] = 2
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        dictIn['hunger'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['hunger']) in range (80,91):
            assert True
        else:
            print("Expected: 80 to 91")
            print("Got: " + str(results['hunger']))
            assert False, "Hunger value was not as expected."

    def test_stokeFire_valuesHungerThreeFriends(self,dictIn=dictIn):
        """Test what happens to the hunger value when a player stokes the fire, and there is wood, and three friends."""
        dictIn['friends'] = 3
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        dictIn['hunger'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['hunger']) in range (80,91):
            assert True
        else:
            print("Expected: 80 to 91")
            print("Got: " + str(results['hunger']))
            assert False, "Hunger value was not as expected."

    def test_stokeFire_valuesHungerFourFriends(self,dictIn=dictIn):
        """Test what happens to the hunger value when a player stokes the fire, and there is wood, and four friends."""
        dictIn['friends'] = 4
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        dictIn['hunger'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['hunger']) in range (80,91):
            assert True
        else:
            print("Expected: 80 to 91")
            print("Got: " + str(results['hunger']))
            assert False, "Hunger value was not as expected."

    def test_stokeFire_valuesHungerFiveFriends(self,dictIn=dictIn):
        """Test what happens to the hunger value when a player stokes the fire, and there is wood, and five friends."""
        dictIn['friends'] = 5
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        dictIn['hunger'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['hunger']) in range (80,91):
            assert True
        else:
            print("Expected: 80 to 91")
            print("Got: " + str(results['hunger']))
            assert False, "Hunger value was not as expected."

    def test_stokeFire_valuesHungerSixFriends(self,dictIn=dictIn):
        """Test what happens to the hunger value when a player stokes the fire, and there is wood, and six friends."""
        dictIn['friends'] = 6
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        dictIn['hunger'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['hunger']) in range (80,91):
            assert True
        else:
            print("Expected: 80 to 91")
            print("Got: " + str(results['hunger']))
            assert False, "Hunger value was not as expected."

    def test_stokeFire_valuesHungerSevenFriends(self,dictIn=dictIn):
        """Test what happens to the hunger value when a player stokes the fire, and there is wood, and seven friends."""
        dictIn['friends'] = 7
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        dictIn['hunger'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['hunger']) in range (80,91):
            assert True
        else:
            print("Expected: 80 to 91")
            print("Got: " + str(results['hunger']))
            assert False, "Hunger value was not as expected."

    def test_stokeFire_valuesHungerEightFriends(self,dictIn=dictIn):
        """Test what happens to the hunger value when a player stokes the fire, and there is wood, and eight friends."""
        dictIn['friends'] = 8
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        dictIn['hunger'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['hunger']) in range (80,91):
            assert True
        else:
            print("Expected: 80 to 91")
            print("Got: " + str(results['hunger']))
            assert False, "Hunger value was not as expected."

    def test_stokeFire_valuesHungerNineFriends(self,dictIn=dictIn):
        """Test what happens to the hunger value when a player stokes the fire, and there is wood, and nine friends."""
        dictIn['friends'] = 9
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        dictIn['hunger'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['hunger']) in range (80,91):
            assert True
        else:
            print("Expected: 80 to 91")
            print("Got: " + str(results['hunger']))
            assert False, "Hunger value was not as expected."

    def test_stokeFire_valuesHungerTenFriends(self,dictIn=dictIn):
        """Test what happens to the hunger value when a player stokes the fire, and there is wood, and ten friends."""
        dictIn['friends'] = 10
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        dictIn['hunger'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['hunger']) in range (80,91):
            assert True
        else:
            print("Expected: 80 to 91")
            print("Got: " + str(results['hunger']))
            assert False, "Hunger value was not as expected."

    def test_stokeFire_valuesHungerElevenFriends(self,dictIn=dictIn):
        """Test what happens to the hunger value when a player stokes the fire, and there is wood, and eleven friends."""
        dictIn['friends'] = 11
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        dictIn['hunger'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['hunger']) in range (80,91):
            assert True
        else:
            print("Expected: 80 to 91")
            print("Got: " + str(results['hunger']))
            assert False, "Hunger value was not as expected."

    def test_stokeFire_valuesHungerTwelveFriends(self,dictIn=dictIn):
        """Test what happens to the hunger value when a player stokes the fire, and there is wood, and twelve friends."""
        dictIn['friends'] = 12
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        dictIn['hunger'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['hunger']) in range (80,91):
            assert True
        else:
            print("Expected: 80 to 91")
            print("Got: " + str(results['hunger']))
            assert False, "Hunger value was not as expected."

    def test_stokeFire_valuesAnxietyNoFriends(self,dictIn=dictIn):
        """Test what happens to the anxiety value when a player stokes the fire, and there is wood, and no friends."""
        dictIn['friends'] = 0
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        dictIn['hunger'] = 90
        dictIn['anxiety'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['anxiety']) in range (80,91):
            assert True
        else:
            print("Expected: 80 to 91")
            print("Got: " + str(results['anxiety']))
            assert False, "Hunger value was not as expected."

    def test_stokeFire_valuesAnxietyOneFriends(self,dictIn=dictIn):
        """Test what happens to the anxiety value when a player stokes the fire, and there is wood, and one friends."""
        dictIn['friends'] = 1
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        dictIn['hunger'] = 90
        dictIn['anxiety'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['anxiety']) in range (80,91):
            assert True
        else:
            print("Expected: 80 to 91")
            print("Got: " + str(results['anxiety']))
            assert False, "Hunger value was not as expected."

    def test_stokeFire_valuesAnxietyTwoFriends(self,dictIn=dictIn):
        """Test what happens to the anxiety value when a player stokes the fire, and there is wood, and two friends."""
        dictIn['friends'] = 2
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        dictIn['hunger'] = 90
        dictIn['anxiety'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['anxiety']) in range (80,91):
            assert True
        else:
            print("Expected: 80 to 91")
            print("Got: " + str(results['anxiety']))
            assert False, "Hunger value was not as expected."

    def test_stokeFire_valuesAnxietyThreeFriends(self,dictIn=dictIn):
        """Test what happens to the anxiety value when a player stokes the fire, and there is wood, and three friends."""
        dictIn['friends'] = 3
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        dictIn['hunger'] = 90
        dictIn['anxiety'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['anxiety']) in range (80,91):
            assert True
        else:
            print("Expected: 80 to 91")
            print("Got: " + str(results['anxiety']))
            assert False, "Hunger value was not as expected."

    def test_stokeFire_valuesAnxietyFourFriends(self,dictIn=dictIn):
        """Test what happens to the anxiety value when a player stokes the fire, and there is wood, and four friends."""
        dictIn['friends'] = 4
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        dictIn['hunger'] = 90
        dictIn['anxiety'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['anxiety']) in range (80,91):
            assert True
        else:
            print("Expected: 80 to 91")
            print("Got: " + str(results['anxiety']))
            assert False, "Hunger value was not as expected."

    def test_stokeFire_valuesAnxietyFiveFriends(self,dictIn=dictIn):
        """Test what happens to the anxiety value when a player stokes the fire, and there is wood, and five friends."""
        dictIn['friends'] = 5
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        dictIn['hunger'] = 90
        dictIn['anxiety'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['anxiety']) in range (80,91):
            assert True
        else:
            print("Expected: 80 to 91")
            print("Got: " + str(results['anxiety']))
            assert False, "Hunger value was not as expected."

    def test_stokeFire_valuesAnxietySixFriends(self,dictIn=dictIn):
        """Test what happens to the anxiety value when a player stokes the fire, and there is wood, and six friends."""
        dictIn['friends'] = 6
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        dictIn['hunger'] = 90
        dictIn['anxiety'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['anxiety']) in range (80,91):
            assert True
        else:
            print("Expected: 80 to 91")
            print("Got: " + str(results['anxiety']))
            assert False, "Hunger value was not as expected."

    def test_stokeFire_valuesAnxietySevenFriends(self,dictIn=dictIn):
        """Test what happens to the anxiety value when a player stokes the fire, and there is wood, and seven friends."""
        dictIn['friends'] = 7
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        dictIn['hunger'] = 90
        dictIn['anxiety'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['anxiety']) in range (80,91):
            assert True
        else:
            print("Expected: 80 to 91")
            print("Got: " + str(results['anxiety']))
            assert False, "Hunger value was not as expected."

    def test_stokeFire_valuesAnxietyEightFriends(self,dictIn=dictIn):
        """Test what happens to the anxiety value when a player stokes the fire, and there is wood, and eight friends."""
        dictIn['friends'] = 8
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        dictIn['hunger'] = 90
        dictIn['anxiety'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['anxiety']) in range (80,91):
            assert True
        else:
            print("Expected: 80 to 91")
            print("Got: " + str(results['anxiety']))
            assert False, "Hunger value was not as expected."

    def test_stokeFire_valuesAnxietyNineFriends(self,dictIn=dictIn):
        """Test what happens to the anxiety value when a player stokes the fire, and there is wood, and nine friends."""
        dictIn['friends'] = 9
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        dictIn['hunger'] = 90
        dictIn['anxiety'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['anxiety']) in range (80,91):
            assert True
        else:
            print("Expected: 80 to 91")
            print("Got: " + str(results['anxiety']))
            assert False, "Hunger value was not as expected."

    def test_stokeFire_valuesAnxietyTenFriends(self,dictIn=dictIn):
        """Test what happens to the anxiety value when a player stokes the fire, and there is wood, and ten friends."""
        dictIn['friends'] = 10
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        dictIn['hunger'] = 90
        dictIn['anxiety'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['anxiety']) in range (80,91):
            assert True
        else:
            print("Expected: 80 to 91")
            print("Got: " + str(results['anxiety']))
            assert False, "Hunger value was not as expected."

    def test_stokeFire_valuesAnxietyElevenFriends(self,dictIn=dictIn):
        """Test what happens to the anxiety value when a player stokes the fire, and there is wood, and eleven friends."""
        dictIn['friends'] = 11
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        dictIn['hunger'] = 90
        dictIn['anxiety'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['anxiety']) in range (80,91):
            assert True
        else:
            print("Expected: 80 to 91")
            print("Got: " + str(results['anxiety']))
            assert False, "Hunger value was not as expected."

    def test_stokeFire_valuesAnxietyTwelveFriends(self,dictIn=dictIn):
        """Test what happens to the anxiety value when a player stokes the fire, and there is wood, and twelve friends."""
        dictIn['friends'] = 12
        dictIn['wood'] = 100
        dictIn['warmth'] = 90
        dictIn['hunger'] = 90
        dictIn['anxiety'] = 90
        results = actions.stoke_fire(dictIn)
        if dictIn == results:
            assert False, "Function didn't modify any values."
        if int(results['anxiety']) in range (80,91):
            assert True
        else:
            print("Expected: 80 to 91")
            print("Got: " + str(results['anxiety']))
            assert False, "Hunger value was not as expected."

    # gather_wood Tests

    def test_gatherWood_veryAnxious(self,dictIn=dictIn):
        """Test what happens when a player tries to gather wood, but is too scared"""
        dictIn['anxiety'] = 0
        results = actions.gather_wood(dictIn)
        if results['status'] == 'Too Scared to Gather Wood':
            assert True
        else:
            assert False, "Status was not as expected."

    def test_gatherWood_veryCold(self,dictIn=dictIn):
        """Test what happens when a player tries to gather wood, but is too cold"""
        dictIn['anxiety'] = 100
        dictIn['warmth'] = 0
        results = actions.gather_wood(dictIn)
        if results['status'] == 'Too Cold to Gather Wood':
            assert True
        else:
            assert False, "Status was not as expected."

    def test_gatherWood_noFriends(self,dictIn=dictIn):
        """Test what happens when a player tries to gather wood, and can, with no friends"""
        dictIn['anxiety'] = 100
        dictIn['warmth'] = 100
        dictIn['friends'] = 0
        results = actions.gather_wood(dictIn)
        if results['status'] == 'Cold from Gathering Wood':
            assert True
        else:
            assert False, "Status was not as expected."
