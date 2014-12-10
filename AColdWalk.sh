clear
sleep 1s
echo "A Cold Walk"
echo ""
echo "jm | Design"
echo ""
echo ""
echo "Press enter to continue."
read input
clear
echo "Loading"
sleep 1s
clear
echo "Loading."
sleep 1s
clear
echo "Loading.."
sleep 1s
clear
echo "Loading..."
clear
sleep 1s
echo "It began for me simply enough."
echo "..."
echo ""
echo "... Just another cold day, in July."
echo ""
echo ""
echo "Press enter to continue."
read input
clear
echo "I remember the rain, most of all."
echo "It came down with a vengeance. As if the heavens themselves had decided to open up."
echo "..."
echo ""
echo "I adored it."
echo ""
echo ""
echo "Press enter to continue."
read input
clear
echo "However, as to the wooden cabin I was living in..."
echo ""
echo "Let's just say it began to deteriorate quickly."
echo ""
echo ""
echo "Press enter to continue."
read input
clear
echo "It's freezing outside."
echo ""
echo "But the fire is down to embers."
echo ""
echo "Enter A for: Stoke fire."
echo "Enter B for: Look for wood."
echo ""
echo "..."
read input
clear
if [ $input = 'A' ]
then
	echo "The fire warms the room!"
	WARMTH="100"
	echo "Warmth... " $WARMTH
	WOOD="10"
	echo "Wood... " $WOOD
else
	echo "It's freezing out here!"
	echo "... Lucky there's lots of bracken to burn."
	WARMTH="80"
	echo "Warmth... " $WARMTH
	WOOD="20"
	echo "Wood... " $WOOD
fi
function gatherWood {
	echo "It's freezing out here!"
	echo "... Lucky there's lots of bracken to burn."
	WARMTH=$WARMTH - 10
	WOOD=$WOOD + 10
	echo "Warmth... " $WARMTH
	echo "Wood... " $WOOD
}
function stokeFire {
	echo "The fire warms the room!"
	WARMTH=$WARMTH + 10
	WOOD=$WOOD - 10
	echo "Warmth... " $WARMTH
	echo "Wood... " $WOOD
}
echo ""
echo ""
echo "Enter A to gather more wood."
echo "Enter B to stoke the fire."
read input
clear
if [ $input = 'A' ]
then
	gatherWood
else
	stokeFire
fi
