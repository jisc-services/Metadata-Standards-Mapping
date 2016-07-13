source venv/bin/activate
rm -rf build
mkdir -p build/css
cp css/* build/css/
python schema_tables.py > build/index.html
