python gpxmerge.py -i"./../../../Outdoor/0010journeys/**/*Bike.gpx" -o"./output/trip/bike/"
python gpxmerge.py -i"./../../../Outdoor/0010journeys/**/*Mount*.gpx" -o"./output/trip/mountain/"
python gpxmerge.py -i"./../../../Outdoor/0010journeys/**/*Walk*.gpx" -o"./output/trip/walk/"
python gpxmerge.py -i"./../../../Outdoor/0010journeys/**/*Raft*.gpx" -o"./output/trip/raft/"
python gpxmerge.py -i"./../../../Outdoor/0010journeys/**/*Ski*.gpx" -o"./output/trip/ski/"
python gpxmerge.py -i"./../../../Outdoor/0010journeys/**/*Car*.gpx" -o"./output/trip/car/"
python gpxmerge.py -i"./../../../Outdoor/0015pvd/**/*.gpx" -o"./output/pvd/"
python gpxmerge.py -i"./../../../Outdoor/0040competition/**/*.gpx" -o"./output/competition/"
python gpxmerge.py -i"./../../../Outdoor/0020plansjourney/**/*.gpx" -o"./output/plans_trip/"
python gpxmerge.py -i"./../../../Outdoor/0025planspvd/**/*.gpx" -o"./output/plans_pvd/"
python gpxcleaner.py -i"./output/**/*.gpx" --ignore_time --ignore_elevation --replace_original