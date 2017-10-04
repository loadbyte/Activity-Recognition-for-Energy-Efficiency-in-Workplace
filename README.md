# Activity Recognition for Energy Efficiency in Workplace

## Abstract
 - Detection of human activities is a set of techniques that can be used in wide range of applications, including smart homes and healthcare.
 - In Activity recognition, we need to correctly identify and recognize the individual’s current activities.
 - Designed an IoT device to monitor the activities of the user, without breaching the privacy of the user.
 - Implemented <b>KNN Algorithm</b> to learn the pattern in the sensor data, which has been used to recognize the user activity.
 
## Architecture and IoT setup

 - The IoT device is placed in the Robotics Lab in Dept. of Computer Science at IIT Guwahati.
 - The IoT device is fitted with PIR, PING and LIGHT sensor. All these sensors gave us different sensor values of the student's activities performed in the lab.

| <img src="/Images/Pi Setup.jpg" width="250px" alt="IoT">  | <img src="/Images/Arch.PNG" width="622px" alt="System Architecture for the test bed"> |
|:---:|:---:|
| IoT device setup | System Architecture for the test bed |

## Activity Classes
The following four classes have been identified suitable for the problem.
1) Sitting + Screen ON
2) Idle + Screen ON
3) Sitting + Screen OFF
4) Idle + Screen OFF

## Data

 - The data has been collected for 24 hours each day and it has been manually annotated.
 - The following is the snapshot of the readings from LIGHT, PING and PIR sensor, during the beginning of SITTING activity.

| <img src="/Images/data.PNG" width="436px" alt="Data recorded from IoT">  | <img src="/Images/norm.PNG" width="436px" alt="Normalized data"> |
|:---:|:---:|
| Data recorded from IoT - Annotated | Normalized data |

## Sensor Readings and Activity Patterns

### Light Sensor
 - The light sensor provides us the luminosity in the environment. 
 - It is fixed to the system monitor, which has been used to infer whether the system monitor is ON / OFF. 
 - Assuming each individual in the lab has an independent system, we can use this light sensor information to infer,
    1) When did the individual start working each day
    2) What is the total duration of working time, each day

<img src="/Images/light.png" alt="Light Sensor Reading">

### Ping Sensor
 - Raspberry Pi is used to trigger the Ping sensor to send an ultrasonic pulse.
 - The pulse waves bounce off from any nearby objects and some are reflected back to the sensor.
 - The sensor detects these return waves and measures the time gap between the trigger and returned pulse.
 - This information will be utilized to identify, if there is any human in-front of the system.
 
<img src="/Images/ping.png" alt="Ping Sensor Reading">

### PIR Sensor
 - Ping sensor cannot differentiate an object / chair from a human being.
 - PIR sensor can detects changes in the amount of infrared radiation it receives.
 - The infrared heat emitted by the human body is used to detect the motion of a human being before the system.

<img src="/Images/pir.png" alt="PIR Sensor Reading">

## Sitting Activity Sensor Data Analysis
 - SITTING activity cannot be recognized only with the help of PING sensor, due to the interruption of the PING values because of other objects like chair. 
 - Hence, PIR and PING is used as a combination to track this activity.
 - If we analyse the data, we can infer that the PIR values show human motion from time-step 10-20 and the PING reading has dropped down ultimately at 22, indicating some person has come-in and sat before the system.

<img src="/Images/sitting.png" alt="Output Analysis for Sitting activity">

## Running the algorithm
 - Clone the repository and retain the same folder structure with the dataset in place.
 - Execute the following command.
```
python knn.py
```
## Result
 - The data collected from the IoT device is manually annotated.
 - Raw data has been normalized to feed to the algorithm.
 - The KNN algorithm has been implemented to identify the pattern in the sensor data and recognize the activity.
 - The following is a snapshot of the KNN result.

<img src="/Images/Knn Result.PNG" alt="K-NN Recognition results">
