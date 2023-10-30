# Preboarder
*This app is on the merchant's side and hence will have the prerequisite of the merchant having the python height measure app which we have built and added to this repo in the python folder
as a direct .py file. The python file produces a .csv which must be uploaded to the merchant's database, from which height information can be accessed by this web app.*

## Airline Preboarding App ##
This app uses OpenCv and TensorFLowIo with webcam recognition to 'scan' a passenger pre-boarding the flight and give them an ergonomic and optimized seat position reccomendation throught an algorthim
which estimates the best seat on the basis of age, family, disabilities if any and height.

First, the airline could use the python application to scan the height of the passenger. This is done by measuring the pixels on screen and converting it by a factor which was tested while the scanned subjects stood at a distance of 4 meters from the camera, a setting the airline can control and change in code. After this, the height details (cm) are transferred into the web app with the help of a .csv file which stores one value, the height data. The uploading of this data can also be controlled by the merchant so for the demo, we have made it a manual process.

The web app is first used to scan and recognize the passenger using tensorflow.io files in js, for our demo, it can recognize any injuries and return keywords like bandage, arm sling, cast, etc. These keywords are stored and also the next step of the process scan a QR code in the demo, which we beleive could be scanning the ticket in a real life application to directly lift detials like age and gender of the passenger. 

With these details, an algorthim used in the js section estimates based on age, injuries and travelling with or without family (something scanned from the ticket) if the person could be placed in front or back section, in a bulkhead rows, near a washroom (for senior citizens), in an aisle seat(for those with injuries) etc.

This is a very basic implementation of the idea and can be tested by downloading the index.html along with the sample.csv file and uploading the sample.csv for the app to get a sample height information.
