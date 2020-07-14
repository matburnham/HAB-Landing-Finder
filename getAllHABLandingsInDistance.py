# Query all the hourly predictors at https://ukhas.org.uk/frontpage:radiosondes

while read url
do
  ./getHABLandingsInDistance.py $@ $url
done <<< 'http://predict.habhub.org/hourly/aberporth/
http://predict.habhub.org/hourly/camborne/
http://predict.habhub.org/hourly/cardington/
http://predict.habhub.org/hourly/castorbay/
http://predict.habhub.org/hourly/herstmonceux/
http://predict.habhub.org/hourly/larkhill/
http://predict.habhub.org/hourly/watnall/'
