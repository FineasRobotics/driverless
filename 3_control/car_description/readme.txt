run the following commands

	roslaunch car_description car_control.launch
	ctrl + t
	roscd car_description/src
	python controller.py
	
if u want to controll the car by ur self 
	publish at car/cmd_vel with a twist message

else for random controll do the following
	   ctrl + t
	   roscd car_description/src
	   python talker.py


