# Our car

## To launch the car:
- source your workspace
- run `roslaunch car_description car_control.launch`
- In a new tab: 
```
roscd car_description/src
python controller.py
```
## To control the car directly with messages:
- publish at car/cmd_vel with a twist message

## To give random directions to the car:
- In a new tab:
```
roscd car_description/src
python talker.py
```


