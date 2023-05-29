# resin-io-projects-ETANixieClock
This project takes the [ETANixieClock](https://wp.me/p85ddV-Ad) Raspberry pi project and converts it into a Resin-io (Resin-io was recently changed to Balena-io) Docker Device.  See the complete blog for this project at [Easy IoT Fleet Deployment of ETA Nixie Tube Clocks](https://surfncircuits.com/?p=2665).  The goal of the blog and project is to allow on the fly updates of the code along with a method to maintian persistant data when the code is updated.    It also includes a way to externally setup a wifi connection when a valid wifi is not available, by converting the Raspberry Pi into an Access Point.   This method follows examples from the [Resin-io repository](https://github.com/resin-io-projects/resin-wifi-connect-example)
For the Resin-io dashboard, two appliation parameters per device are needed to be sent to the Docker Containter.   
1. The GOOGLEKEY is the client key you get from google for a google maps account.  This is a good way to keep this private.   See instructions in the [BLOG](https://surfncircuits.com/?p=2665) on how to get this client Key.
2. The TIMEZONE paramater is the set to you time zone.  For example, 'America/Los_Angeles'.   See the entry at [Wikipedia](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) for a valid timezone name.    

The Setuplocations.py file is a python script that allows for each ETA clock to be customized for a given location and individual ETA destinations.   This will need to be run through the terminal window of the device as shown in the [BLOG](https://surfncircuits.com/?p=2665).  This data will be persistant between code updates.  Future upgrades of the code should allow this to be updated from a web server....

The TestDigits.py file is a python script designed to test, debug, and burn-in Nixie Tubes assembled for the [ETANixieClock](https://wp.me/p85ddV-Ad) schematic and PCB layout.  Burn-in is often needed to get rid of [cathode](http://www.tube-tester.com/sites/nixie/different/cathode%20poisoning/cathode-poisoning.htm) poisoning on older tubes and this program can be used to test it out and burnin a set of nixie tubes.  It also is good to debug other visual issues with Nixie tubes, like setting the bias resistors so that all digits light up correctly with the power supply voltage.   