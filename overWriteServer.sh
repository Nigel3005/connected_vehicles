git add .
git commit -m "autopush"
git push
ssh -i "niels.pem" ubuntu@ec2-15-188-90-156.eu-west-3.compute.amazonaws.com
cd django
./overwrite.sh

