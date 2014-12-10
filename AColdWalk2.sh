clear
echo "A Cold Walk"
sleep 1s
echo ""
echo ""
echo "jm | Design"
sleep 1s
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

$WARMTH="$((50 + 50))"
$WOOD="$((50 + 50))"
$FOOD="$((50 + 50))"
$HEALTH="$((50 + 50))"
$ANXIETY="$((1 - 1))"
read input

stokeFire() {
  if [ "$(($WOOD + 0))" -ge "1" ]
  then
    echo "The fire warms the room."
    $(($WOOD - 10))
    $(( $WARMTH + 10))
    echo "Warmth... " $WARMTH
    echo "Wood... " $WOOD
  else
    echo "No wood left!"
  fi
}

gatherWood() {
  if [ "$(($WARMTH + 0))" -ge "1" ]
    then
    echo "It's freezing out here!"
    echo "... Lucky there's lots of bracken to burn."
    $(($WOOD + 10))
    $(( $WARMTH - 10))
    echo "Warmth... " $WARMTH
    echo "Wood... " $WOOD
  else
    echo "I'm too cold!"
  fi

}

clear
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
if [ $input = 'A' ]
  then
  stokeFire
else
  gatherWood
fi
