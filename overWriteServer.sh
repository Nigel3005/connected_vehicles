python manage.py makemigrations
python manage.py migrate
git add .
echo Commit text: 
read pushname
git commit -m $pushname
git push